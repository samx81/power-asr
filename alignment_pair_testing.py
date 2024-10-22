from power.aligner import PowerAligner
from power.levenshtein import ExpandedAlignment

lexicon = "lex/cmudict.0.7a.json"
lexicon = "lex/cmudict.rep.json"


def collapse_list(seq):
    return list(dict.fromkeys(seq))


def align_pair(expanded_align: ExpandedAlignment, align_type='ref'):
    """
    `align_type` are either `ref` or `hyp`
    """
    type_id = 1 if align_type == 'ref' else 2

    smap = getattr(expanded_align, f"s{type_id}_map")
    # Be careful of the parentheses at the end, you need to run this `tokens` function
    s_tokens = list(getattr(expanded_align, f"s{type_id}_tokens")())
    align_result = [""] * (smap[-1]+1)
    for pos, tk in zip(collapse_list(smap), s_tokens):
        align_result[pos] = tk
    return align_result


### Printing Helpers ###
def print_phones(ref, hyp):
    buf_r, buf_h = [], []
    for r, h in zip(ref, hyp):
        if r == '|' and buf_r:
            print(' '.join(buf_r))
            print(' '.join(buf_h))
            print('----')
            buf_h.clear()
            buf_r.clear()
        else:
            buf_r.append(r)
            buf_h.append(h)
    print(' '.join(buf_r))
    print(' '.join(buf_h))


def print_tokens_and_map(expanded_align: ExpandedAlignment):
    print(expanded_align.s1_tokens())
    print(expanded_align.s1_map)
    print(expanded_align.s2_tokens())
    print(expanded_align.s2_map)


hyp = 'THREE WHAT IS YOUR FIGURET OLD STORE ACTIVITY MY FAVORET STORE ACTIVITY IS GOING CYCLING'
ref = "THREE WHAT IS YOUR FAVORITE OUTDOOR ACTIVITY MY FAVORITE OUTDOOR ACTIVITY EASE GOING CYCLING"
aligner = PowerAligner(ref, hyp, lowercase=True, lexicon=lexicon)
aligner.align()
for i in range(len(aligner.split_regions)):

    print(aligner.split_regions[i])
    print(aligner.phonetic_alignments[i])
    print('-----')

    # print_tokens_and_map(aligner.split_regions[i])
    print('-----')

    ref = align_pair(aligner.split_regions[i], 'ref')
    hyp = align_pair(aligner.split_regions[i], 'hyp')
    print(ref)
    print(hyp)
    print('-----')
    print(aligner.split_regions[i].align)

    # If Eval result, is mostly correct (I guess if all words in a region or only last word is error)
    # no phontic align will run
    if not aligner.phonetic_alignments[i]:
        print('## NO PHONITC ALIGN ##')
        continue
    # New a list(size should be the same between two list, and the size is s1_map[-1])
    # then fill s1_tokens with s1_map index
    # print_tokens_and_map(aligner.phonetic_alignments[i])

    ref = align_pair(aligner.phonetic_alignments[i], 'ref')
    hyp = align_pair(aligner.phonetic_alignments[i], 'hyp')
    print_phones(ref, hyp)

    print('====')
exit()
hyp = 'de pamendle onda mom i not war toes we had it to the womans de patmens first and loks'
ref = "department store last Sunday We headed to the women's department first and looked"
aligner = PowerAligner(ref, hyp, lowercase=True, lexicon=lexicon)
aligner.align()
for i in range(len(aligner.split_regions)):

    print(aligner.split_regions[i])
    print(aligner.phonetic_alignments[i])
    print('-----')

    # print_tokens_and_map(aligner.split_regions[i])
    print('-----')

    ref = align_pair(aligner.split_regions[i], 'ref')
    hyp = align_pair(aligner.split_regions[i], 'hyp')
    print(ref)
    print(hyp)
    print('-----')
    print(aligner.split_regions[i].align)

    # If Eval result, is mostly correct (I guess if all words in a region or only last word is error)
    # no phontic align will run
    if not aligner.phonetic_alignments[i]:
        print('## NO PHONITC ALIGN ##')
        continue
    # New a list(size should be the same between two list, and the size is s1_map[-1])
    # then fill s1_tokens with s1_map index
    # print_tokens_and_map(aligner.phonetic_alignments[i])

    ref = align_pair(aligner.phonetic_alignments[i], 'ref')
    hyp = align_pair(aligner.phonetic_alignments[i], 'hyp')
    print_phones(ref, hyp)

    print('====')


# ref = "Student student student"
# hyp = 'SUBDUED THE STEWARD STUD'
# aligner = PowerAligner(ref, hyp, lowercase=True, lexicon=lexicon)
# aligner.align()
# for i in aligner.error_indexes:
#     print(aligner.split_regions[i])
#     print(aligner.phonetic_alignments[i])
#     print('-----')

# for s1, s2 in zip(aligner.power_alignment.s1_tokens(), aligner.power_alignment.s2_tokens()):
#     print(s1, '|', s2)
# print('====')

# for reg in aligner.phonetic_alignments:
#     print(reg.s1_tokens())
#     print(reg.s2_map)
# # for it in aligner.:
# #     print(it)

# for reg in aligner.split_regions:
#     print(reg.s1_tokens())
#     print(reg.s2_map)

#     print(reg)
