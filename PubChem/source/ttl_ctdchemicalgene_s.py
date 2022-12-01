from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

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

    cid = id2uri(row["cid"], "cid")
    gid = id2uri(row["geneid"], "gid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

