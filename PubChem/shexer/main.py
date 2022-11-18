from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE, TURTLE
import datetime
import glob

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, "JST")
now = datetime.datetime.now(JST)

target_classes = [
    "http://purl.obolibrary.org/obo/CHEBI_24431",
    "http://togodb.org/ctdchemicalgene_s",
    "http://togodb.org/pathwayreaction_s",
    # "http://togodb.org/dgidb_s__drugchemblid",
    "http://purl.org/spar/fabio/journalArticle",
    # "http://togodb.org/chembldrug_s__drugchemblid",
    "http://id.nlm.nih.gov/mesh/vocab#Concept",
    "http://www.biopax.org/release/biopax-level3.owl#Protein",
    "http://www.biopax.org/release/biopax-level3.owl#Gene",
    "http://semanticscience.org/resource/CHEMINF_000412",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property",
    "http://www.w3.org/2000/01/rdf-schema#Class",
]

namespaces_dict = {
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
    "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
    "http://www.w3.org/2001/XMLSchema#": "xsd",
    "http://rdf.glycoinfo.org/SugarBind/ontology#": "",
    "http://purl.jp/bio/12/glyco/glycan#": "glycan",
    "http://rdf.glycoinfo.org/SugarBind/Id/": "id",
    "http://rdf.glycoinfo.org/ontology/interaction#": "interaction",
    "http://www.w3.org/2002/07/owl#": "owl",
    "http://rdf.glycoinfo.org/glycan/": "glycoinfo",
    "http://purl.jp/bio/12/glyco/glycan#": "glycan",
    "http://purl.obolibrary.org/obo/": "obo",
    "http://xmlns.com/foaf/0.1/": "foaf",
    "http://purl.org/dc/terms/": "dcterms",
    "http://www.w3.org/2004/02/skos/core#": "skos",
    "http://www.ncbi.nlm.nih.gov/pubmed/": "pubmed",
    "http://www.biopax.org/release/biopax-level3.owl#": "bp",
    "http://semanticscience.org/resource/": "cheminf",
    "http://rdf.wwpdb.org/schema/pdbx-v40.owl#": "PDBo",
    "http://id.nlm.nih.gov/mesh/vocab#": "meshv",
    "https://www.uniprot.org/core/": "up",
    "http://purl.org/spar/fabio/": "fabio",
    "http://purl.org/spar/cito/": "cito",
}

graph_list_of_files_input = glob.glob("RDF/pubchem/*")

shaper = Shaper(
    target_classes=target_classes,
    graph_list_of_files_input=graph_list_of_files_input,
    input_format=TURTLE,
    namespaces_dict=namespaces_dict,  # Default: no prefixes
    instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
)

output_file = f"PubChem/shexer/shex_{now.strftime('%Y%m%d%H%M%S')}.shex"

shaper.shex_graph(
    output_file=output_file,
    acceptance_threshold=0.1,
)

print("Done!")
