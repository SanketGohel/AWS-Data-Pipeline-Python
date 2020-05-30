import XmlDictConfig
import XmlListConfig
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter  = logging.Formatter('%(asctime)s: %(filename)s: %(levelname)s: %(message)s')
# file_handler = logging.FileHandler('SearchKey.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

#Extracting the( values from the dictionaries and storing in the varaible testData{} 
class SearchKey:

	flag = False
	testData= {}

	#print(xmldict)

	def __getitem__(self, xmldict, key):
		return xmldict.__getitem__(key)


	def recSearchKey(self, xmldict, key):
		#global flag, testData
		#print("type of root: ", type(xmldict))
		#print("keys: ", xmldict.keys())
		if type(xmldict) is XmlDictConfig.XmlDictConfig or type(xmldict) is dict:
			#print("keys in dict: ", xmldict.keys())
			if key in xmldict.keys():
				#print("first If ",key)
				#testData = xmldict.values()

				SearchKey.flag = True
				return key
				#return str("key found")
			else:
				#print("Inside else",key)
				for i in xmldict.values():
					if (type(i) is XmlDictConfig.XmlDictConfig or type(i) is XmlListConfig.XmlListConfig or type(i) is dict) and not SearchKey.flag:
						#print(" if dictionary: ", type(i))
						tester = SearchKey.recSearchKey(SearchKey,i,key)
						#print("I: Tester: ",tester)
						if(tester == key):
							#print("I1: TEST: ", tester)
							SearchKey.testData = xmldict
							#print("Test:", SearchKey.testData)
							#return SearchKey.testData
						
		elif type(xmldict) is XmlListConfig.XmlListConfig:
			#print("list: ", xmldict)
			if key in xmldict:
				SearchKey.flag = True
				#testData = xmldict.values()
				#return "List exists"
			else:
				#print("in list: ", xmldict)
				for i in xmldict:
					if (type(i) is XmlDictConfig.XmlDictConfig or type(i) is XmlListConfig.XmlListConfig or type(i) is dict) and not SearchKey.flag:
						#print(" if dictionary: ", type(i))
						tester = SearchKey.recSearchKey(SearchKey, i, key)
						#print("I2: Tester: ",tester)
						if(key == tester):
							#print("I2: TEST2: ", key)
							#print("I2: TEST2: ", xmldict)
							SearchKey.testData = xmldict
							#print("Test1:", SearchKey.testData)
							#return SearchKey.testData


		#return SearchKey.testData