#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
#from modelmaker.predictor import Predictor

session = Session()
#session = Session(username="xxx",password="xxxx",host_base="xxxxx", region="xxxx", bucket="xxxx")
#session = Session(method="https")#31.5
#/s3 api/
#base_bucket_path="s3://aiteam"

#session.create_directory('aiteam/','wjm_test')
#session.upload_data('ai-team/final/','./3.txt')
#session.upload_data('ai-team/final/',['/home/wangjm/Final/modelmaker/upload_2','3.txt'])
session.upload_data('ai-team/wjm-imagenet/try/',['/home/wangjm2/wangjm12138git/modelmaker/test/try/make','/home/wangjm2/wangjm12138git/modelmaker/test/try/test2'])
#session.upload_data('ai-team/final/upload_2/a/b/','./3.txt')
#session.download_data('ai-team/wjm-imagenet/try/','/home/wangjm2/wangjm12138git/modelmaker/test/')
#session.download_data('ai-team/wjm-imagenet/train/train-00000-of-01024','/home/wangjm2/wangjm12138git/modelmaker/test/')
#session.download_data('ai-team/final/','/home/wangjm/Final/modelmaker/download')
#
#session.create_directory('ai-team/edfg/','upload')
#session.upload_data('ai-team/edfg/upload/','./3.txt')
#session.delete_directory('ai-team/edfg/','upload')

