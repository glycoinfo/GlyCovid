from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    protacxn: Q9HC98
    geneid: 10783
    ligand: compound 22 [PMID: 20462760]
    ligandid: 8205
    cid: 24863112
    primarytarget: No
    type: Inhibitor
    action: Inhibition
    units: -
    affinity: 5.78
    pmids: 20462760
    targetid: 2121
    targetname: NIMA related kinase 6
    targetspecies: Human
    genesymbol: NEK6
    cmpdname: N-(7-Chloro-1-oxo-1,2-dihydroisoquinolin-6-yl)-2-(cyclopropylamino)-2-phenylacetamide
    dois: 10.1016/j.bmcl.2010.04.07
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

