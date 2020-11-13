import os
import sys
import time
import random

src_file_path = sys.argv[1]
tgt_output_path = sys.argv[2]
# FILENAME = "foo.txt"
# output = "randCat.txt"

offset = 20

rand = random.randrange(10) + offset


with open(src_file_path,'r') as src:
    with open(tgt_output_path, 'w') as tgt:
        lines = src.read().replace('\n',' ')
        words = lines.split(' ')
        # new_lines = []
        i = 0
        while i < len(words):
            rand_seg = ' '.join(words[:rand])
            words = words[rand:]
            tgt.write(rand_seg+ '\n')
            # new_lines.append(rand_seg)
        tgt.close()
    src.close()
