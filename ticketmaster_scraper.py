# Junk code to scrape TicketMaster.
# It uses BeautifulSoup so inefficiently, it hurts.

from __future__ import division
from BeautifulSoup import BeautifulSoup
import math
import re
import time
import urllib2

possible_concerts = 0
concerts_per_page = 30

concerts = []

# Just realized that this doesn't bother checking for duplicates
# We can build a better data structure that keys in off of composite keys - or use awk :-D.

class Concert:
    def __init__(self, artist, tickets, venue, city, date):
        self.artist = to_unicode(artist)
        self.tickets = tickets
        self.venue = to_unicode(venue)
        self.city = to_unicode(city)
        self.date = to_unicode(date)

def to_unicode(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

def GrabPossibleCount():
    # Go to the base page and seed the amount of possible concerts
    # I am just hard coding this for now (3607 at the current time)
    globals()['possible_concerts'] = 300

def ScrapeTicketMasterPage(ticketmaster_url):
    url = urllib2.urlopen(ticketmaster_url)
    soup = BeautifulSoup(url)

    table_listing = soup.findAll("table", attrs={"class" : "tableListing"})
    rows = table_listing[0].contents[1].contents

    for row in rows:
        r = str(row).strip()
        s = BeautifulSoup(r)
        tds = s.findAll("td")
        
        if len(tds) > 0:
            artist, tickets = s.findAll("a", attrs={"class" : "findTickets"})
            artist = artist.contents[0]        
            tickets = tickets.contents[0] == u'Find Tickets&nbsp;&raquo;'
        
            # So hackish, it hurts
            venue = s.findAll("span", attrs={"class" : "tableListing-venue"})
            
            m = re.compile("<\/a>,(.*)<\/span>")
            city = re.findall(m, str(venue[0]))
            
            if (len(city) > 0):
                city = city[0].strip()
            else:
                city = ''
            
            venue = BeautifulSoup(str(venue[0]))
            venue = venue.findAll("a")
            venue = venue[0].contents[0]

            date = s.findAll("span", attrs={"class" : "tableListing-date"})
            
            if (len(date[0]) == 3):
                date = date[0].contents[0] + " " + date[0].contents[2]
            else:
                # If I can't parse the date, set the availability to False
                tickets = False
        
            concerts.append(Concert(artist, tickets, venue, city, date))

def RunScraper():
    # Calculate the max pages (remember to use the future division module)
    total_pages = int(math.ceil(possible_concerts / concerts_per_page))
    
    print "There are %d pages to scrape!" % (total_pages)
    
    for current_page in range(0, total_pages+1):
        page = "http://www.ticketmaster.co.uk/browse?category=10001&root=&rdc_select=n1095&rdc_syear=&rdc_smonth=&rdc_sday=&rdc_eyear=&rdc_emonth=&rdc_eday=&dma=&start=%d&rpp=%d&type=selected"
        start = current_page * (concerts_per_page) + 1
        page = page % (start, concerts_per_page)
        ScrapeTicketMasterPage(page)
        
        # Wait 2 seconds and print a bit of a status
        print "This tool has currently collected: %d concerts" % (len(concerts))
        time.sleep(2)

def CSVPrint():
    # Print the output (simple CSV format)
    for c in concerts:
        if (c.tickets):
            print "%s,%s,%s,%s,%s" % (c.artist.encode('utf-8'), c.tickets, c.venue.encode('utf-8'), c.city.encode('utf-8'), c.date.encode('utf-8'))
        else:
            print "%s,%s,%s,%s" % (c.artist.encode('utf-8'), c.tickets, c.venue.encode('utf-8'), c.city.encode('utf-8'))

GrabPossibleCount()
RunScraper()
CSVPrint()
