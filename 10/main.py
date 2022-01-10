import cProfile
import logging

from loadValues import LoadValues


def is_correct_close(opener, closer):
    return (opener == '(' and closer == ')') or (opener == '[' and closer == ']') or (opener == '{' and closer == '}') \
           or (opener == '<' and closer == '>')


def score_incorrect(op):
    if op == ')':
        return 3
    elif op == ']':
        return 57
    elif op == '}':
        return 1197
    elif op == '>':
        return 25137
    else:
        return 0

def score_closer(op):
    if op == '(':
        return 1
    elif op == '[':
        return 2
    elif op == '{':
        return 3
    elif op == '<':
        return 4
    else:
        return 0

def score_completion(operators):
    score = 0
    while operators:
        op = operators.pop()
        score *= 5
        score += score_closer(op)
    return score


def parse_line(line):
    operators = []

    correct = True

    for op in line:
        if (op == '(') or (op == '[') or (op == '{') or (op == '<'):
            operators.append(op)
        else:
            tmp = is_correct_close(operators.pop(), op)
            if not tmp:
                return (op, operators)
    return ('', operators)


def main():
    number = 0

    lv = LoadValues("input")
    lines = lv.strip_lines()

    tmp = [parse_line(line) for line in lines]
    print(tmp)

    star1 = [score_incorrect(res[0]) for res in tmp ]
    number = sum(star1)

    print("Star 1 : ", number)


    number = 0
    star2 = sorted([score_completion(res[1]) for res in tmp if res[0] == ''])
    print(star2)
    number = star2[len(star2)//2]
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
