import re
import glob
import shutil
import os
import copy
import sys
from glob import glob
import re


def main(file_list):
    try:
        shutil.rmtree('data/test/')
    except:
        pass
    os.mkdir('data/test')

    bef_dir = './data/2021-07-28/dir/'
    aft_dir = './data/2021-09-05/dir/'
    for i in range(len(file_list)):
        with open(bef_dir + file_list[i], 'r') as f:
            bef_fileText = f.read()
        with open(aft_dir + file_list[i], 'r') as f:
            aft_fileText = f.read()
            aft_fileText_list = aft_fileText.split('\n')
        diff_text = aft_fileText_list[0] + '\n'
        for l in range(len(aft_fileText_list)):
            if aft_fileText_list[l] not in bef_fileText:
                diff_text += aft_fileText_list[l] + '\n'

        with open('./data/test/' + file_list[i], "w") as f:
            f.write(diff_text)
        print(file_list[i], 'complete!!')


def countrow(file_list):
    bef_dir = './data/2021-07-28/dir/'
    aft_dir = './data/2021-10-14/dir/'
    diff_dir = './data/test/'
    for i in range(len(file_list)):
        print(file_list[i], end="")
        with open(bef_dir + file_list[i], 'r') as f:
            bef_fileText = f.read()
            print(',', len(bef_fileText.split('\n')), end="")
        with open(aft_dir + file_list[i], 'r') as f:
            aft_fileText = f.read()
            print(',', len(aft_fileText.split('\n')), end="")
        with open(diff_dir + file_list[i], 'r') as f:
            diff_fileText = f.read()
            print(',', len(diff_fileText.split('\n')), end="")
        print()


def get_genedir_diff():
    bef_dir = "data/2021-07-28/gene"
    aft_dir = "data/2021-09-05/gene"

    files = os.listdir(bef_dir)
    bef_folders = [f for f in files if os.path.isdir(os.path.join(bef_dir, f))]
    print("bef: ", len(bef_folders))
    files = os.listdir(aft_dir)
    aft_folders = [f for f in files if os.path.isdir(os.path.join(bef_dir, f))]
    print("aft: ", len(aft_folders))

    result1 = list(set(bef_folders) - set(aft_folders))
    print("消去されたid?")
    print("bef - aft = ", result1)
    result2 = list(set(aft_folders) - set(bef_folders))
    print("追加されたid?")
    print("aft - bef = ", result2)


def get_rownum_of_genelist():
    bef_dir = "data/2021-07-28/gene"
    aft_dir = "data/2021-09-05/gene"
    files = os.listdir(bef_dir)
    bef_folders = [f for f in files if os.path.isdir(os.path.join(bef_dir, f))]
    files = os.listdir(aft_dir)
    aft_folders = [f for f in files if os.path.isdir(os.path.join(bef_dir, f))]

    bef_dirs = []
    for foldname in bef_folders:
        files = glob(bef_dir + "/" + foldname + "/*.csv")
        bef_dirs += files
    aft_dirs = []
    for foldname in aft_folders:
        files = glob(aft_dir + "/" + foldname + "/*.csv")
        aft_dirs += files
    bef_dirs = glob(bef_dir + "/6137/*.csv")
    aft_dirs = glob(aft_dir + "/6137/*.csv")

    file_list = [
        'pathwaygene',
        'bioactivity_gene',
        'ctdchemicalgene',
        'gene_disease',
        'pathwayreaction',
        'bioassay',
        'dgidb',
        'gtopdb',
        'pdb',
        'chembldrug',
        'drugbank',
    ]
    bef_dirs = [dirname.split("/gene/")[1] for dirname in bef_dirs
                if re.split("[\s\.]", dirname.split("_")[-1])[0] in file_list]
    aft_dirs = [dirname.split("/gene/")[1] for dirname in aft_dirs
                if re.split("[\s\.]", dirname.split("_")[-1])[0] in file_list]

    both_exis = list(set(bef_dirs) & set(aft_dirs))
    bef_only = list(set(bef_dirs) - set(aft_dirs))
    aft_only = list(set(aft_dirs) - set(bef_dirs))
    print("7-28 only: ", bef_only)
    print("9-05 only: ", aft_only)
    print("overlap: ", both_exis)
    print("7-28 only: ", len(bef_only), "\t", "9-05 only: ",
          len(aft_only), "overlap :", len(both_exis))


if __name__ == '__main__':
    file_list = [
        'pathwaygene_s.csv',
        'bioactivity_gene_s.csv',
        'ctdchemicalgene_s.csv',
        'gene_disease_s.csv',
        'pathwayreaction_s.csv',
        'bioassay_s.csv',
        'dgidb_s.csv',
        'gtopdb_s.csv',
        'pdb_s.csv',
        'chembldrug_s.csv',
        'drugbank_s.csv',
    ]

    # main(file_list)
    # countrow(file_list)

    # get_genedir_diff()
    # get_rownum_of_genelist()

    f = open("data/2022-07-22/dir/gene_disease_s.csv")
    srcdb = {}
    contents = f.read()
    rows = contents.split("\n")
    for row in rows:
        cols = row.split(",")
        if len(cols) < 2:
            continue
        try:
            srcdb[cols[2]] += 1
        except:
            srcdb[cols[2]] = 0
    print(srcdb)

