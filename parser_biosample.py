import sys,gzip

try:
    infile = sys.argv[1]
except:
    print 'python parser_biosample.py biosample_set.xml.gz'
    exit(1)

chk=0
content = list()
print '#SRA\tTaxonomy Id\tTaxonomy Name\tSubmitter\tStudy Name\tStudy Design\tSex\tIsolation Source\tSample Type\tStudy Disease\tAffected/Tumor'
for recs in gzip.open(infile):
    if chk == 0 and recs.strip().startswith('<BioSample '):
        chk = 1
        content = ['-','-','-','-','-','-','-','-','-','-','-']

    if chk == 1 and recs.strip().startswith('</BioSample>'):

        if content[0] == '-':
            pass
        else:
            i=0
            for x in content:
                if x == '-':
                    i+=1
            if i < 7:
                print '%s'%('\t'.join(content))
            else:
                pass
        #content = list()
        content = ['-','-','-','-','-','-','-','-','-','-','-']
        chk = 0

    if chk == 1 and recs.strip().startswith('<Id db="SRA">'):
        recs = (recs.strip().split('">')[-1]).split('<')[0]
        #print recs
        if recs.strip() == '':
            content[0] = '-'
        else:
            content[0] = recs

    if chk == 1 and recs.strip().find('<Organism taxonomy_id=') != -1:
        rec = recs.strip().split('="')
        tax_id = rec[1].strip().split('"')[0]
        tax_name = rec[2].strip().split('"')[0]
        if tax_id.strip() == '':
            content[1] = '-'
        else:
            content[1] = tax_id.strip()

        if tax_name.strip() == '':
            content[2] = '-'
        else:
            content[2] = tax_name.strip()

    if chk == 1 and recs.strip().find('<Attribute attribute_name="submitter handle"') != -1:
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip() == '':
           content[3] = '-'
        else:
           content[3] = recs

    if chk == 1 and recs.strip().find('<Attribute attribute_name="study name"') != -1:
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip()  == '':
            content[4] = '-'
        else:
            content[4] = recs

    if chk == 1 and recs.strip().find('<Attribute attribute_name="study design"') != -1:
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip() == '':
            content[5] = '-'
        else:
            content[5] = recs

    if chk == 1 and (recs.strip().find('<Attribute attribute_name="host_sex"') != -1 or recs.strip().find('<Attribute attribute_name="sex"') != -1):
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip() == '':
            content[6] = '-'
        else:
            content[6] = recs

    if chk == 1 and (recs.strip().find('<Attribute attribute_name="isolation_source"') != -1 or recs.strip().find('<Attribute attribute_name="body site"') != -1):
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip()  == '':
            content[7] = '-'
        else:
            content[7] = recs

    if chk == 1 and recs.strip().find('<Attribute attribute_name="analyte type"') != -1:
        recs = recs.strip().split('">')[-1].split('<')[0]
        #print recs
        if recs.strip() == '':
            content[8] = '-'
        else:
            content[8] = recs

    if chk == 1 and recs.strip().find('<Attribute attribute_name="study disease"') != -1:
        recs = recs.strip().split('">')[-1].split('<')[0]
        if recs.strip() == '':
            content[9] = '-'
        else:
            content[9] = recs

    if chk == 1 and (recs.strip().find('<Attribute attribute_name="subject is affected"') != -1 or recs.strip().find('<Attribute attribute_name="is tumor"') !=-1):
        recs = recs.strip().split('">')[-1].split('<')[0]
        if recs.strip() == '':
            content[10] = '-'
        else:
            content[10] = recs
