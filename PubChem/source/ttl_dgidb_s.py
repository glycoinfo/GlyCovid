from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    geneid: 10018
    genename: BCL2L11
    geneclaimname: BCL2L11
    interactionclaimsource: PharmGKB
    interactiontypes: NULL
    sid: 103245522
    cid: 5291
    drugname: IMATINIB
    drugclaimname: imatinib
    drugclaimprimaryname: imatinib
    drugchemblid: CHEMBL941
    pmids: 24223824
    cmpdname: Imatinib
    dois: 10.1371/journal.pone.0078582
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

