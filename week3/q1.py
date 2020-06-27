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

