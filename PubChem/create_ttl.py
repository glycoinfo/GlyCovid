import csv
import glob
import os
import re
import shutil
import sys
from copy import copy
from urllib.parse import quote

import rdflib
from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import FOAF, RDF, RDFS, XSD

def create_ttl(dir_name, file_name, service):
    # print("create", file_name + ".ttl", "from", dir_name)
    g = Graph()
    #############################
    # predicate
    #############################
    detected_by = URIRef("http://www.bioassayontology.org/bao#BAO_0002875")
    pub_id = URIRef("http://purl.obolibrary.org/obo/IAO_0000119")

    has_interaction_type_obo = URIRef("http://purl.obolibrary.org/obo/INO_0000154")
    has_interaction_type_bp = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#interactionType"
    )
    souce_db = URIRef("http://purl.org/dc/elements/1.1/source")
    has_interaction_id = URIRef("http://purl.org/dc/elements/1.1/identifier")
    organizm = URIRef("http://semanticscience.org/resource/SIO_000253")
    has_interactorA = URIRef(
        "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"
    )
    has_interactorB = URIRef(
        "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"
    )

    #############################
    # classes
    #############################
    molecular_interaction = URIRef("http://biomodels.net/SBO/SBO_0000344")
    publication_identifier = URIRef("http://purl.obolibrary.org/obo/NCIT_C93638")
    interaction_id = URIRef("http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId")
    functional_entiry = URIRef("http://biomodels.net/SBO/SBO_0000241")
    host_organism = URIRef("http://purl.obolibrary.org/obo/EUPATH_0000591")
    in_vitro = URIRef("http://www.bioassayontology.org/bao#BAO_0020008")
    chemical_synthesis = URIRef("http://semanticscience.org/resource/SIO_000559")
    unidentified = URIRef("http://purl.bioontology.org/ontology/SNOMEDCT/69910005")

    ############################
    # code
    ############################

    # object
    db_list = dict()
    # key = dbname, value = uriの辞書を作成
    with open("uri_list/object_uri_list2.csv") as f1:
        reader = csv.reader(f1, delimiter="\t")
        for row in reader:
            db_list[row[0]] = rdflib.Namespace(row[1])
            if " " in row[0]:
                db_list[row[0].replace(" ", "")] = rdflib.Namespace(row[1])

    with open(dir_name) as f1:
        """column number
        0, InteractorA
        1, InteractorB
        2, AlternativeA
        3, AlternativeB
        4, AliasesA
        5, AliasesB
        6, Detection methods
        7, First_author
        8, Publication
        9, TaxonomyA
        10, TaxonomyB
        11, Interaction types
        12, Source/databases
        13, Interaction_id
        14, Score
        """
        reader = csv.reader(f1, delimiter="\t")
        next(reader)
        for row_bef in reader:
            row = except_columns(row_bef)
            if (
                row[0] == "-"
                or row[1] == "-"
                or row[0] == ""
                or row[1] == ""
                or "Missing" in row[0]
                or "Missing" in row[1]
                or "unassigned" in row[8]
                or "REACT_" in row[13]
            ):
                continue
            if "psi-mi" in row[8] or "psi-mi" in row[13]:
                continue

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

            if row[8] != "-" and row[8] != "":
                if re.search(r"\d{2}\.\d{4}\/\d{4}\.\d{2}\.\d{2}\.\d{6}", row[8]):
                    row[8] = row[8].replace("pubmed", "doi")
                Publication_id = create_object_uri(row[8], db_list)
                g.add((Interactor_ab, pub_id, Publication_id))
                g.add((Publication_id, RDF.type, publication_identifier))

            if row[9] != "-" and row[9] != "":
                Taxon_id = create_object_uri(row[9], db_list)
                if re.search(r"taxid:\s?-1.+", row[9]):
                    blanck_node = BNode()
                    g.add((Interactor_ab, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, in_vitro))
                elif re.search(r"taxid:\s?-2.+", row[9]):
                    blanck_node = BNode()
                    g.add((Interactor_ab, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, chemical_synthesis))
                else:
                    g.add((Interactor_ab, organizm, Taxon_id))
                    g.add((Taxon_id, RDF.type, host_organism))

            if row[9] != "-" and row[9] != "":
                Taxon_id = create_object_uri(row[9], db_list)
                if re.search(r"taxid:\s?-1.+", row[9]):
                    blanck_node = BNode()
                    g.add((Interactor_a, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, in_vitro))
                elif re.search(r"taxid:\s?-2.+", row[9]):
                    blanck_node = BNode()
                    g.add((Interactor_a, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, chemical_synthesis))
                else:
                    g.add((Interactor_a, organizm, Taxon_id))
                    g.add((Taxon_id, RDF.type, host_organism))

            if row[10] != "-" and row[10] != "":
                Taxon_id = create_object_uri(row[10], db_list)
                if re.search(r"taxid:\s?-1.+", row[10]):
                    blanck_node = BNode()
                    g.add((Interactor_b, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, in_vitro))
                elif re.search(r"taxid:\s?-2.+", row[10]):
                    blanck_node = BNode()
                    g.add((Interactor_b, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, chemical_synthesis))
                elif re.search(r"taxid:\s?-3.*", row[10]):
                    blanck_node = BNode()
                    g.add((Interactor_b, organizm, blanck_node))
                    g.add((blanck_node, RDF.type, unidentified))
                else:
                    g.add((Interactor_b, organizm, Taxon_id))
                    g.add((Taxon_id, RDF.type, host_organism))

            if row[11] != "-" and row[11] != "":
                Interaction_type = create_object_uri(row[11], db_list)
                g.add((Interactor_ab, has_interaction_type_bp, Interaction_type))
                g.add((Interactor_ab, has_interaction_type_obo, Interaction_type))

            if row[12] != "-" and row[12] != "":
                Source_database = create_object_uri(row[12], db_list)
                g.add((Interactor_ab, souce_db, Source_database))

            if row[13] != "-" and row[13] != "":
                Interaction_id = create_object_uri(row[13], db_list)
                g.add((Interactor_ab, has_interaction_id, Interaction_id))
                g.add((Interaction_id, RDF.type, interaction_id))

        g.serialize(
            destination="turtle/" + service + "/" + file_name + ".ttl",
            format="turtle",
        )


def main(dir_name: str):
    services_list = gm.list_serveice()
    for service in services_list:
        try:
            shutil.rmtree("turtle/" + service)
        except:
            pass
        try:
            os.mkdir("turtle/" + service)
        except:
            pass
        dir_list = glob.glob(dir_name + service + "/*.tsv", recursive=True)
        for i in range(len(dir_list)):
            print("... create ttl from", dir_list[i], "\t", i + 1, "/", len(dir_list))
            create_ttl(dir_list[i], service + str(i), service)


if __name__ == "__main__":
    print("start create ttl")
    dir_name = "turtle/"
    main(dir_name)
