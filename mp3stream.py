import urllib
import eyeD3

def getEyeD3Tags(path):
    """"""
    trackInfo = eyeD3.Mp3AudioFile(path)
    tag = trackInfo.getTag()
    tag.link(path)
 
    print "Artist: %s" % tag.getArtist()
    print "Album: %s" % tag.getAlbum()
    print "Track: %s" % tag.getTitle()
    print "Track Length: %s" % trackInfo.getPlayTimeString()
    print "Release Year: %s" % tag.getYear()


target = open("broadcast.mp3", "wb")
conn = urllib.urlopen("http://72.26.204.32:80/drumandbass_hi?fe8e8eb42c69b8279b")
while True:
    target.write(conn.read(5200))

#getEyeD3Tags("broadcast.mp3")
