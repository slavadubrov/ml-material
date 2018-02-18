import sys, os
import multiprocessing
from tqdm import tqdm

def mapper(line):

    map_dict = {}
    for word in line.strip().split():
        if word in map_dict:
            map_dict[word] += 1
        else:
            map_dict[word] = 1
    return map_dict

def reducer():
    cpus = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpus)

    reduce_dict = {}

    with open('document.txt') as source_file, open('output2.txt', 'w') as output_file:
        for map_dict in tqdm(p.imap_unordered(mapper, source_file)):
            for word in map_dict:
                if word in reduce_dict:
                    reduce_dict[word] = reduce_dict[word] + map_dict[word]
                else:
                    reduce_dict[word] = map_dict[word]

        for word in reduce_dict:
            output_file.write('{}\t{}\n'.format(word, reduce_dict[word]))

reducer()
