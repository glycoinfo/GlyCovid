from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    mecid: 4919
    cid: 51049968
    chemblid: CHEMBL2178422
    drugname: RIMEGEPANT
    moa: Calcitonin gene-related peptide type 1 receptor antagonist
    action: ANTAGONIST
    targetchemblid: CHEMBL3798
    targetname: Calcitonin gene-related peptide type 1 receptor
    protacxns: Q16602
    geneids: 10203
    pmids: 23153230
    cmpdname: Rimegepant
    dois: 10.1021/jm3013147
    """

    cid = id2uri(row["cid"], "cid")
    chembl = id2uri(row["chemblid"], "chembl")
    protein = id2uri(row["protacxns"], "protein")
    gid = id2uri(row["geneids"], "gid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)
    g_add_with_valid(g, cid, u.cid2chembl, chembl)

    g_add_with_valid(g, chembl, RDF.type, u.chembl)

    g_add_with_valid(g, protein, RDF.type, u.protein)
    g_add_with_valid(g, protein, u.protein2gid, gid)

    g_add_with_valid(g, gid, RDF.type, u.gid)
    g_add_with_valid(g, gid, u.gid2pmid, pmid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

