import numpy as np
import os

tagindexhtml = open('../website/tags/index.html','w');
count = 1

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


def initalize():
	tagindexhtml.write('<!DOCTYPE HTML>\n');
	tagindexhtml.write('<html>\n');
	tagindexhtml.write('\n');
	tagindexhtml.write('<head>\n');
	tagindexhtml.write('\t<title>Tags</title>\n');
	tagindexhtml.write('\t<meta name="description" content="website description" />\n');
	tagindexhtml.write('\t<meta name="keywords" content="website keywords, website keywords" />\n');
	tagindexhtml.write('\t<meta http-equiv="content-type" content="text/html; charset=windows-1252" />\n');
	tagindexhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Tangerine&amp;v1" />\n');
	tagindexhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" />\n');
	tagindexhtml.write('\t<link rel="stylesheet" type="text/css" href="../style/style.css" />\n');
	tagindexhtml.write('</head>\n');
	tagindexhtml.write('\n');
	tagindexhtml.write('<body>\n');
	tagindexhtml.write('\t<div id="main">\n');
	tagindexhtml.write('\t\t<div id="header">\n');
	tagindexhtml.write('\t\t\t<div id="logo">\n');
	tagindexhtml.write('\t\t\t\t<h1>LightOJ Solutions</h1>\n');
	tagindexhtml.write('\t\t\t</div>\n');
	tagindexhtml.write('\t\t\t<div id="menubar">\n');
	tagindexhtml.write('\t\t\t\t<ul id="menu">\n');
	tagindexhtml.write('\t\t\t\t\t<li><a href="../">List of Problems</a></li>\n');
	tagindexhtml.write('\t\t\t\t\t<li class="current"><a>Search by Tags</a></li>\n');
	tagindexhtml.write('\t\t\t\t</ul>\n');
	tagindexhtml.write('\t\t\t</div>\n');
	tagindexhtml.write('\t\t</div>\n');
	tagindexhtml.write('\t\t<div id="site_content">\n');
	tagindexhtml.write('\t\t\t<div id="sidebar_container">\n');
	tagindexhtml.write('\t\t\t\t<img class="paperclip" src="../style/paperclip.png" alt="paperclip" />\n');
	tagindexhtml.write('\t\t\t\t<div class="sidebar">\n');
	tagindexhtml.write('\t\t\t\t<!-- insert your sidebar items here -->\n');
	tagindexhtml.write('\t\t\t\t<h3>About Me</h3>\n');
	tagindexhtml.write('\t\t\t\t<h3><a href="https://www.facebook.com/utk3995">Utkarsh Srivastava</a></h3><br/>\n');
	tagindexhtml.write('\t\t\t\t<p> Student of IIIT Allahabad </p>\n');
	tagindexhtml.write('\t\t\t\t<h4>Programmer | Developer | Reader<br/><br/>\n');
	tagindexhtml.write('\t\t\t\t</div>\n');
	tagindexhtml.write('\t\t\t</div>\n');
	tagindexhtml.write('\t\t\t<div id="content">\n');
	

def footer(lastupdate):
	tagindexhtml.write('\t\t\t</div>\n');
	tagindexhtml.write('\t\t</div>\n');
	tagindexhtml.write('\t\t<div id="footer">\n');
	tagindexhtml.write('\t\t\t<p> Last Updated on : <a>'+ lastupdate +'</a></p>\n');
	tagindexhtml.write('\t\t</div>\n');
	tagindexhtml.write('\t</div>\n');
	tagindexhtml.write('</body>\n');
	tagindexhtml.write('</html>\n');
	tagindexhtml.close()

def add(tag):
	global count
	filename = get_filename(tag)
	content = '<a href="'+ filename +'.html">'+tag+'</a>'
	tagindexhtml.write('\t\t\t\t<h4 style = "font-size: 16px; LINE-HEIGHT:25px;"> '+str(count)+'. '+content+'</h4>\n');
	count = count + 1
