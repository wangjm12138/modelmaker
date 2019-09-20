from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()

#Model.predict_machine(session)
#Model.preset_model(session)
#Model.predict_framework(session)
#Model.model_list(session)
#Model.model_list(session,model_id=502508)
#Model.destory_model(session,model_id=502350)
#Model.destory_model_version(session,model_version_id=502709)
#Model.model_version_info(session,model_version_id=502508)

model_instance=Model(
					 modelmaker_session = session,
                     model_name      = "basic-model-predict",                    # 模型名称
                     model_version   = "1.1.2",                       # 模型版本
                     model_framework  = 500001,                      # 模型框架id
                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
					 model_code_dir      = "s3://ai-team/0611-113341/", # 推理代码目录
                     model_path = "s3://ai-team/wjm_test_deploy/",   #模型组件路径
                     model_boot_file     = "predict.py")              # 启动文件

model_instance.create_model()
p = model_instance.deploy_predictor(
            predictor_name="basic-new222",
            predictor_type="ONLINE_SERVICE",
            predictor_models=[{"weight":100,"resourceId":502204,"instanceCount":1}])
p.stop()
#model_instance.delete_model()

#Model.model_list(session)
#model_instance.info()
#model_instance.get_model_version_id()
##model_instance = Model(session)
##model_instance.model_info(model_id=500406)
#model_instance.create_model(
#                     model_name      = "basic-model-new2",                    # 模型名称
#                     model_version   = "1.1.2",                       # 模型版本
#                     model_framework  = 500001,                      # 模型框架id
#                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
#                     model_code_dir      = "s3://aiteam/mnist/code/", # 推理代码目录
#                     model_path = "s3://aiteam/wjm_output/V0001/",   #模型组件路径
#                     model_boot_file     = "predict.py")              # 启动文件
#predictor_response = model_instance.deploy_predictor(
#                                                service_name  = "ssss-basic-predict",
#                                                service_type  = "ONLINE_SERVICE",
#                        service_models = [{"modelVersionId":500565,"weight":100,"resourceId":500004,"instanceCount":1}]
#)
