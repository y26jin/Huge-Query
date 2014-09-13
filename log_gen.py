import os
import random
import glob

if __name__=="__main__":
    word_path = "/usr/share/dict/words"
    word_set = open(word_path,'r').readlines()
    
    log_path = "./words.log"
    fp_log = open(log_path,'a+')
    for i in range(12800000):
        temp_word = word_set[random.randint(0,len(word_set)-1)]+'\n'
        fp_log.write(temp_word)
    fp_log.close()
