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
