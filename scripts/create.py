import numpy as np
import os
import mechanize
from shutil import copyfile
from bs4 import BeautifulSoup
import requests
import re
import os.path
import indexFile
import problemFile
import tagFile
import tagIndexFile
import taggetter
from time import gmtime, strftime


#converts the source cpp file so that it can be displayed on a webpage
def convertSource():
	for file in os.listdir("../source/source_cpp/"):
		if file.endswith(".cpp"):
			copyfile('../source/source_cpp/'+file,'./input.cpp')
			os.system("./convertor")
			copyfile('./output.cpp','../source/converted_cpp/'+file)
			os.system("rm ./output.cpp")
			os.system("rm ./input.cpp")


#returns the forumcode for the question code
def get_forum_code(quesitonCode):
	url = br.open("http://www.lightoj.com/forum_showproblem.php?problem="+str(quesitonCode))
	returnPage = url.read() 
	words = returnPage.split("=")
	forumCode = words[5]
	words = forumCode.split("'")
	forumCode = words[0]
	return forumCode


#saves the images for the problem if available
def save_images(body , quesitonCode):
    start = 0
    flag = 0
    sub = "src="
    while True:
        start = body.find(sub,start)
        if start == -1: return
        if (flag == 0):
        	flag = 1
        	directory = "../website/files/data/problems/desc/"+str(quesitonCode)
        	if not os.path.exists(directory):
        		os.makedirs(directory)
        newurl = "http://lightoj.com/"
        i = start+5
        while (body[i] != '"'):
        	newurl = newurl + body[i]
        	i = i+1
        #print newurl
        words = newurl.split("/")
        filename = words[7]
        filepathname = "../website/files/data/problems/desc/"+str(quesitonCode)+"/"+filename
        #print filepathname
        url = br.open(newurl)
        returnPage = url.read()
        output = open(filepathname,"wb")
        output.write(returnPage)
        output.close() 
        start += len(sub)


def cleanify():
	command = "../source/tags/*"
	os.system('rm '+command)


lastupdate = strftime("%a, %d %b %Y", gmtime())

cleanify()

convertSource();
indexFile.initalize()


br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.lightoj.com/login_main.php")	   #Url that contains signin form
br.select_form(nr=0)
br['myuserid'] = ""  #your user id here
br['mypassword'] = "" #your password here
result = br.submit().read()
if (result == "<script>location.href='login_success.php'</script>"):
    print "Login Success"
else:
    print "Login Failure"

list_of_tags = []

for file in os.listdir("../source/converted_cpp/"):
	if file.endswith(".cpp"):
		words = file.split(".")
		quesitonCode = words[0]
		print quesitonCode
		url = br.open("http://lightoj.com/volume_showproblem.php?problem="+str(quesitonCode))
		returnPage = url.read() 
		returnHtml = open('temphtml.html','w')
		returnHtml.write(returnPage)
		returnHtml.close()
		os.system("./probStatementExtractor")
		pageTitle = br.title()
		words = pageTitle.split("::")
		questionTitle = words[1]
		words = questionTitle.split("-")
		problemName = words[1]
		probStatementFile = open('probstatement.txt','r')
		problemStatement = probStatementFile.read()
		probStatementFile.close()
		os.system("rm ./temphtml.html")
		os.system("rm ./probstatement.txt")

		#getting tags
		forumCode = get_forum_code(quesitonCode)
		tags = taggetter.get_tags(forumCode)
		for tag in tags:
			list_of_tags.append(tag)

		#saving images for the problems if applicable
		save_images(problemStatement,quesitonCode)

		#add the problem link to the index file
		indexFile.add(quesitonCode,questionTitle)

		#create problem file and save it to website/files
		problemFile.create(quesitonCode,questionTitle,tags,problemStatement,lastupdate)


#close the index file
indexFile.footer(lastupdate)

#create tag files

#first individual tag files
for file in os.listdir("../source/tags/"):
		if file.endswith(".txt"):
			words = file.split(".")
			tagName = words[0]
			tagFile.initalize(tagName)
			fileopen = open('../source/tags/'+file);
			content = fileopen.readlines()
			content = [x.strip() for x in content]
			for eachContent in content:
				tagFile.add(eachContent)
			tagFile.footer(lastupdate)
			fileopen.close()

list_of_tags = set(list_of_tags)
#tag index file
tagIndexFile.initalize()
for tag in list_of_tags:
	tagIndexFile.add(tag)
tagIndexFile.footer(lastupdate)
