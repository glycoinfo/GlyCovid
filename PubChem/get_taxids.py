import collections
from rdf import delete_patywayreaction_in_pathwaygene_deirectory
import time
from tqdm import tqdm
import itertools as itr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback
from selenium.webdriver.chrome.options import Options
import pandas as pd
import re
import glob
import shutil
import os
import copy
import sys
import pathlib
import datetime


def get_taxids(d_today):
    file_list = glob.glob("./data/" + d_today + "/dir/*_s.csv", recursive=True)
    taxid_list = []
    for file_name in file_list:
        print('\n----- file name :', file_name)
        data = pd.read_csv(file_name)
        data = data.dropna()
        try:
            taxids = data[['taxids']].values.tolist()
            taxid_list += taxids 
        except:
            pass
        try:
            taxids = data[['taxid']].values.tolist()
            taxid_list += taxids 
        except:
            pass
    for i in range(len(taxid_list)):
        taxid_list[i] = taxid_list[i][0]
    taxid_list = list(set(taxid_list))
    print(taxid_list)

if __name__ == '__main__':
    d_today = '2021-07-28'
    get_taxids(d_today)
