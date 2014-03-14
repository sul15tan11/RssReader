    # ------------------ Database Connection ------
import MySQLdb
def connectDB():
        
        # Open database connection
    db = MySQLdb.connect("localhost","root","","TESTDB" )
        
        # prepare a cursor object using cursor() method
    cursor = db.cursor()
        
        # execute SQL query using execute() method.
    #cursor.execute("SELECT VERSION()")
        
        # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
        
    print "Database version : %s " % data
        
        # disconnect from server
    db.close()
    
    return

def createTable():

    
    # Open database connection
    db = MySQLdb.connect("localhost","root","","TESTDB" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS RSSFEEDS")
    
    # Create table as per requirement
    sql = """CREATE TABLE RSSFEEDS (
             FEED_CATEGORY  CHAR(100) NOT NULL,
             TAG_TITLE  CHAR(200) NOT NULL,
             DESCRIPTION  CHAR(200),
             URL_LINK VARCHAR(250)
              )"""
    
    cursor.execute(sql)
    
    # disconnect from server
    db.close()
    return

def insertValuesInDB(BBC_News_Feed_Name, title, xmlDataDescription, urlLink):
     
    # Open database connection
    db = MySQLdb.connect("localhost","root","","TESTDB" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to INSERT a record into the database.
   
    
     #sql = """INSERT INTO RSSFEEDS(TAG_TITLE,
     #       DESCRIPTION, URL_LINK)
     #        VALUES ('Macaa', 'Mohan','http://www.bbc.co.uk/news/magazine-26519670#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa ')"""
    
    
    try:
       # Execute the SQL command
       # cursor.execute(sql)   
       cursor.execute('insert into RSSFEEDS values("%s", "%s", "%s", "%s")' % \
            (BBC_News_Feed_Name,title,xmlDataDescription,urlLink ))    
       
       # Commit your changes in the database
       db.commit()
    except e:
       # Rollback in case there is any error
       db.rollback()
    
    # disconnect from server
    db.close()
    return