from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    protacxn: Q16602
    geneid: 10203
    genesymbol: CALCRL
    cid: 6918509
    drugtype: small molecule
    drugname: Olcegepant
    druggroup: investigational
    drugaction: NULL
    drugdetail: DB04869
    targettype: target
    targetid: BE0009009
    targetname: Calcitonin gene-related peptide type 1 receptor
    targetcomponent: Q16602
    targetcomponentname: Calcitonin gene-related peptide type 1 receptor
    generalfunc: Receptor for calcitonin-gene-related peptide (CGRP) together with RAMP1 and receptor for adrenomedullin together with RAMP3 (By similarity). Receptor for adrenomedullin together with RAMP2. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.
    specificfunc: Adrenomedullin receptor activity
    pmids: 28165287
    cmpdname: Olcegepant
    dois: 10.1177/0333102417691762
    """

    protein = id2uri(row["protacxn"], "protein")
    gid = id2uri(row["geneid"], "gid")
    cid = id2uri(row["cid"], "cid")
    drugbank = id2uri(row["drugdetail"], "drugbank")
    pmid = id2uri(row["pmid"], "pmid")

    g_add_with_valid(g, protein, RDF.type, u.protein)

    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, drugbank, RDF.type, u.drugbank)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

