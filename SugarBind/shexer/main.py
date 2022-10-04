from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE
import datetime
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

target_classes = [
    "<http://rdf.glycoinfo.org/SugarBind/ontology#ReferencedInteraction>",
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
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
                   }


shaper = Shaper(target_classes=target_classes,
                # raw_graph=raw_graph,
                url_endpoint="http://0.0.0.0:3030/sugarbnid_10_4_2/query",
                # graph_list_of_files_input=["output/referenced_interaction.ttl"],
                input_format=NT,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = f"shexer/shaper{now.strftime('%Y%m%d%H%M%S')}.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.1)

print("Done!")
