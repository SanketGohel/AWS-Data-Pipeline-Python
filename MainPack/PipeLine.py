import XmlDictConfig
from SearchKey import SearchKey as sk
import xml.etree.ElementTree as ET
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
		xmldict = XmlDictConfig.XmlDictConfig(root)
		return xmldict

	def searching(self, xmldict):
		key = input("Enter the value you want to insert into the Table: ")

		#print("xml dict: ", xmldict)
		sk.recSearchKey(sk,xmldict,key)
		print("test data: ",sk.testData)
		# print("Key Found = ",requiredKeyVal)

		return sk.testData

if __name__ == '__main__':
	pipe = PipeLine()
	xmlDict = pipe.transforming()
	data = pipe.searching(xmlDict)
