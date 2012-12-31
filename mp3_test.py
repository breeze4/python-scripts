import eyeD3
 
#----------------------------------------------------------------------
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

getEyeD3Tags("16 Miss You Paradise (Venom One Exte.mp3")
