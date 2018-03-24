#!/usr/bin/env python3
"""application.py."""

# Internal reporting tool for Logs Analysis

from helpers import Log


def main():
    """Format the output for display."""
    # connect to database
    db = Log("news")

    print("LOGS ANALYSIS\nPLEASE WAIT...\n")

    # query database for requests
    articles = db.top_articles(3)
    authors = db.top_authors()
    errors = db.badHttpStatus()

    # format articles for output
    print("Most popular articles of all time")
    for title, views in articles:
        print("\"{}\" - {} views".format(title, views))

    # format authors for output
    print("\nMost popular article authors of all time")
    for name, views in authors:
        print("{} - {} views".format(name, views))

    # format errors for output
    print("\nMore than 1 percent of requests failed")
    for date, percent in errors:
        print("{} -- {}% errors".format(date, round(percent, 2)))

    print("")


if __name__ == "__main__":
    main()
