#import library to do http requests:
import urllib2
import urllib
#checking the SQL #checking the SQL #checking the SQL #checking the SQL 


#import MySQLdb
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
from urllib2 import URLError

# Import from anpther python file to call  ( printMenue and readingFunction) function  ....

#all these imports are standard on most modern python implementations  

# if you want to open file in a directory
# file = open('rss.xml')
#  print file.read()


#download the file:
#file = urllib2.urlopen('http://www.somedomain.com/somexmlfile.xml')

# or

#-----------------------------------------------------------------------------------------------------------
#--------------------------------------------- FUNCTION TO PRINT MENU ----------------

def readingXMLFile(file,urlLink):
    
    #convert to string:
    data = file.read()
    #close file because we don't need it anymore:
    file.close()
      
    #parse the xml you downloaded
    dom = parseString(data)
    
    #-------------- 
    
    
    from xml.dom import minidom
    # To count the number of 
    xmldoc = minidom.parse(urllib2.urlopen(urlLink))
    itemlist = xmldoc.getElementsByTagName('item') 
    numOfINews = len(itemlist)
    print " \n\n Number of News Feeds in [ ",numOfINews
    
    
    
    
    # this variable to syncronise the category since there are two category in each item
    # so it skips the category which has a link instead of category name
    catSync =1
    #------------------------------
    
    
    #------------------ Using numOfINews+1 coz of the page title so, by sing +1 will be ignored
    for i in range (0,numOfINews+1):
    
    
        #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name title:
        #using [i+1] to overcome (0,1) coz the first two title are for "most popular"
        
        # it can be used ( if i ==1 or 0) and start with [1] instead of [i+1]
        xmlTagTitle = dom.getElementsByTagName('title')[i+1].toxml()
        #strip off the tag (<title>data</title>  --->   data) 
        xmlDataTitle = xmlTagTitle.replace('<title>','').replace('</title>','').encode('utf-8').strip()
        
        xmlTagLink = dom.getElementsByTagName('link')[i+1].toxml()
        #strip off the tag (<link>data</link>  --->   data):
        xmlDataLink = xmlTagLink.replace('<link>','').replace('</link>','').encode('utf-8').strip()
        xmlVidID = xmlTagLink.replace('<link>http://www.youtube.com/watch?v=','').replace('&amp;feature=youtube_gdata</link>','').encode('utf-8').strip()
        
        xmlTagcategory = dom.getElementsByTagName('category')[i+catSync]
    # xmlDataDescription = xmlTagDescription.replace('<description>','').replace('</description>','')   
    # ---- To Solve    #--------  UnicodeEncodeError: 'ascii' codec can't encode character u'\xa3'
       # xmlDatacategory = xmlTagcategory.replace('<category>','').replace('</category>','').encode('utf-8').strip()
   
   
   
        if i == 0:
                print "-----------------------------------------------------------------------------------------------"
                print "------------------------------------ [", xmlDataTitle,"] -------------------------------------"
                print "-----------------------------------------------------------------------------------------------"
        
        else:    
            #print out the xml tag and data in this format: <tag>data</tag>
            print "Tiltel :", i, xmlDataTitle
            print "xmlVidID :", xmlVidID
            print "Link :", xmlDataLink
            #print "Description :", xmlDatacategory
            print "category :", xmlTagcategory.firstChild.nodeValue
            print "\n"
            catSync+=1;
            
            
            
            


    return xmlDataTitle
# --------------------------------------------------------------------------

def getNewsFeedsURL( chossenFeed ):
    
    urlLink = ""
    BBC_News_Feed_Name =""
    
    if chossenFeed == "1":
            urlLink = "http://feeds.bbci.co.uk/news/rss.xml"
            BBC_News_Feed_Name ="Top Stories"
    elif chossenFeed =="2":
             urlLink = "http://feeds.bbci.co.uk/news/world/rss.xml"
             BBC_News_Feed_Name ="World"
    elif chossenFeed=="3":
             urlLink = "http://feeds.bbci.co.uk/news/uk/rss.xml"
             BBC_News_Feed_Name ="UK"
    elif chossenFeed =="4":
             urlLink = "http://feeds.bbci.co.uk/news/business/rss.xml"
             BBC_News_Feed_Name ="Business"
    elif chossenFeed =="5":
            urlLink = "http://feeds.bbci.co.uk/news/politics/rss.xml"
            BBC_News_Feed_Name ="Politics"
    elif chossenFeed =="6":
            urlLink = "http://feeds.bbci.co.uk/news/politics/rss.xml"
            BBC_News_Feed_Name ="Health"
    elif chossenFeed =="7":
            urlLink = "http://feeds.bbci.co.uk/news/education/rss.xml"
            BBC_News_Feed_Name ="Education & Family"
    elif chossenFeed =="8":
            urlLink = "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml"
            BBC_News_Feed_Name ="Science & Environment"
    elif chossenFeed =="9":
            urlLink = "http://feeds.bbci.co.uk/news/technology/rss.xml"
            BBC_News_Feed_Name ="Technology"
    elif chossenFeed =="10":
            urlLink = "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"
            BBC_News_Feed_Name ="Entertainment & Arts"
    return (urlLink, BBC_News_Feed_Name)



#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------




# --------




"""
url = 'http://10.0.2.2/android_connect/create_calls.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }




data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()


"""
