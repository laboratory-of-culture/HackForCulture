import pandas as pd
from keyword_extractor import keyphrases_handler
from sentence_transformers import SentenceTransformer
from twitter_parser import *
from bert_semantic_search import semantic_search
embedder = SentenceTransformer('bert-base-nli-mean-tokens')


twitter_username = 'elonmusk'

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

N = 2
recommendations = semantic_search(user_keys, corpus, corpus_embeddings, embedder, N)
for res, dist in recommendations:
    row = df.loc[ df[df['keywords']==res].index[0] , : ]
    print("Seems like event {} fits you. Please visit {}".format(row['name'].strip(), row['link']))

# df['keywords'] = ' '.join([key[0] for key in keyphrases_handler(df['desc'], 5)]) 

