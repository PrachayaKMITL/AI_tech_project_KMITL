import re 
import nltk 
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize  

class nlpCleaner :
    def extract_csv(df,title_column):
        for i in len(df.axes(0)):
            text_column = np.array(df[title_column]) 

    def remove_stopword(df):
        stopwords = set(stopwords.words('english'))
        df['clean_title'] = df['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))






