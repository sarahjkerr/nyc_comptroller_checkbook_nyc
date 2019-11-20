# Accessing the NYC Comptroller's Office Checkbook NYC Data: Some Learnings

## Background
The New York City Comptroller's Office publishes the City's "day-to-day spending" in an online tool called [Checkbook NYC](https://www.checkbooknyc.com/spending_landing/yeartype/B/year/120).

This is super useful for all kinds of interesting open data analysis!

Folks can query contract, budget, spending, payroll, and revenue data directly on the website using robust parameters. Since these queries can be rather large, Checkbook NYC assigns users a query tracking number so they can monitor their status, and will send an email when the final results are ready for download.

Folks can also query the data by sending an XML via POST to the endpoint 'https://www.checkbooknyc.com/api'.
