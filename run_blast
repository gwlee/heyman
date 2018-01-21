# -*- coding: utf-8 -*-

import os,re,glob
import multiprocessing

THREAD_NUM = 8

current_path = os.path.dirname(os.path.realpath(__file__))

def blast(q,d,o):
        os.system('blastp -query %s -db %s -max_target_seqs 1 -outfmt "6 std qlen slen score" -num_threads 4 -out %s'%(q,d,o))

db_list = glob.glob('*faa')

combination_list = list()
for q in query_list:
        for d in db_list:
                if os.path.isfile('Q.%s_D.%s.blastp'%(q.strip().split('.')[0],d.strip().split('.')[0])):
                        pass
                else:
                        combination_list.append((q.strip(),d.strip(),'Q.%s_D.%s.blastp'%(q.strip().split('.')[0],d.strip().split('.')[0])))

combination_list.sort()

for c in [combination_list[i:i+THREAD_NUM] for i in range(0,len(combination_list), THREAD_NUM)]:
        proc_list = list()
        for item in c:
                p = multiprocessing.Process(target=blast, args=(item[0],item[1],item[2]))
                p.daemon = True
                proc_list.append(p)

        for p in proc_list:
                p.start()

        for p in proc_list:
                p.join()
