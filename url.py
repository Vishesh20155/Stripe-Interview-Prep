from urllib.parse import urlparse, parse_qs, urlsplit

url = "https://www.example.com/search?q=query&q=iota&page=1&sort=asc"

# Parse the URL
parsed_url = urlparse(url)

# Get the query parameters as a dictionary
query_params = parse_qs(parsed_url.query)

# Access specific parameters
q_param = query_params.get('q', None)
page_param = query_params.get('page', None)
sort_param = query_params.get('sort', None)

print("q:", q_param)
print("page:", page_param)
print("sort:", sort_param)

split_url = urlsplit(url)

print(split_url)
query_params = parse_qs(split_url.query)
print(query_params)

x = "asdfghjk"
x.split()