import json
from jsonschema import validate
import sys
instance={
	"name":"sfdsafg",
	"type": "CUSTOM",
	"mirrorUrl":"fdassga",
	"codeUrl": "s3://code",
	"codeVersion": "1.0",
	"gitInfo": {
		"username": "sf",
		"password": "docker://sd",
		"branch": "XXX"
	},
	"envs":[
		{
		"name":"sf",
		"value":"docker://sd"
		}
	],
	"command": "sdfs",
	"args": "xxgsge",
	"inputFiles":[
		{
		"name":"sf",
		"path":"docker://sd",
		}
	],
	"dataUrl": "s3://input/ss",
	"output": "s3://input/v1",
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
	with open("../Custom.json",'r') as f:
		train_preset_algorithm_schema = json.load(f)
#except json.decoder.JSONDecodeError:
except Exception as e:
	print(e)
	print("json format is error!!!")
	sys.exit(0)
print("json format is right!")
#print(train_preset_algorithm_schema)
validate(instance=instance,schema=train_preset_algorithm_schema)
