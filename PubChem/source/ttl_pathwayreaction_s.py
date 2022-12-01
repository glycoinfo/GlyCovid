from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import json
import csv

def create_ttl(g, u, row):
    """
    name: Programmed Cell Death
    source: Reactome
    externalid: R-HSA-5357801
    url: https://reactome.org/content/detail/R-HSA-5357801
    definition: ATP + BCL2L11:DYNLL1:microtubules ⟶ ADP + DYNLL1:microtubules + p-BIM
    reaction: <a href='https://pubchem.ncbi.nlm.nih.gov/compound/5461108'>ATP</a> + BCL2L11:DYNLL1:microtubules ⟶ <a href='https://pubchem.ncbi.nlm.nih.gov/compound/7058055'>ADP</a> + <a href='https://pubchem.ncbi.nlm.nih.gov/protein/O43521'>p-BIM</a> + DYNLL1:microtubules
    control: activated by <a href='https://pubchem.ncbi.nlm.nih.gov/protein/P45983'>mitogen-activated protein kinase 8</a>
    cids: 5461108|7058055
    protacxns: O43521|P45983|P63167
    geneids: 10018|5599|8655
    ecs: 2.7.11.24
    pmids: 12591950
    """

    cid = id2uri(row["cids"], "cid")
    protein = id2uri(row["protacxns"], "protein")
    gid = id2uri(row["geneids"], "gid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, protein, RDF.type, u.protein)

    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

def check_csv_data():
    csv_file_path = "PubChem/data/dir/pathwayreaction_s.csv"
    source_list = []
    with open(csv_file_path) as f1:
        reader = csv.reader(f1, delimiter=",")
        for row in reader:
            if row[1] not in source_list:
                source_list.append(row[1])
    for source in source_list:
        print(source)
    """Reactome                                                                                                                                     │
    PathBank                                                                                                                                     │
    BioCyc                                                                                                                                       │
    WikiPathways                                                                                                                                 │
    PharmGKB                                                                                                                                     │
    INOH                                                                                                                                         │
    COVID-19 Disease Map
    """

if __name__ == "__main__":
    check_csv_data()
