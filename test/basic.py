#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()
#session = Session(username="xxx",password="xxxx",host_base="xxxxx", region="xxxx", bucket="xxxx")

#/基础镜像/#
job_name="wjm-basic-train"
basic_estimator = Estimator(
                      modelmaker_session=session,
					  #/train information/#
                      framework=500100,                                               # AI引擎版本?
                      framework_type='BASIC_FRAMEWORK',                             # AI引擎版本?
					  #/train code/#
					  code_dir="/home/wangjm/wangjm12138_git/train.py",                          # 训练代码目录,s3路径?
                      boot_file="train.py",                						   # 训练启动脚本目录,s3路径？
					  #/output/
					  output_path="s3://aiteam/wjm_output/",			          # 训练输出位置，s3路径？
					  #/resource allocation/
					  train_instance_type=500200,                                     # 训练环境规格 resource_id
                      train_instance_count=1,                                       # 训练环境规格数量
                      volume_size=1)                                                 # 训练附加卷
basic_estimator.fit("s3://aiteam/mnist/data/", wait = True, logs = True, job_name=job_name)

basic_estimator.create_model(
                     model_name      = "basic-model",                    # 模型名称
                     model_version   = "1.1.1",                       # 模型版本
                     model_framework  = 500150,                      # 模型框架id
#                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
					 model_code_dir      = "s3://aiteam/mnist/code/", # 推理代码目录
#					 model_path = "s3://aiteam/wjm_output/V0001/",   #模型组件路径
                     model_boot_file     = "predict.py")              # 启动文件

#predictor_response = basic_estimator.deploy_predictor(
#						service_name  = "basic-predict",
#						service_type  = "ONLINE_SERVICE",
#                        service_models = [{"weight":100,"resourceId":500550,"instanceCount":1}])
