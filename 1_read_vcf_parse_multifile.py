# Katie Amberg-Johnson
# Goal: Read in each vcf file in the directory and extract gene name, SNP type, and type of SNP from the SNPeff notation.
# Retain information regarding the origin of each SNP (each file represents a different sample).
# Input: a folder containing vcf files that have been annotated with SNPeff
# Output: a dictionary that describes the SNP types for each vcf files and
# a dictionary that have a list of genes from each vcf file.
import sys
import re
import os

path = sys.argv[1]  # folder that contains the data
dirs = os.listdir(path)
file_number_id = 0  # each sample file will get a unique number ID
outer_d_SNPtype = {}
outer_d_gene_name = {}


for file in dirs:  # walk through dir
    if re.match('.*\.vcf$', file):  # only want the vcf files
        file_number_id += 1  # make a number identifier for each file
        # print(file_number_id)
        vcf_file = file
        vcf_file_path = os.path.join(path, vcf_file)
        SNP_type_list = []  # clear in between files
        gene_names = []
        with open(vcf_file_path, 'r') as vcf:
            for line in vcf:
                vcf_line = line.rstrip('\n').split('\t')
                if vcf_line[0][0] == '#':  # header always starts with #
                    pass
                else:
                    # get to SNPeff annotation
                    info = vcf_line[7].rstrip('\n').split(';')
                    # SNPeff only annotates SNPs for which the DB has
                    # information on
                    if info[-1].startswith('EFF='):
                        SNPeff_split = info[-1].rstrip('\n').split('|')
                        # print(SNPeff_split) #check the annotation
                        SNP_type = re.search(
                            '(?<=EFF=)(\w+)',
                            SNPeff_split[0]).group(0)  # general name of SNP type
                        SNP_type_list.append(SNP_type)
                        gene_names.append(SNPeff_split[-2])
            outer_d_gene_name[str(file_number_id)] = gene_names
            SNP_type_inner_d = {
                x: SNP_type_list.count(x) for x in SNP_type_list}
            outer_d_SNPtype[str(file_number_id)] = SNP_type_inner_d
            # print(outer_d_SNPtype)
            # print(outer_d_gene_name)

print(outer_d_SNPtype)
# generates a dictionary with keys = file_number_ids and values = dict
# with keys = SNP types and values = abundance
print(outer_d_gene_name)
# generates a dictionary with keys = file_number_ids and values = list of
# gene names
