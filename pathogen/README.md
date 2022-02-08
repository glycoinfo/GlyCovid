# Pathogen rdf project
## About
This 'pathogen' folder treats glycan microarray data retrieved from [Longitudinal Development of Antibody Responses in COVID-19 Patients of Different Severity with ELISA, Peptide, and Glycan Arrays: An Immunological Case Series](http://www.ncbi.nlm.nih.gov/pmc/articles/pmc8067489/) Suplementary data.
In this project the glycan code translated into [GlyTouCan](https://glytoucan.org) accession number, and it is available to check through [this CSV](./pathogens_glycans.csv).

## Original ontology
For the purpose of referring binding strength obtained in the experiment on the web, newly structured ontology was created as you can see in this [file](./pathogen_base.owl)

### PREFIXes used in the ontology
- PREFIX glycovid: <http://rdf.glycoinfo.org/GlyCovid/Id/>
- PREFIX glycovidOntology: <http://rdf.glycoinfo.org/GlyCovidRDF/Ontology#>
- PREFIX owl: <http://www.w3.org/2002/07/owl#>
- PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
- PREFIX xml: <http://www.w3.org/XML/1998/namespace>
- PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
- PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
- PREFIX foaf: <http://xmlns.com/foaf/0.1/>
- PREFIX bibo: <http://purl.org/ontology/bibo/>
- PREFIX glycoinfo: <http://rdf.glycoinfo.org/glycan/>
- PREFIX sio: <http://semanticscience.org/resource/>


## Turtle format files
Turtle formtted triples are stored in the .ttl files in the output folder.
- 'glycan.ttl' stores glycan node which is used in the glycan array.
- 'patient.ttl' stores patients information joined the experiment.
- 'sample_glycan.ttl' stores reference node which maps sample and glycan.
- 'sample.ttl' stores samples obtained from patients.

## Virtual environment(optional)
The 'main.py' works with external libraries listed on 'requirements.txt' which lists version of them as well.
For proceeding the python code in virtual environment, please follow the command below.
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

