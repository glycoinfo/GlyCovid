import csv
import glob
import os
import re
import shutil
import sys
from copy import copy

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from mylib import general_method as gm
from mylib.psiquic_class import PQdata, PQdataList


def get_target_id(column_data: str, db_name: str):
    if db_name in column_data:
        return (
            column_data.split(db_name + ":")[1]
            .split("(")[0]
            .split("|")[0]
            .replace('"', "")
        )
    else:
        False


def has_bar_in_row(row):
    for column in row:
        if "|" in column:
            return True
    return False


def has_bar_in_row_list(row_list: list):
    for row in row_list:
        if has_bar_in_row(row):
            return True
    return False


def expansion_tsv_row(row_list: list):
    result_list = []
    for row in row_list:
        if has_bar_in_row(row):
            for i in range(len(row)):
                if "|" in row[i]:
                    row_a = copy(row)
                    row_a[i] = re.split("|", row[i])[0]
                    row_b = copy(row)
                    row_b[i] = re.split("[|\t$]", row[i])[1]
                    result_list.append(row_a)
                    result_list.append(row_b)
                    break
        else:
            result_list.append(row)

    if has_bar_in_row_list(result_list):
        result_list = expansion_tsv_row(result_list)
    return result_list


def list2tsv(data: list):
    result = ""
    for i in range(len(data)):
        if i != 0:
            result += "\t"

        if "psi-mi" in data[i]:
            result += data[i].split('"')[1].split(":")[1]
        elif ":" in data[i]:
            result += data[i].split(":")[1].split("(")[0]
        else:
            result += data[i]
    return result


def except_columns(row):
    except_list = [2, 3, 4, 5, 7, 14]
    for i in range(len(row)):
        if i in except_list:
            row[i] = ""
    return row


# barで分けて展開したものをファイルの保存


def expansion_tsv(dirname):
    services_list = gm.list_serveice()
    in_dir = "data/"
    out_dir = "expdata/"
    for service in services_list:
        try:
            shutil.rmtree(dirname + out_dir + service)
        except:
            pass
        try:
            os.mkdir(dirname + out_dir + service)
        except:
            pass
        dir_list = glob.glob(dirname + in_dir + service + "/*.tsv", recursive=True)
        for i in range(len(dir_list)):
            print("... expantion tsv :", dir_list[i], "\t", i + 1, "/", len(dir_list))
            with open(dir_list[i]) as f1:
                reader = csv.reader(f1, delimiter="\t")
                with open(
                    dirname + out_dir + service + "/" + dir_list[i].split("/")[-1],
                    mode="w",
                ) as f:
                    f.write("")
                for row_bef in reader:
                    row_bef = except_columns(row_bef)
                    row_list = expansion_tsv_row([row_bef])
                    # print("------------------------------\n")
                    with open(
                        dirname + out_dir + service + "/" + dir_list[i].split("/")[-1],
                        mode="a",
                    ) as f:
                        for row in row_list:
                            f.write("\t".join(row) + "\n")


if __name__ == "__main__":
    dirname = "/Users/kouiti/localfile/glycovid/glycovid_PSIQUIC/"
    expansion_tsv(dirname)
