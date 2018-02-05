# Katie Amberg-Johnson
# Goal: find the overlapping genes between the samples.
# Input: (d): dictionary with each gene name from each sample. Produced by 1_read_vcf_parse_multifile.py.
# Output: the names of the overlapping genes as well as a venn diagram
# describing the amount of overlap.

# data comes from 1_read_vcf_parse_multifile.py
d = {
    '3': [
        'TGGT1_280070A',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410610',
        'TGGT1_322300',
        'TGGT1_411040',
        'TGGT1_411310',
        'TGGT1_411520',
        'TGGT1_293770',
        'TGGT1_208540',
        'TGGT1_209430',
        'TGGT1_321540',
        'TGGT1_254470',
        'TGGT1_222710',
        'TGGT1_210980',
        'TGGT1_210960',
        'TGGT1_267875',
        'TGGT1_306230',
        'TGGT1_206550',
        'TGGT1_202610',
        'TGGT1_255860',
        'TGGT1_229140',
        'TGGT1_229380',
        'TGGT1_229440',
        'TGGT1_231970',
        'TGGT1_232100',
        'TGGT1_233100',
        'TGGT1_272550',
        'TGGT1_272420',
        'TGGT1_270840',
        'TGGT1_213340',
        'TGGT1_286440',
        'TGGT1_285540',
        'TGGT1_245730',
        'TGGT1_247350',
        'TGGT1_248540',
        'TGGT1_249810',
        'TGGT1_251490',
        'TGGT1_307040',
        'TGGT1_309730',
        'TGGT1_309980',
        'TGGT1_313090',
        'TGGT1_228330',
        'TGGT1_214830',
        'TGGT1_215100',
        'TGGT1_215260',
        'TGGT1_280070A',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410610',
        'TGGT1_322300',
        'TGGT1_411040',
        'TGGT1_411310',
        'TGGT1_411520',
        'TGGT1_293770',
        'TGGT1_208540',
        'TGGT1_209430',
        'TGGT1_321540',
        'TGGT1_254470',
        'TGGT1_222710',
        'TGGT1_210980',
        'TGGT1_210960',
        'TGGT1_267875',
        'TGGT1_306230',
        'TGGT1_206550',
        'TGGT1_202610',
        'TGGT1_255860',
        'TGGT1_229140',
        'TGGT1_229380',
        'TGGT1_229440',
        'TGGT1_231970',
        'TGGT1_232100',
        'TGGT1_233100',
        'TGGT1_272550',
        'TGGT1_272420',
        'TGGT1_270840',
        'TGGT1_213340',
        'TGGT1_286440',
        'TGGT1_285540',
        'TGGT1_245730',
        'TGGT1_247350',
        'TGGT1_248540',
        'TGGT1_249810',
        'TGGT1_251490',
        'TGGT1_307040',
        'TGGT1_309730',
        'TGGT1_309980',
        'TGGT1_313090',
        'TGGT1_228330',
        'TGGT1_214830',
        'TGGT1_215100',
        'TGGT1_215260'],
    '2': [
        'TGGT1_257910A',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410060',
        'TGGT1_410890',
        'TGGT1_410900',
        'TGGT1_411310',
        'TGGT1_411310',
        'TGGT1_411520',
        'TGGT1_411560',
        'TGGT1_295610',
        'TGGT1_207410',
        'TGGT1_253930',
        'TGGT1_254470',
        'TGGT1_299210',
        'TGGT1_410360',
        'TGGT1_264752',
        'TGGT1_289190',
        'TGGT1_289280',
        'TGGT1_290290',
        'TGGT1_291020',
        'TGGT1_291020',
        'TGGT1_291340',
        'TGGT1_305890',
        'TGGT1_305890',
        'TGGT1_306020',
        'TGGT1_206510',
        'TGGT1_203200',
        'TGGT1_202445',
        'TGGT1_263050',
        'TGGT1_261050',
        'TGGT1_260440',
        'TGGT1_258580',
        'TGGT1_258540',
        'TGGT1_229140',
        'TGGT1_229630',
        'TGGT1_230690',
        'TGGT1_231970',
        'TGGT1_272550',
        'TGGT1_270510',
        'TGGT1_239365',
        'TGGT1_242055',
        'TGGT1_243960',
        'TGGT1_220212',
        'TGGT1_213580',
        'TGGT1_213620',
        'TGGT1_286440',
        'TGGT1_285500',
        'TGGT1_284598',
        'TGGT1_249770',
        'TGGT1_278600',
        'TGGT1_277010',
        'TGGT1_277010',
        'TGGT1_306860',
        'TGGT1_309220',
        'TGGT1_313370',
        'TGGT1_314780',
        'TGGT1_227948',
        'TGGT1_226470',
        'TGGT1_225990',
        'TGGT1_224205',
        'TGGT1_223450A',
        'TGGT1_235640',
        'TGGT1_214880',
        'TGGT1_275490'],
    '1': [
        'TGGT1_360840',
        'TGGT1_410060',
        'TGGT1_410890',
        'TGGT1_410890',
        'TGGT1_365150',
        'TGGT1_410920',
        'TGGT1_410920',
        'TGGT1_329400',
        'TGGT1_411420',
        'TGGT1_411510',
        'TGGT1_306688',
        'TGGT1_411560',
        'TGGT1_294350',
        'TGGT1_207880',
        'TGGT1_209250',
        'TGGT1_254420',
        'TGGT1_254470',
        'TGGT1_410360',
        'TGGT1_223045',
        'TGGT1_318760',
        'TGGT1_318525',
        'TGGT1_266750',
        'TGGT1_291020',
        'TGGT1_292035',
        'TGGT1_305470',
        'TGGT1_281520',
        'TGGT1_260680',
        'TGGT1_259210',
        'TGGT1_257340',
        'TGGT1_229670',
        'TGGT1_232010',
        'TGGT1_272550',
        'TGGT1_272370',
        'TGGT1_271950',
        'TGGT1_270190',
        'TGGT1_269850',
        'TGGT1_269075',
        'TGGT1_242625',
        'TGGT1_244580',
        'TGGT1_213520',
        'TGGT1_286440',
        'TGGT1_285780',
        'TGGT1_217480',
        'TGGT1_247850',
        'TGGT1_248540',
        'TGGT1_248710',
        'TGGT1_277940',
        'TGGT1_277010',
        'TGGT1_277010',
        'TGGT1_306860',
        'TGGT1_312150',
        'TGGT1_313090',
        'TGGT1_313380',
        'TGGT1_314020',
        'TGGT1_315270',
        'TGGT1_226270',
        'TGGT1_225200',
        'TGGT1_234410',
        'TGGT1_214300',
        'TGGT1_214590',
        'TGGT1_214830']}

# convert each into a set
one = set(d['1'])
two = set(d['2'])
three = set(d['3'])

# get the intersection
one_two = one.intersection(two)
one_two_three = one_two.intersection(three)
one_three = one.intersection(three)
two_three = two.intersection(three)

# These are the overlapping genes:
print(one_two_three)

# get the remainders
one_minus_two = one.difference(two)
one_alone = one_minus_two.difference(three)

two_minus_one = two.difference(one)
two_alone = two_minus_one.difference(three)

three_minus_one = three.difference(one)
three_alone = three_minus_one.difference(two)

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles

plt.figure(figsize=(4, 4))
v = venn3(
    subsets=(
        1, 1, 1, 1, 1, 1, 1), set_labels=(
            'Sample 1', 'Sample 2', 'Sample 3'))

v.get_label_by_id('100').set_text(len(one_alone))
v.get_label_by_id('010').set_text(len(two_alone))
v.get_label_by_id('001').set_text(len(three_alone))
v.get_label_by_id('110').set_text(len(one_two))
v.get_label_by_id('101').set_text(len(one_three))
v.get_label_by_id('011').set_text(len(two_three))
v.get_label_by_id('111').set_text(len(one_two_three))

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')

plt.title("Overlapping Hits between Samples")

plt.show()
