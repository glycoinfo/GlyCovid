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


def delete_patywayreaction_in_pathwaygene_deirectory(d_today):
    l_pathwayreaction = glob.glob(
        ".//data/" + d_today + "/dir/pathwaygene/*_pathwayreaction*.csv", recursive=True)
    for i in range(len(l_pathwayreaction)):
        os.remove(l_pathwayreaction[i])
        print('removed -> ', l_pathwayreaction[i])


def curate_file_conmma_inquote(d_today):
    l_pathwayreaction = glob.glob(
        "./data/" + d_today + "/dir/pathwaygene/*_pathway*.csv", recursive=True)
    for i in range(len(l_pathwayreaction)):
        with open(l_pathwayreaction[i], 'r') as f:
            fileText = f.read()
            pre = fileText
            fileText = fileText.replace('\t', '')
            fileText = fileText.replace('   ', '')
        if(pre != fileText):
            print('replace: ', l_pathwayreaction[i])
            with open(l_pathwayreaction[i], "w") as f:
                f.write(fileText)
    l_pathwayreaction = glob.glob(
        "./data/" + d_today + "/dir/pathwayreaction/*_pathwayreaction.csv", recursive=True)
    for i in range(len(l_pathwayreaction)):
        with open(l_pathwayreaction[i], 'r') as f:
            fileText = f.read()
            pre = fileText
            fileText = fileText.replace('\t', '')
            fileText = fileText.replace('   ', '')
        if(pre != fileText):
            print('replace: ', l_pathwayreaction[i])
            with open(l_pathwayreaction[i], "w") as f:
                f.write(fileText)


def make_csv_for_togo():
    # csv内の文字列を分割する必要のあるcolumnsのdict
    columns_dict = {
        'data/dir/bioactivity_gene': [],
        "data/dir/bioassay": ["pmids"],
        "data/dir/chembldrug": ["pmids", "dois"],
        "data/dir/ctdchemicalgene": ["pmids"],
        "data/dir/dgidb": ["pmids", "dois"],
        "data/dir/drugbank": ["pmids", "dois"],
        "data/dir/gene_disease": ["pmids", "dois"],
        "data/dir/gtopdb": ["pmids", "dois"],
        "data/dir/pathwaygene": ["pmids"],
        "data/dir/pathwayreaction": ["pmids"],
        "data/dir/pdb": ["pmids", "dois"]
    }
    # RDF作成上必要のないcolumnsのdict
    droplist = [
        ["aidtype", "aidmdate", "hasdrc", "rnai", "acname",
            "acvalue", "aidsrcname", "cmpdname", "ecs", "repacxn"],
        ["aiddesc", "aidsrcid", "aidsrcname", "aidmdate", "cids", "sids", "geneids",
            "aidcategories", "protacxns", "depcatg", "rnai", "ecs", "repacxns", "annotation"],
        ["moa", "action"],
        ["genesymbol", "taxname", "interaction"],
        ["geneclaimname", "interactionclaimsource", "interactiontypes",
            "drugclaimname", "drugclaimprimaryname"],
        ["genesymbol", "drugtype", "druggroup", "drugaction", "targettype", "targetid",
            "targetcomponent", "targetcomponentname", "generalfunc", "specificfunc"],
        ["genesymbol", "directevidence"],
        ["ligand", "primarytarget", "type", "action", "units",
            "affinity", "targetname", "targetspecies", "genesymbol"],
        ["pwtype", "category", "srcid", "extid", "core", "cids",
            "geneids", "protacxns", "ecs", "annotation"],
        ["cids", "geneids", "protacxns", "ecs"],
        ["resolution", "expmethod", "lignme", "cids", "protacxns", "geneids"]
    ]

    i = 0
    for directory, columns in columns_dict.items():
        # csvファイルは任意のディレクトリに保存
        file_list = glob.glob(f'{directory}/*.csv')
        print(f'Number of files: {len(file_list)}')

        for file_name in file_list:
            print(file_name)
            df = pd.read_csv(file_name)
            # df = df.drop(droplist[i], axis=1)
            new_df = pd.DataFrame(columns=df.columns)

            for index in tqdm(df.index, desc=file_name):
                data = df.iloc[index].to_dict()
                # 一つのセルに|,で区切られた複数のidを分割し、それぞれ新しい行にする
                for data_set in itr.product(*[filter(lambda a: a != '', re.split('[|,]', str(data[column]))) for column in columns]):
                    for column, value in zip(columns, data_set):
                        data[column] = value
                    new_df = new_df.append(data, ignore_index=True)

            new_df.to_csv(f'{directory}_s.csv', index=False,
                          mode='a', header=file_name == file_list[0])
        i += 1


def getColumnNum(bar_column_list, column_num=-1):
    # 初期化
    if column_num == -1:
        column_num = [copy.deepcopy(bar_column_list)]
        for i in range(len(column_num[0])):
            column_num[0][i]['count'] = 0
    # 終了判定
    done = True
    for i in range(len(bar_column_list)):
        if bar_column_list[i]['count'] != column_num[-1][i]['count']:
            done = False
    if done:
        return column_num
    # カラムのカウント
    column_num.append(copy.deepcopy(column_num[-1]))
    column_num[-1][-1]['count'] += 1
    for i in range(len(column_num[-1])):
        if(column_num[-1][-1 * i]['count'] > bar_column_list[-1 * i]['count']):
            column_num[-1][-1 * i]['count'] = 0
            column_num[-1][-1 * i - 1]['count'] += 1
    getColumnNum(bar_column_list, column_num)
    return column_num


def sepalateBar(fileText):
    if '|' not in fileText:
        return fileText

    fileText_list = fileText.split('\n')
    bar_row_list = []
    for l in range(len(fileText_list)-1, 0, -1):
        if '|' in fileText_list[l]:
            bar_row_list.append(fileText_list[l])
            fileText_list.pop(l)
    for bar_row in bar_row_list:
        bar_column_list = []
        column_list = bar_row.split(',')
        for l in range(len(column_list)):
            bar_count = column_list[l].count('|')
            if bar_count > 0:
                bar_column_list.append({'num': l, 'count': bar_count})

    result = getColumnNum(bar_column_list)

    for l in range(len(result)):
        print(l, ':\t', result[l])
    print(bar_column_list)

    fileText = '\n'.join(fileText) + ','
    row_list = fileText.split('\n')
    row_count = 0
    for row in row_list:
        for pattern in result:
            fileText = fileText[0:-1] + '\n'
            columns = row.split(',')
            for i in range(len(columns)):
                no_bar = True
                for r in pattern:
                    if i == r['num']:
                        no_bar = False
                        fileText += columns[r['num']
                                            ].split('|')[r['count']] + ','
                    if no_bar:
                        fileText += columns[i] + ','
        print('->', row_count, '/', len(row_list))
        row_count += 1
    return fileText


def curate_csv_file():
    file_list = glob.glob("./data/dir/*_s.csv", recursive=True)
    for i in range(len(file_list)):
        with open(file_list[i], 'r') as f:
            fileText = f.read()
            # 行の最後が,で終わっている場合エラーになるのでnanにする
            fileText = re.sub('\,\\n', ',nan\n', fileText)
            fileText = re.sub(' ', '', fileText)
            fileText = re.sub('　', '', fileText)
            # |で区切られている列を複製して分割
            # if '|' in fileText:
            #     print(file_list[i], 'has |')
            # fileText = sepalateBar(fileText)

        # with open(file_list[i], "w") as f:
        with open('./data/test/' + file_list[i].split('/')[-1], "w") as f:
            f.write(fileText)

        print('Done: ', file_list[i])


if __name__ == "__main__":
    get_new_gene_file()
    gene_list = get_new_gene_list()

    scrape(gene_list)
    delete_patywayreaction_in_pathwaygene_deirectory()
    curate_file_conmma_inquote()
    make_csv_for_togo()

    curate_csv_file()
