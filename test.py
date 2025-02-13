from Twitter import Twitter

COOKIE = '<YOUR_COOKIE>'

if __name__ == '__main__':
  twitter = Twitter(COOKIE)

  user = twitter.get_user_detail('elonmusk')
  print(user)
