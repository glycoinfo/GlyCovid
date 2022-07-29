import glob
import os
import re
import shutil
import sys

# Ignore artifacts:
sys.path.append("/Users/kouiti/localfile/glycovid/glycovid_PSIQUIC")

from mylib import general_method as gm


def toURI(text: str, prefix):
    if text[0:1] == "<" and text[-1:] == ">":
        return text
    else:
        for key in prefix:
            if re.match(r"^" + key, text):
                text = text.replace(key, prefix[key][:-1], 1)
                text += ">"
                return text
    print("error: in toURI: ", text)
    sys.exit()


def create_owl(file: str, out_dir: str, s: str, po: dict) -> None:
    with open(file) as f:
        isRdf = False
        prefix = dict()
        rdfs = list()
        for line in f:
            if line == "\n":
                if isRdf:
                    rdfs.append(rdf)
                rdf = []
                isRdf = True
                continue
            if not isRdf:
                cols = line.split(" ")
                prefix[cols[1]] = cols[2]
            else:
                line = line.replace("\n", "")
                rdf.append(line)
            if line == "\n":
                rdfs.append(rdf)
                rdf = []
                isRdf = True
                continue
    owl_list = list()
    for rdf in rdfs:
        owl_s_list = list()
        assert len(rdf) > 1, "Rdf import error !"
        for r in rdf:
            col = re.split(r"\s+", r)
            if col[-1][-1] == ",":
                col[-1] = col[-1][0:-1]
                col.append(",")
            # print(col)
            # spo
            if len(col) == 4:
                if col[0] != "":
                    uri = toURI(col[0], prefix)
                    create_spo(col, owl_s_list, s, po, uri)
                    uri = toURI(col[2], prefix)
                    prouri = toURI(col[1], prefix)
                    create_spo(col, owl_list, s, po, uri, prouri)
                    owl_s_list.append("\t" + prouri + " " + uri + " ;")
                else:
                    uri = toURI(col[2], prefix)
                    prouri = toURI(col[1], prefix)
                    create_spo(col, owl_list, s, po, uri, prouri)
                    owl_s_list.append("\t" + prouri + " " + uri + " ;")
            # po
            elif len(col) == 3:
                uri = toURI(col[1], prefix)
                create_spo(col, owl_list, s, po, uri, prouri)
                owl_s_list.append("\t" + prouri + " " + uri + " ;")
            else:
                print("error >>", len(col), col)
                sys.exit()
        owl_s_list[-1] = owl_s_list[-1][:-1] + "."
        owl_list.extend(owl_s_list)
        owl_list.append("")
        owl_list.append("")
        # break
    with open("owl/03_03/psicquic_temp_03_03.owl") as f:
        temp_text = f.read()
    with open(
        out_dir + "/" + file.split("/")[-1].split(".")[0] + ".owl.ttl", mode="w"
    ) as f:
        f.write(temp_text + "\n\n")
    # print("------------------------------\n")
    with open(
        out_dir + "/" + file.split("/")[-1].split(".")[0] + ".owl.ttl", mode="a"
    ) as f:
        for line in owl_list:
            f.write(line + "\n")
            # print(line)


def create_spo(
    col: list, owl_list: list, s: str, po: dict, uri: str, property: str = None
) -> None:
    if property is None:
        owl_list.append("### " + uri)
        owl_list.append(uri + " rdf:type owl:NamedIndividual ,")
        owl_list.append("\t\t" + s + " ;")
        return
    for p in po:
        if property == p:
            owl_list.append("### " + uri)
            owl_list.append(uri + " rdf:type owl:NamedIndividual ,")
            owl_list.append("\t\t" + po[p] + " .")
            owl_list.append("")
            owl_list.append("")
            return
    if (
        re.match(r".+/MI_\d+>", uri)
        or uri == "http://www.bioassayontosiyousuru.org/bao#BAO_0020008"
        or uri == "http://semanticscience.org/resource/SIO_000559"
    ):
        return
    # print(col)
    print("error: create_spo", uri, property)
    sys.exit()


def main(dirname: str, test: bool):
    s = "<http://www.biopax.org/release/biopax-level3.owl#MolecularInteraction>"
    po = {
        "<http://purl.obolibrary.org/obo/IAO_0000119>": "<http://purl.obolibrary.org/obo/NCIT_C93638>",
        # "obo:INO_0000154": "",
        "<http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A>": "<http://biomodels.net/SBO/SBO_0000241>",
        "<http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B>": "<http://biomodels.net/SBO/SBO_0000241>",
        # "bpo:interactionType": "",
        "<http://semanticscience.org/resource/SIO_000253>": "<http://purl.obolibrary.org/obo/EUPATH_0000591>",
        "<http://purl.org/dc/elements/1.1/identifier>": "<http://rdf.glycoinfo.org/ontology/interaction#InteractionId>",
        # "dc:source": "",
        # "bao:BAO_0002875": "",
    }
    services_list = gm.list_serveice()
    for service in services_list:
        try:
            os.mkdir(dirname)
        except:
            pass
        try:
            shutil.rmtree(dirname + "/" + service)
        except:
            pass
        try:
            os.mkdir(dirname + "/" + service)
        except:
            pass
        dir_list = glob.glob("turtle/" + service + "/*.ttl", recursive=True)
        for i in range(len(dir_list)):
            print("... create owl from", dir_list[i], "\t", i + 1, "/", len(dir_list))
            create_owl(dir_list[i], dirname + "/" + service, s, po)
            if test:
                break
    try:
        os.mkdir(dirname + "/all")
    except:
        pass
    dir_list = glob.glob("owl/03_03/data/**/*.owl.ttl", recursive=True)
    for i in range(len(dir_list)):
        bef_dir = dir_list[i]
        if "all" in bef_dir:
            continue
        aft_dir = re.sub(r"owl/03_03/data/[^/]+", "owl/03_03/data/all", dir_list[i])
        print("copy", bef_dir, "to", aft_dir)
        shutil.copy(bef_dir, aft_dir)
        # return


if __name__ == "__main__":
    dirname = "owl/03_03/data"
    # main(dirname, True)
    main(dirname, False)
