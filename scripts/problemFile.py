import numpy as np
import os


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


def print_tags(tags,questionTitle,quesitonCode,problemhtml):
	count = 0;
	for tag in tags:
		filelink = get_filelink(tag)
		filename = get_filename(tag)
		problemhtml.write('<a href= ../tags/'+filelink+'.html>'+tag+'</a>');
		count = count + 1
		if (count != len(tags)):
			problemhtml.write(", ")

		#create respective tag file
		tagfile = open('../source/tags/'+filename+'.txt',"a")
		tagfile.write('<a href=../files/'+str(quesitonCode)+'.html>'+questionTitle+'</a><br>\n');
		tagfile.close()


def create(questionCode , questionTitle , tags , problemStatement,lastupdate):
	cppfile  = open('../source/converted_cpp/'+str(questionCode)+'.cpp','r')
	cppcode = cppfile.read()
	cppfile.close()

	problemhtml = open('../website/files/'+questionCode+'.html','w')
	problemhtml.write('<!DOCTYPE HTML>\n');
	problemhtml.write('<html>\n');
	problemhtml.write('\n');
	problemhtml.write('<head>\n');
	problemhtml.write('\t<title> Problem '+ str(questionCode) +'</title>\n');
	problemhtml.write('\t<meta name="description" content="website description" />\n');
	problemhtml.write('\t<meta name="keywords" content="website keywords, website keywords" />\n');
	problemhtml.write('\t<meta http-equiv="content-type" content="text/html; charset=windows-1252" />\n');
	#problemhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Tangerine&amp;v1" />\n');
	#problemhtml.write('\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" />\n');
	problemhtml.write('\t<link rel="stylesheet" type="text/css" href="../style/style.css" />\n');

	problemhtml.write('\t<script type="text/javascript" src="../scripts/shCore.js"></script>\n')
	problemhtml.write('\t<script type="text/javascript" src="../scripts/shBrushCpp.js"></script>\n')
	problemhtml.write('\t<link type="text/css" rel="stylesheet" href="../styles/shCoreDefault.css"/>\n')
	problemhtml.write('\t<script type="text/javascript">SyntaxHighlighter.all();</script>\n')

	problemhtml.write('</head>\n');
	problemhtml.write('\n');
	problemhtml.write('<body>\n');
	problemhtml.write('\t<div id="main">\n');
	problemhtml.write('\t\t<div id="header">\n');
	problemhtml.write('\t\t\t<div id="logo">\n');
	problemhtml.write('\t\t\t\t<h1>LightOJ Solutions</h1>\n');
	problemhtml.write('\t\t\t</div>\n');
	problemhtml.write('\t\t\t<div id="menubar">\n');
	problemhtml.write('\t\t\t\t<ul id="menu">\n');
	problemhtml.write('\t\t\t\t\t<li class="current"><a>'+str(questionCode)+'</a></li>\n');
	problemhtml.write('\t\t\t\t\t<li><a href="../">List of Problems</a></li>\n');
	problemhtml.write('\t\t\t\t\t<li><a href="../tags">Search by Tags</a></li>\n');
	problemhtml.write('\t\t\t\t</ul>\n');
	problemhtml.write('\t\t\t</div>\n');
	problemhtml.write('\t\t</div>\n');
	problemhtml.write('\t\t<div id="site_content">\n');
	problemhtml.write('\t\t\t<div id="sidebar_container">\n');
	problemhtml.write('\t\t\t\t<img class="paperclip" src="../style/paperclip.png" alt="paperclip" />\n');
	problemhtml.write('\t\t\t\t<div class="sidebar">\n');
	problemhtml.write('\t\t\t\t<!-- insert your sidebar items here -->\n');
	problemhtml.write('\t\t\t\t<h3>About Me</h3>\n');
	problemhtml.write('\t\t\t\t<h3><a href="https://www.facebook.com/utk3995">Utkarsh Srivastava</a></h3><br/>\n');
	problemhtml.write('\t\t\t\t<p> Student of IIIT Allahabad </p>\n');
	problemhtml.write('\t\t\t\t<h5>Programmer | Developer | Reader<br/><br/></h5>\n');
	problemhtml.write('\t\t\t\t</div>\n');
	problemhtml.write('\t\t\t</div>\n');
	problemhtml.write('\t\t\t<div id="content">\n');

	problemhtml.write('<h1><u>Question Code</u> : '+str(questionCode)+'</h1>\n')
	problemhtml.write('<h1><u>Problem Name</u> : <a href=http://lightoj.com/volume_showproblem.php?problem='+str(questionCode)+' target="_blank" >'+questionTitle+'</a></h1><br/>\n')
	problemhtml.write('<h3><u>Problem Tags</u> : \n')

	print_tags(tags,questionTitle,questionCode,problemhtml)

	problemhtml.write('<br/><br/>\n')
	problemhtml.write('<h3><u>Problem Statement</u> : </h3>\n')
	problemhtml.write(problemStatement+'<br/>');
	problemhtml.write('<h3><u>Code</u> : </h3>\n')
	problemhtml.write('<pre class="brush: cpp;">\n')
	problemhtml.write(cppcode);
	problemhtml.write('\t\t\t</div>\n');
	problemhtml.write('\t\t</div>\n');
	problemhtml.write('\t\t<div id="footer">\n');
	problemhtml.write('\t\t\t<p> Last Updated on : <a>'+ lastupdate +'</a></p>\n');
	problemhtml.write('\t\t</div>\n');
	problemhtml.write('\t</div>\n');
	problemhtml.write('</body>\n');
	problemhtml.write('</html>\n');
	problemhtml.close()