from .power import ExpandedAlignment


def collapse_list(seq):
    return list(dict.fromkeys(seq))


def align_pair(exp_align: ExpandedAlignment, align_ref=True):
    """
    `align_type` are either `ref` or `hyp`
    """
    if align_ref:
        smap, s_tokens = exp_align.s1_map, list(exp_align.s1_tokens())
    else:
        smap, s_tokens = exp_align.s2_map, list(exp_align.s2_tokens())
    smap = collapse_list(smap)

    if not smap:
        return []
    align_result = [""] * (smap[-1]+1)

    for pos, tk in zip(smap, s_tokens):
        align_result[pos] = tk
    return align_result
