#import library to do http requests:
import urllib2
import urllib
#checking the SQL #checking the SQL #checking the SQL #checking the SQL 


#import MySQLdb
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
from urllib2 import URLError 
from xml.dom import minidom


#------------------------------------------------------------------------------------------------

# xmldoc = minidom.parse(urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml'))
xmldoc = minidom.parse('books.xml')
itemlist = xmldoc.getElementsByTagName('title') 
print len(itemlist)
    
print itemlist[0].firstChild.nodeValue

for s in itemlist :
    print "Text : ", s.firstChild.nodeValue
    
    
    
#------------------------------------------------------------------------------------------------


       # xmldoc = minidom.parse(urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml'))
xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('item') 
print len(itemlist)
print itemlist[0].attributes['name'].value

for s in itemlist :
    print s.attributes['name'].value