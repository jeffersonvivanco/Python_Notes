from urllib import request, parse

# url being accessed
url = 'http://localhost:8080'

# dictionary of query params if any
params = {
    'name1': 'value1',
    'name2': 'value2'
}

# encode the query string
querystring = parse.urlencode(params)

# make a get request and read the response
u = request.urlopen(url+'?'+querystring)
resp = u.read()
