# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:22:51 2020

@author: Buzzi
"""

import pandas as pd
import numpy as np
from keras import preprocessing
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()

def clean_text(news):

    letters_only = re.sub("[^a-zA-Z]", " ", news)

    words = letters_only.lower().split()

    stops = set(stopwords.words("english"))

    meaningful_words = [w for w in words if not w in stops]  #returns a list

    singles = [stemmer.stem(word) for word in meaningful_words]

    return( " ".join( singles ))

max_nb_words = 115720
tokenizer = preprocessing.text.Tokenizer(num_words=max_nb_words, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
