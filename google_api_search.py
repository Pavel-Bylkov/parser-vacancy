import pprint

from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.coursera import Search as CourseraSearch
from search_engine_parser.core.engines.yandex import Search as YandexSearch
from search_engine_parser.core.engines.youtube import Search as YoutubeSearch

search_args = ('Курс UX дизайнер', 1)
gsearch = GoogleSearch()
gresults = gsearch.search(*search_args, url="google.ru", hl='ru', as_sitesearch='netology.ru')
a = {
  "Google": gresults
  }

# pretty print the result from each engine
for k, v in a.items():
    print(f"-------------{k}------------")
    for result in v:
        pprint.pprint(result)

# print first title from google search
print(gresults["titles"][0])
# print 10th link from yahoo search
print(gresults["links"][9])
# print 6th description from bing search
print(gresults["descriptions"][5])

# print first result containing links, descriptions and title
print(gresults[0])
