import tweepy as tw
import pandas as pd
import get_token


def extractTweet():

    body = ['consumer_key','consumer_secret','access_token']
    secret = get_token.print_env(body)
    consumer_secret = secret['consumer_secret']
    consumer_key = secret['consumer_key']

    auth = tw.AppAuthHandler(consumer_key, consumer_secret)
    query_search= "Bolsonaro"  + " -filter:retweets" 
    api = tw.API(auth)
    cursor_tweets = tw.Cursor(api.search,
                          since="2021-07-01",
                          # until="2021-07-25",
            q=query_search).items(200)

    tweets_dict = {}
    tweets_dict = tweets_dict.fromkeys(['created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted'])
    

    for tweet in cursor_tweets:
        for key in tweets_dict.keys():
            try:
                twvalue = tweet._json[key]
                tweets_dict[key].append(twvalue)
            except KeyError:
                twvalue = ""
                if(tweets_dict[key] is None):
                    tweets_dict[key] = [twvalue]
                else:
                    tweets_dict[key].append(twvalue)
            except:
                tweets_dict[key] = [twvalue]
    
    dfTweets = pd.DataFrame.from_dict(tweets_dict)
    print(dfTweets.head())
    print(f'Quantidade de posts retornados: {dfTweets.shape[0]}')

extractTweet()