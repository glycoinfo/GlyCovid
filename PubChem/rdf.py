import collections
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


def get_new_gene_file():
    d_today = str(datetime.date.today())
    current_download_url = 'https://pubchem.ncbi.nlm.nih.gov/#query=covid-19&tab=gene'
    options = webdriver.ChromeOptions()
    # デフォルトダウンロードフォルダを変更する
    options.add_experimental_option(
        "prefs", {"download.default_directory": 'datalist_csv'})
    # 自動テストソフトウェアによって制御されていますというメッセージを非表示にする
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # 拡張機能の自動更新をさせない（アプリ側の自動アップデートとドライバーの互換性によるエラーを回避）
    options.add_experimental_option('useAutomationExtension', False)
    # ヘッドレスモードの設定
    options.add_argument('--headless')
    driver = webdriver.Chrome("./chromedriver", chrome_options=options)
    try:
        driver.implicitly_wait(5)
        driver.get(current_download_url)
        driver.find_element_by_tag_name('body').click()
        for i in range(5):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        # JavaScrptの実行
        # downloadのdropdownをクリックして開く
        elements = driver.find_elements_by_xpath(
            '//*[@id="Download"]/div/div[2]')
        elements[0].click()
        # csvを選択してgenelistをダウンロード
        elements = driver.find_elements_by_xpath(
            '//*[@id="collection-results-container"]/div/aside/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/a/span')
        elements[0].click()
        time.sleep(10)
        os.rename('./datalist_csv/PubChem_gene_text_covid-19_summary.csv',
                  './datalist_csv/PubChem_gene_text_covid-19_summary_' + d_today + '.csv')
    except:
        traceback.print_exc()
    finally:
        driver.quit()


def get_new_gene_list():
    d_today = str(datetime.date.today())
    now_genelist = {
            'date': d_today,
            'file_dir': './datalist_csv/PubChem_gene_text_covid-19_summary_' + d_today + '.csv',
            'csv': ""
            }
    now_genelist['csv'] = pd.read_csv(now_genelist['file_dir'])
    current_genelist['csv'] = pd.read_csv(current_genelist['file_dir'])
    gene_list = list(
        set(now_genelist['csv']['geneid']) - set(current_genelist['csv']['geneid']))
    return gene_list


def scrape(gene_list):
    """
    Scrate every gene resource in PubChem web page and save data/gene/ directory
    """
    # 任意のディレクトリを指定
    download_directory = 'data//gene/'
    download_url = 'https://pubchem.ncbi.nlm.nih.gov/gene/'
    # gene_csv = pd.read_csv("./datalist_/Pubchem_gene_text_covid-19.csv")
    for i in range(len(gene_list)):
        print('get new gene ', gene_list[i])
        current_download_directory = download_directory + \
            str(gene_list[i])
        current_download_url = download_url + str(gene_list[i])
        options = webdriver.ChromeOptions()
        # デフォルトダウンロードフォルダを変更する
        options.add_experimental_option(
            "prefs", {"download.default_directory": current_download_directory})
        # 自動テストソフトウェアによって制御されていますというメッセージを非表示にする
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        # 拡張機能の自動更新をさせない（アプリ側の自動アップデートとドライバーの互換性によるエラーを回避）
        options.add_experimental_option('useAutomationExtension', False)
        # ヘッドレスモードの設定
        options.add_argument('--headless')
        driver = webdriver.Chrome("./chromedriver", chrome_options=options)
        try:
            driver.implicitly_wait(5)
            driver.get(current_download_url)
            driver.find_element_by_tag_name('body').click()
            for i in range(100):
                driver.find_element_by_tag_name(
                    'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(7)
            # JavaScriptの実行
            # ダウンロードボタンを押すために邪魔となっているsticky-barをremoveする
            driver.execute_script(
                "document.getElementsByClassName('sticky-bar')[0].remove();")
            elements = driver.find_elements_by_xpath(
                "//button[@data-action='download-section-menu-open']/span")
            for e in elements:
                e.click()
                save_button = driver.find_elements_by_xpath(
                    "//span[text()='CSV']")
                save_button[0].click()
                time.sleep(3)
        except:
            traceback.print_exc()
        finally:
            driver.quit()


def mkdir():
    """
    data/gene/のファイルを分類してdata/dir/に入れていく
    """
    mkdir_dir = 'data/dir/'
    directry = 'data/gene'
    mkdir_tuple = (
        'pdb',
        'bioactivity_gene',
        'drugbank',
        'chembldrug',
        'gtopdb',
        'bioassay',
        'gene_disease',
        'geneinter',
        'dgidb',
        'ctdchemicalgene',
        'pathwayreaction',
        'pathwaygene',
        'rhea'
    )
    for f in mkdir_tuple:
        os.mkdir(mkdir_dir + f)

    # 任意の親ディレクトリに各ファイル用のディレクトリを作成　
    # pdbディレクトリの作成
    l = glob.glob(directry + "/**/*_pdb*.csv", recursive=True)
    for i in range(len(l)):
        new_path = shutil.copy(l[i], mkdir_dir+"pdb")
    # tested compounds (bioactivity gene)ディレクトリの作成
    l_bio_gene = glob.glob(
        directry + "/**/*_bioactivity_gene*.csv", recursive=True)
    for i in range(len(l_bio_gene)):
        new_path_bio_gene = shutil.copy(
            l_bio_gene[i], mkdir_dir+"bioactivity_gene")
    # drugbank drugsディレクトリの作成
    l_drugbank = glob.glob(directry + "/**/*_drugbank*.csv", recursive=True)
    for i in range(len(l_drugbank)):
        new_path_drugbank = shutil.copy(l_drugbank[i], mkdir_dir+"drugbank")
    # chembl drugディレクトリの作成
    l_chembl = glob.glob(
        directry + "/**/*_chembldrugtargets*.csv", recursive=True)
    for i in range(len(l_chembl)):
        new_path_chembl = shutil.copy(l_chembl[i], mkdir_dir+"chembldrug")
    # guide to pharmacology ligands ディレクトリ
    l_gtopdb = glob.glob(directry + "/**/*_gtopdb*.csv", recursive=True)
    for i in range(len(l_gtopdb)):
        new_path_gtopdb = shutil.copy(l_gtopdb[i], mkdir_dir+"gtopdb")
    # bioassay ディレクトリ
    l_bioassay = glob.glob(directry + "/**/*_bioassay*.csv", recursive=True)
    for i in range(len(l_bioassay)):
        new_path_bioassay = shutil.copy(l_bioassay[i], mkdir_dir+"bioassay")
    # ctd gene-disease ディレクトリ
    l_gene_disease = glob.glob(
        directry + "/**/*_ctd_gene_disease*.csv", recursive=True)
    for i in range(len(l_gene_disease)):
        new_path_gene_disease = shutil.copy(
            l_gene_disease[i], mkdir_dir+"gene_disease")
    # gene-gene interaction ディレクトリ
    l_geneinter = glob.glob(
        directry + "/**/*_geneinteractions*.csv", recursive=True)
    for i in range(len(l_geneinter)):
        new_path_geneinter = shutil.copy(l_geneinter[i], mkdir_dir+"geneinter")
    # drug-gene interaction ディレクトリ
    l_dgidb = glob.glob(directry + "/**/*_dgidb*.csv", recursive=True)
    for i in range(len(l_dgidb)):
        new_path_dgidb = shutil.copy(l_dgidb[i], mkdir_dir+"dgidb")
    # ctd chemical-gene interactions ディレクトリ
    l_ctdchemicalgene = glob.glob(
        directry + "/**/*_ctdchemicalgene*.csv", recursive=True)
    for i in range(len(l_ctdchemicalgene)):
        new_path_ctdchemicalgene = shutil.copy(
            l_ctdchemicalgene[i], mkdir_dir+"ctdchemicalgene")
    # pathwayreaction ディレクトリ
    l_pathwayreaction = glob.glob(
        directry + "/**/*_pathwayreaction*.csv", recursive=True)
    for i in range(len(l_pathwayreaction)):
        new_path_pathwayreaction = shutil.copy(
            l_pathwayreaction[i], mkdir_dir+"pathwayreaction")
    # pathwayディレクトリ
    l_pathway = glob.glob(directry + "/**/*_pathway*.csv", recursive=True)
    for i in range(len(l_pathway)):
        new_path_pathway = shutil.copy(l_pathway[i], mkdir_dir+"pathwaygene")
    # RHEAディレクトリ
    l_rhea = glob.glob(directry + "/**/*_rhea*.csv", recursive=True)
    for i in range(len(l_rhea)):
        new_path_rhea = shutil.copy(l_rhea[i], mkdir_dir+"rhea")



if __name__ == "__main__":
    get_new_gene_file()
    gene_list = get_new_gene_list()

    scrape(gene_list)
    mkdir()
