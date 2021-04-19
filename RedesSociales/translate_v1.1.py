import pandas as pd
from textblob import TextBlob
from pandas import DataFrame
import re


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\2705"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


def translate_content(df):
    df['comments'] = df['comments'].apply(lambda x: deEmojify(x) )
    df['translate_comments']=df['comments'].apply(lambda x:TextBlob(x).translate(to='en'))
    df['translate_comments'] = df['translate_comments'].apply(str)
    columnas = ['translate_comments']
    df[columnas] = df[columnas].replace({',':''}, regex=True)
    df.to_csv(r'C:\Users\heromero\Desktop\Stefanini\Desarollo_Redes_sociales\Nueva carpeta\IGphotoDownloader\translate.csv')

df = pd.read_csv('df_spanish.csv')
translate_content(df)






