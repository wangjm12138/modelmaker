import os
import sys
import json
import unittest
from jsonschema import validate
from parameter import Basic_Framework

def find_check_schema(filename):
	abs_path = os.path.dirname(os.path.abspath(__file__))
	file_path = os.path.join(abs_path,"../{}.json".format(filename))
	print("schema file {}".format(file_path))
	try:
		with open(file_path,'r') as f:
			target_schema = json.load(f)
	except Exception as e:
		print(e)
		print("schema json format is error!!!")
		sys.exit(0)
	print("schema json format is right!")
	return target_schema

def Framework(unit):
	Flag=1
	target_schema = find_check_schema(unit)
	try:
		validate(instance=Basic_Framework,schema=target_schema)
	except Exception as e:
		#print(e)
		Flag=0
	return Flag,e


class Test_json(unittest.TestCase):

#	def setUp(self):
#		print("environment start")
#
#	def tearDown(self):
#		print("clean up environment")

	def test_Basic_Framework(self):
		self.assertEqual(1,Framework('Basic_Framework'))

	def test_Preset_Algorithm(self):
		self.assertEqual(1,Framework('Preset_Algorithm'))
	#def test_Basic_Framework(self):
	#	self.assertEqual(3,add(1,2))
			
	#def test_is_print(self):
	#	self.assertEqual(2,multi(1,2))



if __name__ == '__main__':
	tests = [Test_json('test_Basic_Framework'),Test_json('Preset_Algorithm')]
	suit = unittest.TestSuite()
	suit.addTests(tests)

	runner = unittest.TextTestRunner()
	runner.run(suit)
