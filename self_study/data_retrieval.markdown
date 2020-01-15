---
title: 'Self-study track: data retrieval'
author: 'Jason T. Kiley'
date: 'January 12, 2020'

geometry: margin=1.1in
fontsize: 12pt
mainfont: 'Source Serif Pro'
monofont: 'Source Code Pro'
urlcolor: 'Blue'

---

# Data Retrieval

This data retrieval self-study track is designed to help you programmatically access, retrieve, and structure data of interest in research.
The techniques covered include web scraping, API access, and SQL.

The internet has a wealth of text and data sources---from press releases to Kickstarter to to social media---that can allow us to examine novel research questions that are hard to examine otherwise.
In some cases, these sources are accessible on the web, though they often require some transformation to extract the data that we want.
These techniques work best when there is on (or a small number) of websites with a lot of data.
This is true because we generally have to write bespoke code for each website that we want to gather data from (and sometimes per section).
There are some great Python packages that do most of the heavy lifting, but we have to link them together.
As a result, this web-scraping topic is perhaps the most independent topic across these self-study tracks.

In some cases, services and data providers provide a structured way to obtain data.
Some of these use an Application Programming Interface ("API"), and these often have tools designed to interface with them directly.
For example, the `pandas-datareader` Python package provides an interface to [many sources](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html) that have provide structured data, including many financial data sources, FRED, Eurostat, and OECD.
In addition, sources like Wharton Research Data Services ("WRDS") have their own packages that allow data access, in this case using SQL to specify queries.


# Resources

1. Web scraping in its most basic form generally involves retrieving the HTML for a page and navigating the contents using a Python package called [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
    - These [video tutorials](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS) do a good job of walking you through the basics and some of the common problems. Note, the author is using a text editor and a terminal, but you can do this in Jupyter instead.
    - Some folks I know like to use [scrapy](https://scrapy.org) to automate the retrieval part. I tend to write my own with the [requests](https://2.python-requests.org/en/master/) package, but this may be a higher ROI for you.
    - As I mention in the workshop, I like to start with getting what I want from one target page, then building the automation to find, retrieve, and process a lot of pages. Sometimes, the processing is complex and there are many pages to gather, so you might choose to retrieve and save the pages. While those are being retrieved, you can work on developing the processing using the saved files. Just be sure that you get the processing working and then process all pages with the same code to keep all of your data consistent.
    - Websites don't like it when web scrapers are heavy users of their servers. In general, my advice is to be cool about it. Don't pull more than a page every 10 seconds or so (maybe slower for smaller sites).
    - For some commercial subscription sources, scraping is against their terms of service, so be careful. Often, asking your research librarians about the data is a better idea, because (a) they can clear it with the provider, and (b) sometimes they will query their data and send you structured data (which is much less work).
1. Some web pages send your web browser code that it runs in order to get data. As a result, our standard techniques of requesting pages and finding the content we want within them will not work. [Selenium](https://www.seleniumhq.org) is a Python package that allows us to programmatically control a web browser and have open the pages for us (including executing dynamic code) and then retrieving the data.
    - [This tutorial](https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/) is a good place to get started.
    - Some social media sites load more data when you scroll to the bottom of the page, so scrolling down and pausing while waiting for more data (often 3-5 seconds) can often be enough of a rate limit to be cool, as I mention in the prior resource.
1. As I mentioned above, [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/index.html) provides an interface to a number of high-quality data sources. In addition, if you start building your own more advanced tools, the project structure using classes is a good exemplar.
1. Read [*Teach Yourself SQL in 10 Minutes*](https://forta.com/books/0672336073/), 4th edition, by Ben Forta. The title is perhaps a bit optimistic, though the design of the book (like others in the series) is that it teaches you one specific topic in each of many short chapters. I like this book because it quickly gives you enough of a skillset to handle some common tasks. It's not that deep, but it is very high ROI. Some notes:
    - This is also on the data handling self study, reflecting how useful SQL is in general.
    - SQL has a standard version (called ANSI SQL) and many DMBS-specific customizations. As a result, you will often find yourself searching to find out how to do a particular thing with a particular DBMS (see e.g., [datetimes in SQLite](https://stackoverflow.com/questions/12406295/how-to-query-in-sqlite-for-different-date-format)).
    - I suggest using SQLite built into Python (see e.g., [a tutorial](https://likegeeks.com/python-sqlite3-tutorial/)) for learning and for most project use. For a lot of things we do, it works fine, and it's a large step up in learning and complexity to run a server-based DBMS like PostgreSQL.
    - For retrieval, WRDS has a [Python package](https://github.com/wharton/wrds) that allows you to access WRDS using SQL queries in Python. Do note that, like when developing any query, you should use a `LIMIT` statement with a reasonable limit (I often use 100 or 1000) until you are satisfied that it is doing exactly what you want.
