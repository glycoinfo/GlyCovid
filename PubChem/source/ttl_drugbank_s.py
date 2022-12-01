from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    protacxn: Q16602
    geneid: 10203
    genesymbol: CALCRL
    cid: 6918509
    drugtype: small molecule
    drugname: Olcegepant
    druggroup: investigational
    drugaction: NULL
    drugdetail: DB04869
    targettype: target
    targetid: BE0009009
    targetname: Calcitonin gene-related peptide type 1 receptor
    targetcomponent: Q16602
    targetcomponentname: Calcitonin gene-related peptide type 1 receptor
    generalfunc: Receptor for calcitonin-gene-related peptide (CGRP) together with RAMP1 and receptor for adrenomedullin together with RAMP3 (By similarity). Receptor for adrenomedullin together with RAMP2. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.
    specificfunc: Adrenomedullin receptor activity
    pmids: 28165287
    cmpdname: Olcegepant
    dois: 10.1177/0333102417691762
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

