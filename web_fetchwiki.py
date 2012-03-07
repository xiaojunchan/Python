import urllib2
import sys

text = '_'.join(sys.argv[1:])
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
link = 'http://en.wikipedia.org/w/index.php?title='+text+'&printable=yes'
infile = opener.open(link)
page = infile.read()

f = open("temp.htm",'w')
f.write(page)
f.close()