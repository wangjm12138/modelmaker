import json
from jsonschema import validate
import sys
#https://www.cnblogs.com/ChangAn223/p/11234348.html
instance={
	"name":"sfdsafg",
	"type": "BASIC_FRAMEWORK",
	"frameworkId":12345,
	"codeUrl": "s3://code",
	"gitInfo": {
		"username": "sf",
		"password": "docker://sd",
		"branch": "XXX"
	},
	"startup": "startup.txt",
	"startupType": "NORMAL",
	"parameters":[
		{
		"name":"name",
		"value":"value"
		}
	],
	"inputFiles":[
		{
		"name":"sf",
		"path":"docker://sd"
		}
	],
	"dataUrl": "s3://input/ss",
	"output": "s3://output/v1",
	"monitors":[
		{
		"name":"Loss",
		"regular":"loss=\d+",
		"sample":"loss=20",
		}
	],
	"resourceId":23,
	"resourcePoolType":"PUBLIC_POOL",
	"customResource":{
		"cpu":1,
		"memory":1,
		"gpuModel":"model",
		"gpuCount":1
	},
	"description":"sdfsa",
	"volumeSize":5, 
	"instance":10,
	"maxRuntime":100034,
	"isFlowInput":1,
}
try:
	with open("../Basic_Framework.json",'r') as f:
		train_preset_algorithm_schema = json.load(f)
#except json.decoder.JSONDecodeError:
except Exception as e:
	print(e)
	print("json format is error!!!")
	sys.exit(0)
print("json format is right!")
#print(train_preset_algorithm_schema)
validate(instance=instance,schema=train_preset_algorithm_schema)
