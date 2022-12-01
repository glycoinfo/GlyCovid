from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    cid: 370
    chemicalid: D005707
    chemicalname: Gallic Acid
    genesymbol: BCL2L11
    geneid: 10018
    taxname: Mus musculus
    taxid: 10090
    interaction: Gallic Acid results in decreased expression of BCL2L11 mRNA
    pmids: 29205955
    """

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

