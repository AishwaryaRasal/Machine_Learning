#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

d = os.listdir('fisher-scop-data-copy')
svmerr = 0
nberr = 0
nmerr = 0
n = 0
l = 2
for i in range(0, len(d), 1):
    if re.match('\d.\d', d[i]) != None:
        d2 = os.listdir('fisher-scop-data-copy/' + d[i])

        # ### get negative train and test ####

        for j in range(0, len(d2), 1):
            if d2[j].find('fold0.neg-train') != -1:
                negtrain = 'fisher-scop-data-copy/' + d[i] + '/' + d2[j]

                # negtrain='fisher/' + d[i] + '/' + d2[j]

                negtest = negtrain.replace('train', 'test')
                print ('negtrain: ', negtrain)
                print ('negtest: ', negtest)

        # ### descend into subdirectories ####

        for j in range(0, len(d2), 1):
            if d2[j].find('fold') == -1:
                d3 = os.listdir('fisher-scop-data-copy/' + d[i] + '/'
                                + d2[j])

                # d3=os.listdir('fisher/' + d[i] + '/' + d2[j])

                for k in range(0, len(d3), 1):
                    if d3[k].find('pos-train') != -1:
                        n += 1
                        print ('n: ', n)
                        postrain = 'fisher-scop-data-copy/' + d[i] \
                            + '/' + d2[j] + '/' + d3[k]

                        # postrain = 'fisher/' + d[i] + '/' + d2[j] + '/' + d3[k]

                        postest = postrain.replace('train', 'test')
                        print ('postrain: ', postrain)
                        print ('postest: ', postest)

                        os.system('python3 formatdata.py' + ' '
                                  + postrain + ' ' + negtrain + ' '
                                  + postest + ' ' + negtest)
                        os.system('python3 pce.py data trainlabels 10 > feature'
                                  )
                        os.system('python3 svm.py feature trainlabels 0.1 > prediction_svm'
                                  )
                        os.system('python3 error.py labels prediction_svm > error1'
                                  )
                        f = open('error1')
                        e1 = float(f.readline())
                        f.close()
                        print (d2[j] + ': ' + 'SVM error = ', e1)
                        svmerr += e1
                        sys.stdout.flush()
                        os.system('python3 nb_scilearn.py feature trainlabels > prediction_nb'
                                  )
                        os.system('python3 error.py labels prediction_nb > error2'
                                  )
                        f = open('error2')
                        e2 = float(f.readline())
                        f.close()
                        print (d2[j] + ': ' + 'naive_bayes error = ',
                               e2)
                        nberr += e2
                        sys.stdout.flush()
                        os.system('python3 gradient_descent.py feature trainlabels > prediction_nm'
                                  )
                        os.system('python3 error.py labels prediction_nm > error3'
                                  )
                        f = open('error3')
                        e3 = float(f.readline())
                        f.close()
                        print (d2[j] + ': ' + 'Nearest mean error = ',
                               e3)
                        nmerr += e3
                        sys.stdout.flush()

svmerr /= n
print ('average SVM error: ', svmerr)
nberr /= n
print ('average Naive Bayes error: ', nberr)
nmerr /= n
print ('average Nearest Mean error: ', nmerr)

sys.stdout.flush()


			
