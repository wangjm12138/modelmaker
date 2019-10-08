#-*-coding:utf-8-*-
from modelmaker.session import Session
from modelmaker.estimator import Estimator
from modelmaker.model import Model
from modelmaker.predictor import Predictor
#session = Session(username="xxx",password="xxxx",host_base="xxxxx", region="xxxx", bucket="xxxx")
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
#p.info()
#p.start()
#p.stop()
#p.delete()
#Predictor.STOP(session,service_id=502400)
#Predictor.DELETE(session,service_id=502400)
