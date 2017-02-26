

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
		if item.strip() not in newLis:
			newLis.append(item.strip())
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
def getPhoneNumberForMueseum(loc):
	loc = loc.replace(" ","%20")
	url = "http://www.bing.com/search?q=art%20museum%20in%20"+loc+"&qs=n&form=QBRE&sp=-1&pq=art%20museum%20in%20"+loc+"&sc=0-24&sk=&cvid=35B371D5F8904D80B7D7E80EDCB66D7C"
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('div',attrs={"class":"b_factrow"}):
		a = str(link)
		if '<div class="b_factrow">' in a:
			if '<span' not in a:
				sentence = a[a.find(">")+1:a.find("\xc2\xb7")]
				beg = a.find("(")
				num = a[beg:a.find("</div>")]
				res = ""
				for i in num:
					if i.isdigit():
						res = res+i
				return res,sentence
	return url
print getPhoneNumberForMueseum("Katy Texas")
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
		return s+a[beg:a.find('"',beg+6)].replace('src="',"")

def getPaintingArtist(soup):
	for link in soup.findAll('h2'):
		a = str(link)
		a = a[a.find(">")+1:a.find("</h1>")].strip().replace('"',"")
		return a[:a.find("-")].strip()


def getPaintingInfo(soup):

	artist = getPaintingArtist(soup)
	if artist == None:
		return None
	#print artist
	year = getPaintingYear(soup)
	if year == None:
		return None
	#print title+" "+artist+" "+str(year)
	artists = ['Leonardo Da Vinci', 'Vincent Van Gogh', 'Edvard Munch', 'Pablo Picasso', 'Jan Vermeer', 'Rembrandt Van Rijn', 'Gustav Klimt', 'Claude Monet', 'Georges Pierre Seurat', 'Grant Wood', 'James Abbott Mcneill Whistler', 'Rene Magritte', 'Pierre', 'Edouard Manet', 'Caspar David Friedrich', 'Francisco De Goya', 'Michelangelo Buonarroti', 'Raphael (Raffaello Sanzio Da Urbino)', 'Henri Matisse', 'Joan Miro', 'Andrea Mantegna', 'Max Beckmann', 'Caravaggio (Michelangelo Merisi)', 'Diego Velazquez', 'Rose Maynard Barton', 'Jackson Pollock', 'Paul Gauguin', 'Arshile Gorky', 'Paul Cezanne', 'Giuseppe Arcimboldo', 'Albrecht Durer', 'Emile Nolde', 'Suzanne Valadon', 'Gustave Caillebotte', 'Salvador Dali', 'Wassily Kandinsky', 'Jean Joseph Benjamin Constant', 'August Macke', 'Georges Braque', 'Pieter Bruegel The Younger', 'Jean Antoine Watteau', 'Henri Rousseau', 'Jean Frederic Bazille', 'Lucian Freud', 'Pavel Filonov', 'Robert Delaunay', 'Sandro Botticelli', 'Matthias Gr\\xc3\\xbcnewald', 'Marc Chagall', 'Ernst Ludwig Kirchner', 'Georgios Jakobides', 'Marcel Duchamp', 'Frida Kahlo', 'Paul Delvaux', 'Egon Schiele', 'Oskar Kokoschka', 'Bernardo Bellotto', 'Amedeo Modigliani', 'Albert Bierstadt', 'Umberto Boccioni', 'Albert Charles Lebourg', 'Edward Hopper', 'Edgar Degas', 'Giovanni Antonio Canal (Canaletto)', 'Denis Maurice', 'Giorgio De Chirico', 'Otto Dix', 'Camille Pissarro', 'William Holman Hunt', 'William Merritt Chase', 'Mary Stevenson Cassatt', 'Frederick Childe Hassam', 'Fernand Leger', 'Agnolo Bronzino', 'Paul Signac', 'Franz Marc', 'William Turner', 'Jean', 'Juan Gris', 'Max Ernst', 'Max Liebermann', 'John Singer Sargent', 'Alfred Sisley', 'Domenico Campagnola', 'Yves Tanguy', 'Balthus (Balthasar Klossowski)', 'Francis Picabia', 'El Greco (Dom\\xc3\\xa9nikos Theotokopoulos)', 'John Everett Millais', "Georgia O'keeffe", 'Arnold Bocklin', 'Paolo Veronese', 'Bernardo Strozzi', 'John Singleton Copley', 'Gustave Courbet', 'Gerard David', 'John William Waterhouse', 'Winslow Homer', 'Eug\\xc3\\xa8ne Delacroix', 'George Stubbs', 'Andy Warhol', 'Tiziano Vecellio (Titian)', 'Francis Bacon', 'Jan Matejko', 'Benjamin West', 'William Adolphe Bouguereau', 'Pieter Bruegel The Elder', 'Alexandre Cabanel', 'Berthe Morisot', 'Ivan Ivanovich Shishkin', 'Lawrence Alma', 'Jean L\\xc3\\xa9on G\\xc3\\xa9r\\xc3\\xb4me', 'Thomas Cole', 'Edwin Lord Weeks', 'Nicolas Poussin', 'Peter Paul Rubens', 'Annibale Carracci', 'John Atkinson Grimshaw', 'John Constable', 'Mark Rothko (Marcus Rothkowitz)', 'Barnett Newman', 'Hans Memling', 'Frans Snyders', 'Pieter De Hooch', 'John Henry Twachtman', 'Albert Edelfelt', 'Albrecht Altdorfer', 'Aurelio Arteta', 'George Grosz', 'Jacopo Carucci (Pontormo)', 'Frederic Edwin Church', 'Tom Wesselmann', 'Thomas Hart Benton', 'Lovis Corinth (Franz Heinrich Louis)', 'Phillip Leslie Hale', 'Jean Theodoor Toorop', 'Franz Xaver Winterhalter', 'Theodore Clement Steele', 'Willard Leroy Metcalf', 'Charles Fran\\xc3\\xa7ois Daubigny', 'Ivan Aivazovsky', 'Giovanni Battista Tiepolo', 'Giovanni Bellini', 'Tamara De Lempicka', 'Giorgione (Giorgio Barbarelli Da Castelfranco)', 'Paul Delaroche (Hippolyte Delaroche)', 'Jacob Jordaens', 'Jasper Johns', 'Hieronymus Bosch', 'Sebastiano Ricci', 'David Hockney', 'Robert Rauschenberg', 'Peter Max', 'Paolo Uccello', 'Ilya Yefimovich Repin', 'Giotto Di Bondone', 'Roy Lichtenstein', 'Jan Van Eyck', 'Rogier Van Der Weyden', 'Anthony Van Dyck', 'Fernand Edmond Jean Marie Khnopff', 'Geertgen Tot Sint Jans', 'Katsushika Hoki', 'Hans Holbein The Younger', 'Thomas Eakins', 'Piero Della Francesca', 'Luca Signorelli', 'Parmigianino', 'Gentile Bellini', 'Lucas Cranach The Elder', 'Tintoretto (Jacopo Comin)', 'Richard Lindner', 'Rosso Fiorentino', 'Jan Brueghel The Elder', 'Georges De La Tour', 'Richard Hamilton']
	data = [year]
	for i in artists:
		if i == artist:
			data.append(1)
		else:
			data.append(0)
	return data
"""
pages = []

titles = []
urls = []
alldata = []
count = 0
crawl("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/ListOfTop1000MostPopularPainting?OpenForm",pages)
for i in pages:
	if "Open&A" in i:
		try:
			source_code=requests.get(i)
			plain_text=source_code.text
			soup=BeautifulSoup(plain_text)
			title = getPaintingTitle(soup)
			if title == None:
				continue
			url = getPaintingUrl(soup)
			if url == None:
				continue
			data = getPaintingInfo(soup)
			if data == None:
				continue
			urls.append(url)
			titles.append(title)
			alldata.append(data)
			print title+" added!"
			count = count+1
			if count > 170:
				break

		except:
			print "error ar "+i
print titles
print "\n\n\n"
print urls
print "\n\n\n\n\n"
print alldata

#print artists

#getPaintingInfo("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/A?Open&A=8XYFFG")
#print getPaintingArtist("http://en.most-famous-paintings.com/MostFamousPaintings.nsf/A?Open&A=8XYFFG")

import pyrebase

config = {
  "apiKey": "AIzaSyDbBdcTPairEDTvEZF_5Gri6AlsBWmukmw",
  "authDomain": "artc-82804.firebaseapp.com",
  "databaseURL": "https://artc-82804.firebaseio.com",
  "storageBucket": "artc-82804.appspot.com"

}

#arr = ['Leonardo Da Vinci ', 'Vincent Van Gogh ', 'Edvard Munch ', 'Pablo Picasso ', 'Jan Vermeer ', 'Rembrandt Van Rijn ', 'Gustav Klimt ', 'Claude Monet ', 'Georges Pierre Seurat ', 'Grant Wood ', 'James Abbott Mcneill Whistler ', 'Rene Magritte ', 'Pierre', 'Edouard Manet ', 'Caspar David Friedrich ', 'Francisco De Goya ', 'Michelangelo Buonarroti ', 'Raphael (Raffaello Sanzio Da Urbino) ', 'Henri Matisse ', 'Joan Miro ', 'Andrea Mantegna ', 'Max Beckmann ', 'Caravaggio (Michelangelo Merisi) ', 'Diego Velazquez ', 'Rose Maynard Barton ', 'Jackson Pollock ', 'Paul Gauguin ', 'Arshile Gorky ', 'Paul Cezanne ', 'Giuseppe Arcimboldo ', 'Albrecht Durer ', 'Emile Nolde ', 'Suzanne Valadon ', 'Gustave Caillebotte ', 'Salvador Dali ', 'Wassily Kandinsky ', 'Jean Joseph Benjamin Constant ', 'August Macke ', 'Georges Braque ', 'Pieter Bruegel The Younger ', 'Jean Antoine Watteau ', 'Henri Rousseau ', 'Jean Frederic Bazille ', 'Lucian Freud ', 'Pavel Filonov ', 'Robert Delaunay ', 'Sandro Botticelli ', 'Matthias Gr\xc3\xbcnewald ', 'Marc Chagall ', 'Ernst Ludwig Kirchner ', 'Georgios Jakobides ', 'Marcel Duchamp ', 'Frida Kahlo ', 'Paul Delvaux ', 'Egon Schiele ', 'Oskar Kokoschka ', 'Bernardo Bellotto ', 'Amedeo Modigliani ', 'Salvador Dali', 'Albert Bierstadt ', 'Umberto Boccioni ', 'Albert Charles Lebourg ', 'Edward Hopper ', 'Edgar Degas ', 'Giovanni Antonio Canal (Canaletto) ', 'Denis Maurice ', 'Giorgio De Chirico ', 'Otto Dix ', 'Camille Pissarro ', 'William Holman Hunt ', 'William Merritt Chase ', 'Mary Stevenson Cassatt ', 'Frederick Childe Hassam ', 'Fernand Leger ', 'Agnolo Bronzino ', 'Paul Signac ', 'Franz Marc ', 'Pablo Picasso', 'William Turner ', 'Jean', 'Juan Gris ', 'Claude Monet', 'Max Ernst ', 'Edouard Manet', 'Max Liebermann', 'Ernst Ludwig Kirchner', 'John Singer Sargent ', 'Alfred Sisley ', 'Domenico Campagnola ', 'Yves Tanguy ', 'Balthus (Balthasar Klossowski) ', 'Francis Picabia ', 'El Greco (Dom\xc3\xa9nikos Theotokopoulos) ', 'John Everett Millais ', "Georgia O'keeffe ", 'Giorgio De Chirico', 'Arnold Bocklin ', 'Paolo Veronese ', 'Bernardo Strozzi ', 'Edgar Degas', 'John Singleton Copley ', 'Gustave Courbet ', 'Gerard David ', 'John William Waterhouse ', 'Winslow Homer ', 'Eug\xc3\xa8ne Delacroix ', 'George Stubbs ', 'Andy Warhol', 'Tiziano Vecellio (Titian) ', 'Francis Bacon ', 'Jan Matejko ', 'Benjamin West ', 'William Adolphe Bouguereau ', 'Pieter Bruegel The Elder ', 'Alexandre Cabanel ', 'Berthe Morisot ', 'Ivan Ivanovich Shishkin ', 'Albert Charles Lebourg', 'Lawrence Alma', 'Jean L\xc3\xa9on G\xc3\xa9r\xc3\xb4me ', 'Thomas Cole ', 'Edwin Lord Weeks ', 'Nicolas Poussin ', 'Peter Paul Rubens ', 'Annibale Carracci ', 'John Atkinson Grimshaw', 'John Constable ', 'Mark Rothko (Marcus Rothkowitz) ', 'Barnett Newman ', 'Hans Memling ', 'Frans Snyders', 'Pieter De Hooch ', 'John Henry Twachtman ', 'Albert Edelfelt ', 'Albrecht Altdorfer ', 'Aurelio Arteta', 'George Grosz ', 'Jacopo Carucci (Pontormo)', 'Frederic Edwin Church ', 'Tom Wesselmann', 'Thomas Hart Benton', 'Lovis Corinth (Franz Heinrich Louis) ', 'Phillip Leslie Hale ', 'Jean Theodoor Toorop ', 'Franz Xaver Winterhalter ', 'Theodore Clement Steele', 'Willard Leroy Metcalf ', 'Charles Fran\xc3\xa7ois Daubigny ', 'John Atkinson Grimshaw ', 'Ivan Aivazovsky ', 'Giovanni Battista Tiepolo ', 'Theodore Clement Steele ', 'Giovanni Bellini ', 'Tamara De Lempicka ', 'Giorgione (Giorgio Barbarelli Da Castelfranco) ', 'Paul Delaroche (Hippolyte Delaroche) ', 'Jacob Jordaens ', 'Francis Bacon', 'Jasper Johns ', 'Jasper Johns', 'Mark Rothko (Marcus Rothkowitz)', 'Hieronymus Bosch ', 'Sebastiano Ricci ', 'Gustav Klimt', 'David Hockney', 'Grant Wood', 'Robert Rauschenberg', 'Peter Max', 'Paolo Uccello', 'Sandro Botticelli', 'Ilya Yefimovich Repin ', 'Giotto Di Bondone ', 'Roy Lichtenstein ', 'Jan Van Eyck ', 'Jan Van Eyck', 'Rene Magritte', 'Rogier Van Der Weyden ', 'Anthony Van Dyck ', 'Rembrandt Van Rijn', 'Fernand Edmond Jean Marie Khnopff', 'Peter Paul Rubens', 'Geertgen Tot Sint Jans ', 'Katsushika Hoki ', 'Paolo Uccello ', 'Hans Holbein The Younger ', 'Thomas Eakins ', 'Piero Della Francesca ', 'Piero Della Francesca', 'Paul Cezanne', 'Luca Signorelli ', 'Hans Memling', 'Parmigianino ', 'Gentile Bellini ', 'Lucas Cranach The Elder ', 'Tintoretto (Jacopo Comin) ', 'Richard Lindner', 'Rosso Fiorentino', 'Jan Brueghel The Elder ', 'Georges De La Tour ', 'David Hockney ', 'Richard Hamilton']
#newArr = deleteDuplicates(arr)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#db.child("artists").push(str(newArr))
#print "Done!"
db.child("titless").push(str(titles))
db.child("urlss").push(str(urls))
db.child("dataImgs").push(str(alldata))
def getData(name):
	movie = db.child(name).get()
	s = str(movie.val())
	if s.startswith("OrderedDict") == False:
		return s
	return s

#arr = eval(getData("artistsNames"))
#print len(arr)



"""



















