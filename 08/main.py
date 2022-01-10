import cProfile
import logging

from loadValues import LoadValues


def parse_display_line(ln):
    split_ln = ln.split(' | ')
    signals = split_ln[0].split(' ')
    value = split_ln[1].split(' ')
    return (signals, value)

def one_for_seven_eight_in_value(value):
    res = [(seg==2 or seg==4 or seg==3 or seg==7) for seg in [len(seg) for seg in value]]
    return sum(res)

def find_segments(signals):
    segment_mapping = {}
    number_mapping = []*10
    length_mapping = {}
    for sig in signals:
        tmp = list(sig)
        l_tmp = len(tmp)
        if l_tmp in length_mapping:
            length_mapping[l_tmp].append(tmp)
        else:
            length_mapping[l_tmp] = [tmp]
    one = length_mapping[2][0]
    seven = length_mapping[3][0]
    segment_mapping['a'] = (set(one)^set(seven)).pop()
    c_f = set(length_mapping[2][0])
    b_d = c_f ^ set(length_mapping[4][0])
    (n1, n2, n3) = length_mapping[6]

    for n in (n1,n2,n3):
        if len(set(n) & b_d) < 2:
            segment_mapping['b'] = (set(n) & b_d).pop()
    segment_mapping['d'] = (b_d ^ set(segment_mapping['b'])).pop()

    (n1, n2, n3) = [set(n) for n in length_mapping[5]]
    tmp = n1 & n2 & n3
    segment_mapping['d'] = (tmp & set(length_mapping[4][0])).pop()
    segment_mapping['g'] = (tmp ^ set(segment_mapping['a']) ^ set(segment_mapping['d'])).pop()

    (n1, n2, n3) = [set(n) for n in length_mapping[6]]
    a_b_f_g = n1 & n2 & n3
    segment_mapping['f'] = (a_b_f_g ^ set(segment_mapping['a']) ^ set(segment_mapping['b']) ^ set(segment_mapping['g'])).pop()
    segment_mapping['c'] = (c_f ^ set(segment_mapping['f'])).pop()

    segment_mapping['e'] = (set(length_mapping[7][0]) ^ set([val for val in segment_mapping.values()])).pop()

    return(segment_mapping)

def build_num_list_from_segments(segment_mapping):
    num_list = []
    num_from_segments = {}
    base_segments = [
        'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
        'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
    ]

    for i in range(len(base_segments)):
        dest_seg = ''.join(sorted([segment_mapping[l] for l in base_segments[i]]))
        # print(dest_seg)
        num_list.append(dest_seg)
        num_from_segments[dest_seg] = i
    return num_from_segments


def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()
    entries = [parse_display_line(ln) for ln in lines]

    for (signals, value) in entries:
        tmp = one_for_seven_eight_in_value(value)
        number += tmp
        # print(tmp, value)

    print("Star 1 : ", number)

    number = 0
    for entry in entries:
        segments = find_segments(entry[0])
        # print(segments)
        num_list = build_num_list_from_segments(segments)
        # print(num_list)

        value = 0
        for digit in entry[1]:
            ordered = ''.join(sorted(list(digit)))
            value = value * 10 + num_list[ordered]
        # print(value)
        number += value

    print("Star 2 : ", number)


##
if __name__ == '__main__':
    pr = cProfile.Profile()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Started')
    pr.enable()
    main()
    pr.disable()

    logging.info('Finished')
    # pr.print_stats()
