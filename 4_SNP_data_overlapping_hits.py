# Katie Amberg-Johnson
# Goal: for the overlapping SNPs, export information about them from SNPeff annotation
# Make a pretty table, using prettytable!
# Input: (d) set that contains the overlapping genes. Produced by 3_overlapping_set.py.
# Ouptut: a prettytable that contains information about the SNPs contained
# in those genes.

# data from 3_overlapping_set.py
d = {'TGGT1_254470', 'TGGT1_272550', 'TGGT1_286440', 'TGGT1_410060'}

import sys
import re
import tables
import os
from prettytable import PrettyTable

path = sys.argv[1]  # folder that has the vcf files
dirs = os.listdir(path)
file_number_id = 0

d_list = list(d)  # turn data into list
count = 0
x = PrettyTable(["Gene_ID",
                 "Sample_ID",
                 "Chromosome/Contig",
                 "Reference Nucleotide",
                 "Alternative Nucleotide",
                 "SNP_type"])

for file in dirs:  # walk through dir
    if re.match('.*\.vcf$', file):  # only want the vcf files
        file_number_id += 1  # make a number identifier for each file
        # print(file_number_id)
        vcf_file = file
        vcf_file_path = os.path.join(path, vcf_file)
        with open(vcf_file_path, 'r') as vcf:
            for line in vcf:
                vcf_line = line.rstrip('\n').split('\t')
                if vcf_line[0][0] == '#':  # header always starts with #
                    pass
                else:
                    # get to SNPeff annotation
                    info = vcf_line[7].rstrip('\n').split(';')
                    chromosome = vcf_line[0]
                    reference = vcf_line[3]
                    alternative = vcf_line[4]
                    # SNPeff only annotates SNPs for which the DB has
                    # information on
                    if info[-1].startswith('EFF='):
                        SNPeff_split = info[-1].rstrip('\n').split('|')
                        # print(SNPeff_split[-2]) #check the annotation
                        SNP_type = re.search(
                            '(?<=EFF=)(\w+)',
                            SNPeff_split[0]).group(0)  # general name of SNP
                        for item in d_list:
                            # look for only overlapping genes
                            if str(item) == str(SNPeff_split[-2]):
                                #print(item, file_number_id, chromosome, reference, alternative, SNP_type)
                                x.add_row([item,
                                           file_number_id,
                                           chromosome,
                                           reference,
                                           alternative,
                                           SNP_type])

print(x.get_string(sortby='SNP_type', reversesort=True))
# print(x)
