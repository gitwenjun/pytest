# API 接口自动化实例

---
## 框架设计
- pytest
- request
- allure

---
## 目录结构
    .pytest_cache           --cache缓存功能(系统自己生成)
    allure                  --生成报告，临时目录，压缩文件
    common                  --公共包
    config                  --配置文件
    data                    --存放session
    logs                    --存放日志
    send_email              --发送邮件
    testcase_py             --测试用例
    testcase_yaml           --测试用例数据
    utils                   --工具类
    venv                    --虚拟环境
    pytest.ini              --pytest配置文件
    all.py                  --执行总文件
    requirements.txt        --依赖包
---
## 安装依赖

    pip install requirements.txt
---
## 执行主文件

    在项目根目录运行"all.py"文件即可执行整个项目
---
## allure报告及配置文件参数说明

    详细内容请看"pytest配置文件说明.text"
---
## 核心思想
    主要的核心框架就是分层+PO模式（POM）。基础封装层BasePage，PO页面对象层，
    TestCase测试用例层。然后再加上日志处理logging模块,ini配置文件读取模块，
    pytest或unittest+ddt数据驱动模块等等
---
## 常用框架
- python+selenium+unittest+htmltestrunner
- python+pytest+allure
- robotframework+Selenium2Library
---

## 以后的发展方向
    python+pytest+allure+docker+svn/github+jenkins

