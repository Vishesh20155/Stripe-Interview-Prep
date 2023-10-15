# JSON in Python

* As per valid JSON schema, strings must be enclosed in double quotes (“)

* This is invalid JSON: 
`"{'akshat' : 1, 'nikhil' : 2}"`

* flatten a JSON using flatten_json library:
    `
    from flatten_json import flatten
    `
    
    `
    flat_json = flatten(unflat_json)
    `

* Reading from JSON file:
    `
    f = open('data.json')`

    `
    data = json.load(f)
    `

* Writing to a JSON file using json.dump()

`with open("sample.json", "w") as outfile:`
  
  `json.dump(x, outfile, indent=4)`

* Sort JSON by value: https://www.geeksforgeeks.org/python-sort-json-by-value/

* Custom Encoding using JSONEncoder: Converts a custom object to JSON object. Implementation in `custom_json_encoding.py`. Done with help of `cls` parameter of `dumps`. 
    * In `json_encoding.py`, encoding done using `default` param of dumps

* Custom Decoding using `object_hook`. Pass a method returning required object. Implementation in `custom_json_decoding.py`

* All JSON links: https://www.geeksforgeeks.org/python-json/