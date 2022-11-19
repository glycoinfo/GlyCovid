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

from .uri_ref import uri_ref

def create_ttl(dir_name):
    g = Graph()
    u =uri_ref.uri_ref()

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


        g.serialize(
            destination="turtle/bioactivity_gene.ttl",
            format="turtle",
        )


