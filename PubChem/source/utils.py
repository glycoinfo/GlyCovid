from rdflib import URIRef

from copy import copy
import re


def uri_ref():
    return {
        #############################
        # predicate
        #############################
        "detected_by": URIRef("http://www.bioassayontology.org/bao#BAO_0002875"),
        "pub_id": URIRef("http://purl.obolibrary.org/obo/IAO_0000119"),
        "has_interaction_type_obo": URIRef(
            "http://purl.obolibrary.org/obo/INO_0000154"
        ),
        "has_interaction_type_bp": URIRef(
            "http://www.biopax.org/release/biopax-level3.owl#interactionType"
        ),
        "souce_db": URIRef("http://purl.org/dc/elements/1.1/source"),
        "has_interaction_id": URIRef("http://purl.org/dc/elements/1.1/identifier"),
        "organizm": URIRef("http://semanticscience.org/resource/SIO_000253"),
        "has_interactorA": URIRef(
            "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"
        ),
        "has_interactorB": URIRef(
            "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"
        ),
        #############################
        # classes
        #############################
        "molecular_interaction": URIRef("http://biomodels.net/SBO/SBO_0000344"),
        "publication_identifier": URIRef("http://purl.obolibrary.org/obo/NCIT_C93638"),
        "interaction_id": URIRef(
            "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"
        ),
        "functional_entiry": URIRef("http://biomodels.net/SBO/SBO_0000241"),
        "host_organism": URIRef("http://purl.obolibrary.org/obo/EUPATH_0000591"),
        "in_vitro": URIRef("http://www.bioassayontology.org/bao#BAO_0020008"),
        "chemical_synthesis": URIRef("http://semanticscience.org/resource/SIO_000559"),
        "unidentified": URIRef(
            "http://purl.bioontology.org/ontology/SNOMEDCT/69910005"
        ),
    }


def has_bar_in_row(row):
    for column in row:
        if "|" in column:
            return True
    return False


def has_bar_in_row_list(row_list: list):
    for row in row_list:
        if has_bar_in_row(row):
            return True
    return False


def expansion_tsv_row(row_list: list):
    result_list = []
    for row in row_list:
        if has_bar_in_row(row):
            for i in range(len(row)):
                if "|" in row[i]:
                    row_a = copy(row)
                    row_a[i] = re.split("|", row[i])[0]
                    row_b = copy(row)
                    row_b[i] = re.split("[|\t$]", row[i])[1]
                    result_list.append(row_a)
                    result_list.append(row_b)
                    break
        else:
            result_list.append(row)

    if has_bar_in_row_list(result_list):
        result_list = expansion_tsv_row(result_list)
    return result_list
