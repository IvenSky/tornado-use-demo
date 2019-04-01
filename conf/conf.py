import logging

#Index Server Setting

INDEX_SERVER_PORT = 8070
INDEX_SERVER_REG = r"/index"

#Log Setting
#默认日志启动等级
LOG_LEVEL=logging.DEBUG 
#日志内容格式
LOG_FMAT="%(asctime)s %(levelname)-7s  %(message)s"
#日志文件存储路径及文件名前缀
LOG_FILE="./logs/devinfo.log"
LOG_FILE_MR=""
LOG_FILE_FM=""
LOG_SUFFIX="%y%m%d%H"
#日志文件滚动间隔时间 "H" 小时 "D"天
LOG_WHEN="H"
LOG_INTERV=1
#最大日志文件保留数量
LOG_BAKCOUNT=12
