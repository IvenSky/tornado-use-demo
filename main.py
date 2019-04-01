import tornado.ioloop
import tornado.web
import tornado.options
import conf.conf  as cfg
from common.log import logger
from tornado.options import define, options
from HttpReqHandler import IndexHandler

define("port",default=cfg.INDEX_SERVER_PORT,help="server listening port",type=int)

application = tornado.web.Application([(cfg.INDEX_SERVER_REG,IndexHandler),])

def start():
	tornado.options.parse_command_line()
	application.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	start()
	logger.debug("服务开启 .....")
