from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    protacxn: Q9HC98
    geneid: 10783
    ligand: compound 22 [PMID: 20462760]
    ligandid: 8205
    cid: 24863112
    primarytarget: No
    type: Inhibitor
    action: Inhibition
    units: -
    affinity: 5.78
    pmids: 20462760
    targetid: 2121
    targetname: NIMA related kinase 6
    targetspecies: Human
    genesymbol: NEK6
    cmpdname: N-(7-Chloro-1-oxo-1,2-dihydroisoquinolin-6-yl)-2-(cyclopropylamino)-2-phenylacetamide
    dois: 10.1016/j.bmcl.2010.04.07
    """

    protein = id2uri(row["protacxn"], "protein")
    gid = id2uri(row["geneid"], "gid")
    cid = id2uri(row["cid"], "cid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, protein, RDF.type, u.protein)
    g_add_with_valid(g, protein, u.protein2gid, gid)

    g_add_with_valid(g, gid, RDF.type, u.gid)
    g_add_with_valid(g, gid, u.gid2pmid, pmid)

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    
    return g

