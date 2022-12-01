from rdflib.namespace import RDF

def create_ttl(g, u, row):
    """
    rhid: 20345
    equation: [thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + H(+) + NADPH
    htmlequation: <a href='https://pubchem.ncbi.nlm.nih.gov/compound/15938972'>NADP<small><sup>+</sup></small></a> + [thioredoxin]-dithiol = <a href='https://pubchem.ncbi.nlm.nih.gov/compound/15983949'>NADPH</a> + [thioredoxin]-disulfide + <a href='https://pubchem.ncbi.nlm.nih.gov/compound/1038'>H<small><sup>+</sup></small></a>
    direction: =
    otherdirections: 20346|20347|20348
    cids: 15983949|1038|15938972
    protacxns: P56431|Q9ZL18|Q58931|P0A9P4|Q1RJD8|Q4ULP1|Q68WT3|Q92I02|Q9ZD97|P0A9P5|P39916|P43788|P57399|P80892|P81433|Q89AJ2|Q9KSS4|O66790|O83790|P94284|O84101|Q9PKT7|Q9Z8M4|O30973|O32823|P46843|P47348|P50971|P52213|P52215|P66010|P66011|P75531|P80880|P99101|P9WHH0|P9WHH1|Q05741|Q5HHQ4|Q5HQW4|Q6GB66|Q6GIM7|Q8CPY8|Q928B5|Q98PK9|Q9PR71|P38816|D4APQ6|P29509|P43496|P51978|Q6BIS1|Q6C7L4|Q6FR39|Q6HA24|Q75CM8|Q7Z7S3|Q8J0U0|Q92375|Q16881|A6QP01|P62341|P62342|Q19892|Q1H5H1|Q5ZJN8|Q6PBD1|Q6PHY8|Q802F2|Q9U3N5|Q9VMV6|O62768|O89049|P
    pmids: 11012661
    ecs: 1.8.1.9
    geneids: 1452444|61754092|949054|917715|1209097|56470832|57739856|57879332|884181|1245727|45050363|987338|1099326|936549|45427913|886232|61470992|50019306|61171736|29672186|856506|9523739|851955|3881395|2904781|2911244|2889334|2894621|4619415|3361358|7296|783831|51714|69227|185097|365802|425041|394463|352921|352919|181343|33725|282388|31760|177466|100174180|114112|232223|26462|50493|282389|10587|40475|50551|8622741|813514|4344159|4340912|4330505|818766|816248|829698
    dois: 10.1046/j.1432-1327.2000.01701.x
    """

    Interactor_ab = create_subject_uri(row[0], row[1])
    g.add((Interactor_ab, RDF.type, molecular_interaction))

    Interactor_a = create_object_uri(row[0], db_list)
    g.add((Interactor_ab, has_interactorA, Interactor_a))
    g.add((Interactor_a, RDF.type, functional_entiry))
    Interactor_b = create_object_uri(row[1], db_list)
    g.add((Interactor_ab, has_interactorB, Interactor_b))
    g.add((Interactor_b, RDF.type, functional_entiry))

    if row[6] != "-" and row[6] != "":
        Detection_method = create_object_uri(row[6], db_list)
        g.add((Interactor_ab, detected_by, Detection_method))
    return g

