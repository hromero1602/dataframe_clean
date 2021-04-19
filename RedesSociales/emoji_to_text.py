import pandas as pd
import demoji

def emoji_to_text(text):
    demoji.findall(text)
    text = demoji.findall(text)
    temp_list = demoji_text.values()
    temp_list = demoji_text.values()
    no_emoji_df = pd.DataFrame(temp_list, columns = ['emoji_Text'])
    print(no_emoji_df)
    no_emoji_df.to_csv(r'C:\Users\heromero\Desktop\Stefanini\Desarollo_Redes_sociales\Nueva carpeta\IGphotoDownloader\emoji_to_text.csv')

text = (r"emoji.txt")