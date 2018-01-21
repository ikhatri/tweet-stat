from analyze import *

# Testing:
# x = [[1, 2], [5, 9], [4, 6]]
# y = [1, 3, 2, 6, 7]
# print(flatten(x))
# print(difference(flatten(x), y))

 tweet1 = {"username": "@realDonaldTrump", "source": "Twitter for Android",
            "content": "@azizansari This is a tweet! #TWEET #Twitter", "favorites": 32, "retweets": 5}
 tweet2 = {"username": "@realDonaldTrump", "source": "Twitter for iPhone", "content": "@mike_pence @kanye This is, too.",
           "favorites": 8, "retweets": 15}
 tweet3 = {"username": "@realDonaldTrump", "source": "Twitter for Android", "content": "", "favorites": 16,
           "retweets": 4}
 tweet4 = {"username": "@realDonaldTrump", "source": "Twitter for iPhone", "content": "MORE TWEETS! #TWEET",
           "favorites": 19, "retweets": 2}
 tweet5 = {"username": "@realDonaldTrump", "source": "Twitter for iPhone",
           "content": "@kanye I'm voting for you in 2020! #kanye2020", "favorites": 44, "retweets": 2}
 tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]

print(len(tweets))
# print(to_text(tweets)) # => ["This is a tweet!", "This is, too.", "More tweets!"
# print(to_text(to_lowercase(tweets)))
# print(to_text(nonempty(tweets)))
# print(total_word_count(nonempty(tweets)))
# print(hashtags(tweet1))
# print(mentions(tweet2))
# print(all_hashtags(tweets))
# print(all_mentions(tweets))
# print(to_text(all_caps_tweets(tweets)))
# print(count_individual_words(tweets))
# print(count_individual_hashtags(tweets))
# print(count_individual_mentions(tweets))
# print(to_text(iphone_tweets(tweets)))
# print(to_text(android_tweets(tweets)))
# print(average_favorites(tweets))
# print(average_retweets(tweets))
# print(sort_by_favorites(tweets))
# print(sort_by_retweets(tweets))
# print(upper_quartile(sort_by_favorites(tweets)))
# print(lower_quartile(sort_by_favorites(tweets)))
# print(top_quarter_by(sort_by_favorites(tweets), "favorites"))
# print(n_most_common(2, count_individual_words(tweets)))
