
## ModelMaker Python SDK
ModelMaker Python SDK是由网宿有限公司提供的开源库，提供在网宿AI开发平台上的训练和部署。

ModelMaker能够提供三种形式的训练和部署，预置算法，基础框架和自定义的镜像方式。预置算法部分是由网宿提供的常见的算法框架并且已经大幅度的优化在GPU上的训练，基础框架部分包含了tensorflow框架，用户根据约定好的规则，定义好的模型，输入，输出函数即可进行训练并支持分布式。当用户需要用自己算法在网宿AI开发平台上训练，即可选择自定义的框架，按照约定规则即可实现训练和部署。
### 环境准备
推荐用conda创建个虚拟环境  
conda create -n py3.6 python=3.6  
conda activate py3.6
### 依赖包
* python 3.6
* requests > 2.14.2
* urllib3 > 1.21.1
* boto3 > 1.4.5
* botocore > 1.5.92
### 安装
pip install modelmaker-1.0.0-py3-none-any.whl
### SDK配置
在使用ModelMaker变成之前，您需要提供必要的配置信息以便SDK可以连接到ModelMaker的服务，具体的步骤如下：
1. 用户的目录下创建.modelmaker目录，将ModelMaker中的config.json拷贝至创建的.modelmaker目录下
2. 打开.modelmaker目录下的config.json文件，用真实的账户名，密码，服务器地址替换掉usrename,password,iam_server  

**说明：sdk配置是非必须的，如今ModelMaker的鉴权(session)是使用token方式，通过用户名,密码,服务器的地址获取，也可以在session创建过程中程序人为指定,详细查看后面的内容**
### 日志等级调整
默认的日志等级是INFO，如果需要调整为debug来查看具体api的运行过程的url，头部，body部分，可以用一下命令：  
export MODELMAKER_LEVEL=10  
**说明：日志等级表[10,20,30,40]=[DBUG,INFO,WARNING,ERROR]**
### 作业管理
1. 创建训练任务
```
#-*-coding:utf-8-*-
from modelmaker.session import Session

session = Session()
#session = Session(username="cdy",password="cyd@Pass1",iam_server="172.16.14.201:9048/mmr")

###/自定义镜像/#
job_name="wjm-custom-train1"
custom_estimator = Estimator(
                      modelmaker_session=session,
                      #/train information/#
                      framework_type='CUSTOM',                                      # 框架类型用户自定义
                      user_image_url='172.16.14.172/test/custom:v1.0',              # 用户自定义镜像地址
                      #/train input/#     
                      user_command="/bin/bash",                                # 用户命令          
                      user_command_args="/home/test/start.sh",                            # 用户命令参数      
                      #monitors=[{'name':'.*?loss\s=\s(.*)\s,\sstep\s=\s(.*)','accuracy':'.*?accuracy\s=\s(.*)','loss1':'.*?loss\s=\s(.*)\s,\sstep\s=\s(.*)'}],   # 训练监控指标
                      #/output/
                      output_path="s3://aiteam/wjm_output/",                  # 训练输出位置，s3路径？
                      #/resource allocation/
                      train_instance_type=500050,                                     # 训练环境规格 resource_id
                      train_instance_count=1,                                       # 训练环境规格数量    
                      volume_size=1)                                                 # 训练附加卷
                      
custom_estimator.fit(inputs=None, wait = True, logs = True, job_name=job_name)

```
**说明：以上是创建自定义的训练任务，framework_type='CUSTOM'，其他的预置算法，基础框架，framework_type字段分别为'PRESET_ALGORITHM'和'BASIC_FRAMEWORK'，不同框架相应参数也不同，具体框架哪些参数是必须和非必须请您查看下面api参考，ModelMaker内部会做参数校验，当参数错误会提醒您重新更改**  
2. 创建模型和部署服务，Estimator实例后既可以训练量也可以创建模型和部署服务
```
custom_estimator.create_model(
                     model_name      = "wjm-custom-model",                    # 模型名称
                     model_version   = "1.1.3",                       # 模型版本
                     model_path      = "s3://aiteam/image-class/",                # 模型地址
                     model_framework_type  = "CUSTOM",        # 模型框架类型
                     model_mirrorUrl   = "172.16.14.172/test/cuda:9.0-devel-ubuntu16.04")           # 模型版本

predictor_instance = custom_estimator.deploy_predictor(
                        service_name  = "wjm-custom-predictor1",
                        service_type  = "ONLINE_SERVICE",
                        service_models = [{"modelVersionId"=50283,"weight":100,"resourceId":500151,"instanceCount":1}])

```
**注：其中创建模型时候create_model的model_path和model_framewrok_type可以选择不填会自动根据训练任务的output_path和framework_type，同理部署deploy_predictor的service_models["modelVersionId"]也可以不填会自动根据创建模型填写相应id**  
当Estimator实例化后可以调用相应的实例方法
```
"""//查询训练版本运行监控"""
custom_estimator.get_resource_monitor()
"""//查询训练版本指标监控"""
custom_estimator.get_performance_monitor()
"""//查询训练版本日志，需要指定log_id"""
custom_estimator.get_job_log(log_id=0)
"""//查询训练版本输出"""
custom_estimator.get_job_output()
"""//停止训练"""
custom_estimator.stop_job()
"""//删除训练"""
custom_estimator.delete_job()
```
3. 查询资源规格列表
```
#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator

session = Session()
#session = Session(username="cdy",password="cyd@Pass1",iam_server="172.16.14.201:9048/mmr")

"""//获取训练机器列表"""
#Estimator.get_train_instance_types(session)
"""//获取开发机器列表"""
#Estimator.get_development_instance_types(session)
"""//获取部署机器列表"""
#Estimator.get_reasoning_instance_types(session)

```
其中第一步创建训练任务的train_instance_type的id值需在Estimator.get_train_instance_types获得的列表中，train_instance_count最大支持10，volume_size最大也只支持10。
4. 查询预置算法列表
```
"""获取预置算法"""
#Estimator.get_preset_algorithm(session)
```
当创建训练任务的类型是framework_type='PRESET_ALGORITHM'需在此查询的列表中
5. 查询基础框架训练列表
```
"""//获取基础框架训练列表"""
#Estimator.get_train_framework_list(session)
```
当创建训练任务的类型是framework_type='BASIC_FRAMEWORK'需在此查询的列表中
6. 查询预置模型列表
```
"""获取预置模型"""
#Estimator.get_preset_model(session)
```
当创建模型model_framework_type="PRESET_MODEL"的类型是需在此查询的列表中
7. 查询基础框架模型部署列表
```
"""//获取基础框架模型部署列表"""
#Estimator.get_reasoning_framework_list(session)
```
当创建模型model_framework_type  = 'BASIC_FRAMEWORK'的类型是需在此查询的列表中
8. 其他
```
"""//获取训练全部作业列表"""
#Estimator.get_job_info(session)
"""//指定训练作业id，获取训练作业详情,id需存在!!!!，不然报错"""
#Estimator.get_job_info(session,job_id=502408)
"""//指定训练作业版本id，获取训练作业版本详情,version_id需存在!!!，不然报错"""
#Estimator.get_job_version_info(session,version_id=12345)
"""------------训练删除"""
"""//指定训练作业id，删除全部的版本,id需存在!!!!，不然报错"""
#Estimator.destory_job(session,job_id=12345)
"""//指定训练作业版本id，删除该版本,id需存在!!!!，不然报错"""
#Estimator.destory_job_version(session,version_id=502758)
```
### 模型管理
1. 创建模型
```
#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.model import Model
session = Session()
#session = Session(username="cdy",password="cyd@Pass1",iam_server="172.16.14.201:9048/mmr")
model_instance = Model(session)
model_instance.create_model(
                     model_name      = "basic-model",                    # 模型名称
                     model_version   = "1.1.1",                       # 模型版本
                     model_framework  = 500150,                      # 模型框架id
#                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
                     model_code_dir      = "s3://aiteam/mnist/code/", # 推理代码目录
#                    model_path = "s3://aiteam/wjm_output/V0001/",   #模型组件路径
                     model_boot_file     = "predict.py")              # 启动文件
```
2. 部署服务
```
redictor_response = basic_estimator.deploy_predictor(
                                                service_name  = "basic-predict",
                                                service_type  = "ONLINE_SERVICE",
                        service_models = [{"weight":100,"resourceId":500151,"instanceCount":1}])

```
3. 查询预置模型/基础框架模型列表，以及推理机器类型，这部分在作业管理也可以查询得到，属于重复内容
```
"""//获取预置模型列表"""
#model_instance.get_preset_model()
"""//获取基础框架模型列表"""
#model_instance.get_reasoning_framework_list()
"""//获取推理机器类型"""
#model_instance.get_reasoning_instance_types()
```
4. 查询模型列表，详情，模型id，模型版本id，服务id
```
"""//获取全部模型"""
#model_instance.get_model_info()
"""//指定模型id，获取模型详情,id需存在!!!!，不然报错"""
#model_instance.get_model_info(model_id=43452)
"""//返回service_id"""
#model_instance.get_service_id()
"""//返回model_id"""
#model_instance.get_model_id()
"""//返回model_version_id"""
#model_instance.get_model_version_id()
```
5. 删除
```
"""//指定模型id,删除,id需存在"""
#model_instance.delete_model(model_id=222)
"""//指定模型版本id,删除,id需存在，如果create_model已经创建可省略id"""
#model_instance.delete_model_version(model_version_id=22)
"""//指定服务id,删除,id需存在"""
#model_instance.delete_service(service_id=24)
```
### 服务管理
1. 关联服务id
```
predictor_instance = Predictor(session,service_id=1000) #
```
2. 服务相关操作
```
"""//获取服务详情"""
#predictor_instance.get_service_info()
"""//获取服务列表"""
#predictor_instance.get_service_list()
"""//启动服务"""
#predictor_instance.start_service()
"""//停止服务"""
#predictor_instance.stop_service()
"""//删除服务"""
#predictor_instance.delete_service()

```
