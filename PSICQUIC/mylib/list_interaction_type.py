import csv
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from mylib import general_method as gm
from mylib.psiquic_class import PQdataList, PQdata


def list_interaction_typs(dirname):
    services_list = gm.list_serveice()
    column_label = gm.list_column_label()
    pqdatalist = PQdataList()

    interaction_ids = []
    for service in services_list:
        dir_name = dirname + service + "/" + service
        with open(dir_name + ".tsv") as f1:
            reader = csv.reader(f1, delimiter="\t")
            header = next(reader)
            # print("file: ", dir_name + ".txt", "\tdata: ", header[11])
            for row in reader:
                if row[11] not in interaction_ids:
                    interaction_ids.append(row[11])
    for interaction_id in interaction_ids:
        print(interaction_id)


if __name__ == "__main__":
    dirname = "test_data/"
    list_interaction_typs(dirname)
