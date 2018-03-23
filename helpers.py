import psycopg2
import atexit


class Log:
    """
    Log defines necessary methods to search news database.
    Database name is passed as an argument to object.
    """

    def __init__(self, database):

        # create connection to database
        self.conn = psycopg2.connect(database=database)
        self.cursor = self.conn.cursor()

        # automatically close database before termination
        atexit.register(self.closeDatabase)

    def top_articles(self, count):
        """Returns most viewed articles"""

    def top_authors(self):
        """Returns list of most popular authors"""

    def badHttpStatus(self):
        """Returns the date and percentage when more than 1% requests failed"""

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

    def closeDatabase(self):
        self.cursor.close()
        self.conn.close()
