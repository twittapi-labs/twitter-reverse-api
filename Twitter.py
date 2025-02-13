import json
import requests

class Twitter:
  def __init__(self, cookie: str):
    self.cookie = cookie
    self.twitter_base_api_url = 'https://x.com/i/api/graphql'
    self.authorization = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    self.csrf_token = self._extract_csrf_token_from_cookie(cookie)
    self.headers = {
      'Cookie': self.cookie,
      'x-csrf-token': self.csrf_token,
      'Authorization': self.authorization,
      'x-twitter-client-language': 'en',
      'x-twitter-auth-type': 'OAuth2Session',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    self.param_features = {
      'common': {
        'rweb_tipjar_consumption_enabled': True,
        'responsive_web_graphql_exclude_directive_enabled': True,
        'verified_phone_label_enabled': False,
        'creator_subscriptions_tweet_preview_api_enabled': True,
        'responsive_web_graphql_timeline_navigation_enabled': True,
        'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
        'communities_web_enable_tweet_community_results_fetch': True,
        'c9s_tweet_anatomy_moderator_badge_enabled': True,
        'articles_preview_enabled': True,
        'tweetypie_unmention_optimization_enabled': True,
        'responsive_web_edit_tweet_api_enabled': True,
        'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
        'view_counts_everywhere_api_enabled': True,
        'longform_notetweets_consumption_enabled': True,
        'responsive_web_twitter_article_tweet_consumption_enabled': True,
        'tweet_awards_web_tipping_enabled': False,
        'creator_subscriptions_quote_tweet_preview_enabled': False,
        'freedom_of_speech_not_reach_fetch_enabled': True,
        'standardized_nudges_misinfo': True,
        'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
        'rweb_video_timestamps_enabled': True,
        'longform_notetweets_rich_text_read_enabled': False,
        'longform_notetweets_inline_media_enabled': False,
        'responsive_web_enhance_cards_enabled': False
      },
      'user_detail': {
        'hidden_profile_likes_enabled': True,
        'hidden_profile_subscriptions_enabled': True,
        'rweb_tipjar_consumption_enabled': True,
        'responsive_web_graphql_exclude_directive_enabled': True,
        'verified_phone_label_enabled': False,
        'subscriptions_verification_info_is_identity_verified_enabled': True,
        'subscriptions_verification_info_verified_since_enabled': True,
        'highlights_tweets_tab_ui_enabled': True,
        'responsive_web_twitter_article_notes_tab_enabled': True,
        'creator_subscriptions_tweet_preview_api_enabled': True,
        'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
        'responsive_web_graphql_timeline_navigation_enabled': True
      }
    }

  def _extract_csrf_token_from_cookie(self, cookie: str) -> str:
    cookies = cookie.split('; ')
    csrf_token = ''

    for c in cookies:
      if c.startswith('ct0'):
        csrf_token = c.split('=')[1]
        break

    return csrf_token
  
  def _flatten_params(self, params: dict) -> dict:
    flattened_params = {}

    for key, value in params.items():
      if isinstance(value, (list, dict)):
        flattened_params[key] = json.dumps(value)
      else:
        flattened_params[key] = str(value)

    return flattened_params
  
  def _make_request(self, url: str, params: dict) -> dict:
    flattened_params = self._flatten_params(params)
    response = requests.get(url, headers=self.headers, params=flattened_params)

    return response.json()

  # User Endpoints
  def get_user_detail(self, username: str):
    url = f'{self.twitter_base_api_url}/qW5u-DAuXpMEG0zA1F7UGQ/UserByScreenName'
    params = {
      'variables': {
        'screen_name': username,
        'withSafetyModeUserFields': True
      },
      'features': self.param_features['user_detail'],
      'fieldToggles': {
        'withAuxiliaryUserLables': False
      }
    }

    return self._make_request(url, params)

  def get_user_following(self, user_id: str, count: int = 20, cursor: str = None):
    url = f'{self.twitter_base_api_url}/7FEKOPNAvxWASt6v9gfCXw/Following'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_user_followers(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/DMcBoZkXf9axSfV2XND0Ig/Followers'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_blue_verified_followers(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/BBHG1SUP_oNxDWJ40Y4ZRQ/BlueVerifiedFollowers'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_user_subscriptions(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/VVNxHD4NVaSTU9Jtnb_n8Q/UserCreatorSubscriptions'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_user_tweets(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': True,
        'withQuickPromoteEligibilityTweetFields': True,
        'withVoice': True,
        'withV2Timeline': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common'],
      'fieldToggles': {
        'withArticlePlainText': False
      }
    }

    return self._make_request(url, params)

  def get_user_replies(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/E4wA5vo2sjVyvpliUffSCw/UserTweetsAndReplies'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': True,
        'withCommunity': True,
        'withVoice': True,
        'withV2Timeline': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common'],
      'fieldToggles': {
        'withArticlePlainText': False
      }
    }

    return self._make_request(url, params)

  def get_user_medias(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/MOLbHrtk8Ovu7DUNOLcXiA/UserMedia'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        'withClientEventToken': False,
        'withBirdwatchNotes': False,
        'withVoice': True,
        'withV2Timeline': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common'],
      'fieldToggles': {
        'withArticlePlainText': False
      }
    }

    return self._make_request(url, params)

  def get_user_highlights(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/3meQSPRxtj9adgM59i_XOg/UserHighlightsTweets'
    params = {
      'variables': {
        'userId': user_id,
        'count': count,
        'includePromotedContent': False,
        'withVoice': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common'],
      'fieldToggles': {
        'withArticlePlainText': False
      }
    }

    return self._make_request(url, params)

  # List Endpoints
  def get_list_tweets(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/F9aW7tjdTWE9m5qHqzEpUA/ListLatestTweetsTimeline'
    params = {
      'variables': {
        'listId': list_id,
        'count': count,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_list_members(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/3dQPyRyAj6Lslp4e0ClXzg/ListMembers'
    params = {
      'variables': {
        'listId': list_id,
        'count': count,
        'withSafetyModeUserFields': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_list_followers(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/fHOf5iOSMpDxnNLl1hppYg/ListSubscribers'
    params = {
      'variables': {
        'listId': list_id,
        'count': count,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  # Search Endpoints
  def search(
    self, keyword: str,
    search_type: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/TQmyZ_haUqANuyBcFBLkUw/SearchTimeline'
    params = {
      'variables': {
        'rawQuery': keyword,
        'count': count,
        'querySource': 'recent_search_click',
        'product': search_type,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  # Tweet Endpoints
  def get_tweet_detail(self, tweet_id: str):
    url = f'{self.twitter_base_api_url}/VwKJcAd7zqlBOitPLUrB8A/TweetDetail'
    params = {
      'variables': {
        'focalTweetId': tweet_id,
        'referrer': 'profile',
        'controller_data': 'DAACDAABDAABCgABAAAAAAAAAAAKAAkTUc6UAFWQAQAAAAA=',
        'with_rux_injections': False,
        'includePromotedContent': True,
        'withCommunity': True,
        'withQuickPromoteEligibilityTweetFields': True,
        'withBirdwatchNotes': True,
        'withVoice': True,
        'withV2Timeline': True
      },
      'features': self.param_features['common'],
      'fieldToggles': {
        'withArticleRichContentState': True,
        'withArticlePlainText': False,
        'withGrokAnalyze': False
      }
    }

    return self._make_request(url, params)

  def get_tweet_quotes(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/TQmyZ_haUqANuyBcFBLkUw/SearchTimeline'
    params = {
      'variables': {
        'rawQuery': f'quoted_tweet_id:{tweet_id}',
        'count': count,
        'querySource': 'tdqt',
        'product': 'Top',
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_tweet_retweeters(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/lR6N-4vjw47alP1RHfhxkg/Retweeters'
    params = {
      'variables': {
        'tweetId': tweet_id,
        'count': count,
        'includePromotedContent': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_tweet_likes(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/arbFn-zD2IR_uDsOydGdgg/Favoriters'
    params = {
      'variables': {
        'tweetId': tweet_id,
        'count': count,
        'includePromotedContent': True,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)

  def get_tweet_hidden_replies(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None
  ):
    url = f'{self.twitter_base_api_url}/JhfEJx42t-k-sGP-qGLWXw/ModeratedTimeline'
    params = {
      'variables': {
        'rootTweetId': tweet_id,
        'count': count,
        'includePromotedContent': False,
        **({'cursor': cursor} if cursor else {})
      },
      'features': self.param_features['common']
    }

    return self._make_request(url, params)
