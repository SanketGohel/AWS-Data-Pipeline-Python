# import logging
#from Foratting.XmlDictConfig import XmlDictConfig

import XmlDictConfig
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter  = logging.Formatter('%(asctime)s: %(filename)s: %(levelname)s: %(message)s')
# file_handler = logging.FileHandler('XmlListConfig.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)



class XmlListConfig(list):
	def __init__(self, aList):
		for element in aList:
			if element:
				# treat like dict
				if len(element) == 1 or element[0].tag != element[1].tag:
					self.append(XmlDictConfig.XmlDictConfig(element))
					# treat like list
				elif element[0].tag == element[1].tag:
					self.append(XmlListConfig(element))
			elif element.text:
				text = element.text.strip()
				if text:
					self.append(text)
			
		#logger.debug('Element {} need to be fixed'.format(element))

