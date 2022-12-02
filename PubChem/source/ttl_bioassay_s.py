from rdflib.namespace import RDF
from source.utils import id2uri, g_add_with_valid
import csv
import json

def create_ttl(g, u, row):
    """
    aid: 624099
    aidtype: Other
    aidname: An siRNA screen for human genes that are involved in human papilloma virus (HPV) E2 transcriptional repression of the E6 and E7 oncogenes
    aiddesc: An essential step in the pathogenesis of human papillomavirus (HPV)-associated cancers is the dysregulated expression of the viral oncogenes. The papillomavirus E2 protein can silence the long control region (LCR) promoter that controls viral E6 and E7 oncogene expression. The mechanisms by which E2 represses oncogene expression and the cellular factors through which E2 mediates this silencing are largely unknown. We conducted an unbiased, genome-wide siRNA screen and series of secondary screens that identi
    aidsrcid: 46
    aidsrcname: ICCB-Longwood Screening Facility, Harvard Medical School
    aidextid: HMS729
    aidmdate: 20161014
    cids: NULL
    sids: 56478464|56478466|56478467|56478468|56478469|56478470|56478471|56478472|56478473|56478474|56478476|56478477|56478478|56478479|56478480|56478481|56478483|56478484|56478485|56478486|56478487|56478488|56478489|56478490|56478491|56478492|56478493|56478494|56478495|56478496|56478497|56478498|56478499|56478500|56478501|56478502|56478503|56478504|56478505|56478506|56478507|56478508|56478509|56478510|56478511|56478512|56478513|56478515|56478516|56478517|56478518|56478519|56478520|56478521|56478522|56478523|56478524
    geneids: 1|2|9|10|12|13|14|15|16|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|43|47|48|49|50|51|52|53|54|55|56|58|59|60|70|71|72|81|86|87|88|89|90|91|92|93|94|95|97|98|100|101|102|103|104|105|107|108|109|111|112|113|114|115|116|117|118|119|120|123|124|125|126|127|128|130|131|132|133|134|135|136|140|141|142|143|146|147|148|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|172|173|174|175|176|177|178|181|182|183|185|186|187|189|190|191|196|197|199|202|203|204|205|207|20
    aidcategories: RNAi
    protacxns: NULL
    depcatg: Research and Development
    pmids: 20133580|20181716
    rnai: 1
    ecs: NULL
    repacxns: NULL
    taxids: NULL
    cellids: NULL
    targettaxid: 
    annotation: NULL
    """

    cid = id2uri(row["cids"], "cid")
    sid = id2uri(row["sids"], "sid")
    gid = id2uri(row["geneids"], "gid")
    protein = id2uri(row["protacxns"], "protein")
    pmid = id2uri(row["pmids"], "pmid")

    g_add_with_valid(g, cid, RDF.type, u.cid)

    g_add_with_valid(g, sid, RDF.type, u.sid)
    g_add_with_valid(g, sid, u.sid2cid, cid)
    g_add_with_valid(g, sid, u.sid2pmid, pmid)

    g_add_with_valid(g, gid, RDF.type, u.gid)
    g_add_with_valid(g, gid, u.gid2pmid, pmid)

    g_add_with_valid(g, protein, RDF.type, u.protein)
    g_add_with_valid(g, protein, u.protein2gid, gid)

    g_add_with_valid(g, pmid, RDF.type, u.pmid)
    return g

