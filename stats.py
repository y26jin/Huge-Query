import os
import glob
import operator
import random

if __name__=="__main__":
    log_path = "./words.log"
    log_file_size = os.path.getsize(log_path)
    small_size = 1000000
    num_small_files = log_file_size / small_size + 1
    
    # hash each word to smaller file
    fp_log = open(log_path, 'r')
    for line in fp_log:
        index = random.randint(0, num_small_files)
        temp_path = "./small-pieces/words-"+str(index)+".log"
        temp_file = open(temp_path,'a+')
        temp_file.write(line)
        temp_file.close()
    
    # compute frequency of each small files
    small_freq = {}
    big_freq = {}
    for i in range(num_small_files):
        temp_path = "./small-pieces/words-"+str(i)+".log"
        temp_f = open(temp_path,'r')
        lines = temp_f.readlines()
        for l in lines:
            if l in small_freq:
                small_freq[l] = small_freq[l] + 1
            else:
                small_freq[l] = 1
        small_freq = sorted(small_freq.iteritems(), key=operator.itemgetter(1))
        max_val = small_freq[-1][1]
        temp_tuple = small_freq.pop()
        while temp_tuple[1] == max_val:
            if temp_tuple[0] in big_freq:
                big_freq[temp_tuple[0]] = big_freq[temp_tuple[0]] + 1
            else:
                big_freq[temp_tuple[0]] = temp_tuple[1]
            temp_tuple = small_freq.pop()
        small_freq = {}
    print sorted(big_freq.iteritems(), key=operator.itemgetter(1))
    
        
