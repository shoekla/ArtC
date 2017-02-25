

import urllib2
import re
import nltk
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
def is_in_arr(lis,s):
	result=False
	for item in lis:
		if item==s:
			result=True
	return result
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis

def getData(url):
	try:

		regex='<p>(.+?)</p>'
		headers='Info In Paragrapgh'

		pattern = re.compile(regex);
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		title=re.findall(pattern,htmltext)
		if len(str(title))>=1:
			return title
		else:
			return "nothing"
	except:
		print "Data Error At "+str(url)

def getName(url):

	regex='<title>(.+?)</title>'
	headers='Title:'
	pattern = re.compile(regex);
	htmlfile=urllib2.urlopen(url)
	htmltext=htmlfile.read()
	title=re.findall(pattern,htmltext)
	for college in colleges:
		if college in str(title):
			str(title).replace(college,"")
	return title

def getGoodLink(url):
	k = url.rfind("/")
	return url[:k+1]
def getHTML(url):
	try:
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		htmltext.replace("<!Doctype html>","")
		htmltext.replace("<html","")
		htmltext.replace("</html>","")
		tokens = nltk.word_tokenize(htmltext)
		return tokens
	except:
		return "Error Occured"
#nltk.download()
def checkNum(num):
	num=num[7:]
	if len(num)==10:
		for item in num:
			if str(item).isalpha():
				return False
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				return False
			else:
				return True
	elif len(num)==12:
		d=0
		first=num[:3]
		second=num[4:7]
		third=num[8:13]
		for item in first:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		for item in second:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		for item in third:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		if d==0:
			return True
		else:
			return False
	else:
		return False

def getPhone(url):
	try:
		tokens=getHTML(url)
		nums=[1,2,3,4,5,6,7,8,9,0]
		contacts=[]
		string=""

		for i in range(0,len(tokens)):
			item=tokens[i]
			if len(item)==10:
				number=True

				if item.isalpha():
					number=False

				if item[3:6]=="555":
					number=False

				if str(item[0])!="1" or str(item[0])!="2" or str(item[0])!="3" or str(item[0])!="4" or str(item[0])!="5" or str(item[0])!="6" or str(item[0])!="7" or str(item[0])!="8" or str(item[0])!="9" or str(item[0])!="0":
					number=False
				if number==True and item not in contacts:
					contacts.append(item)
			if len(item)==12:
				number=True
				"""
				if item[3]!= "-" or item[7]!="-":
					if item[3]!="." or item[7]!=".":
						number=False
				"""
				if str(item[0]).isalpha() or str(item[1]).isalpha() or str(item[2]).isalpha() or str(item[3]).isalpha() or str(item[4]).isalpha() or str(item[5]).isalpha() or str(item[6]).isalpha() or str(item[7]).isalpha() or str(item[8]).isalpha() or str(item[9]).isalpha() or str(item[10]).isalpha() or str(item[11]).isalpha():
					number=False
				if item[4:7]=="555":
					number=False

				if number==True and item not in contacts:
					if "Fax" in tokens[i-2]:
						contacts.append("Fax: "+item)
					else:
						contacts.append("Phone: "+item)
			resCon=[]
			for item in contacts:
				if checkNum(str(item)):
					resCon.append(item)
		return resCon
	except:
		return "Error Occured"

def getEmail(url):
	try:
		tokens=getHTML(url)
		contacts=[]
		for i in range(0,len(tokens)):
			if "@" in tokens[i]:
				string= str(tokens[i-1])
				if string[0].isalpha():
					string = string +str(tokens[i])
					string = string +str(tokens[i+1])
					endA=str(tokens[i+1])
					if endA.find(".")>=0:
						if is_in_arr(contacts,tokens[i])==False:
							if string.endswith(".")==False:
								contacts.append(string)
			if "at"==tokens[i]:
				if tokens[i-1]=="[" and tokens[i+1]=="]":
					string=str(tokens[i-2])+"@"+str(tokens[i+2])
					contacts.append(string)
			if len(tokens[i])==3:
				if tokens[i].isalpha==False:
					if (tokens[i+1].isalpha==False and len(tokens[i+1])==3) and (tokens[i+2].isalpha()==False and len(tokens[i+2])==3) and item not in contacts:
						string = str(tokens[i]) +str(tokens[i+1])+str(tokens[i+2])
						contacts.append("Email: "+string)
		new = deleteDuplicates(contacts)
		return new
	except:
		return "Error Occured"

def crawl(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test:
					if href_test.startswith("http"):
						if href_test not in pages:
							pages.append(str(href))
					else:
						lin=getGoodLink(url)
						if (lin+str(href)) not in pages:
							pages.append(lin+str(href))

	except:
		print "Error at: "+str(url)
def getPaintingYear(soup):
	for link in soup.findAll('p'):
		if str(link).startswith("<p title="):
			pa = str(link)
			pa = pa.replace(")","").replace(".","")
			arr = pa.split(" ")
			for i in arr:
				if i.isdigit() and len(i) == 4:
					return int(i)
#print getPaintingYear("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/A?Open&A=5ZKEMD")

def getPaintingTitle(soup):
	for link in soup.findAll('h1'):
		a = str(link)
		return a[a.find(">")+1:a.find("</h1>")].strip().replace('"',"")
def getPaintingUrl(soup):
	for link in soup.findAll('img',attrs={"class":"zoomImg"}):
		s="http://en.most-famous-paintings.com"
		a = str(link)
		beg = a.find('src="')
		return s+a[beg:a.find('"',beg+5)]
def getPaintingArtist(url):
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	title = getPaintingTitle(soup)
	for link in soup.findAll('h2'):
		a = str(link)
		a = a[a.find(">")+1:a.find("</h1>")].strip().replace('"',"")
		return a[:a.find("-")]
def getPaintingInfo(url):
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	title = getPaintingTitle(soup)
	if title == None:
		return None
	#print title
	artist = getPaintingArtist(soup)
	if artist == None:
		return None
	#print artist
	year = getPaintingYear(soup)
	if year == None:
		return None
	#print title+" "+artist+" "+str(year)
	return [title,artist,year]

pages = []
artists = []
count = 0
crawl("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/ListOfTop1000MostPopularPainting?OpenForm",pages)
for i in pages:
	if "Open&A" in i:
		a = getPaintingArtist(i)
		a = a.replace("</h","")
		if a != None and a not in artists:
			print a
			artists.append(a)
			count = count + 1
			if count > 200:
				break
print artists
#getPaintingInfo("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/A?Open&A=8XYFFG")
#print getPaintingArtist("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/A?Open&A=8XYFFG")
def crawlImg(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('img'):

			href=link.get('src')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "1.1" in href:
					pages.append(href)


	except:
		print "Error at: "+str(url)
import pyrebase

config = {
  "apiKey": "AIzaSyDbBdcTPairEDTvEZF_5Gri6AlsBWmukmw",
  "authDomain": "artc-82804.firebaseapp.com",
  "databaseURL": "https://artc-82804.firebaseio.com",
  "storageBucket": "artc-82804.appspot.com"

}

db.child("artists").push(str(artists))
print "Done!"



































