from functools import *
import json
import math

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

"""
Key: xs and ys represent a list of arbitrary elements
Key: Functions that take in 'tweet' or 'tweets' will either take a single tweet
or a list of tweets where tweets are python dicts
"""


def flatten(xs):
    """Flattens a list of lists to simply a list"""
    return [dis for dat in xs for dis in dat]


def difference(xs, ys):
    """Finds all the elements that are in either xs or ys but not both"""
    return list(filter(lambda x: x not in ys, xs)) + list(filter(lambda y: y not in xs, ys))


def to_text(tweets):
    """Converts from a list of tweets to a list of tweet contents"""
    return [x["content"] for x in tweets]


def to_lowercase(tweets):
    """Converts the content of each tweet in the list of tweets to lowercase"""
    return list(map(lambda x: {**x, **{"content": x["content"].lower()}}, tweets))


def nonempty(tweets):
    """Removes all tweets with empty contents from the list of tweets"""
    return list(filter(lambda x: bool(x["content"]), tweets))


def total_word_count(tweets):
    """Calculates the total number of words in each tweet in a list"""
    return len(flatten([x["content"].split() for x in tweets]))


def hashtags(tweet):
    """Gets a list of all the hashtags from the speciﬁed tweet"""
    return list(filter(lambda x: x[0] == '#', tweet["content"].split()))


def mentions(tweet):
    """Gets a list of all the mentions from the speciﬁed tweet"""
    return list(filter(lambda x: x[0] == '@', tweet["content"].split()))


def all_hashtags(tweets):
    """Returns a list of all hashtags from a list of tweets"""
    return flatten([hashtags(x) for x in tweets])


def all_mentions(tweets):
    """Returns a list of all mentions from a list of tweets"""
    return flatten([mentions(x) for x in tweets])


def all_caps_tweets(tweets):
    """Returns a list of all tweets that are completely capitalized from the given list of tweets"""
    return list(filter(lambda x: x["content"].isupper(), tweets))


def count_individual_words(tweets):
    """Counts all the words in all the tweets and returns the count as a dictionary mapping each word to its count"""
    count_map = {}
    loc = flatten([x.split() for x in to_text(tweets)])
    [count_map.setdefault(x, loc.count(x)) for x in loc]
    return count_map


def count_individual_hashtags(tweets):
    """Counts all the hashtags in all the tweets and returns the count as a dictionary mapping each word to its count"""
    count_map = {}
    loh = all_hashtags(tweets)
    [count_map.setdefault(x, loh.count(x)) for x in loh]
    return count_map


def count_individual_mentions(tweets):
    """Counts all the mentions in all the tweets and returns the count as a dictionary mapping each word to its count"""
    count_map = {}
    lom = all_mentions(tweets)
    [count_map.setdefault(x, lom.count(x)) for x in lom]
    return count_map


def n_most_common(n, word_count):
    """Calculates the n most common keys in word_count, sorted from most to least common and sorted in alphabetical order when the number of occurrences is the same"""
    keys = sorted(word_count.keys())
    count_list = [(x, word_count[x]) for x in keys]
    sorted_count_list = sorted(count_list, key = lambda x: x[1], reverse=True)
    return sorted_count_list[0:n]


def iphone_tweets(tweets):
    """Filters a list of tweets to find only those made from an iPhone"""
    return list(filter(lambda x: x["source"] == "Twitter for iPhone", tweets))


def android_tweets(tweets):
    """Filters a list of tweets to find only those made from an Android device"""
    return list(filter(lambda x: x["source"] == "Twitter for Android", tweets))


def average_favorites(tweets):
    """Computes the average number of favorites from the list of tweets, rounding appropriately"""
    lof = [x["favorites"] for x in tweets]
    return round(reduce(lambda x, y: x + y, lof) / len(lof))


def average_retweets(tweets):
    """Computes the average number of retweets from the list of tweets, rounding appropriately"""
    lor = [x["retweets"] for x in tweets]
    return round(reduce(lambda x, y: x + y, lor) / len(lor))


def sort_by_favorites(tweets):
    """Sorts the tweets by the number of favorites they have"""
    return sorted(tweets, key=lambda x: x["favorites"])


def sort_by_retweets(tweets):
    """Sorts the tweets by the number of retweets they have"""
    return sorted(tweets, key=lambda x: x["retweets"])


def upper_quartile(tweets):
    """Finds the tweet representative of the upper quartile"""
    return tweets[math.floor(len(tweets) * (3 / 4))]


def lower_quartile(tweets):
    """Finds the tweet representative of the lower quartile"""
    return tweets[math.floor(len(tweets) * (1 / 4))]


def top_quarter_by(tweets, factor):
    """Finds all tweets with factor greater than or equal to the upper quartile"""
    upper = tweets[math.floor(len(tweets) * (3 / 4))][factor]
    return list(filter(lambda x: x[factor] >= upper, tweets))


def bottom_quarter_by(tweets, factor):
    """Finds all tweets with factor less than or equal to the lower quartile"""
    lower = tweets[math.floor(len(tweets) * (1 / 4))][factor]
    print(lower)
    return list(filter(lambda x: x[factor] >= lower, tweets))