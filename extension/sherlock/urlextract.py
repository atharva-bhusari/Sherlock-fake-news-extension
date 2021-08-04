import sys
from newspaper import Article
import datetime
import csv
import pandas as pd
import numpy as np
from .fake_news import choice,pred

def prediction(news_url):
    article = Article(news_url)
    article.download()
    article.parse()
    article.nlp()


    title=article.title
    title1 = [title]
    text=article.text
    author=article.authors
    dt=article.publish_date
    x = datetime.datetime.now()
    date=x.strftime("%x")

    columns = ['Title', 'Text', 'Author', 'Date']
    metadata = {'Title':[title], 'Text':[text], 'Author':[author], 'Date':[date]}
    df = pd.DataFrame(metadata, columns=columns)
    result = pred(df['Text'])[0]
    message = choice(result)

    dict = [{'Title':title, 'Text': text, 'Author': author, 'Date': date, 'Result': result}]

    csv_file = 'news articles.csv'
    try:
        with open(csv_file, 'a', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=dict[0].keys(),)
            for data in dict:
                writer.writerow(data)
    finally:
        csvfile.close()
    print(result)
    return message
