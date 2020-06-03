import XmlDictConfig as xdc
from SearchKey import SearchKey as sk
import xml.etree.ElementTree as ET
from CreateTable import CreateTable as ct
import collections 
# import xmltodict


# Converting the xml file to dictionaries
class PipeLine:
	# XmlDictConfig = newnw
	def __init__(self):
		pass


	def transforming(self):
		tree = ET.parse(
			'G:/My Drive/Sanket/Project/Twitter-api/test/extracted/tar/I20200107/UTIL10524/US10524999-20200107/US10524999-20200107.xml')
		root = tree.getroot()
		xmldict = xdc.XmlDictConfig(root)
		return xmldict

	def searching(self, xmldict,key):
		
		#print("xml dict: ", xmldict)
		sk.recSearchKey(sk,xmldict,key)

		#print("test data: ",sk.testData)
		# print("Key Found = ",requiredKeyVal)

		return sk.testData

	# def flatten(data,sep = ""):
	# 	obj = collections.dict()

	# 	def recurse(t,parent_key = " "):
	# 		if isintance(t,list):
	# 			for i in range(len(t))




if __name__ == '__main__':
	key = input("Enter the value you want to insert into the Table: ")
	pipe = PipeLine()
	xmlDict = pipe.transforming()
	data = pipe.searching(xmlDict,key)
	cloudtb = ct.createquery(ct,key, data,'US10524999-20200107')
