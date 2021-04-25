import os
import sys


path = str(sys.argv[1])
files = os.listdir(path)
for file in files:

    if os.path.splitext(file)[1] == '.conllu':
          
        print('python3.7 -m predpatt {} --resolve-relcl --resolve-conj --resolve-appos > {}'.format(path + '/' + file,os.path.splitext(file)[0]))
        os.system('python3.7 -m predpatt {} --resolve-relcl --resolve-conj --resolve-appos > {}'.format(path + '/' + file,os.path.splitext(file)[0]))

