#-*-coding:utf-8-*-
import sys
from modelmaker.session import Session
#from modelmaker.estimator import Estimator
#from modelmaker.model import Model
#from modelmaker.predictor import Predictor

session = Session()
#session = Session(username="cdy", password="cyd@Pass1", iam_server="http://172.16.14.201:9048/mmr")

#####/自定义镜像/#
#job_name="wjm-custom-train2"
#custom_estimator = Estimator(
#                      modelmaker_session=session,
#					  #/train information/#
#                      framework_type='CUSTOM',                                      # 框架类型用户自定义
#					  user_image_url='172.16.14.172/test/custom:v1.0',              # 用户自定义镜像地址
#					  #/train input/#
#					  user_command="/bin/bash",                                # 用户命令
#					  user_command_args="/home/test/start.sh",                            # 用户命令参数
#					  monitors=[{r'name':r'accuracy',r'regular':r'.*?accuracy\s=\s(.*)',r'sample':r'.*?loss\s=\s(.*)\s,\sstep\s=\s(.*)'}],   # 训练监控指标
#					  #/output/
#					  output_path="s3://aiteam/wjm_output/V0001/",                  # 训练输出位置，s3路径？
#					  #/resource allocation/
#					  train_instance_type=500050,                                     # 训练环境规格 resource_id
#                      train_instance_count=1,                                       # 训练环境规格数量
#                      volume_size=1)                                                 # 训练附加卷
#
#custom_estimator.fit(inputs=None, wait = False, logs = False, job_name=job_name)
#custom_estimator.create_model(
#                     model_name      = "wjm-custom-model",                    # 模型名称
#                     model_version   = "1.1.3",                       # 模型版本
#					 model_path      = "s3://aiteam/image-class/",                # 模型地址
#                     model_framework_type  = "CUSTOM",        # 模型框架类型
#                     model_mirrorUrl   = "172.16.14.172/test/cuda:9.0-devel-ubuntu16.04")           # 模型版本
#
#predictor_instance = custom_estimator.deploy_predictor(
#						service_name  = "wjm-custom-predictor1",
#						service_type  = "ONLINE_SERVICE",
#                        service_models = [{"weight":100,"resourceId":500151,"instanceCount":1}])
#
