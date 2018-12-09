import unittest
from conf import config
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib.send_email import send_report
# 遍历指定文件夹下及子包下的所有测试用例  test_
all = unittest.defaultTestLoader.discover("./testcase")


if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(all)  # 两个不能同时使用
    config.logging.info("测试开始" + "=" * 50)
    with open(config.report_file, "wb") as f:  # 二进制写模式
        HTMLTestRunner(stream=f, title="User接口测试报告", description="测试报告").run(all)

    if config.is_send_report:
        send_report()
        config.logging.info("发送邮件成功")

    config.logging.info("测试结束" + "=" * 50)