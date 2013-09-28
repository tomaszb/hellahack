from BeautifulSoup import BeautifulSoup
import urllib2
import re

def findsongs(site):
	result = {}
	html_page = urllib2.urlopen(site)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		hreffound = link.get('href')
		if hreffound:
			if (hreffound.find("youtube.com") > -1) or (hreffound.find("soundcloud.com") > -1) or (hreffound.find("vimeo.com") > -1):
				if link.text:
					result[link.text] = hreffound
	
	return result				

if __name__ == '__main__':
	findsongs()

