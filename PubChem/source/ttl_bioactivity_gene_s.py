from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json


def create_ttl(g, u, row: dict):
    """
    baid: 99415175
    activity: Active
    aid: 47346
    sid: 103186613
    cid: 44273608
    geneid: 10203
    pmid: 9438028
    aidtype: Confirmatory
    aidmdate: 20181015
    hasdrc: 0
    rnai: 0
    protacxn: Q16602
    acname: IC50
    acqualifier: =
    acvalue: 5
    aidsrcname: ChEMBL
    aidname: CGRP1 receptor affinity on human neuroblastoma cells SK-N-MC, which selectively express the human CGRP1 receptor.
    cmpdname: Yvptdvgseaf
    targetname: CALCRL - calcitonin receptor like receptor (human)
    targeturl: /gene/10203
    ecs: NULL
    repacxn: Q16602
    taxids: NULL
    cellids: NULL
    targettaxid
    """

    sid = id2uri(row["sid"], "sid")
    cid = id2uri(row["cid"], "cid")
    gid = id2uri(row["geneid"], "gid")
    pmid = id2uri(row["pmid"], "pmid")
    protein = id2uri(row["protacxn"], "protein")

    g_add_with_valid(g, sid, RDF.type, u.sid)
    g_add_with_valid(g, sid, u.sid2cid, cid)
    g_add_with_valid(g, sid, u.sid2pmid, pmid)

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, gid, RDF.type, u.gid)
    g_add_with_valid(g, gid, u.gid2pmid, pmid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)

    g_add_with_valid(g, protein, RDF.type, u.protein)
    
    return g


if __name__ == "__main__":
    create_ttl(0,0,0)
