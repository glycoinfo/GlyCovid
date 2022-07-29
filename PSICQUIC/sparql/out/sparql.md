



# covid_proteins
### SPARQL query
```
PREFIX : <http://purl.uniprot.org/core/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>

SELECT ?child_taxon ?interactor ?other_interactor_chebi_uri
WHERE {
  # 1. コロナウイルスに関係するタンパク質一覧を取得
  bind(taxon:2697049 as ?taxon)
  SERVICE <https://sparql.uniprot.org> {
    # taxonの祖先を取得
    ?taxon rdfs:subClassOf+ ?ancestor .
    ?ancestor :scientificName ?name ;
              :partOfLineage ?part_of_lineage .
    { ?ancestor  up:rank up:Species .} UNION
    { ?ancestor  up:rank up:Genus .} 
    
    # 取得した祖先が持つ子に当たる種を含む全てのタンパク質
    ?child_taxon rdfs:subClassOf ?ancestor .
    ?child_taxon a up:Taxon .
    ?protein up:organism ?child_taxon.
    ?protein a up:Protein .
  }
	# 取得したuniprotのうりをpsicquicで使用しているものに変換
  BIND(URI(REPLACE(str(?protein), "http://purl.uniprot.org/uniprot/", "http://rdf.glycoinfo.org/dbid/uniprot/", "i")) as ?covid_uniprot_uri)

  # 2. 取得したタンパク質が含まれるpsiquicのinteractionを検索
	?interactor a <http://biomodels.net/SBO/SBO_0000241> .
	FILTER(?interactor = ?covid_uniprot_uri)

  {
		?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A> ?interactor .
		?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B> ?other_interactor .
	} UNION {
		?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B> ?interactor .
		?interaction <http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A> ?other_interactor .
	}

  # 糖鎖に関するタンパク質の反応相手が糖鎖であるものをGlyTouCanから検索
  FILTER CONTAINS (str(?other_interactor), "http://rdf.glycoinfo.org/dbid/CHEBI")
  BIND(URI(REPLACE(str(?other_interactor), "http://rdf.glycoinfo.org/dbid/CHEBI/", "http://rdf.glycoinfo.org/chebi/", "i")) AS ?other_interactor_chebi_uri)
  SERVICE <https://ts.glycosmos.org/sparql> {
    ?glytoucan_uri glycan:has_resource_entry ?other_interactor_chebi_uri .
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
      "child_taxon",
      "interactor",
      "other_interactor_chebi_uri"
    ]
  },
  "results": {
    "bindings": [
      {
        "child_taxon": {
          "type": "uri",
          "value": "http://purl.uniprot.org/taxonomy/2697049"
        },
        "interactor": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P0DTC2"
        },
        "other_interactor_chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/17012"
        }
      },
      {
        "child_taxon": {
          "type": "uri",
          "value": "http://purl.uniprot.org/taxonomy/2697049"
        },
        "interactor": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P0DTC2"
        },
        "other_interactor_chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/17012"
        }
      },
      {
        "child_taxon": {
          "type": "uri",
          "value": "http://purl.uniprot.org/taxonomy/2697049"
        },
        "interactor": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P0DTC2"
        },
        "other_interactor_chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/17012"
        }
      },
      {
        "child_taxon": {
          "type": "uri",
          "value": "http://purl.uniprot.org/taxonomy/2697049"
        },
        "interactor": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P0DTC2"
        },
        "other_interactor_chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/17012"
        }
      },
      {
        "child_taxon": {
          "type": "uri",
          "value": "http://purl.uniprot.org/taxonomy/2697049"
        },
        "interactor": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P0DTC2"
        },
        "other_interactor_chebi_uri": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/chebi/17012"
        }
      }
    ]
  }
}
```
</details>
