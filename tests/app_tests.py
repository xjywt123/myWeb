import sys
sys.path.append("..")
from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# resp = app.request("/hello",method = 'GET',data = None,
	# host = 'localhost:8081',headers = None,https = False)
	# assert_response(resp,status = "404")

	# resp = app.request("/")
	# assert_response(resp)

	resp = app.request("/",method = "POST")
	assert_response(resp,contains = "Nobody")

	data = {'name':'Zed','greet':'Hola'}
	resp = app.request("/",method = "POST",data = data)
	assert_response(resp,contains = Zed)