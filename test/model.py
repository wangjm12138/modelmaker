from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()

model_instance = Model(session)
#model_instance.model_info(model_id=500406)
#model_instance.create_model(
#                     model_name      = "basic-model-new2",                    # 模型名称
#                     model_version   = "1.1.2",                       # 模型版本
#                     model_framework  = 500001,                      # 模型框架id
#                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
#                     model_code_dir      = "s3://aiteam/mnist/code/", # 推理代码目录
#                     model_path = "s3://aiteam/wjm_output/V0001/",   #模型组件路径
#                     model_boot_file     = "predict.py")              # 启动文件
predictor_response = model_instance.deploy_predictor(
                                                service_name  = "ssss-basic-predict",
                                                service_type  = "ONLINE_SERVICE",
                        service_models = [{"modelVersionId":500565,"weight":100,"resourceId":500004,"instanceCount":1}]
)
