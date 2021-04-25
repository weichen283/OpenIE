import os
import sys

try:
    path = str(sys.argv[1])
    files = os.listdir(path)
    for file in files:
        f = open(path + '/' + file, 'r')
        fh = open(os.path.splitext(file)[0], 'w')
        line = f.readline()
        while line != "":
            temp = line.split('\t')
            if temp[0] != '\n':
                fh.write(temp[1]+'\n')
            line = f.readline()
        f.close()
        fh.close()
except:
    print(file)

