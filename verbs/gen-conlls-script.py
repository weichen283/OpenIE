import sys
import os
import stanza
from stanza.utils.conll import CoNLL


stanza.download('en', package='genia')

tok = stanza.Pipeline('en', package='genia', processors='tokenize')

nlp = stanza.Pipeline('en', package='genia', processors='tokenize,pos,lemma,depparse', tokenize_pretokenized=True)


path = str(sys.argv[1])
files = os.listdir(path)

for file in files:

        with open(path + '/' + file, "r") as f1:
                data = f1.read()


        tokdoc = (tok(data))

        tokenizeddoc = ''
        for sent in tokdoc.sentences:
                for token in sent.tokens:
                        tokenizeddoc = tokenizeddoc + token.text + ' '
                tokenizeddoc = tokenizeddoc + '\n'



        tokenized_doc = tokenizeddoc.replace(" - ", "-")


        doc = (nlp(tokenized_doc))
        dicts = doc.to_dict()


        conll = CoNLL.convert_dict(dicts)


        file = file + ".conllu"

        f = open(file, "w")
        for x in conll:
                for y in x:
                        yy = y[:-1]
                        for q in yy:
                                f.write(q + "\t")
                        f.write(y[-1] + "\n")
                f.write("\n")
        f.close()

        print("\n" + "Output written on " + file + "\n")
