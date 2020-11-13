import os
import time

FILENAME = "foo.txt"
OUTPUT = "labeling.txt"
PUNC = ["\"", "!", "?",".",",","\'"]

def labeling(tokens):
    labels = []
    i = 0 
    for token in tokens:
        upper_ch = 0
        punc_ch = 0
        punc = ""
        for chr in token:
            if chr.isupper():
                upper_ch = 1
            if chr in PUNC:
                if punc_ch ==1:
                    punc = punc + chr
                else:
                    punc_ch = 1
                    punc = chr

        if upper_ch == 1:
            if punc_ch == 1:
                labels.append("U"+punc)
            else:
                labels.append("U")
        else:
            if punc_ch == 1:
                labels.append("L"+punc)
            else:
                labels.append("L")

    # print(labels)

    labels = ' '.join(labels)
    labels = labels + '\n'
    print(labels)
    return labels
            # elif chr in PUNC:

            


if __name__ == "__main__":

    with open(FILENAME, 'r') as src:
        with open(OUTPUT,'w') as tgt:
            lines = src.readlines()
            for line in lines:
                line = line[:-1]
                token = line.split(' ')
                label = labeling(token)
                tgt.write(label)
            tgt.close()
        src.close()