import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

def get_movie_data(name):
    endpoint = 'http://www.omdbapi.com/'
    paramDict = {}
    paramDict['t'] = name
    paramDict['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=paramDict)

    return json.loads(this_page_cache.text)

get_movie_data("Venom")
get_movie_data("Baby Mama")

