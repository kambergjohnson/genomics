# Katie Amberg-Johnson
# Goal: make a pie chart describe the types of SNP that occur in our sample
# Input: (d): dictionary with information about each SNP type. Produced by script 1_read_vcf_parse_multifile.py
# Ouptut: piechart describing the types of mutations in my samples.
from pylab import *

# dictionary from 1_read_vcf_parse_multifile.py
d = {
    '2': {
        'SYNONYMOUS_CODING': 7,
        'INTRON': 38,
        'STOP_GAINED': 3,
        'NON_SYNONYMOUS_CODING': 13},
    '3': {
        'SYNONYMOUS_CODING': 9,
        'INTRON': 37,
        'STOP_GAINED': 1,
        'NON_SYNONYMOUS_CODING': 19},
    '4': {
        'SYNONYMOUS_CODING': 4,
        'INTRON': 62,
        'STOP_GAINED': 2,
        'NON_SYNONYMOUS_CODING': 26}}

final_total_list = []
SC = []
NSC = []
I = []
SG = []

# build lists that contain aggregate information from the dictionary
for key in d:
    for k in d[key]:
        if k == 'SYNONYMOUS_CODING':
            SC.append(d[key][k])
        if k == 'INTRON':
            I.append(d[key][k])
        if k == 'STOP_GAINED':
            SG.append(d[key][k])
        if k == 'NON_SYNONYMOUS_CODING':
            NSC.append(d[key][k])

# sum the information for the pie chart
SC_sum = sum(SC)
NSC_sum = sum(NSC)
I_sum = sum(I)
SG_sum = sum(SG)

total = float(sum([SC_sum, NSC_sum, I_sum, SG_sum]))

# get the percent for the pie chart
percent_SC = 100 * (SC_sum / total)
percent_NSC = 100 * (NSC_sum / total)
percent_I = 100 * (I_sum / total)
percent_SG = 100 * (SG_sum / total)

# make a square figure and axes
figure(1, figsize=(6, 6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = [
    'SYNONYMOUS_CODING',
    'INTRON',
    'STOP_GAINED',
    'NON_SYNONYMOUS_CODING']
values = [percent_SC, percent_I, percent_SG, percent_NSC]

pie(values, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

title('SNP Types Across All Samples', bbox={'facecolor': '0.8', 'pad': 5})

show()
