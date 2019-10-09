
# ModelMaker Python SDK（2.0.0）
ModelMaker Python SDK是由网宿有限公司提供的开源库，提供在网宿AI开发平台上的训练和部署。

ModelMaker能够提供三种形式的训练和部署，预置算法，基础框架和自定义的镜像方式。预置算法部分是由网宿提供的常见的算法框架并且已经大幅度的优化在GPU上的训练，基础框架部分包含了tensorflow框架，用户根据约定好的规则，定义好的模型，输入，输出函数即可进行训练并支持分布式。当用户需要用自己算法在网宿AI开发平台上训练，即可选择自定义的框架，按照约定规则即可实现训练和部署。

**注：本文档针对的是Modelmaker2.0.0版本！！！**

## 环境准备
推荐用conda创建个虚拟环境  
conda create -n py3.6 python=3.6  
conda activate py3.6
## 依赖包
* python 3.6
* requests > 2.14.2
* urllib3 > 1.21.1
* boto3 > 1.4.5
* botocore > 1.5.92
## 安装
pip install modelmaker

## SDK配置文件

mlcmd命令行配置生成config.json文件，安装完modelmaker后，执行mlcmd命令，会得到引导配置，需要配置：

- user name（ai平台用户名）
- passord（ai平台密码）
- host_base（api的接口地址），默认为https://mmr.wangsucloud.com:9948/mmr
- Region（地区），默认为js01
- Versify_ssl（是否ssl加密），默认为Yes
- S3_protocol（s3的接口协议），默认为http
- Bucket（s3存储桶地址）

![cfg.png](https://github.com/wangjm12138/modelmaker/blob/beta_version/picture/cfg.png?raw=true)

<center>图1</center>

在Save settings会生成json文件，存储在~/.modelamker/config.json下：

格式为：

![json.png](https://github.com/wangjm12138/modelmaker/blob/beta_version/picture/json.png?raw=true)

<center>图2</center>

## 日志等级调整

默认的日志等级是INFO，如果需要调整为debug来查看具体api的运行过程的url，头部，body部分，可以用一下命令：  
export MODELMAKER_LEVEL=10  
**说明：日志等级表[10,20,30,40]=[DBUG,INFO,WARNING,ERROR]**

## 作业管理
### 1.创建训练任务简单示例

```
#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()
job_name="wjm-basic-train"
basic_estimator = Estimator(
                      modelmaker_session=session,
                      framework=500000,     # 深度学习框架类型
                      framework_type='BASIC_FRAMEWORK', # 平台框架类型
                      code_dir="s3://ai-team/wjm-mnist-tfrecode-code/",                   
                      codeVersion="1.0",    # 代码版本
                      boot_file="mnist.py", # 训练启动脚本
                      boot_type="NORMAL",   # 训练启动方式
                      output_path="s3://ai-team/wjm-mnist-tfrecode-output/V0008/",       
                      #resource_pool_type="PUBLIC_POOL",
                      train_instance_type=502201,# 训练机器规格 resource_id
                      train_instance_count=1,# 训练环境规格数量
                      volume_size=1)# 训练附加卷

basic_estimator.fit("s3://ai-team/wjm-mnist-tfrecode-data/", wait = True, logs = True, job_name=job_name)

basic_model = basic_estimator.create_model(
                     model_name      = "basic-model",                # 模型名称
                     model_version   = "1.1.1",                      # 模型版本
                     model_framework  = 500150,                      # 模型框架id
                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
                     model_code_dir      = "s3://aiteam/mnist/code/",# 推理代码目录
                     model_path = "s3://aiteam/wjm_output/V0001/",   # 模型组件路径
                     model_boot_file     = "predict.py")             # 启动文件

basic_predictor = basic_estimator.deploy_predictor(
                       service_name  = "basic-predict",
                       service_type  = "ONLINE_SERVICE",
                       service_models = [{"weight":100,"resourceId":500550,"instanceCount":1}])                      

```
### 2.SDK模块介绍

SDK的包括四大模块：

- Session模块，负责鉴权，获取token，s3的接口函数

- Estimator模块，负责创建训练任务，模型管理，部署服务

- Model模块，负责模型管理，部署服务

- Predictor模块，负责部署服务

其中Session鉴权的优先级是：输入参数>配置文件

如输入参数已经配置username=xiaohong,password=123456等，如果配置文件如图2，那么根据优先级最终username=xiaohong。

```
session = Session(username="xiaohong",password="123456",host_base="xxxx", region="xxxx", bucket="xxxx")
```

Estimator模块和Model模块，Predictor模块的关系如下图：向下兼容，每个Estimator的实例estimator可以创建模型管理，部署服务，每个Model的实例model可以创建部署服务，可以结合以下代码和第一点的代码加以理解。

![two.png](https://github.com/wangjm12138/modelmaker/blob/beta_version/picture/one.png?raw=true)

<center>图3</center>

```
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()
model_instance=Model(
                     modelmaker_session = session,
                     model_name      = "basic-model-predict",        # 模型名称
                     model_version   = "1.1.2",                      # 模型版本
                     model_framework  = 500001,                      # 模型框架id
                     model_framework_type  = 'BASIC_FRAMEWORK',      # 模型框架
                     model_code_dir      = "s3://ai-team/0611-113341/", # 推理代码目录
                     model_path = "s3://ai-team/wjm_test_deploy/",   #模型组件路径
                     model_boot_file     = "predict.py")             # 启动文件

model_instance.create_model()
p = model_instance.deploy_predictor(
            predictor_name="basic-new222",
            predictor_type="ONLINE_SERVICE",
            predictor_models=[{"weight":100,"resourceId":502204,"instanceCount":1}])
#p.stop()
```

```
#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
session = Session()

Predictor.service_list(session)
Predictor.service_machine(session)
p=Predictor(modelmaker_session=session,
            predictor_name="basic-new",
            predictor_type="ONLINE_SERVICE",
            predictor_models=[{"weight":100,"resourceId":502204,"instanceCount":1,"modelVersionId":502712}])
p.deploy_predictor()
p.stop()
p.update(predictor_models=[{"weight":100,"resourceId":502204,"instanceCount":1,"modelVersionId":502708}])
```

上面讲述了Estimator/Model/Predictor三种类的关系，Estimator的实例通过create_model实例方法拥有创建Model实例和Predictor实例的权利，Model实例拥有创建Predictor实例的权利。除了这种依赖关系，三种的类方法和实例方法有相同之处，如图：
![two.png](https://github.com/wangjm12138/modelmaker/blob/beta_version/picture/two.png?raw=true)

<center>图4</center>

Estimator/Model/Predictor是训练任务，模型管理，部署服务封装为三个的类，其中类的方法主要做查询，比如查询训练的机器类型，训练框架类型，举例如下：

```
###//获取预置算法
#Estimator.preset_algorithm(session)
###//获取训练框架列表
#Estimator.train_framework(session)
```

更多的关于类方法的api接口，可以查看后面的api接口函数的类方法部分。和Estimator类方法一样的，Mdoel和Predictor的类方法也主要是查询相关的信息，类方法有个共同点就是，参数都需要有**session**。

Estimator/Model/Predictor类都可以创建实例，当estimator/model/predictor实例调用了fie/create_model/deploy_predictor后，发送了请求到ai平台，构建了训练任务/模型管理/部署服务，此时实例会激活更多的实例方法，例如estmator.infor()实例方法，即可查询此次构建的训练任务的信息，在没有通过fit()方法激活，此实例方法是无法使用的！！！，更多的实例方法可以查看后面的api接口函数的实例方法部分。

### 3.平台的参数介绍

第1点中构建训练任务的时候，输入参数framework_type='BASIC_FRAMEWORK'，这里的框架和framework=500000 深度学习框架类型不同，为了避免混淆，在这里做说明，framework_type是AI平台定义的训练活动的一种框架或者叫模式，用户在需要通过AI平台训练时，通常会采用三种方式：

1. 用户采用平台已有的预置算法+用户数据集
2. 用户编写一部分代码+平台框架+用户数据集
3. 用户将代码放置于容器，上传到平台运行+用户数据集

这三种方式即ai平台定义的框架，第一种为framework_type='PRESET_ALGORITHM'，第二种为framework_type='BASIC_FRAMEWORK'，第三种为framework_type='CUSTOM'，主要针对不同需求的用户，以满足不同用户需求。

更多关于训练，模型，部署的参数可以产看后面的参数列表部分。

## API接口函数

### Estimator类方法

```
#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator

session = Session()
##//获取预置模型
Estimator.preset_model(session)
###//获取预置算法
Estimator.preset_algorithm(session)
###//获取训练框架列表
Estimator.train_framework(session)
###//获取开发框架列表
Estimator.development_framework(session)
###//获取部署框架列表
Estimator.predict_framework(session)
###//获取训练机器列表
Estimator.train_machine(session)
###//获取开发机器列表
Estimator.development_machine(session)
###//获取部署机器列表
Estimator.predict_machine(session)
##//获取训练全部作业列表
Estimator.train_list(session)
##//指定训练作业id，获取训练作业详情,id需存在!!!!，不然报错
Estimator.train_list(session,job_id=503902)
##//指定训练作业版本id，获取训练作业版本详情,version_id需存在!!!，不然报错
Estimator.train_version_info(session,version_id=502957)
##//指定训练作业id，删除全部的版本,id需存在!!!!，不然报错
Estimator.destory_job(session,job_id=12345)
##//指定训练作业版本id，删除该版本,id需存在!!!!，不然报错
Estimator.destory_job_version(session,version_id=502758)
```
### Estimator实例方法

```
如果已经fit()函数已调用过，version_id不需要填
##//获取训练详情
estimator.info(version_id=xxxx)
##//获取训练运行监控
estimator.resource(version_id=xxxx)
##//获取训练指标监控
estimator.metric(version_id=xxxx)
##//获取训练log,需制定log的id，每次200条
estimator.log(version_id=xxxx,log_id=0)
##//获取训练输出
estimator.artifacts(version_id=xxxx)
##//删除训练
estimator.delete(version_id=xxxx)
##//停止训练
estimator.stop(version_id=xxxx)
```

### Model类方法

```
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model

session = Session()
##//获取部署机器类型
Model.predict_machine(session)
##//获取预置模型
Model.preset_model(session)
##//获取部署框架
Model.predict_framework(session)
##//获取模型列表
Model.model_list(session)
##//指定模型id，获取模型版本列表
Model.model_list(session,model_id=502508)
##//指定模型id，删除模型(会删除该模型下所有版本)
Model.destory_model(session,model_id=502350)
##//指定模型版本id，删除模型版本
Model.destory_model_version(session,model_version_id=502709)
##//指定模型版本id，获取模型版本信息
Model.model_version_info(session,model_version_id=502508)
```

### Model实例方法

```
需要调用过create_model方法后，才能激活，否则无法使用
##//获取当前模型详情
model.info()
##//删除当前模型
model.delete_model()
##//获取当前模型版本id
model.get_model_version_id()
##//获取当前模型id
model.get_model_id()
##//获取当前服务id
model.get_service_id()
```

### Predictor类方法

```
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor

session = Session()
##//获取部署服务列表
Predictor.service_list(session)
##//获取部署机器类型
Predictor.service_machine(session)
##//指定service_id获取服务信息
Predictor.service_info(session,service_id=xxxx)
##//指定service_id,启动
Predictor.START(session，service_id=xxxx)
##//指定service_id,停止
Predictor.STOP(session，service_id=xxxx)
##//指定service_id,删除
Predictor.DELETE(session，service_id=xxxx)
```

### Predictor实例方法

```
##//获取当前服务信息
predictor_instance.info()
##//更新当前服务信息
predictor_instance.update(**kwargs)
##//启动当前服务
predictor_instance.start()
##//停止当前服务
predictor_instance.stop()
##//删除当前服务
predictor_instance.delete()
```

## 参数列表

### Estimator参数：

参数名 | 是否必填 | 格式 | 样式
---|--- |--- |---
train_instance_type | 是 | 整型 | train_instance_type=500550
train_instance_count | 是 （<10）| 整型 | train_instance_count=1
volume_size | 是（<10）| 整型 | volume_size=1

预置算法：

训练参数名 | 是否必填 | 格式 | 样式
---|--- |--- |--- 
algorithm | 是 | 整型 | algorithm=500000
output_path | 是 | 字符串 | output_path="s3://xxxx"
framework_type | 是 | 字符串 | framework_type='PRESET_ALGORITHM'
max_runtime | 否 | 整型 | max_runtime=24*3600
hyperparameters | 否 | 列表 | hyperparameters=[{"name":"name","value":"value"}]
init_model | 否 | 字符串 | init_model="docker://sd"

基础框架：

训练参数名 | 是否必填 | 格式 | 样式
---|---|--- |---
code_dir | 否（与git_info二选一必填）| 字符串 | code_dir="s3://xxxx"
git_info | 否（与code_dir二选一必填）| 字典 | git_info={"username":"XXX","password":"xxx","branch":"XXXX"}
framework | 是| 整型 | framework=500100
framework_type | 是| 字符串 | framework_type="BASIC_FRAMEWORK"
boot_file | 是| 字符串 | boot_file="train.py"
output_path | 是| 字符串 | output_path="s3://xxxx"
input_files | 否| 列表 | input_files=[{"name":"sf","path":"docker://sd"}]
monitors | 否| 列表 | monitors=[{r"name":r"Loss",r"regular":r"loss=\d+",r"sample":"loss=20"}]
hyperparameters | 否| 列表 | hyperparameters=[{"name":"name","value":"value"}]
max_runtime | 否| 整型 | max_runtime=24*3600

自定义：

训练参数名 | 是否必填| 格式 | 样式
---|---|--- |---
code_dir | 否（与git_info二选一必填）| 字符串 | code_dir="s3://xxxx"
git_info | 否（与code_dir二选一必填）| 字典 | git_info={"username":"xxx","password":"xxx","branch":"XXXX"}
framework_type | 是| 整型 | framework_type="CUSTOM"
user_image_url | 是| 字符串| user_image_url="镜像url"
output_path | 是| 字符串 | output_path="s3://xxxx"
user_command | 否| 字符串 | user_command="/bin/bash"
user_command_args | 否| 字符串| user_command_args="/home/test/start.sh"
env | 否| 列表 | env=[{"name":"sf","evn2":"docker://sd}]
monitors | 否| 列表 | monitors=[{r"name":r"Loss",r"regular":r"loss=\d+",r"sample":"loss=20"}]
max_runtime | 否| 整型 | max_runtime=24*3600

### Model参数

训练参数名 | 是否必填 | 格式 | 样式
---|---|---|---
model_version | 是 | 字符串 | model_version="1.1.1.2"
model_framework_type | 否 | 字符串 | model_framework_type="PRESET_MODEL"
model_name | 否 | 字符串 | model_name="preset1-model"
model_framework | 否 | 整型 | model_framework=500000
model_path | 否 | 字符串 | model_path="s3://xxxx"

创建基础框架模型参数列表

训练参数名 | 是否必填 | 格式 | 样式
---|--- | --- | ---
model_framework_type | 否 | 字符串 | model_framework_type='BASIC_FRAMEWORK'
model_name | 否 | 字符串 | model_name="basic-model"
model_version | 是  | 字符串 | model_version = "1.12.1"
model_framework | 是  | 整型 | model_framework=500150
model_path | 是  | 字符串 | model_path="s3://xxxx"
model_code_dir | 是  | 字符串 | model_code_dir="s3://xxxx"
model_git_info | 否  | 列表 | model_git_info=[{"username":"xxx","password":"xxx","branch":"xxxx"}]
model_boot_file | 是 | 字符串 | model_boot_file="predict.py"


创建自定义模型参数列表

训练参数名 | 是否必填 | 格式 | 样式
--- |--- | --- | ---
model_framework_type | 否 | 字符串 | model_framework_type="CUSTOM"
model_name | 否 | 字符串 | model_name="xxx"
model_version | 是 | 字符串 | model_version="1.12.1"
model_mirrorUrl | 是 | 字符串 | model_mirrorUrl="docker:/sdf"
model_path | 是 | 字符串 | model_path="s3://xxx"

预置算法参数列表

训练参数名 | 是否必填 | 格式 | 样式
---|---|---|---
model_version | 是 | 字符串 | model_version="1.1.1.2"
model_framework_type | 是 | 字符串 | model_framework_type="PRESET_MODEL"
model_name | 是 | 字符串 | model_name="preset1-model"
model_framework | 是 | 整型 | model_framework=500000
model_path | 是 | 字符串 | model_path="s3://xxxx"

基础框架参数列表

训练参数名 | 是否必填 | 格式 | 样式
---|--- | --- | ---
model_framework_type | 是 | 字符串 | model_framework_type='BASIC_FRAMEWORK'
model_name | 是 | 字符串 | model_name="basic-model"
model_version | 是  | 字符串 | model_version = "1.12.1"
model_framework | 是  | 整型 | model_framework=500150
model_path | 是  | 字符串 | model_path="s3://xxxx"
model_code_dir | 是  | 字符串 | model_code_dir="s3://xxxx"
model_git_info | 否  | 列表 | model_git_info=[{"username":"xxx","password":"xxx","branch":"xxxx"}]
model_boot_file | 是 | 字符串 | model_boot_file="predict.py"

自定义参数列表

训练参数名 | 是否必填 | 格式 | 样式
--- |--- | --- | ---
model_framework_type | 是 | 字符串 | model_framework_type="CUSTOM"
model_name | 是 | 字符串 | model_name="xxx"
model_version | 是 | 字符串 | model_version="1.12.1"
model_mirrorUrl | 是 | 字符串 | model_mirrorUrl="docker:/sdf"
model_path | 是 | 字符串 | model_path="s3://xxx"

### Predictor参数

训练参数名 | 是否必填 | 格式 | 样式
---|--- | --- | ---
service_name | 是 | 字符串 | service_name="basic-predict"
service_type | 是 | 字符串 | service_type="ONLINE_SERVICE"
service_models | 是 | 列表(字典) | service_models=[{"weight":100,"resourceId":500151,"instanceCount":1}]

备注：service_type只能ONLINE_SERVICE
service_models列表包含是字典，且必须包含weitht，resourceId，instanceCount
