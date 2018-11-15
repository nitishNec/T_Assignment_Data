import os
import sys
import boto3
import botocore

# Some Variables defined which will used in uploads and downloads of s3
Name_of_File_after_Downloads_from_S3 = "Downloads_someFile.txt5"
BucketName = "abh14343"
Upload_key = "/home/shopclues/someFile.txt"
Downloads_Key = "someFile.txt"
Name_of_File_after_Uploads_On_S3 = "someFile.txt"

#Uploading the file to S3 bucket 
def Upload_file_to_S3():

	s3 = boto3.client('s3')
	try:
		s3.upload_file(Upload_key,BucketName,Name_of_File_after_Uploads_On_S3)
	except botcore.exception.ClientError as e:
		if e.response['Error']['Code'] == "403":
			print ("Access Denied Problem")
		else:
			raise


#Dowloading the file from S3 bucket
def Downloads_file_from_S3():
	s3 = boto3.resource('s3')
	try:
		s3.Bucket(BucketName).download_file(Downloads_Key, Name_of_File_after_Downloads_from_S3)
	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code'] == "404":
			print("The object does not exist.")
		else:
        		raise

#Calling the Uploads function
Upload_file_to_S3()

#Calling Downloads Function
Downloads_file_from_S3()
