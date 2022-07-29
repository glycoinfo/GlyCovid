import csv
import glob
import os
import re
import shutil
import sys

sys.path.append("/Users/kouiti/localfile/glycovid/glycovid_PSIQUIC")
from mylib import general_method as gm


def toURI(text: str, prefix) -> str:
    if text[0:1] == "<" and text[-1:] == ">":
        return text
    # escape blank node
    elif text == "[]":
        return text
    else:
        for key in prefix:
            if re.match(r"^" + key, text):
                text = text.replace(key, prefix[key][:-1], 1)
                text += ">"
                return text
    print("error: in toURI: ", text)
    sys.exit()


def validate_uri(uri: str, uri_patterns: list, except_json: dict) -> bool:
    isCorrect = False
    for uri_pattern in uri_patterns:
        if re.match(uri_pattern, uri):
            isCorrect = True
    if not isCorrect:
        isExcept = False
        for except_regex in except_json:
            if re.match(except_regex, uri):
                except_json[except_regex] += 1
                isExcept = True
        if not isExcept:
            print("Error in:" + uri)
            sys.exit()
    return isCorrect


def validate_turtle(file: str, uri_pattern: list, except_json: dict) -> None:
    with open(file) as f:
        prefix = dict()
        for line in f:
            if line == "\n":
                break
            cols = line.split(" ")
            prefix[cols[1]] = cols[2]

    with open(file) as f:
        isRdf = False
        for line in f:
            if line == "\n":
                isRdf = True
                continue
            if isRdf:
                col = re.split(r"\s+", line)
                if col[-1] == "":
                    col.pop(-1)
                if col[-1][-1] == ",":
                    col[-1] = col[-1][0:-1]
                    col.append(",")
                if len(col) == 4:
                    if col[0] != "":
                        uri = toURI(col[0], prefix)
                        validate_uri(uri, uri_pattern, except_json)
                        uri = toURI(col[2], prefix)
                        validate_uri(uri, uri_pattern, except_json)
                    else:
                        uri = toURI(col[2], prefix)
                        validate_uri(uri, uri_pattern, except_json)
                # has blank node
                # example: ['', '[', 'a', 'ns5:SIO_000559', '],', '']
                elif len(col) == 6:
                    uri = toURI(col[3], prefix)
                    validate_uri(uri, uri_pattern, except_json)
                # example: ['', 'ns5:SIO_000253', '[', 'a', 'ns5:SIO_000559', ']', ',']
                elif len(col) == 7:
                    uri = toURI(col[4], prefix)
                    validate_uri(uri, uri_pattern, except_json)
                # po
                elif len(col) == 3:
                    uri = toURI(col[1], prefix)
                else:
                    uri = toURI(line[0], prefix)


def get_except_json():
    return {
        # r"<http://rdf.glycoinfo.org/dbid/taxonomy/-2>": 0,
        # r"<http://rdf.glycoinfo.org/dbid/taxonomy/-1>": 0,
        # r"<http://rdf.glycoinfo.org/dbid/taxonomy/-3>": 0,
        r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/uniprot\/[A-Z0-9]+%23PRO_\d+>": 0,
        r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/uniprot\/[A-Z0-9]+-\d+>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/pubmed\/unassigned\d+>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/rigid\/[A-Za-z0-9\+\/]+>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/reactome\/REACT_\d{4}\.\d>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/uniprot\/Missing-Uniprot-ID-for-[A-Z0-9]+>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/ensembl\/Missing-Ensembl-Gene-ID-for-[-@A-Z0-9]+>": 0,
        # r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/ensembl\/Missing-Ensembl-Gene-ID-for-[-@A-Z0-9]+>": 0,
        r"\[\]": 0,
    }


def main():
    services_list = gm.list_serveice()
    uri_pattern = list()
    with open("turtle/errors.yaml", "w") as f:
        f.write("")
    with open("uri_list/object_uri_list2.csv") as f1:
        reader = csv.reader(f1, delimiter="\t")
        for row in reader:
            # uri_pattern.append("<" + row[1] + ".+" + ">")
            uri_pattern.append("<" + row[1] + row[2] + ">")

    for service in services_list:
        dir_list = glob.glob("turtle/" + service + "/*.ttl", recursive=True)
        except_json = get_except_json()
        for i in range(len(dir_list)):
            print(dir_list[i], "checking ...")
            validate_turtle(dir_list[i], uri_pattern, except_json)
        with open("turtle/errors.yaml", "a") as f:
            f.write(service + ":\n")
        for except_regex in except_json:
            with open("turtle/errors.yaml", "a") as f:
                f.write(
                    "\t"
                    + except_regex.replace("\\/", "/")
                    + ":\t"
                    + str(except_json[except_regex])
                    + "\n"
                )


if __name__ == "__main__":
    main()
