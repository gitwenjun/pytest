from common.all_requests import RequestHandler
from common.assert_response import AssertResponse
from common.logs_handler import logger
from common.yaml_handler import YamlHandler


class ConselFmt:


    def __get_result(self,arg):
        name = arg["name"]
        method = arg["request"]["method"]
        url = arg["request"]["url"]
        headers = arg["request"]["headers"]
        paramse = arg["request"]["paramse"]
        session = YamlHandler().read_yaml("./data/session.yaml")
        if session:
            paramse["token"] = session["token"]
            paramse["uuid"] = session["uuid"]
        return name,method,url,paramse,headers

    def get_result_assert(self,args):
        name,method,url,paramse,headers = ConselFmt().__get_result(args)
        # logger.error(f"headers{headers}")
        res = RequestHandler().sent_request(method=method, url=url, params=paramse,headers=headers).json()
        res_exp = args["validata"][1]["contains"]["err_code"]
        # logger.debug(f"请求参数------{type(paramse)}")
        # logger.debug(f"响应我------{res}")
        res_act = res["data"]["err_code"]
        AssertResponse().assert_contains(name=name,method=method,url=url,parmase=paramse,response=res,response_exp=res_exp,response_act=res_act)