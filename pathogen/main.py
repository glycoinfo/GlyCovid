import csv
import pandas as pd

PREFIX = '@prefix : <http://rdf.glycoinfo.org/GlyCovid/pathogen#> .\n\
@prefix owl: <http://www.w3.org/2002/07/owl#> .\n\
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix xml: <http://www.w3.org/XML/1998/namespace> .\n\
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
@prefix bibo: <http://purl.org/ontology/bibo/> .\n\
@prefix glycovid: <http://rdf.glycoinfo.org/GlyCovid/Id/> .\n\
@prefix glycovidOntology: <http://rdf.glycoinfo.org/GlyCovidRDF/Ontology#> .\n\
@prefix sio: <http://semanticscience.org/resource/> .\n\
@prefix glycoinfo: <http://rdf.glycoinfo.org/glycan/> .\n\
@prefix bao: <http://www.bioassayontology.org/bao#> .\n\
@prefix dcterms: <http://purl.org/dc/terms/> .\n\
@prefix obo: <http://purl.obolibrary.org/obo/> .\n\n\n'

def patient():
    file = open('output/patient.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (PAT) \n')
    file.write('#######################################################\n\n')
    df_base = pd.read_csv('./patients.csv')
    text = ''
    for _ in range(1, 5):
        df = df_base.loc[df_base['patient'] == _]
        df = df[['patient', 'age', 'hospitalized', 'symptom']].drop_duplicates()
        age = df['age'].tolist()[0]
        hospitalized = str(df['hospitalized'].tolist()[0]).lower()
        symptom = str(df['symptom'].tolist()[0])
        symptom = 'sio:SIO_001213' if symptom == 'mild' else 'sio:SIO_001214'
        text += f'glycovid:PAT{ _ } rdf:type owl:NamedIndividual ,\n\t\t\tsio:SIO_000393 ,\n\t\t\t{ symptom } ,\n\t\t\tsio:SIO_010048 ;\n\t\tglycovidOntology:isHospitalized "{ hospitalized }"^^xsd:boolean ;\n\t\tsio:SIO_000300 "{ age }"^^sio:SIO_001013 .\n\n\n'
    file.write(text)
    file.close()

def glycan():
    file = open('output/glycan.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (GLYCAN) \n')
    file.write('#######################################################\n\n')
    text = ''
    df_base = pd.read_csv('./pathogens_glycans.csv')
    for gtcid in df_base['Linkage defined structure']:
        text += f'glycoinfo:{ gtcid } rdf:type owl:NamedIndividual ,\n\t\t\tsio:SIO_001395 .\n\n\n'
    file.write(text)
    file.close()

def sample():
    file = open('output/sample.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (SAMPLE) \n')
    file.write('#######################################################\n\n')
    df_base = pd.read_csv('./patients.csv')
    text = ''
    for _ in ['A', 'G', 'M']:
        for index, row in df_base.iterrows():
            text += f'glycovid:SAM{row["patient"]}_{ row["onset"] }_{ _ } rdf:type owl:NamedIndividual ,\n\t\t\tsio:SIO_001050 ;\n\t\tglycovidOntology:sampledFrom glycovid:PAT{ row["patient"] } ;\n\t\tglycovidOntology:afterOnset "{row["onset"]}"^^sio:SIO_000430 ;\n\t\tbao:BAO_0095007 "{ _ }"^^sio:SIO_010043 .\n\n\n'
    file.write(text)
    file.close()

def sample_glycan():
    file = open('output/sample_glycan.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (SAMPLE_GLYCAN) \n')
    file.write('#######################################################\n\n')
    df_pat = pd.read_csv('./patients.csv')
    df_array = pd.read_csv('./glycan_array_data.csv')
    df_glycan = pd.read_csv('./pathogens_glycans.csv', index_col = 0)

    text = ''
    for _ in ['a', 'g', 'm']:
        for index, row in df_pat.iterrows():
            col = f'{row["patient"] }d{row["onset"]}{_}'
            for glid, score in zip(df_array['Glycan'], df_array[col]):
                gtcid = df_glycan.at[glid, 'Linkage defined structure']
                text += f'glycovid:SAM{ row["patient"] }_{ _.upper() }_{ row["onset"] }_{ gtcid } rdf:type owl:NamedIndividual ;\n\t\tglycovidOntology:hasGlycan glycoinfo:{ gtcid } ;\n\t\tglycovidOntology:hasSample glycovid:SAM{ row["patient"] }_{ row["onset"] }_{ _.upper() } ;\n\t\tglycovidOntology:has_interactor_A glycovid:SAM{ row["patient"] }_{ row["onset"] }_{ _.upper() } ;\n\t\tglycovidOntology:has_interactor_B glycoinfo:{ gtcid } ;\n\t\tbao:BAO_0002875 sio:SIO_001076 ; \n\t\tsio:SIO_000300 "{score}"^^sio:SIO001212 ;\n\t\tobo:IAO_0000119 glycovid:PUB33917609 ;\n\t\tdcterms:references glycovid:PUB33917609 .\n\n\n'
    file.write(text)
    file.close()

patient()
glycan()
sample()
sample_glycan()