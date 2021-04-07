from api_key import line_key
import requests
import tweepy
import json

# ファイルの読み込み
with open('api_key/twitter.json') as f:
    twitter_keys = json.load(f)

# ライン通知  
def notify_message(message):
    LINE_NOTIFY_TOKEN = line_key.LINE_API_KEY
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }
    
    data = {
        'message': message
    }
    
    requests.post(
        url,
        headers=headers,
        data=data
    )
    
# フォロワー数取得
def get_n_followers():
    consumer_key = twitter_keys['consumer_key']
    consumer_secret = twitter_keys['consumer_secret']
    access_token = twitter_keys['access_token']
    access_token_secret = twitter_keys['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    me = api.me()
    n_followers = me.followers_count
    
    return n_followers


def main():
    n_followers = get_n_followers()
    message = f'本日のフォロワー数は{n_followers}です。'
    notify_message(message)

if __name__ == "__main__":
    main()