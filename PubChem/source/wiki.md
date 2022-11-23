# Data resources each csv files which were scraped

## Sample resources

| Name     | URI |   |
|----------|-----|---|
| sid      |     |   |
| cid      |     |   |
| geneid   |     |   |
| pmid     |     |   |
| protaxon |     |   |


## bioactivity_gene
baid,activity,aid,sid,cid,geneid,pmid,aidtype,aidmdate,hasdrc,rnai,protacxn,acname,acqualifier,acvalue,aidsrcname,aidname,cmpdname,targetname,targeturl,ecs,repacxn,taxids,cellids,targettaxid
99415175,Active,47346,103186613,44273608,10203,9438028,Confirmatory,20181015,0,0,Q16602,IC50,=,5,ChEMBL,"CGRP1 receptor affinity on human neuroblastoma cells SK-N-MC, which selectively express the human CGRP1 receptor.",Yvptdvgseaf,CALCRL - calcitonin receptor like receptor (human),/gene/10203,NULL,Q16602,NULL,NULL,

## bioassay
aid,aidtype,aidname,aiddesc,aidsrcid,aidsrcname,aidextid,aidmdate,cids,sids,geneids,aidcategories,protacxns,depcatg,pmids,rnai,ecs,repacxns,taxids,cellids,targettaxid,annotation
624099,Other,An siRNA screen for human genes that are involved in human papilloma virus (HPV) E2 transcriptional repression of the E6 and E7 oncogenes,"An essential step in the pathogenesis of human papillomavirus (HPV)-associated cancers is the dysregulated expression of the viral oncogenes. The papillomavirus E2 protein can silence the long control region (LCR) promoter that controls viral E6 and E7 oncogene expression. The mechanisms by which E2 represses oncogene expression and the cellular factors through which E2 mediates this silencing are largely unknown. We conducted an unbiased, genome-wide siRNA screen and series of secondary screens that identi",46,"ICCB-Longwood Screening Facility, Harvard Medical School",HMS729,20161014,NULL,56478464|56478466|56478467|56478468|56478469|56478470|56478471|56478472|56478473|56478474|56478476|56478477|56478478|56478479|56478480|56478481|56478483|56478484|56478485|56478486|56478487|56478488|56478489|56478490|56478491|56478492|56478493|56478494|56478495|56478496|56478497|56478498|56478499|56478500|56478501|56478502|56478503|56478504|56478505|56478506|56478507|56478508|56478509|56478510|56478511|56478512|56478513|56478515|56478516|56478517|56478518|56478519|56478520|56478521|56478522|56478523|56478524,1|2|9|10|12|13|14|15|16|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|43|47|48|49|50|51|52|53|54|55|56|58|59|60|70|71|72|81|86|87|88|89|90|91|92|93|94|95|97|98|100|101|102|103|104|105|107|108|109|111|112|113|114|115|116|117|118|119|120|123|124|125|126|127|128|130|131|132|133|134|135|136|140|141|142|143|146|147|148|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|172|173|174|175|176|177|178|181|182|183|185|186|187|189|190|191|196|197|199|202|203|204|205|207|20,RNAi,NULL,Research and Development,20133580|20181716,1,NULL,NULL,NULL,NULL,,NULL

## chembldrug
mecid,cid,chemblid,drugname,moa,action,targetchemblid,targetname,protacxns,geneids,pmids,cmpdname,dois
4919,51049968,CHEMBL2178422,RIMEGEPANT,Calcitonin gene-related peptide type 1 receptor antagonist,ANTAGONIST,CHEMBL3798,Calcitonin gene-related peptide type 1 receptor,Q16602,10203,23153230,Rimegepant,10.1021/jm3013147

## ctdchemicalgene
cid,chemicalid,chemicalname,genesymbol,geneid,taxname,taxid,interaction,pmids
370,D005707,Gallic Acid,BCL2L11,10018,Mus musculus,10090,Gallic Acid results in decreased expression of BCL2L11 mRNA,29205955

## dgidb
geneid,genename,geneclaimname,interactionclaimsource,interactiontypes,sid,cid,drugname,drugclaimname,drugclaimprimaryname,drugchemblid,pmids,cmpdname,dois
10018,BCL2L11,BCL2L11,PharmGKB,NULL,103245522,5291,IMATINIB,imatinib,imatinib,CHEMBL941,24223824,Imatinib,10.1371/journal.pone.0078582

## drugbank
protacxn,geneid,genesymbol,cid,drugtype,drugname,druggroup,drugaction,drugdetail,targettype,targetid,targetname,targetcomponent,targetcomponentname,generalfunc,specificfunc,pmids,cmpdname,dois
Q16602,10203,CALCRL,6918509,small molecule,Olcegepant,investigational,NULL,DB04869,target,BE0009009,Calcitonin gene-related peptide type 1 receptor,Q16602,Calcitonin gene-related peptide type 1 receptor,Receptor for calcitonin-gene-related peptide (CGRP) together with RAMP1 and receptor for adrenomedullin together with RAMP3 (By similarity). Receptor for adrenomedullin together with RAMP2. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.,Adrenomedullin receptor activity,28165287,Olcegepant,10.1177/0333102417691762

## gene_disease
geneid,genesymbol,diseasesrcdb,diseaseextid,diseasename,directevidence,pmids,dois
10018,BCL2L11,MeSH,D015209,"Cholangitis, Sclerosing",marker/mechanism,21151127,10.1038/ng.728

## gtopdb
protacxn,geneid,ligand,ligandid,cid,primarytarget,type,action,units,affinity,pmids,targetid,targetname,targetspecies,genesymbol,cmpdname,dois
Q9HC98,10783,compound 22 [PMID: 20462760],8205,24863112,No,Inhibitor,Inhibition,-,5.78,20462760,2121,NIMA related kinase 6,Human,NEK6,"N-(7-Chloro-1-oxo-1,2-dihydroisoquinolin-6-yl)-2-(cyclopropylamino)-2-phenylacetamide",10.1016/j.bmcl.2010.04.070

## pathwaygene
name,pwacc,pwtype,category,url,source,srcid,externalid,extid,taxid,taxname,core,cids,geneids,protacxns,pmids,ecs,annotation
AP-1 transcription factor network,Pathway Interaction Database:ap1_pathway,organism_specific,pathway,http://pid.nci.nih.gov/search/pathway_landing.shtml?pathway_id=ap1_pathway&pathway_name=ap1_pathway&source=NCI-Nature curated&what=graphic&jpg=on,Pathway Interaction Database,4,ap1_pathway,ap1_pathway,NULL,Homo sapiens,1,NULL,58|183|467|573|595|865|983|1027|1029|1278|1385|1386|1437|1499|1758|1843|1906|1958|1997|2033|2099|2113|2167|2353|2354|2355|2624|2697|2908|3091|3105|3458|3491|3558|3565|3567|3569|3576|3586|3725|3726|3727|4094|4097|4312|4318|4502|4602|4609|4773|4878|4922|5179|5328|5728|6347|6667|6934|7040|7054|7076|7157|7205|8061|9988|10018|10987|23373|149603,O00622|O15525|O43521|O75444|P00749|P01019|P01033|P01100|P01106|P01137|P01160|P01210|P01579|P02795|P03372|P03956|P04141|P04150|P04439|P04637|P05112|P05113|P05231|P05305|P05412|P06493|P07101|P08047|P08123|P10145|P10242|P13500|P14780|P14921|P15090|P15336|P15407|P15408|P16220|P17275|P17302|P17535|P18146|P18847|P22301|P23769|P24385|P28562|P30990|P32519|P35222|P42771|P46527|P53539|P60484|P60568|P68133|Q09472|Q13316|Q13469|Q13951|Q15654|Q16665|Q5TA31|Q6UUV9|Q92905|Q99933|Q9NQB0|Q9Y222,1527086|1719551|1749429|1827203|1827665|1945831|2110368|2111020|2111328|2115643|2138276|2467839|2497053|2498083|2504580|2513128|2516828|2825349|2974122|3103098|3130660|3135940|3136397|3142691|3142692|3143919|7623817|8058317|8289796|8397339|8754832|8837781|8875991|8994040|9111306|9349820|9510247|9511728|9878062|9889198|10080190|10359014|10790372|10942775|11756554|12121977|12853483|12881422|14510502|14523011|15308641|15489293|15601844|15699140|15828020|16007074|16518400|17146436|17689131|18247370|18535250|185,1.14.16.2|2.3.1.-|2.3.1.48|2.3.2.27|2.7.11.22|2.7.11.23|3.1.3.16|3.1.3.48|3.1.3.67|3.4.-.-|3.4.21.73|3.4.24.35|3.4.24.7,"COVID-19, COVID19, Coronavirus, Corona-virus, SARS, SARS2, SARS-CoV, SARS-CoV-2 [as per WikiPathways, DrugBank, UniProt, COVID-19 Disease Map]"

## pathwayreaction
name,source,externalid,url,definition,reaction,control,cids,protacxns,geneids,ecs,pmids
Programmed Cell Death,Reactome,R-HSA-5357801,https://reactome.org/content/detail/R-HSA-5357801,ATP + BCL2L11:DYNLL1:microtubules ⟶ ADP + DYNLL1:microtubules + p-BIM,<a href='https://pubchem.ncbi.nlm.nih.gov/compound/5461108'>ATP</a> + BCL2L11:DYNLL1:microtubules ⟶ <a href='https://pubchem.ncbi.nlm.nih.gov/compound/7058055'>ADP</a> + <a href='https://pubchem.ncbi.nlm.nih.gov/protein/O43521'>p-BIM</a> + DYNLL1:microtubules,activated by <a href='https://pubchem.ncbi.nlm.nih.gov/protein/P45983'>mitogen-activated protein kinase 8</a>,5461108|7058055,O43521|P45983|P63167,10018|5599|8655,2.7.11.24,12591950

## pdb
resolution,pdbid,title,expmethod,lignme,glytoucan,cids,protacxns,geneids,pmids,dois
1.31,6X8O,BimBH3 peptide tetramer,X-RAY DIFFRACTION,SCN,NULL,9322,O43521,10018,32966763,10.1016/j.str.2020.09.002

## rhea
rhid,equation,htmlequation,direction,otherdirections,cids,protacxns,pmids,ecs,geneids,dois
20345,[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + H(+) + NADPH,<a href='https://pubchem.ncbi.nlm.nih.gov/compound/15938972'>NADP<small><sup>+</sup></small></a> + [thioredoxin]-dithiol = <a href='https://pubchem.ncbi.nlm.nih.gov/compound/15983949'>NADPH</a> + [thioredoxin]-disulfide + <a href='https://pubchem.ncbi.nlm.nih.gov/compound/1038'>H<small><sup>+</sup></small></a>,=,20346|20347|20348,15983949|1038|15938972,P56431|Q9ZL18|Q58931|P0A9P4|Q1RJD8|Q4ULP1|Q68WT3|Q92I02|Q9ZD97|P0A9P5|P39916|P43788|P57399|P80892|P81433|Q89AJ2|Q9KSS4|O66790|O83790|P94284|O84101|Q9PKT7|Q9Z8M4|O30973|O32823|P46843|P47348|P50971|P52213|P52215|P66010|P66011|P75531|P80880|P99101|P9WHH0|P9WHH1|Q05741|Q5HHQ4|Q5HQW4|Q6GB66|Q6GIM7|Q8CPY8|Q928B5|Q98PK9|Q9PR71|P38816|D4APQ6|P29509|P43496|P51978|Q6BIS1|Q6C7L4|Q6FR39|Q6HA24|Q75CM8|Q7Z7S3|Q8J0U0|Q92375|Q16881|A6QP01|P62341|P62342|Q19892|Q1H5H1|Q5ZJN8|Q6PBD1|Q6PHY8|Q802F2|Q9U3N5|Q9VMV6|O62768|O89049|P,11012661,1.8.1.9,1452444|61754092|949054|917715|1209097|56470832|57739856|57879332|884181|1245727|45050363|987338|1099326|936549|45427913|886232|61470992|50019306|61171736|29672186|856506|9523739|851955|3881395|2904781|2911244|2889334|2894621|4619415|3361358|7296|783831|51714|69227|185097|365802|425041|394463|352921|352919|181343|33725|282388|31760|177466|100174180|114112|232223|26462|50493|282389|10587|40475|50551|8622741|813514|4344159|4340912|4330505|818766|816248|829698,10.1046/j.1432-1327.2000.01701.x

