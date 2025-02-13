# Twitter Reverse API

Twitter Reverse API allows you to interact with Twitter's data by using your own Twitter account's cookie. This API provides endpoints to fetch various types of data from Twitter, such as user profiles, tweets, and more. By leveraging your Twitter cookie, the API ensures that you can access data that is typically restricted or limited by Twitter's public API.

## Sponsors

<div align="center">
  <a href="https://rapidapi.com/Lundehund/api/twitter-x-api" target="_blank">
    <img src="./public/images/twittapi.png" width="100" alt="twittapi">
    <div>
      <b>twittapi</b> is the fastest and most stable Twitter API available. Provides seamless integration and reliable performance for all your Twitter data needs. And don't need to use your cookie or worry about proxy.
    </div>
  </a>
</div>

## Installation

1. Clone the repository:

```bash
git clone https://github.com/twittapi-labs/twitter-reverse-api
cd twitter-reverse-api
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

To use the Twitter class, you need to add your Twitter cookie to the `test.py` file. Note that the cookie must contain `csrf_token` (ct0). Open `test.py` and add your cookie:

```python
from Twitter import Twitter

COOKIE = '<YOUR_COOKIE>'

if __name__ == '__main__':
  twitter = Twitter(COOKIE)

  user = twitter.get_user_detail('elonmusk')
  print(user)
```

Response

```json
{
  "data": {
    "user": {
      "result": {
        "__typename": "User",
        "id": "VXNlcjo0NDE5NjM5Nw==",
        "rest_id": "44196397",
        "affiliates_highlighted_label": {
          "label": {
            "url": {
              "url": "https://twitter.com/X",
              "urlType": "DeepLink"
            },
            "badge": {
              "url": "https://pbs.twimg.com/profile_images/1683899100922511378/5lY42eHs_bigger.jpg"
            },
            "description": "X",
            "userLabelType": "BusinessLabel",
            "userLabelDisplayType": "Badge"
          }
        },
        "has_graduated_access": true,
        "is_blue_verified": true,
        "profile_image_shape": "Circle",
        "legacy": {
          "can_dm": false,
          "can_media_tag": false,
          "created_at": "Tue Jun 02 20:12:29 +0000 2009",
          "default_profile": false,
          "default_profile_image": false,
          "description": "",
          "entities": {
            "description": {
              "urls": []
            }
          },
          "fast_followers_count": 0,
          "favourites_count": 122843,
          "followers_count": 217468317,
          "friends_count": 1021,
          "has_custom_timelines": true,
          "is_translator": false,
          "listed_count": 159782,
          "location": "",
          "media_count": 3344,
          "name": "Elon Musk",
          "normal_followers_count": 217468317,
          "pinned_tweet_ids_str": [
            "1889733204191379930"
          ],
          "possibly_sensitive": false,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/44196397/1726163678",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1874558173962481664/8HSTqIlD_normal.jpg",
          "profile_interstitial_type": "",
          "screen_name": "elonmusk",
          "statuses_count": 70283,
          "translator_type": "none",
          "verified": false,
          "want_retweets": false,
          "withheld_in_countries": []
        },
        "professional": {
          "rest_id": "1679729435447275522",
          "professional_type": "Creator",
          "category": []
        },
        "tipjar_settings": {
          "is_enabled": false
        },
        "super_follow_eligible": true,
        "smart_blocked_by": false,
        "smart_blocking": false,
        "legacy_extended_profile": {},
        "is_profile_translatable": false,
        "has_hidden_likes_on_profile": true,
        "has_hidden_subscriptions_on_profile": true,
        "verification_info": {
          "is_identity_verified": false,
          "reason": {
            "description": {
              "text": "This account is verified because it's an affiliate of @X on X. Learn more",
              "entities": [
                {
                  "from_index": 54,
                  "to_index": 56,
                  "ref": {
                    "url": "https: //twitter.com/X",
                    "url_type": "ExternalUrl"
                  }
                },
                {
                  "from_index": 63,
                  "to_index": 73,
                  "ref": {
                    "url": "https://help.twitter.com/en/rules-and-policies/profile-labels",
                    "url_type": "ExternalUrl"
                  }
                }
              ]
            },
            "verified_since_msec": "-156836000000000",
            "override_verified_year": -3000
          }
        },
        "highlights_info": {
          "can_highlight_tweets": true,
          "highlighted_tweets": "553"
        },
        "user_seed_tweet_count": 0,
        "business_account": {},
        "creator_subscriptions_count": 203
      }
    }
  }
}
```

## Contributing
Contributions are welcome! If you find this project helpful, please consider starring the repository on [GitHub](https://github.com/twittapi-labs/twitter-reverse-api) ⭐️
