import json
from jsonschema import validate
import sys
instance={
	"name":"fdsaasgdsaga",
}
try:
	with open("../mini.json",'r') as f:
		mini = json.load(f)
#except json.decoder.JSONDecodeError:
except Exception as e:
	print(e)
	print("json format is error!!!")
	sys.exit(0)
print("json format is right!")
#print(train_preset_algorithm_schema)
validate(instance=instance,schema=mini)
