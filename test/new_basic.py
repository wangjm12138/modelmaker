#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()
#session = Session(username="xxx",password="xxxx",host_base="xxxxx", region="xxxx", bucket="xxxx")

#yy础镜像/#
job_name="wjm-basic-train"
basic_estimator = Estimator(
                      modelmaker_session=session,
					  #/train information/#
                      framework=500000,                                               # AI引擎版本?
                      framework_type='BASIC_FRAMEWORK',                             # AI引擎版本?
					  #/train code/#
					  code_dir="s3://ai-team/wjm-mnist-tfrecode-code/",                          # 训练代码目录,s3路径?
					  codeVersion="1.0",
                      boot_file="mnist.py",                						   # 训练启动脚本目录,s3路径？
					  boot_type="NORMAL",
					  #/output/
					  output_path="s3://ai-team/wjm-mnist-tfrecode-output/V0008/",			          # 训练输出位置，s3路径？
					  #/resource allocation/
					  #resource_pool_type="PERSONAL_POOL",
					  #custom_resource={'cpu':1,'memory':1,'gpuModel':'K80','gpuCount':1,'requestCpu':1, 'requestMemory':1,'shareGpu':0,'gpuz':1.5},
					  train_instance_type=502201,                                     # 训练环境规格 resource_id
                      train_instance_count=1,                                       # 训练环境规格数量
                      volume_size=1)                                                 # 训练附加卷
basic_estimator.fit("s3://ai-team/wjm-mnist-tfrecode-data/", wait = True, logs = True, job_name=job_name)

#basic_estimator.create_model(
##                     model_name      = "basic-model",                    # 模型名称
#                     model_version   = "1.1.1",                       # 模型版本
##                     model_framework  = 500150,                      # 模型框架id
##                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
#					 model_code_dir      = "s3://aiteam/mnist/code/", # 推理代码目录
##					 model_path = "s3://aiteam/wjm_output/V0001/",   #模型组件路径
#                     model_boot_file     = "predict.py")              # 启动文件

#predictor_response = basic_estimator.deploy_predictor(
#						service_name  = "basic-predict",
#						service_type  = "ONLINE_SERVICE",
#                        service_models = [{"weight":100,"resourceId":500550,"instanceCount":1}])
