import numpy as np
import os

indexhtml = open('../website/index.html','w');
count = 1

def initalize():
	indexhtml.write('<!DOCTYPE HTML>\n');
	indexhtml.write('<html>\n');
	indexhtml.write('\n');
	indexhtml.write('<head>\n');
	indexhtml.write('\t<title> LightOJ Solutions </title>\n');
	indexhtml.write('\t<meta name="description" content="website description" />\n');
	indexhtml.write('\t<meta name="keywords" content="website keywords, website keywords" />\n');
	indexhtml.write('\t<meta http-equiv="content-type" content="text/html; charset=windows-1252" />\n');
	indexhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Tangerine&amp;v1" />\n');
	indexhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" />\n');
	indexhtml.write('\t<link rel="stylesheet" type="text/css" href="style/style.css" />\n');
	indexhtml.write('</head>\n');
	indexhtml.write('\n');
	indexhtml.write('<body>\n');
	indexhtml.write('\t<div id="main">\n');
	indexhtml.write('\t\t<div id="header">\n');
	indexhtml.write('\t\t\t<div id="logo">\n');
	indexhtml.write('\t\t\t\t<h1>LightOJ Solutions</h1>\n');
	indexhtml.write('\t\t\t</div>\n');
	indexhtml.write('\t\t\t<div id="menubar">\n');
	indexhtml.write('\t\t\t\t<ul id="menu">\n');
	indexhtml.write('\t\t\t\t\t<li class="current"><a>List of Problems</a></li>\n');
	indexhtml.write('\t\t\t\t\t<li><a href="tags/">Search by Tags</a></li>\n');
	indexhtml.write('\t\t\t\t</ul>\n');
	indexhtml.write('\t\t\t</div>\n');
	indexhtml.write('\t\t</div>\n');
	indexhtml.write('\t\t<div id="site_content">\n');
	indexhtml.write('\t\t\t<div id="sidebar_container">\n');
	indexhtml.write('\t\t\t\t<img class="paperclip" src="style/paperclip.png" alt="paperclip" />\n');
	indexhtml.write('\t\t\t\t<div class="sidebar">\n');
	indexhtml.write('\t\t\t\t<!-- insert your sidebar items here -->\n');
	indexhtml.write('\t\t\t\t<h3>About Me</h3>\n');
	indexhtml.write('\t\t\t\t<h3><a href="https://www.facebook.com/utk3995">Utkarsh Srivastava</a></h3><br/>\n');
	indexhtml.write('\t\t\t\t<p> Student of IIIT Allahabad </p>\n');
	indexhtml.write('\t\t\t\t<h4>Programmer | Developer | Reader<br/><br/>\n');
	indexhtml.write('\t\t\t\t</div>\n');
	indexhtml.write('\t\t\t</div>\n');
	indexhtml.write('\t\t\t<div id="content">\n');
	

def footer(lastupdate):
	indexhtml.write('\t\t\t</div>\n');
	indexhtml.write('\t\t</div>\n');
	indexhtml.write('\t\t<div id="footer">\n');
	indexhtml.write('\t\t\t<p> Last Updated on : <a>'+ lastupdate +'</a></p>\n');
	indexhtml.write('\t\t</div>\n');
	indexhtml.write('\t</div>\n');
	indexhtml.write('</body>\n');
	indexhtml.write('</html>\n');
	indexhtml.close()

def add(questionCode,questionTitle):
	link = "files/"+str(questionCode)+".html"
	global count
	indexhtml.write('\t\t\t\t<h4 style = "font-size: 16px; LINE-HEIGHT:25px;"> '+str(count)+'. <a href="'+ link +'">'+ questionTitle +'</a></h4>\n');
	count = count + 1
