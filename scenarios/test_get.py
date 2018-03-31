import unittest
import requests

from ddt import ddt, data, unpack

from library.getData import get_xls_data

@ddt
class APITesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @data(*get_xls_data('./data/post_data.xls'))
    @unpack
    def test_post_topic(self,token,title,tab,content,code):

        url = 'http://118.31.19.120:3000/api/v1/topics'

        post_data = {
        "accesstoken":token,
    	"title":title,
    	"tab":tab,
    	"content":content
        }

        res = requests.post(url,json=post_data)
        
        assert res.status_code == code

        # id = r['topic_id']

        # update_topic_url = 'http://118.31.19.120:3000/api/v1/topics/update'

        # update_data = {
        #     "accesstoken":token,
        #     "topic_id":id,
        # 	"title":title,
        # 	"tab":tab,
        # 	"content":content
        # }

        # res = requests.post(update_topic_url,json=update_data)

    
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
