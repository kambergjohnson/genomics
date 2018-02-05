# Katie Amberg-Johnson
# Goal: get information about overlapping SNPs via toxodb
# Input: gene_IDs (list of genes you are interested in, in my case its the overlapping genes) and properties (information you want to get from ToxoDB)
# Output: a prettytable with the relevant information.

import urllib.request
import json
import tables
from prettytable import PrettyTable

# data from 3_overlapping_set.py
gene_IDs = ['TGGT1_254470', 'TGGT1_272550', 'TGGT1_286440', 'TGGT1_410060']

properties = ['gene_type', 'gene_product', 'gene_name',]  # protein_sequence

# request relevant data from toxodb


def request_toxodb(gene_list, prop_list):
    # request information from toxoDB
    request = urllib.request.Request(
        "http://toxodb.org/webservices/GeneQuestions/GeneByLocusTag.json")
    data = urllib.parse.urlencode(
        {'ds_gene_ids_data': ','.join(gene_list), 'o-fields': ','.join(prop_list)}).encode()
    #print(data)
    full_data = json.loads(
        urllib.request.urlopen(
            request,
            data).read().decode())
    #print(full_data)
	#info is dictionary with keys as geneIDs and values as dictionaries with properties 
    info = {}
    # go through json structure and get out information
    nice_data_list = full_data['response']['recordset']['records']
    for result in nice_data_list:
        id = result['id'] 
        info[id] = {}
        #build a dictionary for each geneID with properties
        for field in result['fields']:
            property = field['name']
            value = field['value']
            info[id][property] = value
            #parse for gene length (including introns) 
            if property == 'location_text':
            	#first get everything after colon
            	#then everything before the parentheses
            	#then first and last nucleotide denoted by dash
            	#then remove commas and whitespace
                filter1 = value.split(':')[1] 
                filter2 = filter1.split('(')[0]
                startTrans = filter2.split('-')[0]
                endTrans = filter2.split('-')[1]
                length = int(endTrans.strip().replace(',', '')) - \
                    int(startTrans.strip().replace(',', ''))
                info[id]['gene_name'] = length
    return info

req_data = request_toxodb(gene_IDs, properties)
#build a prettytable
x = PrettyTable(["Gene Name", "Gene Type", "Gene Product"])
for id, data in req_data.items():
    x.add_row([id, data['gene_type'], data['gene_product']])
print(x)
