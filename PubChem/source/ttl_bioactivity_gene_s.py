from rdflib.namespace import RDF
import csv
import json


def create_ttl(g, u, row, prefix, object, linkage):
    """
    baid
    activity
    aid
    sid
    cid
    geneid
    pmid
    aidtype
    aidmdate
    hasdrc
    rnai
    protacxn
    acname
    acqualifier
    acvalue
    aidsrcname
    aidname
    cmpdname
    targetname
    targeturl
    ecs
    repacxn
    taxids
    cellids
    targettaxid
    """

    print(linkage)



    # Interactor_ab = create_subject_uri(row[0], row[1])
    # g.add((Interactor_ab, RDF.type, molecular_interaction))
    #
    # Interactor_a = create_object_uri(row[0], db_list)
    # g.add((Interactor_ab, has_interactorA, Interactor_a))
    # g.add((Interactor_a, RDF.type, functional_entiry))
    # Interactor_b = create_object_uri(row[1], db_list)
    # g.add((Interactor_ab, has_interactorB, Interactor_b))
    # g.add((Interactor_b, RDF.type, functional_entiry))
    #
    # if row[6] != "-" and row[6] != "":
    #     Detection_method = create_object_uri(row[6], db_list)
    #     g.add((Interactor_ab, detected_by, Detection_method))
    # return g

if __name__ == "__main__":
    create_ttl(0,0,0)
