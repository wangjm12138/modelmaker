import json
from jsonschema import validate
import sys
instance={
	"name":"sfdsafg",
	"type": "PRESET_ALGORITHM",
	"algorithmId":12345,
	"parameters":[
		{
		"name":"name",
		"value":"value"
		}
	],
	"modelUrl": "docker://sd",
	"dataUrl": "s3://input/ss",
	"output": "s3://output/v1",
	"resourcePoolType":"PUBLIC_POOL",
	"customResource":{
		"cpu":1,
		"memory":1,
		"gpuModel":"model",
		"gpuCount":1
	},
	"resourceId":23,
	"volumeSize":5, 
	"instance":1,
	"maxRuntime":100034,
	"isFlowInput":1,
	"description":"sdfsa"
}
try:
	with open("../Peset_Algorithm.json",'r') as f:
		train_preset_algorithm_schema = json.load(f)
#except json.decoder.JSONDecodeError:
except Exception as e:
	print(e)
	print("json format is error!!!")
	sys.exit(0)
print("json format is right!")
#print(train_preset_algorithm_schema)
validate(instance=instance,schema=train_preset_algorithm_schema)
