from rdflib.namespace import RDF
from rdflib import Graph, Literal, Namespace, URIRef, BNode
import csv
import json
import traceback

from copy import copy
import re


def g_add_with_valid(g, s, p, o):
    if s and o:
        try:
            g.add((s, p, o))
        except:
            traceback.print_exc()
            print("Triple:", s, p, o)
            print("---------------------------------")
    return g


def uri_ref():
    u = type(
        "URIRef",
        (object,),
        {
            #############################
            # predicate
            #############################
            "sid2cid": URIRef("http://semanticscience.org/resource/CHEMINF_000477"),
            "sid2chembl": URIRef("http://www.w3.org/2004/02/skos/core#exactMatch"),
            "sid2pmid": URIRef("http://purl.org/spar/cito/isDiscussedBy"),
            "gid2pmid": URIRef("http://purl.org/spar/cito/isDiscussedBy"),
            "gid2pdb": URIRef("http://rdf.wwpdb.org/schema/pdbx-v40.owl#link_to_pdb"),
            "gid2disease": URIRef("http://www.w3.org/2000/01/rdf-schema#seeAlso"),
            "gid2pathway": URIRef("http://purl.obolibrary.org/obo/RO_0000056"),
            "protein2gid": URIRef("https://www.uniprot.org/core/encodedBy"),
            "protein2uniprot": URIRef("http://www.w3.org/2004/02/skos/closeMatch"),
            "protein2pathway": URIRef("http://purl.obolibrary.org/obo/RO_0000056"),
            "pathway2soure": URIRef("http://purl.org/dc/terms/source"),
            "cid2pathway": URIRef("http://purl.obolibrary.org/obo/RO_0000056"),
            "cid2drugbank": URIRef("http://www.w3.org/2004/02/skos/exactMatch"),
            "cid2chembl": URIRef("http://www.w3.org/2004/02/skos/exactMatch"),
            #############################
            # classes
            #############################
            "protein": URIRef("https://www.uniprot.org/core/Protein"),
            "gid": URIRef("http://www.biopax.org/release/biopax-level3.owl#Gene"),
            "cid": URIRef("http://purl.obolibrary.org/obo/CHEBI_24431"),
            "sid": URIRef("http://purl.obolibrary.org/obo/CHEBI_24431"),
            "pmid": URIRef("http://purl.org/spar/fabio/JournalArticle"),
            "disease": URIRef("http://id.nlm.nih.gov/mesh/vocab#Concept"),
            "chembl": URIRef("http://semanticscience.org/resource/CHEMINF_000412"),
            "drugbank": URIRef("http://semanticscience.org/resource/CHEMINF_000406"),
            "source": URIRef("http://purl.org/dc/terms/Dataset"),
            # "pathway": URIRef(
            #     "http://www.biopax.org/release/biopax-level3.owl#Pathway"
            # ),
            # "pdb": URIRef("https://rdf.wwpdb.org/schema/pdbx-v50.owl#datablock"),
            # "glycan": URIRef("glycan:Saccharide"),
        },
    )
    return u


def is_uniprot_id(id: str) -> bool:
    if re.match(
        r"^([A-NR-Z][0-9](?:[A-Z][A-Z0-9][A-Z0-9][0-9]){1,2}(?:-\d+)?)|([OPQ][0-9][A-Z0-9][A-Z0-9][A-Z0-9][0-9](?:-\d+)?)(?:\.\d+)?$",
        id,
    ):
        return True
    # print("Not match with Uniprot ID: ", id)
    return False


def is_correct_id(id: str) -> bool:
    if id == "NULL" or id == "" or id == "=":
        return False
    return True


def id2uri(id: str, source: str):
    uri_set = {
        "sid": "http://rdf.ncbi.nlm.nih.gov/pubchem/substance/",
        "gid": "http://rdf.ncbi.nlm.nih.gov/pubchem/gene/",
        "cid": "http://rdf.ncbi.nlm.nih.gov/pubchem/compound/",
        "pmid": "https://identifiers.org/pubmed:",
        "disease": "https://id.nlm.nih.gov/mesh/",
        "pathway": "http://rdf.ncbi.nlm.nih.gov/pubchem/pathway/",
        "drugbank": "https://identifiers.org/drugbank:",
        "chembl": "http://rdf.ebi.ac.uk/resource/chembl/molecule/",
        "glycan": "http://rdf.glycoinfo.org/glycan/",
        "protein": "http://rdf.ncbi.nlm.nih.gov/pubchem/protein/",
        "uniprot": "http://purl.uniprot.org/uniprot/",
        "pdb": "https://rdf.wwpdb.org/pdb/",
        "source": "http://rdf.ncbi.nlm.nih.gov/pubchem/source/",
    }
    # validate uniprot id
    id = re.sub(r"\s", "", id)
    if not is_correct_id(id):
        return False
    if source == "protein" and not is_uniprot_id(id):
        return False
    uri_header = uri_set[source]
    uri = uri_header + id
    return URIRef(uri)


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
