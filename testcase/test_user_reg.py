import unittest
import requests
import json
from lib import db
from lib import load_data
from lib.case_log import log_case_info
from conf import config

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=load_data.get_sheet(config.data_file,"注册")

    def test_user_reg_normal(self):
        if db.check_user("张三丰"):  # 环境准备
            db.del_user("张三丰")
        case_data=load_data.get_case(self.sheet,"test_user_reg_normal")
        url=case_data[2]
        try:
            data=json.loads(case_data[3])
            excepted_res=json.loads(case_data[4])
        except json.decoder.JSONDecodeError as e:
            config.logging.error("用例数据不是合法json")
        # url = 'http://115.28.108.130:5000/api/user/reg/'
        # data = {"name": NAME, "password": "123456"}
        res = requests.post(url=url, json=data)
        # self.assertEqual("成功", res.json()["msg"])
        # self.assertTrue(db.check_user(NAME))
        self.assertDictEqual(excepted_res,res.json())
        log_case_info("test_user_reg_normal",url,case_data[3],case_data[4],res.text)
        try:
            res_json=res.json()
        except json.decoder.JSONDecodeError as e:
             config.logging.error("返回结果不是json格式")

        db.del_user("张三丰")   # 环境清理

    def test_user_reg_use_exist(self):
        case_data=load_data.get_case(self.sheet,"test_user_reg_use_exist")
        url=case_data[2]
        data=json.loads(case_data[3])
        excepted_res=json.loads(case_data[4])
        # url = 'http://115.28.108.130:5000/api/user/reg/'
        # data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url, json=data)
        # self.assertEqual("失败，用户已存在", res.json()["msg"])
        self.assertDictEqual(excepted_res,res.json())
        log_case_info("test_user_reg_use_exist",url,case_data[3],case_data[4],res.text)