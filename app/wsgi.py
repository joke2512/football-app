from wsgiref.simple_server import make_server
from views import search, frontpage, notFound, teamBuilder
import mysql.connector
"""
Webapp 
"""

def app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'html'),
    ]

    start_response(status, response_headers)

    # ROUTING
    if environ["PATH_INFO"] == "/search":
        return [search(environ).encode("utf-8")]
    if environ["PATH_INFO"] == "/teambuilder":
        return [teamBuilder(environ).encode("utf-8")]
    if environ["PATH_INFO"] == "/":
        return [frontpage(environ).encode("utf-8")]
    #else not found
    return [notFound(environ).encode("utf-8")]