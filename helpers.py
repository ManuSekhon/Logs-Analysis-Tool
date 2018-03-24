#!/usr/bin/env python3
"""helpers.py."""

import psycopg2
import atexit


class Log:
    """
    This class defines necessary methods to search news database.

    Database name is passed as an argument to object.
    """

    def __init__(self, database):
        """Initialize the object by connecting to database."""
        # create connection to database
        self.conn = psycopg2.connect(database=database)
        self.cursor = self.conn.cursor()

        # automatically call this function at the end
        atexit.register(self.closeDatabase)

    def top_articles(self, count):
        """Return most viewed articles."""
        try:
            # join tables with SQL like
            # https://stackoverflow.com/a/12785938
            self.cursor.execute("""SELECT articles.title, COUNT(*)
                                FROM articles
                                JOIN log ON
                                    log.path LIKE '%' || articles.slug
                                GROUP BY articles.title ORDER BY COUNT(*) DESC
                                LIMIT {}
                                """.format(count))

            # fetch results from above query
            articles = self.cursor.fetchall()
            return articles

        except psycopg2.Error as e:
            raise RuntimeError("Could not get articles: {}".format(e))

    def top_authors(self):
        """Return list of most popular authors."""
        try:
            self.cursor.execute("""SELECT authors.name, COUNT(*)
                                FROM log
                                JOIN articles ON
                                    log.path LIKE '%' || articles.slug
                                JOIN authors ON
                                    authors.id = articles.author
                                GROUP BY authors.name ORDER BY COUNT(*) DESC
                                """)

            authors = self.cursor.fetchall()
            return authors

        except psycopg2.Error as e:
            raise RuntimeError("Could not get authors: {}".format(e))

    def badHttpStatus(self):
        """Return the date and percentage when more than 1% requests failed."""
        try:
            self.cursor.execute("""SELECT t1.date, (t2.error * 100.0) / t1.total
                                FROM
                                (
                                    SELECT time::timestamp::date as date,
                                    COUNT(*) as total FROM log GROUP BY date
                                ) AS t1
                                JOIN
                                (
                                    SELECT time::timestamp::date as date,
                                    COUNT(*) as error FROM log
                                    WHERE status != (%s) GROUP BY date
                                ) AS t2
                                ON t1.date = t2.date
                                WHERE (t2.error * 100) / t1.total > 1.0
                                """, ("200 OK",))

            status = self.cursor.fetchall()
            return status

        except psycopg2.Error as e:
            raise RuntimeError("Could not set status info: {}".format(e))

    def closeDatabase(self):
        """Close connection to database."""
        self.cursor.close()
        self.conn.close()
