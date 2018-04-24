import psycopg2

def connect():
    return psycopg2.connect("dbname=news")

"""Print the list of the 3 most popular articles of all time."""
def popular_article():
    db=connect()
    c=db.cursor()
    c.execute("SELECT articles.title, COUNT(*) AS num
              "FROM articles"
              "JOIN log
              "ON log.path LIKE concat('/article/%', articles.slug)"
              "GROUP BY articles.title"
              "ORDER BY num DESC"
              "LIMIT 3;")
    results=c.fetchall()
    for i in range(len(results)):
        title=results[i][0]
        views=results[i][1]
        print("%s--%d" % (title,views))
    db.close()

"""Prints the list of the most popular authors of all time."""
def popular_authors():
    db=connect() 
    c=db.cursor()
    c.execute("SELECT authors.name, COUNT(*) AS num"
              "FROM authors"
              "JOIN articles"
              "ON authors.id = articles.author"
              "JOIN log"
              "ON log.path like concat('/article/%', articles.slug)"
              "GROUP BY authors.name"
              "ORDER BY num DESC"
              "LIMIT 3;")
    results=c.fetchall()
    for i in range(len(results)):
        name=results[i][0]
        views=results[i][1]
        print("%s--%d" % (name,views))
    db.close()

"""Prints the day with more that 1% error."""
def error_percent():
    db=connect()
    c=db.cursor()
    c.execute("SELECT date, error_rate"
              "FROM request_error_rate"
              "WHERE error_rate >= 1;")
    results=c.fetchall()
    for i in range(len(results)):
        date=results[i][0]
        err_prc=results[i][1]
        print("%s--%.1f %%" %(date,err_prc))

if __name__ == "__main__":
  print("POPULAR ARTICLES ARE:")
  popular_article()
  print("\n")
  print("POPULAR AUTHORS ARE:")
  popular_authors()
  print("\n")
  print("DAYS WITH MORE THAN 1.0% ERRORS:")
  error_percent()
