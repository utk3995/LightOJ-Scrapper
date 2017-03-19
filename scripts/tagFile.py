import numpy as np
import os

taghtml = open('../website/index.html','w');
count = 1

def shorten(tagName):
	newtag="";
	siz = len(tagName);
	if (siz > 20):
		i = 0
		while (i<17):
			newtag = newtag + tagName[i]
			i=i+1
		newtag = newtag+"..."
	else:
		newtag = tagName
	return newtag

def get_filelink(tag):
	newtag = ""
	for i in tag:
		if (i == ' '):
			newtag = newtag + '%20'
		elif (i == '/'):
			newtag = newtag + '-'
		else:
			newtag = newtag + i
	return newtag

def get_filename(tag):
	newtag = ""
	for i in tag:
		if (i == '/'):
			newtag = newtag + '-'
		else:
			newtag = newtag + i
	return newtag


def initalize(tagName):
	global taghtml
	global count
	count = 1
	filename = get_filename(tagName)
	filelink = get_filelink(tagName)
	taghtml = open('../website/tags/'+filename+'.html','w');
	shorttag = shorten(tagName);
	taghtml.write('<!DOCTYPE HTML>\n');
	taghtml.write('<html>\n');
	taghtml.write('\n');
	taghtml.write('<head>\n');
	taghtml.write('\t<title>'+ tagName +'</title>\n');
	taghtml.write('\t<meta name="description" content="website description" />\n');
	taghtml.write('\t<meta name="keywords" content="website keywords, website keywords" />\n');
	taghtml.write('\t<meta http-equiv="content-type" content="text/html; charset=windows-1252" />\n');
	#taghtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Tangerine&amp;v1" />\n');
	#taghtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" />\n');
	taghtml.write('\t<link rel="stylesheet" type="text/css" href="../style/style.css" />\n');
	taghtml.write('</head>\n');
	taghtml.write('\n');
	taghtml.write('<body>\n');
	taghtml.write('\t<div id="main">\n');
	taghtml.write('\t\t<div id="header">\n');
	taghtml.write('\t\t\t<div id="logo">\n');
	taghtml.write('\t\t\t\t<h1>LightOJ Solutions</h1>\n');
	taghtml.write('\t\t\t</div>\n');
	taghtml.write('\t\t\t<div id="menubar">\n');
	taghtml.write('\t\t\t\t<ul id="menu">\n');
	taghtml.write('\t\t\t\t\t<li class="current"><a>'+shorttag+'</a></li>\n');
	taghtml.write('\t\t\t\t\t<li><a href="../">List of Problems</a></li>\n');
	taghtml.write('\t\t\t\t\t<li><a href="./">Search by Tags</a></li>\n');
	taghtml.write('\t\t\t\t</ul>\n');
	taghtml.write('\t\t\t</div>\n');
	taghtml.write('\t\t</div>\n');
	taghtml.write('\t\t<div id="site_content">\n');
	taghtml.write('\t\t\t<div id="sidebar_container">\n');
	taghtml.write('\t\t\t\t<img class="paperclip" src="../style/paperclip.png" alt="paperclip" />\n');
	taghtml.write('\t\t\t\t<div class="sidebar">\n');
	taghtml.write('\t\t\t\t<!-- insert your sidebar items here -->\n');
	taghtml.write('\t\t\t\t<h3>About Me</h3>\n');
	taghtml.write('\t\t\t\t<h3><a href="https://www.facebook.com/utk3995">Utkarsh Srivastava</a></h3><br/>\n');
	taghtml.write('\t\t\t\t<p> Student of IIIT Allahabad </p>\n');
	taghtml.write('\t\t\t\t<h5>Programmer | Developer | Reader<br/><br/></h5>\n');
	taghtml.write('\t\t\t\t</div>\n');
	taghtml.write('\t\t\t</div>\n');
	taghtml.write('\t\t\t<div id="content">\n');
	

def footer(lastupdate):
	taghtml.write('\t\t\t</div>\n');
	taghtml.write('\t\t</div>\n');
	taghtml.write('\t\t<div id="footer">\n');
	taghtml.write('\t\t\t<p> Last Updated on : <a>'+ lastupdate +'</a></p>\n');
	taghtml.write('\t\t</div>\n');
	taghtml.write('\t</div>\n');
	taghtml.write('</body>\n');
	taghtml.write('</html>\n');
	taghtml.close()

def add(content):
	global count
	taghtml.write('\t\t\t\t<h4 style = "font-size: 16px; LINE-HEIGHT:25px;"> '+str(count)+'. '+content+'</h4>\n');
	count = count + 1
