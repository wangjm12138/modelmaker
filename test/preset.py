#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()

#/预置算法/#
job_name="preset-train"
preset_estimator = Estimator(
                      modelmaker_session=session,
					  #/train information/#
                      framework_type='PRESET_ALGORITHM',                            # 预置算法
                      algorithm = 500000,                                             # 算法id
					  #/output/
					  output_path="s3://aiteam/wjm-test/V0003/",                    # 训练输出位置，s3路径？
					  #/resource allocation/
					  train_instance_type=500200,                                     # 训练环境规格 resource_id
                      train_instance_count=1,                                       # 训练环境规格数量
                      volume_size=1)                                                 # 训练附加卷

preset_estimator.fit( "s3://aiteam/image-class/data/", wait = True, logs = True, job_name=job_name)
preset_estimator.create_model(
                     model_name      = "preset1-model",                       # 模型名称
                     model_version   = "1.1.1.2",                                       # 模型版本
                     model_framework      = 500000)                      # 模型框架
#					 model_path      = "s3://aiteam/image-class/output/1.4/",      # 模型地址
#                    model_framework_type  = "PRESET_MODEL")        # 模型框架类型

predictor_instance = preset_estimator.deploy_predictor(
						service_name  = "preset-service",
						service_type  = "ONLINE_SERVICE",
                        service_models = [{"weight":100,"resourceId":500550,"instanceCount":1}])





