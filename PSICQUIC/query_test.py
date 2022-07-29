from datetime import datetime
import shutil
import os
import xml.etree.ElementTree as ET
from glob import glob
from urllib.request import urlopen


# ------------------ FUNCTIONS ------------------


class PsicquicService:
    def __init__(self, name, restUrl):
        self.name = name
        self.restUrl = restUrl


def readURL(url):
    try:
        fileHandle = urlopen(url)
        content = fileHandle.read()
        fileHandle.close()
    except IOError as e:
        # print('Cannot open URL ' + url)
        import traceback

        error_point = traceback.format_exc().split("\n")[1]
        error_message = traceback.format_exc().split("\n")[-2]
        content = ""
        print(error_message)
    return content


def readActiveServicesFromRegistry():
    registryActiveUrl = "http://www.ebi.ac.uk/Tools/webservices/psicquic/registry/registry?action=ACTIVE&format=xml"

    content = readURL(registryActiveUrl)

    # Create the XML reader
    root = ET.fromstring(content)
    xmlns = "{http://hupo.psi.org/psicquic/registry}"

    services = []

    for service in root.findall(xmlns + "service"):
        name = service.find(xmlns + "name")
        restUrl = service.find(xmlns + "restUrl")

        service = PsicquicService(name.text, restUrl.text)
        services.append(service)

    return services


def queryPsicquic(service_name, psicquicRestUrl, query, offset, maxResults, init):
    interactiontype_except_list = [
        'psi-mi:"MI:0217"(phosphorylation reaction)',
        'psi-mi:"MI:0203"(dephosphorylation reaction)',
        'psi-mi:"MI:1110"(predicted interaction)',
    ]
    dirname = "test_data/" + service_name
    if init:
        try:
            shutil.rmtree(dirname)
        except:
            pass
    try:
        os.mkdir(dirname)
    except:
        pass

    psicquicUrl = (
        psicquicRestUrl
        + "query/"
        + query
        + "?firstResult="
        + str(offset)
        + "&maxResults="
        + str(maxResults)
        + "&format=count"
    )
    max_count = str(readURL(psicquicUrl)).split("'")[1].split("'")[0]
    if max_count == "0":
        print(service_name, "data not found")
        return

    filename = dirname + "/" + service_name + str(0) + ".tsv"

    f = open(filename, "w")
    f.write(
        "Unique identifier for interactor A"
        + "\tUnique identifier for interactor B"
        + "\tAlternative identifier for interactor A"
        + "\tAlternative identifier for interactor B"
        + "\tAliases for A"
        + "\tAliases for B"
        + "\tInteraction detection methods"
        + "\tFirst author"
        + "\tIdentifier of the publication"
        + "\tNCBI Taxonomy identifier for interactor A"
        + "\tNCBI Taxonomy identifier for interactor B"
        + "\tInteraction types"
        + "\tSource databases"
        + "\tInteraction identifier(s)"
        + "\tConfidence score"
    )
    f.close()

    psicquicUrl = (
        psicquicRestUrl
        + "query/"
        + query
        + "?firstResult="
        + str(offset)
        + "&maxResults="
        + str(maxResults)
    )

    print_text = (
        str(datetime.now())
        + "\t>\tloading "
        + service_name
        + "...\t"
        + str(offset)
        + "~"
        + str(maxResults)
        + "\t/ "
        + str(max_count)
        + "\t"
        + str(int(int(offset) / int(max_count) * 100))
        + "%"
    )
    print(print_text)
    psicquicResultLines = readURL(psicquicUrl).splitlines()

    content = ""
    for line in psicquicResultLines:
        line = str(line, encoding="utf8")
        if line.split("\t")[11] not in interactiontype_except_list:
            # content += line + "\n"
            content += "\n" + line
    if len(psicquicResultLines) == 0:
        return

    f = open(filename, "a")
    f.write(content)
    f.close()



def main(query):
    services = readActiveServicesFromRegistry()
    services_list = [
        "BioGrid",
        "bhf-ucl",
        "ChEMBL",
        # "DIP",
        "HPIDb",
        "IntAct",
        "IMEx",
        "mentha",
        "MPIDB",
        "iRefIndex",
        "MatrixDB",
        "MINT",
        "Reactome",
        "Reactome-FIs",
        "EBI-GOA-miRNA",
        "UniProt",
        "MBInfo",
        "BindingDB",
        "VirHostNet",
        "BAR",
        "EBI-GOA-nonIntAct",
        "tfact2gene",
    ]
    import os

    path = os.getcwd()

    print(path)

    for service in services:
        if service.name in services_list:
            queryPsicquic(service.name, service.restUrl, query, 1, 1000, True)


if __name__ == "__main__":
    queryes = ["*"]

    queryes = [
        "species:human"
        + " OR species:9606"
        + " OR taxidA:human"
        + " OR taxidA:9606"
        + " OR taxidB:human"
        + " OR taxidA:9606"
    ]
    queryes[0] = queryes[0].replace(" ", "%20")

    for query in queryes:
        main(query)

