import os
import re
import sys

d=os.listdir('fisher-scop-data-copy')
nmerr=0
nberr=0
n=0

for i in range(0, len(d), 1):
    if(re.match('\d.\d', d[i]) != None):
        d2=os.listdir('fisher-scop-data-copy/' + d[i])
              
        #### get negative train and test ####
        for j in range(0, len(d2), 1):
            if(d2[j].find('fold0.neg-train') != -1):
                negtrain='fisher-scop-data-copy/' + d[i] + '/' + d2[j]
                #negtrain='fisher/' + d[i] + '/' + d2[j]
                negtest = negtrain.replace('train', 'test')
                print("negtrain: ", negtrain)
                print("negtest: ", negtest)
       
                
        #### descend into subdirectories ####
        for j in range(0, len(d2), 1):
            if(d2[j].find('fold') == -1):
                d3=os.listdir('fisher-scop-data-copy/' + d[i] + '/' + d2[j])
                #d3=os.listdir('fisher/' + d[i] + '/' + d2[j])
                       
                for k in range(0, len(d3), 1):
                    if(d3[k].find('pos-train') != -1):
                        n+=1
                        print("n: ", n)
                        postrain = 'fisher-scop-data-copy/' + d[i] + '/' + d2[j] + '/' + d3[k]
                        #postrain = 'fisher/' + d[i] + '/' + d2[j] + '/' + d3[k]
                        postest = postrain.replace('train', 'test')
                        print("postrain: ", postrain)
                        print("postest: ", postest)
       
                        os.system('python3 formatdata.py' + ' ' + postrain + ' ' + negtrain + ' ' + postest + ' ' + negtest)
                        os.system('python3 gradient_descent.py data trainlabels > prediction')
                        os.system('python3 error.py labels prediction > errorout')
                        f = open('errorout')
                        err = float(f.readline())
                        print(d2[j] + ': ' + "nearest mean error = ", err)
                        nmerr += err
                        print("nearest mean error: ", nmerr)
                        os.system('python naive_bayes.py data trainlabels > prediction1')
                        os.system('python3 error.py labels prediction1 > errorout1')
                        f = open('errorout1')
                        err1 = float(f.readline())
                        print(d2[j] + ': ' + "naive bayes error = ", err1)
                        nberr += err1
                        print("naive bayes error: ", nberr)
                        sys.stdout.flush()

nmerr/=n
nberr/=n
print("average nearest mean error: ", nmerr)
print("average naive bayes error: ", nberr)
sys.stdout.flush()
