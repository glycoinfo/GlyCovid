from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

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
    gid = id2uri(row["geneid"], "gid")
    sid = id2uri(row["sid"], "sid")
    cid = id2uri(row["cid"], "cid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, sid, RDF.type, u.sid)

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

