# Accessing the NYC Comptroller's Office Checkbook NYC Data: Some Learnings

## Background
The New York City Comptroller's Office publishes the City's "day-to-day spending" in an online tool called [Checkbook NYC](https://www.checkbooknyc.com/spending_landing/yeartype/B/year/120).

This is super useful for all kinds of interesting open data analysis!

Folks can query contract, budget, spending, payroll, and revenue data directly on the website using robust parameters. Since these queries can be rather large, Checkbook NYC assigns users a query tracking number so they can monitor their status, and will send an email when the final results are ready for download.

Folks can also query the data by sending an XML via POST to the endpoint 'https://www.checkbooknyc.com/api'.

## Querying the API
Suppose you have a list of several organizations whose business business dealings with the city are of interest to you. You can:

1. Read the list into a pandas dataframe
2. Build the XML for the queries using **ElementTree** wrapper
3. POST the XML to the Checkbook NYC endpoint using the **Requests** package
4. Receive the results and parse them accordingly
5. Zip everything back together in a tidy dataframe

There's also a [Python package written by the Comptroller's Office](https://github.com/CityOfNewYork/Comptrollers-Checkbook). However, I wasn't quite able to get this working with 3.6 despite updating the docstrings as needed. It was published in 2013, and there are a handful of pull requests from 2015 still pending, so I don't think it'll be updated anytime soon.
