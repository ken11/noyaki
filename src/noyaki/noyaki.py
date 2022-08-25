import re


# @params
# tokenized_text: list
# labels: list of list
# eg.
# tokenized_text = ['明日', 'は', '田中', 'さん', 'に', '会う']
# labels = [[3, 5, 'PERSON']]
#
# @return
# label_list: list
# eg.
# label_list = ['O', 'O', 'U-PERSON', 'O', 'O', 'O']
def convert(tokenized_text, labels, subword=None, scheme="BILOU"):
    # init return list
    label_list = ['O'] * len(tokenized_text)

    for label in labels:
        begin = label[0]
        end = label[1]
        label_text = label[2]
        position = 0
        targets = []

        for idx, word in enumerate(tokenized_text):
            if type(subword) is str:
                word = re.sub(subword, "", word)
            if begin <= position < end:
                targets.append(idx)
            position += len(word)

        if scheme == "BILOU":
            label_list = _bilou(targets, label_list, label_text)
        elif scheme == "IOB2":
            label_list = _iob2(targets, label_list, label_text)

    return label_list


def _bilou(targets, label_list, label_text):
    if len(targets) == 1:
        label_list[targets[0]] = f'U-{label_text}'
    elif len(targets) == 2:
        label_list[targets[0]] = f'B-{label_text}'
        label_list[targets[1]] = f'L-{label_text}'
    elif len(targets) >= 3:
        label_list[targets.pop(0)] = f'B-{label_text}'
        label_list[targets.pop(-1)] = f'L-{label_text}'
        for i in targets:
            label_list[i] = f'I-{label_text}'
    return label_list


def _iob2(targets, label_list, label_text):
    if len(targets) == 1:
        label_list[targets[0]] = f'B-{label_text}'
    elif len(targets) == 2:
        label_list[targets[0]] = f'B-{label_text}'
        label_list[targets[1]] = f'I-{label_text}'
    elif len(targets) >= 3:
        label_list[targets.pop(0)] = f'B-{label_text}'
        for i in targets:
            label_list[i] = f'I-{label_text}'
    return label_list
