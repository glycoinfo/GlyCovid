import pandas as pd

link_header = 'https://sugarbind.expasy.org'
PREFIX = '@prefix : <http://rdf.glycoinfo.org/SugarBind/ontology#> .\n\
@prefix interaction: <http://rdf.glycoinfo.org/ontology/interaction#> .\n\
@prefix id: <http://rdf.glycoinfo.org/SugarBind/Id/> .\n\
@prefix owl: <http://www.w3.org/2002/07/owl#> .\n\
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix xml: <http://www.w3.org/XML/1998/namespace> .\n\
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
@prefix glycoinfo: <http://rdf.glycoinfo.org/glycan/> .\n\
@prefix glycann: <http://purl.jp/bio/12/glyco/glycan> .\n\
@prefix obo: <http://purl.obolibrary.org/obo/> .\n\
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n\
@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n\
@prefix gold: <http://rdf.glycoinfo.org/gold/id/> .\n\
@prefix dcterms: <http://purl.org/dc/terms/> .\n\
@prefix bibo: <http://purl.org/ontology/bibo/> .\n\
@base <http://purl.jp/bio/12/glyco/diseases#> .\n\n\n'

def ttl_ReferenceInteraction():
    df_lectin = pd.read_csv('data/lectin_list.csv').sort_values(by = 'Lectin ID', ascending = True)                        # open file as pandas data frame
    df_lectin_ns = df_lectin[df_lectin['N/S'] == 1]                                                                         # open file as pandas data frame
    df_lectin_ = df_lectin[df_lectin['N/S'] == 0]                                                                           # open file as pandas data frame
    df_lectin_agent = pd.read_csv('data/lectin_agent.csv')                                                                 # open file as pandas data frame
    df_lectin_area = pd.read_csv('data/lectin_affect.csv')                                                                 # open file as pandas data frame
    df_lectin_ligand = pd.read_csv('data/lectin_ligand.csv').sort_values(by = 'Ligand ID', ascending = True)               # open file as pandas data frame
    df_lectin_pubmed = pd.read_csv('data/lectin_pubmed.csv').sort_values(by = 'Pubmed ID', ascending = True)               # open file as pandas data frame
    df_ligand_structure = pd.read_csv('data/structure_ligand.csv')                                                         # open file as pandas data frame
    df_ligand_names = pd.read_csv('data/ligand_names.csv')                                                                 # open file as pandas data frame
    
    file = open('output/referenced_interaction.ttl', 'w', encoding='UTF-8')                                                # open file named "referenced_interaction.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')                                                 
    file.write('### Individuals (lectin including N/S) \n')                                                                 # inserting ttl header title
    file.write('#######################################################\n\n')

    for index, item in df_lectin_ns.iterrows():
        lectin_id = item['Lectin ID']                                                                                       # extracting lectin id
        filtered_ligand = df_lectin_ligand.loc[df_lectin_ligand['Lectin ID'] == lectin_id]                                  # filtering loaded data frame with lectin id
        filtered_pubmed = df_lectin_pubmed.loc[df_lectin_pubmed['Lectin ID'] == lectin_id]                                  
        filtered_area = df_lectin_area.loc[df_lectin_area['Lectin ID'] == lectin_id]                                        
        filtered_agent = df_lectin_agent.loc[df_lectin_agent['Lectin ID'] == lectin_id]                                     
        title = 'LEC' + str(lectin_id) + '_'                                                                                # initiate title string
        for index, item in filtered_ligand.iterrows():
            title += 'LIG' + str(item['Ligand ID']) + '_'                                                                   # add ligand information to title
        for index, item in filtered_pubmed.iterrows():
            title += 'PUB' + str(item['Pubmed ID']) + '_'                                                                   # add pubmed information to title
        for index, item in filtered_area.iterrows():
            title += 'ARE' + str(item['Affect ID']) + '_'                                                                   # add area information to title
        for index, item in filtered_agent.iterrows():
            title += 'AGE' + str(item['Agent ID']) + '_'                                                                    # add agent information to title
        title = title[:-1]                                                                                                  # cut off last '-' from title string
        file.write(f'interaction:{title} rdf:type owl:NamedIndividual ,\n')                                                            # add ttl type description
        file.write('\t\t\t:ReferencedInteraction ;\n')                                                                      # add ttl class type description
        # lectin
        file.write(f'\t\t:has_lectin id:LEC{lectin_id} ;\n')                               # add ttl object property and lectin URI

        # ligand
        if len(filtered_ligand) > 0:                                                                                        # if ligand exists in filtered data frame
            document = ''                                                                                                   # initiate document as string data
            for index2, item2 in filtered_ligand.iterrows():
                document += f'id:LIG{item2["Ligand ID"]} ,\n\t\t\t'                        # add ligand URI to document
            document = document[:-5] + ';\n'                                                                                # cut off last 5 letters and add \n
            file.write('\t\t:has_ligand ')                                                                                  # add ttl object property
            file.write(document)                                                                                            # inserting ligand information to ttl
        # pubmed
        if len(filtered_pubmed) > 0:                                                                                        # if pubmed exists in filtered data frame
            document = ''
            for index2, item2 in filtered_pubmed.iterrows():
                document += f'id:PUB{item2["Pubmed ID"]} ,\n\t\t\t'                          # add pubmed URI to document
            document = document[:-5] + ';\n'
            file.write('\t\t:has_citation ')
            file.write(document)
        # agent
        if len(filtered_agent) > 0:                                                                                         # if agent exists in filtered data frame
            document = ''
            for index2, item2 in filtered_agent.iterrows():
                document += f'id:AGE{item2["Agent ID"]} ,\n\t\t\t'                          # add agent URI to document
            document = document[:-5] + ';\n'
            file.write('\t\t:has_agent ')
            file.write(document)
        # area
        if len(filtered_area) > 0:                                                                                          # if agent exists in filtered data frame
            document = ''
            for index2, item2 in filtered_area.iterrows():
                document += f'id:ARE{item2["Affect ID"]} ,\n\t\t\t'                  # add agent URI to document
            document = document[:-5] + ';\n'
            file.write('\t\t:has_area ')
            file.write(document)
        file.write(f'\t\trdfs:label "{title}"^^xsd:string .\n\n')                                                           # inserting closing ttl statement

        
    # f.close()
    file.write('\n\n\n#######################################################\n')
    file.write('### Individuals (lectin without N/S) \n')                                                                   # inserting ttl header title
    file.write('#######################################################\n\n')

    for index, item in df_lectin_.iterrows():
        lectin_id = item['Lectin ID']                                                                                       # extracting lectin id
        filtered_ligand = df_lectin_ligand.loc[df_lectin_ligand['Lectin ID'] == lectin_id]                                  # filtering loaded data frame with lectin id
        filtered_pubmed = df_lectin_pubmed.loc[df_lectin_pubmed['Lectin ID'] == lectin_id]
        filtered_area = df_lectin_area.loc[df_lectin_area['Lectin ID'] == lectin_id]
        filtered_agent = df_lectin_agent.loc[df_lectin_agent['Lectin ID'] == lectin_id]
        title = 'LEC' + str(lectin_id) + '_'                                                                                # initiate title string
        for index, item in filtered_ligand.iterrows():
            title += 'LIG' + str(item['Ligand ID']) + '_'                                                                   # add ligand information to title
        for index, item in filtered_pubmed.iterrows():
            title += 'PUB' + str(item['Pubmed ID']) + '_'                                                                   # add pubmed information to title
        for index, item in filtered_area.iterrows():
            title += 'ARE' + str(item['Affect ID']) + '_'                                                                   # add area information to title
        for index, item in filtered_agent.iterrows():
            title += 'AGE' + str(item['Agent ID']) + '_'                                                                    # add agent information to title
        title = title[:-1]
        
        file.write(f'interaction:{title} rdf:type owl:NamedIndividual ,\n')                                                            # add ttl type description
        file.write('\t\t\t:ReferencedInteraction ;\n')                                                                      # add ttl class type description
        # lectin
        file.write(f'\t\t:has_lectin <https://sugarbind.expasy.org/lectins/{lectin_id}> ;\n')                               # add ttl object property and lectin URI

        # ligand
        if len(filtered_ligand) > 0:                                                                                        # if ligand exists in filtered data frame
            document = ''                                                                                                   # initiate document as string data
            for index2, item2 in filtered_ligand.iterrows():
                document += f'<https://sugarbind.expasy.org/ligands/{item2["Ligand ID"]}> ,\n\t\t\t'                        # add ligand URI to document
            document = document[:-5] + ';\n'                                                                                # cut off last 5 letters and add \n
            file.write('\t\t:has_ligand ')                                                                                  # add ttl object property
            file.write(document)                                                                                            # inserting ligand information to ttl
        # pubmed
        if len(filtered_pubmed) > 0:                                                                                        # if pubmed exists in filtered data frame
            document = ''
            for index2, item2 in filtered_pubmed.iterrows():
                document += f'<http://www.ncbi.nlm.nih.gov/pubmed/{item2["Pubmed ID"]}> ,\n\t\t\t'
            document = document[:-5] + ';\n'
            file.write('\t\t:has_pubmed ')
            file.write(document)
        # agent
        if len(filtered_agent) > 0:                                                                                         # if agent exists in filtered data frame
            document = ''
            for index2, item2 in filtered_agent.iterrows():
                document += f'<https://sugarbind.expasy.org/agents/{item2["Agent ID"]}> ,\n\t\t\t'
            document = document[:-5] + ';\n'
            file.write('\t\t:has_agent ')
            file.write(document)
        # area
        if len(filtered_area) > 0:                                                                                          # if area exists in filtered data frame
            document = ''
            for index2, item2 in filtered_area.iterrows():
                document += f'<https://sugarbind.expasy.org/affectedAreas/{item2["Affect ID"]}> ,\n\t\t\t'
            document = document[:-5] + ';\n'
            file.write('\t\t:has_area ')
            file.write(document)
        file.write(f'\t\trdfs:label "{title}"^^xsd:string .\n\n')
    file.close()

def ttl_pubmed():
    df_pubmed = pd.read_csv('data/lectin_pubmed.csv').sort_values(by = 'Pubmed ID', ascending = True)                      # open file as pandas data frame
    file = open('output/pubmed.ttl', 'w', encoding='UTF-8')                                                                # open file named "pubmed.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Pubmed) \n')                                                                               # inserting ttl header title
    file.write('#######################################################\n\n')
    for index, item in df_pubmed.iterrows():
        file.write(f'''id:PUB{item["Pubmed ID"]} rdf:type owl:NamedIndividual ,\n\t\t\t:Pubmed ,\n\t\t\tobo:NCIT_C42881 ;\n\t\tdcterms:references <http://www.ncbi.nlm.nih.gov/pubmed/{item["Pubmed ID"]}> ;\n\t\tbibo:pmid "{item["Pubmed ID"]}"^^xsd:string ;\n\t\trdfs:label "{item["Pubmed ID"]}"^^xsd:string .\n\n''')
                                                                                                                            # inserting ttl content
    file.close()

def ttl_structure():
    df_structure = pd.read_csv('data/structure_ligand.csv').sort_values(by = 'Structure ID', ascending = True)             # open file as pandas data frame
    file = open('output/structure.ttl', 'w', encoding= 'UTF-8')                                                            # open file named "structure.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Structure) \n')                                                                            # inserting ttl header
    file.write('#######################################################\n\n')
    for index, item in df_structure.iterrows():
        # file.write(f'<https://sugarbind.expasy.org/structures/{item["Structure ID"]}> rdf:type owl:NamedIndividual ,\n\t\t\t:Structure ;\n\t\t:glytoucanId glycoinfo:{item["Glytoucan ID"]} ;\n\t\t:structureId "{item["Structure link"]}"^^xsd:anyURI ;\n\t\trdfs:label "{item["Structure ID"]}"^^xsd:string .\n\n')
        file.write(f'''id:STR{item["Structure ID"]} rdf:type owl:NamedIndividual ,
                    glycan:Saccharide ,
                glycan:has_resource_entry <{item["Structure link"]}> ;
                rdfs:label "{item["Structure ID"]}"^^xsd:string .
                \n''')
    file.close()

def ttl_ligand():
    df_ligand = pd.read_csv('data/lectin_ligand.csv').sort_values(by = 'Ligand ID', ascending = True)                      # open file as pandas data frame
    df_ligand_names = pd.read_csv('data/ligand_names.csv').sort_values(by = 'Ligand ID', ascending = True)                 
    df_structure_ligand = pd.read_csv('data/structure_ligand.csv').sort_values(by = 'Ligand ID', ascending = True)         
    file = open('output/ligand.ttl', 'w', encoding='UTF-8')                                                                # open file named "ligand.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Ligand) \n')                                                                               # inserting ttl header
    file.write('#######################################################\n\n')
    for index in range(1, 205):
        file.write(f'''id:LIG{ index } rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C95009 ,\n\t\t\t:Ligand ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/ligands/{ index }> ;\n\t\tdcterms:references <https://sugarbind.expasy.org/ligands/{ index }> ;\n''')
                                                                                                                            # inserting ttl content

        filtered_structure_ligand = df_structure_ligand.loc[df_structure_ligand['Ligand ID'] == index]                      # filtering loaded data frame with ligand id
        if len(filtered_structure_ligand) > 0:                                                                              # if structure ligand exists in filtered data frame
            document = ''                                                                                                   # initiate document as string data
            for index2, item2 in filtered_structure_ligand.iterrows():
                document += f'id:STR{ item2["Structure ID"] } ,\n\t\t\t'                # add structure URI to document
            file.write('\t\t:has_structure ')                                                                               # add ttl object property
            file.write( document[:-5] + ';\n')                                                                              # inserting ligand information to ttl

        filtered_ligand_names = df_ligand_names.loc[df_ligand_names['Ligand ID'] == index]                                  # filtering loaded data frame with ligand id

        if len(filtered_ligand_names) > 0:                                                                                  # if ligand names exists in filtered data frame
            document = ''
            for index2, item2 in filtered_ligand_names.iterrows():
                if item2["Unnamed"]:
                    document += f'"{item2["Ligand ID"] }"^^xsd:string ,\n\t\t\t'
                else:
                    document += f'"{item2["Ligand name"]}"^^xsd:string ,\n\t\t\t'
            file.write('\t\trdfs:label ')
            file.write(document[:-5] + '.\n\n')
    file.close()

def ttl_lectin():
    df_lectin = pd.read_csv('data/lectin_list.csv').sort_values(by = 'Lectin ID', ascending = True)                        # open file as pandas data frame
    df_lectin_ns = df_lectin[df_lectin['N/S'] == 1]                                                                         # filtering loaded data frame with N/S
    file = open('output/lectin.ttl', 'w', encoding='UTF-8')                                                                # open file named "lectin.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Lectin including N/S) \n')                                                                 # inserting ttl header
    file.write('#######################################################\n\n')
    for index, item in df_lectin_ns.iterrows():
        if type(item["Uniprot ID"]) is str:
            file.write(f'''id:LEC{ item["Lectin ID"] } rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C16785 ,\n\t\t\t:Lectin ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\tdcterms:references <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\t:uniprotId <http://purl.uniprot.org/uniprot/{ item["Uniprot link"][32:] }> ;\n\t\trdfs:seeAlso <http://purl.uniprot.org/uniprot/{ item["Uniprot link"][32:] }> ;\n\t\trdfs:label "{item["Lectin ID"]}"^^xsd:string .\n\n''')
        else:
            file.write(f'''id:LEC{item["Lectin ID"]} rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C16785 ,\n\t\t\t:Lectin ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\trdfs:label "{item["Lectin ID"]}"^^xsd:string .\n\n''')
            # file.write(f'''id:LEC{item["Lectin ID"]} rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C16785 ,\n\t\t\t:Lectin ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\t<https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\trdfs:label "{item["Lectin ID"]}"^^xsd:string .\n\n''')
    file.write('#######################################################\n')
    file.write('### Individuals (Lectin without N/S) \n')
    file.write('#######################################################\n\n')
    df_lectin_ = df_lectin[df_lectin['N/S'] == 0]
    for index, item in df_lectin_.iterrows():
        if type(item["Uniprot ID"]) is str:
            file.write(f'''id:LEC{item["Lectin ID"]} rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C16785 ,\n\t\t\t:Lectin ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\tdcterms:references <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\t:uniprotId <http://purl.uniprot.org/uniprot/{ item["Uniprot link"][32:] }> ;\n\t\trdfs:label "{item["Lectin name"]}"^^xsd:string .\n\n''')
        else:
            file.write(f'''id:LEC{item["Lectin ID"]} rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C16785 ,\n\t\t\t:Lectin ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/lectins/{item["Lectin ID"]}> ;\n\t\trdfs:label "{item["Lectin name"]}"^^xsd:string .\n\n''')
    file.close()

def ttl_disease():
    df_disease_agent = pd.read_csv('data/agent_disease.csv').sort_values(by = 'Disease ID', ascending = True)              # open file as pandas data frame
    df_disease_area = pd.read_csv('data/area_disease.csv').sort_values(by = 'Disease ID', ascending = True)
    df_disease_list = pd.read_csv('data/disease_list.csv').sort_values(by = 'Disease ID', ascending = True)
    file = open('output/disease.ttl', 'w', encoding = 'UTF-8')                                                             # open file named "disease.ttl" in "output" folder
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Disease)\n')                                                                               # inserting ttl header
    file.write('#######################################################\n\n')
    for index in range(1, 48):
        disease_name = df_disease_list.loc[df_disease_list['Disease ID'] == index]['Disease Name']                          # filtering loaded data frame with disease name
        disease_doid = df_disease_list.loc[df_disease_list['Disease ID'] == index]['DOID']                          # filtering loaded data frame with disease name
        filtered_disease_agent = df_disease_agent.loc[df_disease_agent['Disease ID'] == index]
        filtered_disease_area = df_disease_area.loc[df_disease_area['Disease ID'] == index]
        if len(filtered_disease_agent) > 0 or len(filtered_disease_area) > 0:
            text = f'''id:DIS{ index } rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C2991 ,\n\t\t\tobo:DOID_4 ;\n'''
            if len(filtered_disease_agent) == 1:                                                                            # if the number related to disease is 1 or not
                for ind, item in filtered_disease_agent.iterrows():
                    text += f"""\t\t:caused_by id:AGE{ str(item['Agent ID']) } ;\n"""         # inserting

            elif len(filtered_disease_agent) > 1:
                firstLoop = True
                for ind, item in filtered_disease_agent.iterrows():
                    if firstLoop:
                        text += f"""\t\t:caused_by id:AGE{ str(item['Agent ID']) } ,\n"""
                        firstLoop = False
                    else:
                        text += f"""\t\t\tid:AGE{ str(item['Agent ID']) } ,\n"""
                text = text[:-2] + ';\n'


            if len(filtered_disease_area) == 1:
                for ind, item in filtered_disease_area.iterrows():
                    text += f"""\t\t:caused_at id:ARE{ str(item['Affected Area ID']) } ;\n"""
            elif len(filtered_disease_area) > 1:
                firstLoop = True
                for ind, item in filtered_disease_area.iterrows():
                    if firstLoop:
                        text += f"""\t\t:caused_at id:ARE{ str(item['Affected Area ID']) } ,\n"""
                        firstLoop = False
                    else:
                        text += f"""\t\t\tid:ARE{ str(item['Affected Area ID']) } ,\n"""
                text = text[:-2] + ';\n'
            text += f'\t\trdfs:label "{ disease_name.values[0] }"^^xsd:string ;\n'
            text += f'\t\trdfs:seeAlso obo:{ disease_doid.values[0].replace(":", "_") } .\n'

            file.write(text + '\n')
    file.close()

def ttl_area():
    df_area_list = pd.read_csv('data/area_list.csv').sort_values(by = 'Affected Area ID', ascending = True)

    file = open('output/area.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Area)\n')
    file.write('#######################################################\n\n')
    for index, item in df_area_list.iterrows():
        category = ''
        text = f'id:ARE{item["Affected Area ID"]} rdf:type owl:NamedIndividual ,\n\t\t\tobo:NCIT_C12801,\n'
        if item["Area Type"] == 1:
            category = 'System'
        elif item["Area Type"] == 2:
            category = 'Organ'
        elif item["Area Type"] == 3:
            category = 'Tissue'
        else:
            category = 'Cell'
        text += f'\t\t:Area ,\n'
        text += f'\t\t:{category} ;\n'
        text += f'\t\tfoaf:homepage <https://sugarbind.expasy.org/affectedAreas/{ item["Affected Area ID"]}> ;\n'
        text += f'\t\trdfs:label "{item["Area Name"]}"^^xsd:string .\n\n'
        file.write(text)
    file.close()

import re
import math
import numpy

def ttl_agent():
    # df_agent_list = pd.read_csv('data/agent_list.csv').sort_values(by = 'Agent ID', ascending = True)
    df_agent_list = pd.read_csv('data/agent_list2.csv').sort_values(by = 'Agent ID', ascending = True)
    df_agent_disease = pd.read_csv('data/agent_disease.csv').sort_values(by = 'Agent ID', ascending = True)
    df_agent_area = pd.read_csv('data/agent_affected_area.csv').sort_values(by = 'Agent ID', ascending = True)

    first = True
    lineage_dictionary = {}
    for inde, item in df_agent_list.iterrows():
        lineage_list = item['Lineage'].split('</a>,')
        for num in range(len(lineage_list)):
            if first:
                first = False
            else:
                parent = re.findall(r'<a href=\"(.*?)\".*?>', lineage_list[num -1])[0][8:]
                child = re.findall(r'<a href=\"(.*?)\".*?>', lineage_list[num])[0][8:]
                # if not (f'{parent}-{child}' in lineage_dictionary):
                #     lineage_dictionary[f'{parent}-{child}'] = [parent, child]
                if not (child in lineage_dictionary):
                    lineage_dictionary[f'{child}'] = parent
    # print(lineage_dictionary)
    file = open('output/agent.ttl', 'w', encoding = 'UTF-8')
    file.write(PREFIX)
    file.write('#######################################################\n')
    file.write('### Individuals (Agent)\n')
    file.write('#######################################################\n\n')
    count = 0
    gold_ttl = list()
    for index, item in df_agent_list.iterrows():

        filtered_agent_disease = df_agent_disease.loc[df_agent_disease['Agent ID'] == item['Agent ID']]
        filtered_agent_area = df_agent_area.loc[df_agent_area['Agent ID'] == item['Agent ID']]
        if len(filtered_agent_disease) > 0 or len(filtered_agent_area) > 0:
            text = f'''id:AGE{ item["Agent ID"] } rdf:type owl:NamedIndividual ,\n\t\t\t:Agent ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/agents/{ item["Agent ID"] }> ;\n\t\tdcterms:references <https://sugarbind.expasy.org/agents/{ item["Agent ID"] }> ;\n'''
            if len(filtered_agent_disease) == 1:
                for ind, ite in filtered_agent_disease.iterrows():
                    text += f'\t\t:causes id:DIS{ ite["Disease ID"] } ;\n\t\t<http://purl.obolibrary.org/obo/NCIT_P331> id:DIS{ ite["Disease ID"] } ;\n'
            elif len(filtered_agent_disease) > 1:
                firstLoop = True
                for ind, ite in filtered_agent_disease.iterrows():
                    if firstLoop:
                        text += f'\t\t:causes id:DIS{ ite["Disease ID"] } ,\n'
                        firstLoop = False
                    else:
                        text += f'\t\t\tid:DIS{ ite["Disease ID"] } ,\n'
                text = text[:-2] + ';\n'
                firstLoop = True
                for ind, ite in filtered_agent_disease.iterrows():
                    if firstLoop:
                        text += f'\t\t<http://purl.obolibrary.org/obo/NCIT_P331> id:DIS{ ite["Disease ID"] },\n'
                        firstLoop = False
                    else:
                        # text += f'\t\t\t<http://purl.obolibrary.org/obo/NCIT_P331> id:DIS{ ite["Disease ID"] },\n'
                        text += f'\t\t\tid:DIS{ ite["Disease ID"] },\n'
                text = text[:-2] + ';\n'
            if len(filtered_agent_area) == 1:
                for ind, ite in filtered_agent_area.iterrows():
                    count += 1
                    text += f'\t\t:found_in id:ARE{ ite["Affected Area ID"] } ;\n'
            elif len(filtered_agent_area) > 1:
                firstLoop = True
                for ind, ite in filtered_agent_area.iterrows():
                    if firstLoop:
                        text += f'\t\t:found_in id:ARE{ ite["Affected Area ID"] } ,\n'
                        firstLoop = False
                        count += 1
                    else:
                        text += f'\t\t\tid:ARE{ ite["Affected Area ID"] } ,\n'
                        count += 1
                text = text[:-2] + ';\n'
            # text += f'\t:agentId "{ item["Agent ID"] }"^^xsd:string ;\n\trdfs:label "{ item["Agent Name"] }"^^xsd:string .\n'
            text += f'\t\trdfs:label "{ item["Agent Name"] }"^^xsd:string ;\n\t\tskos:prefLabel "{ item["Agent Name"] }"^^xsd:string ;\n'
        else:
            text = f'''id:AGE{ item["Agent ID"] } rdf:type owl:NamedIndividual ,\n\t\t\t:Agent ;\n\t\tfoaf:homepage <https://sugarbind.expasy.org/agents/{ item["Agent ID"] }> ;\n\t\tdcterms:references <https://sugarbind.expasy.org/agents/{ item["Agent ID"] }> ;\n\t\trdfs:label "{ item["Agent Name"] }"^^xsd:string ;\n\t\tskos:prefLabel "{ item["Agent Name"] }"^^xsd:string ;\n'''
        
        # lineage_up
        if str(item['Agent ID']) in lineage_dictionary:
            text += f'\t\t:lineage_up id:AGE{ lineage_dictionary[str(item["Agent ID"])] } ;\n'
        # taxonomy ID
        if item['taxonomy ID'] and not numpy.isnan(item['taxonomy ID']):
            text += f'\t\t<http://purl.obolibrary.org/obo/NCIT_P331> <https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={ int(item["taxonomy ID"])}> ;\n'
        # taxonomy Level
        if type(item["taxonomy level"]) == int:
            text += f'\t\t:taxonomyLevel "{ item["taxonomy level"] }"^^xsd:string ;\n'
        # gold
        if type(item["GOLD"]) == str:
            first = True
            for gold in item["GOLD"].split(','):
                if first:
                    text += '\t\trdfs:seeAlso gold:{} ,\n'.format(re.findall(r'([0-9]+)', gold)[0])
                    # text += '\t\t:rdfs:seeAlso <http://rdf.glycoinfo.org/gold/id/{}> ,\n'.format(re.findall(r'([0-9]+)', gold)[0])
                    if re.findall(r'([0-9]+)', gold)[0] not in gold_ttl:
                        gold_ttl.append(re.findall(r'([0-9]+)', gold)[0])
                    first = False
                else:
                    text += '\t\t\tgold:{} ,\n'.format(re.findall(r'([0-9]+)', gold)[0])
                    # text += '\t\t\t<http://rdf.glycoinfo.org/gold/id/{}> ,\n'.format(re.findall(r'([0-9]+)', gold)[0])
                    if re.findall(r'([0-9]+)', gold)[0] not in gold_ttl:
                        gold_ttl.append(re.findall(r'([0-9]+)', gold)[0])
            text = text[:-2] + ';\n'
        # hamap
        if not ('-' in item["HAMAP"]):
            text += '\t\t:hamap "{}"^^xsd:string ;\n'.format( item["HAMAP"].replace('\n', '').replace('\t', '').replace(' ', ''))
            # text += f'''\t:hamap "{ item["HAMAP"].replace('\n', '').replace('\t', '').replace(' ', '') }"^^xsd:string ;\n'''
        # viralzone
        if type(item["Viralzone Link"]) == str:
            text += f'\t\t:viralzone <{ item["Viralzone Link"] }> ;\n\t\tskos:related <{ item["Viralzone Link"] }> ;\n'
        # viralzone Label
        if type(item["Viralzone"]) == str:
            text += f'''\t\t:viralzoneLabel "{item["Viralzone"].replace(' ', '') }"^^xsd:string ;\n'''
        text = text[:-2] + '.\n'
    

        file.write(text + '\n')
    for val in gold_ttl:
        text = f'gold:{ val } foaf:homepage <https://gold.jgi.doe.gov/organisms?id={ val }>.\n'
        # text = f'<http://rdf.glycoinfo.org/gold/id/{ val }> foaf:homepage <https://gold.jgi.doe.gov/organisms?id={ val }>.\n'
        file.write(text)
    
    file.close()

def merge_ttl(files):
    for a in files:
        print(a + '.ttl')

if __name__ == "__main__":
    # ### making ttl file from csv created above
    ttl_ReferenceInteraction()  
    #     # requires lectin_list.csv, lectin_agent.csv, lectin_affect.csv, lectin_ligand.csv, lectin_pubmed.csv, structure_ligand.csv, ligand_names.csv
    ttl_pubmed()                
    #     # requires lectin_pubmed.csv
    ttl_structure()             
    #     # requires structure_ligand.csv
    ttl_ligand()                
    #     # requires lectin_ligand.csv, ligand_names.csv, structure_ligand.csv
    ttl_lectin()                
    #     # requires lectin_list.csv
    ttl_area()                  
    #     # requires area_list.csv
    ttl_agent()                 
    #     # requires agent_list.csv, agent_disease.csv, agent_affected_area.csv
    ttl_disease()               
    #     # requires agent_disease.csv, area_disease.csv, disease_list.csv

    # merge_ttl(['agent', 'area', 'disease', 'lectin', 'ligand', 'pubmed', 'referenced_interaction', 'structure'])
    # passing string arguments which corresponds to the file name stored in the output folder


