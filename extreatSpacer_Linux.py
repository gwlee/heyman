#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'gwlee'

import os,sys

try:
        inputFile = sys.argv[1]

except:
        print 'extreatSpacer_Linux.py <infile> > <output>'
        exit(1)

s = 0
tmpData = list()
for lines in open(inputFile):
        if lines.startswith('Sequence '):
                name = lines.strip().split()[1]
                name = name.replace("'",'')
                tmpData = list()
                #print name
                s = 1

        elif lines.startswith('Time to find repeats'):
                if len(tmpData) == 0:
                        pass
                else:
                        for rec in tmpData:
                                print '>%s|%s\n%s\n\n'%(rec[0].replace(':','|'),rec[1],rec[2])

                s = 0

        elif s == 1:
                if lines.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                        item = lines.strip().split('\t')
                        if len(item) < 4:
                                pass
                        else:
                                tmpData.append((name,item[0],item[3]))

        elif s == 0:
                pass
