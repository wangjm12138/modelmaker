import json
from jsonschema import validate
import sys
instance={
	"name": "1dadg",
	"type":"ONLINE_SERVICE",
	"serviceModels":[
		{
			"modelVersionId":1000,
			"weight":13,
			"resourceId":100,
			"resourcePoolType":"PUBLIC_POOL",
			"customResource":{
				"cpu":1,
				"memory":1,
				"gpuModel":"model",
				"gpuCount":1
			},
		"instanceCount":2,
		"envs":[{
		     "name":"sf",
		     "value":"docker://sd"
		 }]
		}
	]
}
try:
	with open("../Predictor.json",'r') as f:
		train_preset_algorithm_schema = json.load(f)
#except json.decoder.JSONDecodeError:
except Exception as e:
	print(e)
	print("json format is error!!!")
	sys.exit(0)
print("json format is right!")
#print(train_preset_algorithm_schema)
validate(instance=instance,schema=train_preset_algorithm_schema)
