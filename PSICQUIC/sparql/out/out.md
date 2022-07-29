



# query__psicquicinteractor_by_chebiid
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
SELECT ?interaction ?chebi_id

WHERE {
  BIND("chebi" as ?database)
  BIND("157592" as ?id)

  ?interaction a <http://biomodels.net/SBO/SBO_0000344> .
  BIND(?database + "_" + ?id as ?interactor)
  FILTER CONTAINS (str(?interaction), ?interactor)

  ?interaction ?predicate ?object

  FILTER CONTAINS (str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/")

  BIND(REPLACE(str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/", "", "i") AS ?chebi_id)
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "interaction",
      "chebi_id"
    ]
  },
  "results": {
    "bindings": [
      {
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL228"
        },
        "chebi_id": {
          "type": "literal",
          "value": "157592"
        }
      },
      {
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL238"
        },
        "chebi_id": {
          "type": "literal",
          "value": "157592"
        }
      }
    ]
  }
}
```
</details>




# query_glytoucan_by_psicquicinteractor
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
SELECT ?interaction ?glytoucan_url ?chebi_uri

WHERE {
  BIND("chebi" as ?database)
  BIND("157592" as ?id)

  ?interaction a <http://biomodels.net/SBO/SBO_0000344> .
  BIND(?database + "_" + ?id as ?interactor)
  FILTER CONTAINS (str(?interaction), ?interactor)

  ?interaction ?predicate ?object

  FILTER CONTAINS (str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/")

  BIND(REPLACE(str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/", "", "i") AS ?chebi_id)
  BIND(URI(CONCAT("http://rdf.glycoinfo.org/chebi/", ?chebi_id)) as ?chebi_uri)

  SERVICE <https://ts.glycosmos.org/sparql> {
    ?glytoucan_url glycan:has_resource_entry ?chebi_uri .
  }
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "interaction",
      "glytoucan_url",
      "chebi_uri"
    ]
  },
  "results": {
    "bindings": [
      {
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL228"
        },
        "glytoucan_url": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G72701VD"
        },
        "chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/157592"
        }
      },
      {
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL238"
        },
        "glytoucan_url": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G72701VD"
        },
        "chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/157592"
        }
      }
    ]
  }
}
```
</details>




# query_psicquicdata_by_glytoucanid
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?glytoucan_uri ?interaction

WHERE {

  BIND("G72701VD" as ?glytoucan_id)

  SERVICE <https://ts.glycosmos.org/sparql> {
    ?glytoucan_uri dcterms:identifier ?glytoucan_id .
    ?glytoucan_uri glycan:has_resource_entry ?glytoucan_chebi_uri .
    FILTER CONTAINS (str(?glytoucan_chebi_uri), "http://rdf.glycoinfo.org/chebi/")
  }
  BIND(REPLACE(str(?glytoucan_chebi_uri), "http://rdf.glycoinfo.org/chebi/", "", "i") AS ?chebi_id)
  BIND(URI(CONCAT("http://rdf.glycoinfo.org/dbid/CHEBI/", ?chebi_id)) as ?psicquic_chebi_uri)

  ?interaction ?predicarte ?psicquic_chebi_uri
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "glytoucan_uri",
      "interaction"
    ]
  },
  "results": {
    "bindings": [
      {
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G72701VD"
        },
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL228"
        }
      },
      {
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G72701VD"
        },
        "interaction": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/matrixdb.association:chebi_157592__chembl_CHEMBL238"
        }
      }
    ]
  }
}
```
</details>




# query_psicquicinteractin_by_uniprotid
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX gco: <http://purl.jp/bio/12/glyco/conjugate#>

SELECT ?interaction ?detectin_method ?publication_identifier ?interaction_type ?source_database ?interaction_id ?interactor_a ?interactor_b ?host ?glytoucan_uri

WHERE {
  BIND("P02649" as ?uniprot_id)

  ?interaction a <http://biomodels.net/SBO/SBO_0000344> .
  BIND(URI(CONCAT("http://rdf.glycoinfo.org/dbid/uniprot/", ?uniprot_id)) as ?psicquic_uniprot_id)
  ?interaction ?predicate ?psicquic_uniprot_id .

  ?interaction <http://www.bioassayontology.org/bao#BAO_0002875> ?detectin_method .
  ?interaction <http://purl.obolibrary.org/obo/IAO_0000119> ?publication_identifier .
  ?interaction <http://www.biopax.org/release/biopax-level3.owl#interactionType> ?interaction_type .
  ?interaction dc:source ?source_database .
  ?interaction dc:identifier ?interaction_id .
  ?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A> ?interactor_a .
  ?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B> ?interactor_b .
  ?interaction <http://semanticscience.org/resource/SIO_000253> ?host .

  BIND(URI(CONCAT("http://purl.uniprot.org/uniprot/", ?uniprotid)) as ?glytoucan_uniprot_uri)
  SERVICE <https://ts.glycosmos.org/sparql> {
    ?glytoucan_uniprot_uri gco:glycosylated_at ?glycosylation_site .
    ?glycosylation_site gco:has_saccharide ?glytoucan_uri .
  }
}
```




# uniprotid_psicquic_glytoucan
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX gco: <http://purl.jp/bio/12/glyco/conjugate#>

SELECT ?uniprot_uri ?glytoucan_uri

WHERE {
  ?interaction a <http://biomodels.net/SBO/SBO_0000344> .
  ?interaction ?p ?interactor .
  ?interactor a <http://biomodels.net/SBO/SBO_0000241> .
  FILTER CONTAINS (str(?interactor), "http://rdf.glycoinfo.org/dbid/uniprot")
  BIND(REPLACE(str(?interoctor), "http://rdf.glycoinfo.org/dbid/uniprot/", "", "i") as ?uniprot_id)
  BIND(URI(CONCAT("http://purl.uniprot.org/uniprot/", ?uniprot_id)) as ?uniprot_uri)

  SERVICE <https://ts.glycosmos.org/sparql> {
    ?uniprot_uri gco:glycosylated_at ?glycosylation_site .
    ?glycosylation_site gco:has_saccharide ?glytoucan_uri .
  }
}
limit 10
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "uniprot_uri",
      "glytoucan_uri"
    ]
  },
  "results": {
    "bindings": [
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G20861AN"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://identifiers.org/glytoucan/G09724ZC"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "https://purl.org/glyconnect/protein/62"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G20861AN"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "https://purl.org/glyconnect/protein/62"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://identifiers.org/glytoucan/G09724ZC"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G39448FX"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://identifiers.org/glytoucan/G66538GV"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "https://purl.org/glyconnect/protein/62"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G39448FX"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "https://purl.org/glyconnect/protein/62"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://identifiers.org/glytoucan/G66538GV"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/glycan/G61514UE"
        }
      },
      {
        "uniprot_uri": {
          "type": "uri",
          "value": "http://purl.uniprot.org/uniprot/A0A0A6YWP4"
        },
        "glytoucan_uri": {
          "type": "uri",
          "value": "http://identifiers.org/glytoucan/G40702WU"
        }
      }
    ]
  }
}
```
</details>
