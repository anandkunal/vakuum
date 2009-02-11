#!/usr/bin/python2.5

# Some iTunes spelunking I was doing a while back.
# Maybe there's something exciting in here...

from Foundation import *
from ScriptingBridge import *
from pprint import pprint
from struct import unpack
from time import sleep
from urllib import urlopen

# Configuration and stoof
urlWhitespaceReplacement = '+' # This worked with the Last.FM service last time I checked
skipUnplayedTracks = True # If set to False, the score on the bottom is going to be janky
minimumSimilarityChunkPercentage = 0 # 0 should presumably get everything

aliasesToSkip = {}

# The following lines are from: http://discussions.apple.com/thread.jspa?messageID=6305279
# I should really take a look at appscript for this: http://www.math.columbia.edu/~bayer/Python/iTunes/

iTunes = SBApplication.applicationWithBundleIdentifier_('com.apple.iTunes')
lib = iTunes.sources()[0].playlists()[10] # print len(iTunes.sources()[0].playlists())
tracks = lib.elementArrayWithCode_(unpack('>L', 'cFlT')[0])

# The key is the artist name, the value is the playcount (useful for future weightings)
artists = {}
totalCount = 0

# Build a list of the unique artists
for track in tracks:
    artist = track.artist().strip().lower()
    if len(artist) > 0:
        playCount = track.playedCount()
        if skipUnplayedTracks and playCount == 0:
            continue
        else:
            totalCount += playCount
            if artists.has_key(artist):
                artists[artist] += playCount
            else:
                artists[artist] = playCount

recs = {}

# Now, for every artist, go ahead and find all the "similar" artists (sleep in between)
for artist in artists.keys():
    print 'Getting the artist: ', artist
    cleansedArtist = artist.replace(' ', urlWhitespaceReplacement)
    try:
        pagina = urlopen('http://ws.audioscrobbler.com/1.0/artist/' + cleansedArtist + '/similar.txt')
        for line in pagina:
            # To calculate the reliability of the artist: sigma(play count X similarity percentage)
            chunks = line.strip().split(',')
            # Treat the chunk like a percentage
            score = (float(chunks[0])/100) * float(artists[artist])
            recArtist = chunks[2].lower()
            # Ignore if if the similar artist already exists in the dict or aliases
            if artists.has_key(recArtist) or aliasesToSkip.has_key(recArtist):
                continue
            else:
                if recs.has_key(recArtist):
                    recs[recArtist] += score
                else:
                    recs[recArtist] = score
        sleep(2)
        print pprint(recs)
    except UnicodeError:
        # Go back and handle this, use telepopmusik as a case
        pass
    except ValueError:
        # No artist exists with the name: angels - WTF is going on here?
        pass

print '--------------------------'
print pprint(recs)

#print iTunes.currentTrack().name()
#pprint(dir(tracks[0]))
#print tracks[0].artist(), tracks[0].album()
#print pprint(artists)
#print len(artists)
#print totalCount
