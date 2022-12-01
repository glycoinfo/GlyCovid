from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    geneid: 10018
    genesymbol: BCL2L11
    diseasesrcdb: MeSH
    diseaseextid: D015209
    diseasename: Cholangitis, Sclerosing
    directevidence: marker/mechanism
    pmids: 21151127
    dois: 10.1038/ng.728
    """

    gid = id2uri(row["geneid"], "gid")
    disease = id2uri(row["diseaseextid"], "disease") if row["diseasesrcdb"] else False
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, disease, RDF.type, u.disease)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

