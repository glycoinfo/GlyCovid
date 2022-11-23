from rdflib.namespace import RDF
import csv

def create_ttl(g, u, row):
    Interactor_ab = create_subject_uri(row[0], row[1])
    g.add((Interactor_ab, RDF.type, molecular_interaction))

    Interactor_a = create_object_uri(row[0], db_list)
    g.add((Interactor_ab, has_interactorA, Interactor_a))
    g.add((Interactor_a, RDF.type, functional_entiry))
    Interactor_b = create_object_uri(row[1], db_list)
    g.add((Interactor_ab, has_interactorB, Interactor_b))
    g.add((Interactor_b, RDF.type, functional_entiry))

    if row[6] != "-" and row[6] != "":
        Detection_method = create_object_uri(row[6], db_list)
        g.add((Interactor_ab, detected_by, Detection_method))
    return g

def check_csv_data():
    csv_file_path = "PubChem/data/dir/pathwaygene_s.csv"
    source_list = []
    with open(csv_file_path) as f1:
        reader = csv.reader(f1, delimiter=",")
        for row in reader:
            if row[3] not in source_list:
                source_list.append(row[3])
    for source in source_list:
        print(source)
    """
    WikiPathways                                                                                                                                 │
    Reactome                                                                                                                                     │
    PathBank                                                                                                                                     │
    Pathway Interaction Database                                                                                                                 │
    PharmGKB                                                                                                                                     │
    INOH                                                                                                                                         │
    BioCyc
    """

if __name__ == "__main__":
    check_csv_data()
