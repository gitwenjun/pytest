import os

BasePath = os.path.dirname(os.path.dirname(__file__)).replace("/",r"\\")

Log_Path = os.path.join(BasePath,"logs")
Report_Path = os.path.join(BasePath,"report")
Data_Path = os.path.join(BasePath,"data")