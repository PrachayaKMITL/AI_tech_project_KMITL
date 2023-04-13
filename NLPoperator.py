import re 
import nltk as nlp
import pandas as pd
import numpy as np

class nlpCleaner :
    def extract_csv(df,title_column):
        for i in len(df.rows):
            text_column = np.array(df[title_column]) 



