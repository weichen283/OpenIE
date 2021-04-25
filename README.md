# OpenIE

This project will extract predicate-argument structures from biomedical text and generate RDF triples that can be incorporated into the Bio2RDF dataset. Following this, we will focus on drug-virus interaction verbs that are found in the COVID-19 Open Research Dataset.

## Installation

`Stanza` installation:

Go to https://stanfordnlp.github.io/CoreNLP/history.html

Click on 3.9.1 under Version to download the appropriate zip file

unzip stanford-corenlp-full-2018-02-27.zip

Add the following to your bash_profile (assuming you are on unix and bash shell):

    $ export CORENLP_HOME=full_path_of_unzipped_stanford-corenlp-full-2018-02-27
    $ pip3 install stanza

----

The most straight forward way to install `PredPatt` is via pip:

    $ pip3 install git+https://github.com/hltcoe/PredPatt.git

## Usage

Tokenization, deprel analysis.

    $ python gen-conllu.py name_of_datafile

online version: https://corenlp.run/

----

`Predpatt` cmd:

    python3 -m predpatt file.conllu --resolve-relcl --resolve-conj --resolve-appos > outname

## Example

> conllu file:

    1	Active	active	ADJ	JJ	_	3	amod	_	start_char=0|end_char=6
    2	brain	brain	NOUN	NN	_	3	compound	_	start_char=7|end_char=12
    3	stimulation	stimulation	NOUN	NN	_	9	nsubj	_	start_char=13|end_char=24
    4	to	to	PART	TO	_	5	mark	_	start_char=25|end_char=27
    5	abate	abate	VERB	VB	_	3	acl	_	start_char=28|end_char=33
    6	epileptic	epileptic	ADJ	JJ	_	7	amod	_	start_char=34|end_char=43
    7	seizures	seizure	NOUN	NNS	_	5	obj	_	start_char=44|end_char=52
    8	has	have	AUX	VBZ	_	9	aux	_	start_char=53|end_char=56
    9	shown	show	VERB	VBN	_	0	root	_	start_char=57|end_char=62
    10	mixed	mixed	ADJ	JJ	_	11	amod	_	start_char=63|end_char=68
    11	success	success	NOUN	NN	_	9	obj	_	start_char=69|end_char=76
    12	.	.	PUNCT	.	_	9	punct	_	start_char=77|end_char=78

----

> Predpatt output:

sentence: Active brain stimulation to abate epileptic seizures has shown mixed success .

ppatt:

    ?a abate ?b
        ?a: Active brain stimulation
        ?b: epileptic seizures
    ?a has shown ?b
        ?a: Active brain stimulation to abate epileptic seizures
        ?b: mixed success
