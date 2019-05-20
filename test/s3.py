import sys
from boto3.session import Session
import boto3
import logging
from botocore.exceptions import ClientError

#对应上面的ak sk值
#/huadong/
#aws_key = 'f20df5431d074fbc67776c1fb352c209d8454532'
#aws_secret = 'abbeed54092489a87e5948c6cd17baaa2d6369a9'
#
#session = Session(aws_access_key_id=aws_key,
#		aws_secret_access_key=aws_secret, region_name='cn-south-1')
#s3 = session.resource('s3', endpoint_url='http://s3-cn-south-1.wcsapi.com')
#client = session.client('s3', endpoint_url='http://s3-cn-south-1.wcsapi.com')
#bucket = 'ai-team'
#file_obj = client.put_object(Bucket=bucket, Key='wjm_test/')


##region98
aws_key = 'e943f9ff9fb57488c4a3d2abeb87e6e25ec687c7'
aws_secret = 'c7cafd55a61c20277dba84f746897bc1a93476a4'
session = Session(aws_access_key_id=aws_key,
		aws_secret_access_key=aws_secret, region_name='region98')

#endpoint_url需要修改为上面的s3公网域名地址
s3 = session.resource('s3', endpoint_url='http://region98.s1.wcsapi.com')
client = session.client('s3', endpoint_url='http://region98.s1.wcsapi.com')

bucket = 'aiteam'
#file_obj = client.put_object(Bucket=bucket, Key='wjm_test/')

client.download_file(bucket, 'wjm_test/.temp', "tmp.txt")
#resp = client.list_objects(Bucket=bucket)['Contents']
#print(resp)




#import os
# 
#def mkdir_file(file_path):
#
#	path, file_name  = os.path.split(file_path)
#	folder = os.path.exists(path)
#	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
#		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
#	file1 = open(file_path,'w')
#	file1.close()

#file_path = "/home/wangjm/Final/modelmaker/download/b/a.txt"
#mkdir_file(file_path)       

#def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
#	paginator = client.get_paginator('list_objects')
#	for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
#		if result.get('CommonPrefixes') is not None:
#			for subdir in result.get('CommonPrefixes'):
#				download_dir(client, resource, subdir.get('Prefix'), local, bucket)
#		if result.get('Contents') is not None:
#			for file in result.get('Contents'):
#				if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
#					os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
#				resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))
#
#download_dir(client,s3,'/home/wangjm/Final/modelmaker/download','ai-team/edfg/upload_2')
#resp = client.list_objects(Bucket='ai-team',Prefix='edfg/upload_2')
#resp = client.list_objects(Bucket='ai-team', Prefix='edfg/upload_2/a/5.txt')
#client.get_object(Bucket='ai-team', Key='edfg/upload_2/a/')
#with 
#client.download_file('ai-team', 'edfg/upload_2/a/5.txt', "./download/5.txt")
#for obj in resp['Contents']:
#	print(obj['Key'])
#	file_path = os.path.join('./download', obj['Key'])
#	mkdir_file(file_path)

#bucket = s3.Bucket('ai-team')
#object1=s3.Object('ai-team','abc')
#k.set_contents_from_string('')
#往存储空间wjm-test上传本地的1.txt文件
#response = client.list_buckets()
#
#for bucket in response['Buckets']:
#		print(f'  {bucket["Name"]}')


#for bucket in s3.buckets.all():
#		print(bucket.name)
#try:
#client.create_bucket(Bucket="ai2")
#except ClientError as e:
#	logging.error(e)
#	return False
#return True


#bucket = 'ai-team'
#objkey = '4.txt'
#data = open('3.txt', 'rb')

#file_obj = client.put_object(Bucket=bucket, Key='edfg/'+objkey,Body=data)
#file_obj = client.put_object(Bucket=bucket, Key='wang_folder/wang2/')
#file_obj = client.put_object(Bucket=bucket, Key='eeee/abc/')
#file_obj = s3.Bucket(bucket).put_object(Key='bcd/3.txt', Body=data)
#d_file_obj =client.delete_object(Bucket=bucket,Key='bcd/')
#file_obj = s3.Bucket(bucket).put_object(Key='abc/')
#
##下载存储空间wjm-test上面的1.txt文件，保存为tmp.txt
#client.download_file(bucket, objkey, "tmp.txt")

