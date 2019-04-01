import logging
import tornado.web
import conf.conf  as cfg
from logging.handlers import TimedRotatingFileHandler

class mylog():
	def __init__(self,appname,logfile):
		formatter = logging.Formatter(cfg.LOG_FMAT)
		self.RtHandler = TimedRotatingFileHandler(filename=logfile,when=cfg.LOG_WHEN,interval=cfg.LOG_INTERV,backupCount=cfg.LOG_BAKCOUNT)
		self.RtHandler.suffix = cfg.LOG_SUFFIX
		self.logger = logging.getLogger(appname)
		self.logger.setLevel(logging.DEBUG)
		self.logger.addHandler(self.RtHandler)
		
	def __fel__(self):
		self.logger.removeHandler(self.RtHandler)

log = mylog('__name__',cfg.LOG_FILE)	
logger = log.logger 	
