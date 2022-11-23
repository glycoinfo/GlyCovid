from source.utils import uri_ref, expansion_tsv_row
from rdflib import Graph, Literal, Namespace, URIRef, BNode
from source import (
    ttl_bioactivity_gene_s,
    ttl_bioassay_s,
    ttl_chembldtug_s,
    ttl_ctdchemicalgene_s,
    ttl_dgidb_s,
    ttl_drugbank_s,
    ttl_gene_disease,
    ttl_gtopdb_s,
    ttl_pathwaygene_s,
    ttl_pathwayreaction_s,
    ttl_pdb_s,
    ttl_rhea_s,
)
import csv
import json
import glob


def csv2json(csv_path: str) -> list:
    res = []
    with open(csv_path) as f1:
        reader = csv.reader(f1, delimiter=",")
        count = 0
        for row in reader:
            if count == 0:
                header = row
            row_data = {}
            for i, col in enumerate(row):
                row_data[header[i]] = col
            res.append(row_data)
            count += 1
    return res

def load_json(json_path: str):
    f = open(json_path)
    res = json.load(f)
    f.close()
    return res

def create_ttl():
    linkage = csv2json("PubChem/source/ref_definitions/linkage.csv")
    object = csv2json("PubChem/source/ref_definitions/object.csv")
    prefix = load_json("PubChem/source/ref_definitions/prefix.json")
    func_set = {
        "bioactivity_gene": ttl_bioactivity_gene_s.create_ttl,
        "bioassay": ttl_bioassay_s.create_ttl,
        "chembldtug": ttl_chembldtug_s.create_ttl,
        "ctdchemicalgene": ttl_ctdchemicalgene_s.create_ttl,
        "dgidb": ttl_dgidb_s.create_ttl,
        "drugbank": ttl_drugbank_s.create_ttl,
        "gene_disease": ttl_gene_disease.create_ttl,
        "gtopdb": ttl_gtopdb_s.create_ttl,
        "pathwaygene": ttl_pathwaygene_s.create_ttl,
        "pathwayreaction": ttl_pathwayreaction_s.create_ttl,
        "pdb": ttl_pdb_s.create_ttl,
        "rhea": ttl_rhea_s.create_ttl,
    }
    for data_name, ttl in func_set.items():
        # Create RDF graph instance
        g = Graph()
        # Import uri prefix to create rdf from define file
        u = uri_ref()

        # Read csv file of all data/dir/**/.csv
        list_csv_file_path = glob.glob(
            f"PubChem/data/dir/{data_name}/*.csv", recursive=True
        )
        for csv_file_path in list_csv_file_path:
            with open(csv_file_path) as f1:
                reader = csv.reader(f1, delimiter=",")
                next(reader)
                for row_in_bar in reader:
                    # Expansion by | which is separate data in same colmn
                    rows = expansion_tsv_row([row_in_bar])
                    for row in rows:
                        # Create RDF by csv line with each functions
                        g = ttl(g, u, row, prefix, object, linkage)
        return
        g.serialize(
            destination=f"PubChem/turtle/${data_name}.ttl",
            format="turtle",
        )


if __name__ == "__main__":
    create_ttl()

