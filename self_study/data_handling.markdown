---
title: 'Self-study track: data handling'
author: 'Jason T. Kiley'
date: 'January 12, 2020'

geometry: margin=1.1in
fontsize: 12pt
mainfont: 'Source Serif Pro'
monofont: 'Source Code Pro'
urlcolor: 'Blue'

---

# Data Handling

This data handling self-study track is designed to help you handle and transform data in ways that are more sophisticated than most commercial stats packages and much better at handling larger datasets (up to about 100 GB).

In many text analysis projects, one of the key challenges is handling a large amount of text data in ways that allow us to perform content analysis and then merge those results back into our archival data.
Python and pandas make many things easy, and they make some complex things quite straightforward.
One limitation of pandas (and commercial stats packages like Stata) is that they need the computer to have enough memory to hold an entire dataset in memory.
Using a database management system ("DBMS"), even a very lightweight one like SQLite (which is built-in to Python), can allow us to overcome that limitation in a way that works simply with pandas.
Structured query language ("SQL") is the language that we use to interact with a DMBS.
Combined, these tools allow us to efficiently---both in terms of our time and computational resources---handle nearly any kind of text data up to about 100GB in size.
For comparison, I have a 2 million article full-text news database that is 11GB.

My own research has benefitted greatly from adopting Python and pandas for data handling.
I have assembled datasets in a few hundred lines of Python code that are larger and much more complex than datasets that required thousands of lines of Stata code to assemble.
As one small example, Python (and SQL) can do what is called a non-equi-join.
This is a merge where, instead of matching on the equality of two columns, it allows less-than and greater-than comparisons.
These are really helpful when matching on dates such that you want the most recent match.
This is possible in Stata, but you have to write the logic yourself, instead of using the straightforward `df.merge_asof()` in pandas (see [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge_asof.html)).
Also, we can easily do things like querying the news articles for an acquiring firm for the three months before an acquisition.
That requires a custom query for every row in the dataset, but we can automate those with Python and pandas, though it would be a large amount of work with numerous intermediate states in Stata.

There is a largely-absent topic from this self-study: database design.
The two reasons for that are (a) you will pick up enough of the essentials, and (b) it is not, overall, a high return-on-investment skill for research.
We typically use databases as a workaround for memory limitations, so we are less bothered by "bad" design that would create real issues for typical databases that have many transactions and applications built on top of them.


# Resources

1. Wes McKinney's book, [*Python for Data Analysis*](https://wesmckinney.com/pages/book.html). This book covers a lot of ground in a practical way. Do note that pandas is under very active development, so some things may work slightly differently on the most current version. It helps to use the code samples on the book's [Github repository](https://github.com/wesm/pydata-book), as those can be updated by the author.
1. Read [*Teach Yourself SQL in 10 Minutes*](https://forta.com/books/0672336073/), 4th edition, by Ben Forta. The title is perhaps a bit optimistic, though the design of the book (like others in the series) is that it teaches you one specific topic in each of many short chapters. I like this book because it quickly gives you enough of a skillset to handle some common tasks. It's not that deep, but it is very high ROI. Some notes:
    - This is also on the data retrieval self study, reflecting how useful SQL is in general.
    - SQL has a standard version (called ANSI SQL) and many DMBS-specific customizations. As a result, you will often find yourself searching to find out how to do a particular thing with a particular DBMS (see e.g., [datetimes in SQLite](https://stackoverflow.com/questions/12406295/how-to-query-in-sqlite-for-different-date-format)).
    - I suggest using SQLite built into Python (see e.g., [a tutorial](https://likegeeks.com/python-sqlite3-tutorial/)) for learning and for most project use. For a lot of things we do, it works fine, and it's a large step up in learning and complexity to run a server-based DBMS like PostgreSQL.
1. (optional) Read [*SQL Queries for mere mortals*](https://www.pearson.com/us/higher-education/program/Viescas-SQL-Queries-for-Mere-Mortals-A-Hands-On-Guide-to-Data-Manipulation-in-SQL-4th-Edition/PGM1937355.html), 4th edition, by John L. Viescas. This book is also designed for beginners, but it is more comprehensive (if less efficient) than the prior book. As such, it can help understand why things are designed as they are, and that knowledge is often helpful when solving problems.
