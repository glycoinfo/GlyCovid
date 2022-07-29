import re
import sys

def treatIRI(iri: str):
    return iri


class LibOwl:
    def __init__(self, template_file: str):
        self.owl_header = self.getOwlHeader(template_file)
        self.owl_prefix = self.getOwlPrefix(template_file)
        self.owl_annotation_properties = self.getOwlAnnotationProperties(template_file)
        self.owl_object_properties = self.getOwlObjectProperties(template_file)
        self.owl_classes = self.getOwlClasses(template_file)
        # use individual class instances
        # self.owl_individuals = self.getOwlIndividuals(template_file)
        self.owl_individuals = []
        self.owl_individuals_temp = self.getOwlIndividuals(template_file)
        self.owl_comment = self.getOwlComment(template_file)

    def getOwlHeader(self, file: str) -> list:
        text = list()
        with open(file) as f:
            for line in f:
                text.append(line.replace("\n", ""))
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 1
        text.insert(0, "#################################################################")
        return text

    def getOwlPrefix(self, file:str) -> dict:
        prefix = dict()
        with open(file) as f:
            for line in f:
                if line == "\n":
                    return prefix
                col = line.split(" ")
                prefix[col[1]] = col[2]



    def getOwlAnnotationProperties(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Annotation properties" in line:
                    isTarget = True
                if not isTarget:
                    continue
                else:
                    text.append(line.replace("\n", ""))
                    if len(text) > 3 and "#################" in line:
                        break
        assert len(text) > 3
        text.insert(0, "#################################################################")
        return text

    def getOwlObjectProperties(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Object Properties" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line.replace("\n", ""))
                if len(text) > 3 and "#################" in line:
                    break
        assert len(text) > 3
        text.insert(0, "#################################################################")
        return text

    def getOwlClasses(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Classes" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line.replace("\n", ""))
                if len(text) > 3 and "#################" in line:
                    break
        assert len(text) > 3
        text.insert(0, "#################################################################")
        return text

    def getOwlIndividuals(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Individuals" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line.replace("\n", ""))
                if len(text) > 3 and "#################" in line:
                    break
        assert len(text) > 3
        text = text[3:]
        individual = False
        individuals = []
        isType = False
        for t in text:
            col = re.split(r"\s+", t)
            if len(col) == 1 or col[0] == "###":
                continue
            elif col[0] != "" and col[1] == "rdf:type":
                # set rdf:type
                if individual:
                    individuals.append((individual))
                individual = Individual(col[0])
                if col[-1] == ",":
                    isType = True
            elif col[0] == "":
                if isType:
                    individual.typeIs(col[1])
                    assert col[-1] != ",", "cant create multiple class"
                    isType = False
                else:
                    assert col[-1] != ",", "cant create multiple object"
                    individual.addRelation(col[1], col[2])
        individuals.append(individual)
        for i in range(len(individuals)-1, 0, -1):
            if re.match(r"obo:MI_\d{4}", individuals[i].subject):
                individuals.pop(i)
        return individuals

    def getOwlComment(self, file: str) -> list:
        f = open(file, "r")
        text = f.read()
        f.close
        return [text.split("\n")[-1]]

    def importRdf(self, file: str, subject_class:str):
        """ convert rdf data to Individual instance and append in LibOwl.individuals
        """
        # create prefix
        # create rdf.matrix
        with open(file) as f:
            isRdf = False
            prefix = dict()
            rdfs = list()
            for line in f:
                if line == "\n":
                    if isRdf:
                        rdfs.append(rdf)
                    rdf = []
                    isRdf = True
                    continue
                if not isRdf:
                    cols = line.split(" ")
                    prefix[cols[1]] = cols[2]
                else:
                    line = line.replace("\n", "")
                    rdf.append(line)
                if line == "\n":
                    rdfs.append(rdf)
                    rdf = []
                    isRdf = True
                    continue
        # create indivisdual instance from rdf matrix
        # for i in self.owl_individuals:
        #     print(i.type)
        # print(prefix)
        for rdf in rdfs:
            assert len(rdf) > 1, "Rdf import error !"
            for r in rdf:
                col = re.split(r"\s+", r)
                # print(col)
                # spo
                if len(col) == 4:
                    if col[0] != "":
                        uri = self.toURI(col[0], prefix)
                        individual = Individual(uri)
                        individual.typeIs(subject_class)
                        self.owl_individuals.append(individual)
                        uri = self.toURI(col[2], prefix)
                        prouri = self.toURI(col[1], prefix)
                        individual = self.createIndividualFromTemp(prouri, uri)
                        self.owl_individuals.append(individual)
                    else:
                        uri = self.toURI(col[2], prefix)
                        prouri = self.toURI(col[1], prefix)
                        individual = self.createIndividualFromTemp(prouri, uri)
                        self.owl_individuals.append(individual)
                # po
                elif len(col) == 3:
                    uri = self.toURI(col[2], prefix)
                    individual = self.createIndividualFromTemp(prouri, uri)
                    self.owl_individuals.append(individual)
                else:
                    print("error >>", len(col), col)
                    sys.exit()
                print("\t", self.owl_individuals[-1].subject, self.owl_individuals[-1].type)
            return

    def toURI(self, text:str, prefix: dict=None):
        if text[0:1] == "<" and text[-1:] == ">":
            return text
        if prefix is None:
            for key in self.owl_prefix:
                if re.match(r"^"+key, text):
                    text = text.replace(key, self.owl_prefix[key][:-1], 1)
                    text += ">"
                    return text

        else:
            for key in prefix:
                if re.match(r"^"+key, text):
                    text = text.replace(key, prefix[key][:-1], 1)
                    text += ">"
                    return text
            print("error in", text)
            sys.exit()

    def getURIHeader(self, uri:str) -> str:
        return "/".join(uri.split("/")[:-1])


    def createIndividualFromTemp(self, property: str, uri: str):
        individual = Individual(uri)
        print(property)
        for i in self.owl_individuals_temp:
            for relation in i.relations:
                if self.toURI(relation["property"]) == property:
                    print(relation)
                    for ii in self.owl_individuals_temp:
                        if ii.subject == o:
                            print(ii.type)
                            individual.type = ii.type
                    # individual.type = i.type
        if individual.type is None:
            print("eror >>        type is none")
            sys.exit()
        else:
            return individual





class Individual:
    def __init__(self, subject: str):
        subject = treatIRI(subject)
        self.type = None
        self.relations = list()
        self.subject = subject

    def typeIs(self, type: str):
        type = treatIRI(type)
        self.type = type

    def addRelation(self, property: str, object: list):
        property = treatIRI(property)
        self.relations.append({"property": property, "object": object})

    def toStr(self) -> str:
        """
                ###  https://identifiers.org/matrixdb.association:ensembl_ENSG00000023445__uniprotkb_Q04206
                <https://identifiers.org/matrixdb.association:ensembl_ENSG00000023445__uniprotkb_Q04206> rdf:type owl:NamedIndividual ,
                            bpo:MolecularInteraction ;
                         obo:IAO_0000119 <http://glycoinfo.org/dbid/imex/IM-23322> ;
                         obo:INO_0000154 obo:MI_0914 ;
                         bpo:interactionType obo:MI_0914 ;
                         bpo:organism <http://glycoinfo.org/dbid/taxonomy/9606> ;
                         dc:identifier <http://glycoinfo.org/dbid/imex/IM-23322-1> ;
                         dc:source obo:MI_0469 ;
                         bao:BAO_0002875 obo:MI_0402 .
        """
        assert self.type is not None
        textlist = [
                    "### " + self.subject,
                    self.subject + " rdf:type owl:NameIndividual ,",
                    "\t\t" + self.type + ";"
                ]
        for relation in self.relations:
            if len(relation["object"]) == 1:
                textlist.append("\t" + relation["property"] +  " " + relation["object"] + " ;")
            else:
                for i in range(len(relation["object"])):
                    if i == 0:
                        textlist.append("\t" + relation["property"] +  " " + relation["object"] + " ,")
                    else:
                        if i == len(relation["object"] - 1):
                            textlist.append("\t\t " + relation["object"] + " ;")
                        else:
                            textlist.append("\t\t " + relation["object"] + " ,")
        textlist[-1] = textlist[-1][:-1] + "."
        textlist.append("")
        text = ""
        for tl in textlist:
            text += tl + "\n"
        return text



if __name__ == "__main__":
    owl = LibOwl("owl/1_19/psicquic1_19.owl")
    owl.importRdf("turtle/IntAct/IntAct1.ttl", "bpo:MolecularInteraction")
