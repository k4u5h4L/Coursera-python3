import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

def get_movies_from_tastedive(name):
    url = "https://tastedive.com/api/similar"
    paramDiction = {}
    paramDiction['q'] = name
    paramDiction['type'] = "movies"
    paramDiction['limit'] = 5
    this_page_cache = requests_with_caching.get(url, params=paramDiction)
    return json.loads(this_page_cache.text)

def extract_movie_titles(obj):
    return ([i['Name'] for i in obj['Similar']['Results']])
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

