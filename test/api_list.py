#-*-coding:utf-8-*-
import sys
print(sys.path)
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
#import sys
print(sys.path)
#session = Session(username="cdy",password="cyd@Pass1",iam_server="http://172.16.14.201:9048/mmr")
#session = Session()
##/api 部分/


##===================Esitmator【类方法】=======================
##//获取预置模型
#Estimator.get_preset_model(session)
###//获取预置算法
#Estimator.get_preset_algorithm(session)
###//获取训练框架列表
#Estimator.get_train_framework_list(session)
###//获取开发框架列表
#Estimator.get_development_framework_list(session)
###//获取部署框架列表
#Estimator.get_reasoning_framework_list(session)
###//获取训练机器列表
#Estimator.get_train_instance_types(session)
###//获取开发机器列表
#Estimator.get_development_instance_types(session)
###//获取部署机器列表
#Estimator.get_reasoning_instance_types(session)
#------------训练详情
##//获取训练全部作业列表
#Estimator.get_job_info(session)
##//指定训练作业id，获取训练作业详情,id需存在!!!!，不然报错
#Estimator.get_job_info(session,job_id=502409)
##//指定训练作业版本id，获取训练作业版本详情,version_id需存在!!!，不然报错
#Estimator.get_job_version_info(session,version_id=12345)
#------------训练删除
##//指定训练作业id，删除全部的版本,id需存在!!!!，不然报错
#Estimator.destory_job(session,job_id=12345)
##//指定训练作业版本id，删除该版本,id需存在!!!!，不然报错
#Estimator.destory_job_version(session,version_id=502758)

##===================Esitmator【实例方法】=======================
#estimator = Estimator(modelmaker_session=session)
#当训练任务fit方法已经有执行过，会内部存储version_id，则不需要填写version_id，否则要填写,此时类似于【类方法】,version_id需存在!!!!，
#【if】  estimator.fit()

#estimator.get_resource_monitor()
#estimator.get_performance_monitor()
#estimator.get_job_log(log_id=0)
#estimator.get_job_output()
#estimator.delete_job_version()
#estimator.stop_job_version()

#【else】
##//获取训练运行监控
#estimator.get_resource_monitor(version_id=502758)
##//获取训练指标监控
#estimator.get_performance_monitor(version_id=502758)
##//获取训练log,需制定log的id，每次200条
#estimator.get_job_log(version_id=502850,log_id=0)
##//获取训练输出
#estimator.get_job_output(version_id=502758)
##//删除训练
#estimator.delete_job(version_id=502300)
##//停止训练
#estimator.stop_job(job_id=502300)

##===================Model【实例方法】=======================
#model_instance = Model(session) #
###//获取预置模型列表
#model_instance.get_preset_model()
###//获取推理框架列表
#model_instance.get_reasoning_framework_list()
###//获取推理机器类型
#model_instance.get_reasoning_instance_types()
###//获取全部模型
#model_instance.get_model_info()
##//指定模型id，获取模型详情,id需存在!!!!，不然报错
#model_instance.get_model_info(model_id=43452)



##删除
##//指定模型id,删除,id需存在
#model_instance.delete_model(model_id=222)
##//指定服务id,删除,id需存在
#model_instance.delete_service(service_id=24)
#当模型 create_model 方法已经有执行过，会内部存储model_id/model_version_id，删除时则不需要填写model_id/model_version_id，否则要填写
#【if】 create_model
#model_instance.delete_model_version()
#【else】
#model_instance.delete_model_version(model_version_id=22)

##获取模型/服务id,当create_model和deploy_predictor方法都有被调用后，下面可以返回模型id/模型版本id/服务id
##//返回service_id
#model_instance.get_service_id()
##//返回model_id
#model_instance.get_model_id()
##//返回model_version_id
#model_instance.get_model_version_id()

##===================Predictor【实例方法】=======================

#predictor_instance = Predictor(session,service_id=1000) #

##//获取服务id对应详情，如果已经predictor_instance初始化已经有id，则不需要
#predictor_instance.get_service_info(service_id=1000)
##//获取在线服务列表
#predictor_instance.get_service_list()
##//启动在线服务
#predictor_instance.start_service(service_id=1000)
##//停止在线服务
#predictor_instance.stop_service(service_id=1000)
##//删除在线服务
#predictor_instance.delete_service(service_id=1000)


