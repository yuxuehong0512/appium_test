# author_='Yuxuehong';
# date: 2023/8/25 10:11

import pytest


@pytest.hookimpl(hookwrapper=True)  # 固定写法
def pytest_runtest_makereport(item, call):  # 固定写法

    outcome = yield
    # print(outcome)
    report = outcome.get_result()
    # extra = getattr(report,"extra",[])
    # print("extra:",extra)

    print(report.when)
    if report.when == "call": # 过滤前置、后置只保留运行中状态
        print(report.__dict__)
        print(report.outcome) # 用例执行结果
        print(report.sections) # 用例执行过程中捕捉到的输出内容
        print(report.duration)  # 用例执行时间


