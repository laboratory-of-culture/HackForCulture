import pandas as pd
from keyword_extractor import keyphrases_handler
from sentence_transformers import SentenceTransformer
from twitter_parser import *
from bert_semantic_search import semantic_search
import sys
embedder = SentenceTransformer('bert-base-nli-mean-tokens')


twitter_username = sys.argv[1]

# tweets analysis
all_tweets = scrap_tweets_text(twitter_username)
user_keys = keyphrases_handler(scrap_tweets_text(twitter_username), 7) + keyphrases_handler(scrap_bio(twitter_username), 3)
user_keys =  ' '.join([key[0] for key in user_keys])
print("User {} keywords: {}".format(twitter_username, user_keys))

# # events analysis per user
df = pd.read_csv("events_from_terminal.csv", delimiter = '^')
df['keywords'] = df.apply(lambda row: ' '.join([key[0] for key in keyphrases_handler(row.desc, 7)]), axis = 1) 


corpus = df['keywords'].tolist()
corpus_embeddings = embedder.encode(corpus)

N = 1
recommendations = semantic_search(user_keys, corpus, corpus_embeddings, embedder, N)
for res, dist in recommendations:
    row = df.loc[ df[df['keywords']==res].index[0] , : ]
    print("Seems like event {} fits this twitter account. Please visit {}".format(row['name'].strip(), row['link']))



