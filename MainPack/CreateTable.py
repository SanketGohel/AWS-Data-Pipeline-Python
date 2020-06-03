import boto3
import json
from pprint import pprint
 

class CreateTable:

	def fatten(self,d):
		obj = dict()

		def recursion(d,parent_key = ""):

			

			if isinstance(d,dict):
				for k,v in d.items():
					recursion(v,k if parent_key else k)
			else:
				obj[parent_key] = d

		recursion(d)

		return obj

	def createquery(self,key,testData,filename):
		try:

			#Instaniate your dynamoDB client object
			client = boto3.client('dynamodb')
			dynamodb = boto3.resource('dynamodb')
	         #Get an array of table name associated with the current account and endpoint
			existing_table = client.list_tables()['TableNames']
			print('Key : ',existing_table)
			#existing_table = client.describe_table(TableName = key)
			if key in existing_table:
				#print('inside if')
				table_found = True
				print('Table Found', key)
			else:

				table_found = False
				print('Table not  Found', key)
				
				
				#if key not in existing_table:
				#print('Inside else', key)
				table = dynamodb.create_table(
					TableName = key,
					KeySchema = [
						{
							'AttributeName' : 'filename',
							'KeyType': 'HASH'	
						},

						{
							'AttributeName' : 'num',
							'KeyType' : 'RANGE'	
						}
					],
					AttributeDefinitions = [
						{
							'AttributeName': 'filename',
							'AttributeType': 'S'
						},
						{
							'AttributeName': 'num',
							'AttributeType': 'S'
						},
						
						#print('Creating table: ', table_name),
					],
					ProvisionedThroughput = 
					{
						'ReadCapacityUnits' : 5,
						'WriteCapacityUnits': 5
					}
					#TableName = table_name,
				)
				print('table Created', key)
				table.meta.client.get_waiter('table_exists').wait(TableName = key)
			#return table_found

			print("Entering loop:")
			for i in testData:
				items = CreateTable.fatten(self, i) 
				#it = json.dumps(temp)
				#pprint(temp,indent = 2)
				#print("inside for loop", i)
				
				#for k,v in temp.items():
					#print("k:",k," v: ",v)
				#	items[k] = v			
				#print("Inserting the values: ", temp)
				#print("json: ",it)

				items['filename'] = filename

				#items['name'] = items['doc-number']

				print("items: ", items)
				table = dynamodb.Table(key)

				response = table.put_item(
					Item= items

				)				
				





		except Exception as e:

			print(e)

		# except ItemCollectionSizeLimitExceededException:
		# 	print('')



			



	
