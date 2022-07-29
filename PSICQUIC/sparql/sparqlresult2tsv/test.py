import json
def main():
    with open('test.json') as f:
        data_json = json.load(f)
    text = "child_taxon\tchild_taxon_name\tinteractor\tother_interactor_chebi_uri\tglytoucan_uri\n"
    for dd in  data_json["results"]["bindings"]:
        for d in dd:
            # print(d, dd[d]["value"])
            text += dd[d]["value"] + "\t"
        text += "\n"
    print(text)
    f = open("out.tsv", "w")
    f.write(text)
    f.close()


if __name__ == "__main__":
    main()
