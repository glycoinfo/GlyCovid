from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    resolution: 1.31
    pdbid: 6X8O
    title: BimBH3 peptide tetramer
    expmethod: X-RAY DIFFRACTION
    lignme: SCN
    glytoucan: NULL
    cids: 9322
    protacxns: O43521
    geneids: 10018
    pmids: 32966763
    dois: 10.1016/j.str.2020.09.002
    """

    cid = id2uri(row["cids"], "cid")
    protein = id2uri(row["protacxns"], "protein")
    gid = id2uri(row["geneids"], "gid")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, protein, RDF.type, u.protein)
    g_add_with_valid(g, protein, u.protein2gid, gid)

    g_add_with_valid(g, gid, RDF.type, u.gid)
    g_add_with_valid(g, gid, u.gid2pmid, pmid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)

    return g

