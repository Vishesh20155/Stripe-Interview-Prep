# Datetime in python

* String formatting for strptime: https://www.geeksforgeeks.org/python-datetime-strptime-function/?ref=lbp

    * Difference between %-M and %M

* String to datetime object: `datetime.datetime.strptime(data, format)`

* Datetime to String: `datetime_obj.strftime(format)`

* datetime object from timestamp: `time = datetime.fromtimestamp(1568093944)`

* specify parameters in get request as: 
    
    `response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)

    * `parameters` is a dictionary
`