#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
#from modelmaker.predictor import Predictor

#session = Session()
session = Session(username="cdy",password="cyd@Pass1",iam_server="172.16.14.201:9048/mmr")
#session = Session(method="https")#31.5
#/s3 api/
#base_bucket_path="s3://aiteam"

#session.create_directory('aiteam/','wjm_test')
#session.upload_data('ai-team/final/','./3.txt')
#session.upload_data('ai-team/final/',['/home/wangjm/Final/modelmaker/upload_2','3.txt'])
#session.upload_data('ai-team/final/upload_2/a/b/','./3.txt')
#session.download_data('ai-team/final/upload_2/a/5.txt','/home/wangjm/Final/modelmaker/download')
#session.download_data('ai-team/final/upload_2/a/','/home/wangjm/Final/modelmaker/download')
#session.download_data('ai-team/final/','/home/wangjm/Final/modelmaker/download')
#
#session.create_directory('ai-team/edfg/','upload')
#session.upload_data('ai-team/edfg/upload/','./3.txt')
#session.delete_directory('ai-team/edfg/','upload')

