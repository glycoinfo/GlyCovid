from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import json
import csv
import glob

def create_ttl(g, u, row):
    """
    name: AP-1 transcription factor network
    pwacc: Pathway Interaction Database:ap1_pathway
    pwtype: organism_specific
    category: pathway
    url: http://pid.nci.nih.gov/search/pathway_landing.shtml?pathway_id=ap1_pathway&pathway_name=ap1_pathway&source=NCI-Nature curated&what=graphic&jpg=on
    source: Pathway Interaction Database
    srcid: 4
    externalid: ap1_pathway
    extid: ap1_pathway
    taxid: NULL
    taxname: Homo sapiens
    core: 1
    cids: NULL
    geneids: 58|183|467|573|595|865|983|1027|1029|1278|1385|1386|1437|1499|1758|1843|1906|1958|1997|2033|2099|2113|2167|2353|2354|2355|2624|2697|2908|3091|3105|3458|3491|3558|3565|3567|3569|3576|3586|3725|3726|3727|4094|4097|4312|4318|4502|4602|4609|4773|4878|4922|5179|5328|5728|6347|6667|6934|7040|7054|7076|7157|7205|8061|9988|10018|10987|23373|149603
    protacxns: O00622|O15525|O43521|O75444|P00749|P01019|P01033|P01100|P01106|P01137|P01160|P01210|P01579|P02795|P03372|P03956|P04141|P04150|P04439|P04637|P05112|P05113|P05231|P05305|P05412|P06493|P07101|P08047|P08123|P10145|P10242|P13500|P14780|P14921|P15090|P15336|P15407|P15408|P16220|P17275|P17302|P17535|P18146|P18847|P22301|P23769|P24385|P28562|P30990|P32519|P35222|P42771|P46527|P53539|P60484|P60568|P68133|Q09472|Q13316|Q13469|Q13951|Q15654|Q16665|Q5TA31|Q6UUV9|Q92905|Q99933|Q9NQB0|Q9Y222
    pmids: 1527086|1719551|1749429|1827203|1827665|1945831|2110368|2111020|2111328|2115643|2138276|2467839|2497053|2498083|2504580|2513128|2516828|2825349|2974122|3103098|3130660|3135940|3136397|3142691|3142692|3143919|7623817|8058317|8289796|8397339|8754832|8837781|8875991|8994040|9111306|9349820|9510247|9511728|9878062|9889198|10080190|10359014|10790372|10942775|11756554|12121977|12853483|12881422|14510502|14523011|15308641|15489293|15601844|15699140|15828020|16007074|16518400|17146436|17689131|18247370|18535250|185
    ecs: 1.14.16.2|2.3.1.-|2.3.1.48|2.3.2.27|2.7.11.22|2.7.11.23|3.1.3.16|3.1.3.48|3.1.3.67|3.4.-.-|3.4.21.73|3.4.24.35|3.4.24.7
    annotation: COVID-19, COVID19, Coronavirus, Corona-virus, SARS, SARS2, SARS-CoV, SARS-CoV-2 [as per WikiPathways, DrugBank, UniProt, COVID-19 Disease Map]
    """

    cid = id2uri(row["cids"], "cid")
    gid = id2uri(row["geneids"], "gid")
    protein = id2uri(row["protacxns"], "protein")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)
    
    g_add_with_valid(g, gid, RDF.type, u.gid)

    g_add_with_valid(g, protein, RDF.type, u.protein)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    
    return g

def check_csv_data():
    source_list = []
    data_list = []
    list_csv_file_path = glob.glob(
        f"PubChem/data/dir/pathwaygene/*.csv", recursive=True
    )
    for csv_file_path in list_csv_file_path:
        with open(csv_file_path) as f1:
            reader = csv.reader(f1, delimiter=",")
            next(reader)
            for row in reader:
                if row[5] not in source_list:
                    source_list.append(row[5])
                    data_list.append(row[6])
    for i, source in enumerate(source_list):
        print(source_list[i])
        print("\t- ", data_list[i])
    """
    WikiPathways                                                                                                                                 │
    Reactome                                                                                                                                     │
    PathBank                                                                                                                                     │
    Pathway Interaction Database                                                                                                                 │
    PharmGKB                                                                                                                                     │
    INOH                                                                                                                                         │
    BioCyc
    """

if __name__ == "__main__":
    check_csv_data()
