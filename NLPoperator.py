import re 
import nltk 
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize  
from nltk.stem.porter import PorterStemmer

class nlpCleaner :
    def extract_csv(df,title_column):
        for i in len(df.axes(0)):
            text_column = np.array(df[title_column]) 

    def remove_stopword(df):
        stopwords = set(stopwords.words('english'))
        df['clean_title'] = df['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))

    def stemming(content):
        stemmer = PorterStemmer()
        con = re.sub('[^a-zA-Z]',' ',content) #Add stemming to the datapoints in the dataset
        con = con.lower()
        con = con.split()
        [stemmer.stem(word) for word in con if not word in stopwords.words('english')]
        con = ''.join(con)
        return con

