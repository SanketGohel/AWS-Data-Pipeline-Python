import requests
import re
import httplib2
import os
from bs4 import BeautifulSoup, SoupStrainer
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from tarfile import TarFile
import urllib.request as reqobj
import os.path
from os import path


#Checking for the existing file
def file_check(filename):
	print(filename.split(".")[1])
	if path.exists("G:/My Drive/Sanket/Project/Twitter-api/test/extracted/" + filename.split(".")[1] +"/" + filename):
		print("File exists")
		return True
	else:
		print("Does not exists")
		return False



path = 'G:/My Drive/Sanket/Project/Twitter-api/test/extracted/'
download_link = []
http = httplib2.Http()
status,response = http.request("https://bulkdata.uspto.gov/")

#Forloop for scraping the links from the website
for link in BeautifulSoup(response, parse_only = SoupStrainer('a'), features = "html.parser"): #Feching the URLs  
	if link.has_attr('href'):#checking for "href" in the url
		if "Patent Grant Data/XML Version" in link.text or "Patent Grant Full Text Data/XML" in link.text:
			stat,resp = http.request(link['href'])
			for d_link in BeautifulSoup(resp, parse_only = SoupStrainer('a'), features = "html.parser"):
				if d_link.has_attr('href'):
					if (".zip"  in d_link['href']) or (".tar"  in d_link['href']):
						download_link.append(link['href'] + "/" + d_link['href'])

#print(download_link[0])
#Creating loop for two different file format .zip and .tar

#Fetching and downloading .zip fie
for op_link in download_link:
	path += op_link.split("/")[-1][1:]
	if ".zip" in op_link:
		with urlopen("" + op_link) as zipresp:
			print("Inside for loop")
			filename = op_link.split('/')[-1]
			print(filename)
			z_file= open(filename,'wb') #temp
			l = zipresp.readline(900000)
			print("first read")
			counter = 0
			while (len(l) != 0):
				z_file.write(l)
				print("After write");
				print(counter)
				reqobj.urlcleanup()
				l = zipresp.readline(900000)
				counter += 1
			z_file.extractall('extracted/zip/')
#Fetching and downloading .tar fie
	if ".tar" in op_link:
		path += op_link.split("/")[-1][1:]
		print("Inside TAR")
		with urlopen("" + op_link) as tarresp:
			print("Inside for loop")
			filename = op_link.split('/')[-1]
			if file_check(filename) == False:	
				print(filename)
				t_file= open(path + filename,'wb') #temp
				l = tarresp.readline(900000)
				print("first read")
				counter = 0
				while (len(l) != 0):
					t_file.write(l)
					print("After write");
					print(counter)
					reqobj.urlcleanup()
					l = tarresp.readline(900000)
					counter += 1
				t_file.close()
			t_file = TarFile(path + filename, "r")
			print("Extracting")
			t_file.extractall('extracted/tar/')
			
    

            #print("Inside ZIP")
		
	
	