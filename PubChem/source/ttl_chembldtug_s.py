from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    mecid: 4919
    cid: 51049968
    chemblid: CHEMBL2178422
    drugname: RIMEGEPANT
    moa: Calcitonin gene-related peptide type 1 receptor antagonist
    action: ANTAGONIST
    targetchemblid: CHEMBL3798
    targetname: Calcitonin gene-related peptide type 1 receptor
    protacxns: Q16602
    geneids: 10203
    pmids: 23153230
    cmpdname: Rimegepant
    dois: 10.1021/jm3013147
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

