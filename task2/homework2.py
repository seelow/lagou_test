# 补全计算器中加法和除法的测试用例
# 使用参数化完成测试用例的自动生成
# 在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
import pytest

import yaml

with open('./calc.yaml', encoding='utf8') as f:
    config = yaml.safe_load(f)['test']
    # 加法数据驱动
    add_data = config['add']
    add_test_datas = add_data['datas']
    add_ids = add_data['myid']
    # 除法数据驱动
    div_data = config['div']
    div_test_datas = div_data['datas']
    div_ids = div_data['myid']
    # print(div_test_datas)


class TestCal:

    def setup(self):
        print('测试开始')

    def teardown(self):
        print('测试结束')

    @pytest.mark.parametrize('x,y,expect', add_test_datas, ids=add_ids)
    def test_add(self, init_cal, x, y, expect):
        actual = init_cal.add(x, y)
        assert actual == expect

    @pytest.mark.parametrize('x,y,expect', div_test_datas, ids=div_ids)
    def test_div(self, init_cal, x, y, expect):
        if expect == 'error':
            try:
                init_cal.div(x, y)
            except ZeroDivisionError:
                return
        actual = init_cal.div(x, y)
        assert actual == expect
