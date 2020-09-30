from utils import getQstring, dbSearch, knapsack
from templates import searchHTML, frontpageHTML, notFoundHTML, teamBuilderHTML


def search(environ):
    qdict = getQstring(environ)
    if "query" in qdict.keys():
        data = dbSearch(qdict["query"])
        if len(data) == 0:
            return searchHTML.noResults()
        return searchHTML.showResults(data)
    return searchHTML.front()

def teamBuilder(environ):
    qdict = getQstring(environ)
    if "query" in qdict.keys():
        data = knapsack(qdict["query"])
        return teamBuilderHTML.showResults(qdict["query"], data)
    return teamBuilderHTML.front()

def frontpage(environ):
    return frontpageHTML.front()

def notFound(environ):
    return notFoundHTML.main()