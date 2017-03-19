from bs4 import BeautifulSoup
import requests
import mechanize
import re

def get_tags(forumCode):
	tags = []
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open("http://lightoj.com/login_main.php")	   #Url that contains signin form
	br.select_form(nr=0)
	br['myuserid'] = ""	#your id here
	br['mypassword'] = '' #your password here
	result = br.submit().read()
	'''if (result == "<script>location.href='login_success.php'</script>"):
	    print "Success"
	else:
	    print "Failure"'''

	url = "http://lightoj.com/forum_viewtopic.php?topic="+str(forumCode)

	r  = br.open(url)

	data = r.read()

	soup = BeautifulSoup(data, "html.parser")


	for link in soup.find_all('a'):
	    curlink = link.get('href')
	    curlink = str(curlink)
	    if (curlink.find("volume_problemcategory",0) != -1):
	    	#print curlink
			words = curlink.split("=")
			tagname = words[1]
			#print tagname
			tags.append(tagname)

	return tags