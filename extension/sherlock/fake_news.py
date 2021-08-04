# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:49:35 2020

@author: Buzzi
"""
from .clean import tokenizer,clean_text
from keras import preprocessing
import pandas as pd
import numpy as np
from keras.models import load_model

def pred(text):
    mod = load_model('semantic.h5')
    B = text
    B = B.apply(clean_text)
    tokenizer.fit_on_texts(B.values)
    B = preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences(B), maxlen=300)
    ret = (mod.predict_classes(B[0:]))
    return ret

def choice(res):
    switcher = {
        0: "ALERT!!!! Sherlock says this news article is entirely fake!!!!",
        1: "Sherlock says some statements in the article are deceptive!!!",
        2: "Sherlock says that this news is almost FAKE!!! We recommend you to check the facts of the news.",
        3: "Sherlock has detected that the news is TRUE. HAPPY READING!!!!!"
    }

    return switcher.get(res,"Error!!!!")
