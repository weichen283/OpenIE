import sys
import stanza
from stanza.utils.conll import CoNLL

### Package for biomedical text
#stanza.download('en', package='craft')
stanza.download('en', package='genia')

### Tokenize pipeline for biomedical text
#tok = stanza.Pipeline('en', package='craft', processors='tokenize')
tok = stanza.Pipeline('en', package='genia', processors='tokenize')

### Pipeline for biomedical text
### DON'T NEED TO DO THE NEXT ITEMS BECAUSE WE ARE TOKENIZING WITH genia
### Will modify the pre-tokenized text to:
###      - remove spaces around hypens
###      - modify biochem names (with "(" and "/") TODO!!
### then use the next pipeline
#nlp = stanza.Pipeline('en', package='craft', processors='tokenize,pos,lemma,depparse', tokenize_pretokenized=True)
# nlp = stanza.Pipeline('en', package='genia', processors='tokenize,pos,lemma,depparse', tokenize_pretokenized=True)
nlp = stanza.Pipeline('en', package='genia', processors={'tokenize':'genia','pos':'genia','lemma':'genia','depparse':'genia','ner':'ontonotes'}, tokenize_pretokenized=True)

### Input file name on command line
file = str(sys.argv[1])

with open(file, "r") as f1:
		data = f1.read()

### Tokenize the data using Tokenize pipeline
tokdoc = (tok(data))

### Generate new pre-tokenized data, one sentence per line
tokenizeddoc = ''
for sent in tokdoc.sentences:
    for token in sent.tokens:
        tokenizeddoc = tokenizeddoc + token.text + ' '
    tokenizeddoc = tokenizeddoc + '\n'
# print (tokenizeddoc)

### Modify the tokenized data (hyphens, biochem names, ...)
tokenized_doc = tokenizeddoc.replace(" - ", "-")
### Produce conll using stanza pipeline following Stanza website
doc = (nlp(tokenized_doc))

dicts = doc.to_dict()

#------------- change here ----------------------
conll = CoNLL.convert_dict(dicts)


### Output conll in conllu format used by PredPatt
### Output file must have .conllu extension 



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




### Run is successful - provide name of output file in terminal output
print("\n" + "Output written on " + file + "\n")
