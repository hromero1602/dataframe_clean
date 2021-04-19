import time

import beaker.middleware
from bottle import route, redirect, post, run, request, hook
from instagram import client, subscriptions
import requests
import json
import pandas as pd
import click
def get_information_instagram_json(tag):
    
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept-Encoding': 'identity, deflate, compress, gzip',
        'Accept': '*/*'
    }
    
    response = ""
    
    try:
        url = "https://www.instagram.com/explore/tags/"+str(tag)+"/?__a=1"
        r = requests.get(url,headers=headers)
        print("*****URL****")
        print(url)
        print(r.headers)
        content = str(r.content)
        response = json.loads(r.content)
    except Exception as e:
        print("Request has failed!")
    return response

def save_on_file(namefile,information):
    filename=str(namefile)
    with open(filename, 'w') as json_file:
        json.dump(information, json_file)

def process_instagram_info(namefile):
    
    print(namefile)
    filename=str(namefile)
    with open(filename, 'r') as myfile:
        file=myfile.read()
    array_likes=[]
    array_comments=[]
    hashtg = json.loads(file)
    count = hashtg['graphql']['hashtag']['edge_hashtag_to_media']
    
    for edge in count['edges']:
        media_to_cap = edge['node']['edge_media_to_caption']
        aux = 0
        likes = edge['node']['edge_liked_by']
        for like in likes:
            array_likes.append(likes[like])
        for media in media_to_cap:
            node = media_to_cap['edges'][aux]
            aux_text = 0
            aux_comments=""
            for text in node:
                aux_comments+=str(node[text]['text'])
                aux_text=+1
            aux=+1
            array_comments.append(aux_comments)
        
        data = {
            'likes': array_likes,
            'comments': array_comments
        }

        analitica = pd.DataFrame(data)
        analitica.to_csv(r"C:\Users\heromero\Desktop\RedesSociales\ig_post.csv")




@click.command()
@click.option("--tag", prompt="Enter Instagram tag to explore:", help="No special characters allowed")

def main(tag):
    
    print("This is ")
    print("░░░░░░░░░░▄▄█▀▀▄░░░░░░░░░░░░░")
    print("░░░░░░░░▄█████▄▄█▄░░░░░░░░░░░")
    print("░░░░░▄▄▄▀██████▄▄██░░░░░░░░░░")
    print("░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄░░░")
    print("▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄")
    print("█████░█░░▀█░▀▀▀▀▄▀░░░███████▀")
    print("░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀░░░")
    print("░▄████████▀▀▀▄▀░░░░░░░░░░░░░░")
    print("██████░▀▀█▄░░░█▄░░░░░░░░░░░░░")
    print("░▀▀▀▀█▄▄▀░██████▄░░░░░░░░░░░░")
    print("░░░░░░░░░█████████░░░░░░░░░░░")
    
    path_file = (r'C:\Users\heromero\Desktop\RedesSociales\Ig.json')

    while True:
        
        
        
        print("Recuperando tags por: ", tag)
        req = get_information_instagram_json(tag)
        save_on_file(path_file, req)
        
        if req != "":
            process_instagram_info(path_file)
        else:
            print("Sorry!")
        
        time.sleep(50)

if __name__ == '__main__':
    main()