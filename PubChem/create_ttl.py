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
)
import csv


def create_ttl():
    func_set = {
        "bioactivity_gene_s": ttl_bioactivity_gene_s.create_ttl,
        "bioassay_s": ttl_bioassay_s.create_ttl,
        "chembldtug_s": ttl_chembldtug_s.create_ttl,
        "ctdchemicalgene_s": ttl_ctdchemicalgene_s.create_ttl,
        "dgidb_s": ttl_dgidb_s.create_ttl,
        "drugbank_s": ttl_drugbank_s.create_ttl,
        "gene_disease": ttl_gene_disease.create_ttl,
        "gtopdb_s": ttl_gtopdb_s.create_ttl,
        "pathwaygene_s": ttl_pathwaygene_s.create_ttl,
        "pathwayreaction_s": ttl_pathwayreaction_s.create_ttl,
        "pdb_s": ttl_pdb_s.create_ttl,
    }
    for csv_file_name, ttl in func_set.items():
        # Create RDF graph instance
        g = Graph()
        # Import uri prefix to create rdf from define file
        u =uri_ref()

        # Read csv file
        with open(f"PubChem/data/dir/${csv_file_name}.csv") as f1:
            reader = csv.reader(f1, delimiter=",")
            next(reader)
            for row_in_bar in reader:
                # Expansion by | which is separate data in same colmn
                rows = expansion_tsv_row([row_in_bar])
                for row in rows:
                    g = ttl(g, u, row)
        g.serialize(
            destination=f"turtle/${csv_file_name}.ttl",
            format="turtle",
        )


if __name__ == "__main__":
    create_ttl()
