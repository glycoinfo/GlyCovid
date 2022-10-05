# glycovid_PubChem
## RDF schema
![RDF schema](img/schema.png)

## Content
```
# Scrape PubChem data resorces
python rdf.py

## Purpose
PubChemサイトのcovid19ページからプロジェクトで必要なデータである遺伝子、タンパク質、パスウェイの情報をcsvファイルとしてダウンロードする。次にそのファイルからRDFを作るために不必要なデータを削除し整形する。最後に、ファイルを種類別に統合させて一つのファイルにする。それぞれの過程を実行するプログラムをPythonの言語によって実装した。

## Steps

### Step1 スクレイピング
＊まず上記のPubchemページへアクセスし、タブ"gene"をクリックする。https://pubchem.ncbi.nlm.nih.gov/#query=covid-19&tab=gene
そして、右側のSummaryというボタンを押し、csvファイルをダウンロードする。このcsvファイルにはcovid19に関連するすべての遺伝子情報が含まれており、PubChem独自のIDで管理されている。

＊次に、rdf.pyのscrape()関数を実行する。ただし、chromedriverを使ったブラウザクローリングを行うスクレイピングのため、GooggleChromeとchromedriverのバージョンを同期しておく必要がある。また、chromedriverは実行する環境下のディレクトリで管理する必要がある。scrape()関数内で、絶対パスを通す必要がある。

### Step2 ディレクトリ作成
＊スクレイピング後、ファイルを一つにするプログラムを実行するためにそれぞれのファイルを種類別のディレクトリに移動する。rdf.pyのmkdir()関数で実行される。ただし、実行する環境内で、事前に空のディレクトリを準備しておく必要がある。ディレクトリ名は、pdb, bioactive_gene, drugbank, chembldrug, gtopdb, bioassay, gene-disease, dgidb, ctdchemicalgene, pathwayreaction, pathwaygeneである。

### Step3 csvファイルの結合
種類別にcsvファイルを管理できたあと、不必要なカラムは落とし、ファイルを一つに結合する。rdf.pyのmk_csv_for_togo()関数で実行される。
