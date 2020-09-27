from wsgiref.simple_server import make_server
from views import testing
import mysql.connector


# mydb = mysql.connector.connect(
#   host="webapp_db_1",
#   user="",
#   password="helloworld"
# )

def app(environ, start_response):
    response_body = [
        f'{key}: {value}' for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
    ]

    start_response(status, response_headers)
    if environ["PATH_INFO"] == "/hej":
        return ["hej".encode("utf-8")]
    if environ["PATH_INFO"] == "/testing":
        return [testing(environ["QUERY_STRING"]).encode("utf-8")]
    return [response_body.encode('utf-8')]

# server = make_server('localhost', 8080, app=application)
# server.serve_forever()