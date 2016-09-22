# -*- coding: utf-8 -*-

#from bae.core.wsgi import WSGIApplication
#import django
import web

urls = (
        '/', 'index'
        )

class index:
    def GET(self):
        return "Hello, world!"


app = web.application(urls, globals())
app.run()

#application = WSGIApplication(app)


#import logging
#
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')

#
#class HelloWebapp2(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('hello web!\n')
# 

#class CallbackApi(webapp2.RequestHandler):
# 
#    def get(self):
##        logging.debug('recvice GET.')
##        text_log('recvice GET.')
#        self.response.write('recvice GET.')
#
#     
#    def post(self):
#        #接收微信的请求内容
##        logging.debug('recvice POST.')
#        data = self.request.body
##        logging.debug('POST data is: ' + data.replace('\n',''))
##        text_log('POST data is: ' + data.replace('\n',''))
#        self.response.write('recvice POST.')

 
#url config
#urls = [
#    ('/', HelloWebapp2),
##    ('/qiniu_upload_callback', CallbackApi),
#]
#  
#app = webapp2.WSGIApplication(urls, debug=True)
# 
#application = WSGIApplication(app)


#def text_log(msg):
#    import os
#    import time
#    if isinstance(msg, unicode):
#        msg = msg.encode('utf-8')
#    
#    fp = os.path.dirname(os.path.realpath(__file__))
#    # print fp
#    fp = os.path.abspath(os.path.join(fp, 'debug.log'))
#    # print fp
#    with open(fp, 'a') as f:
#        #Thu, 14 Aug 2014 12:55:55 CST,
#        # tt = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
#        tt = time.strftime("%a,%b%d,%Y %H:%M:%S", time.localtime())
#        try:
#            f.write('%s | %s\n' % (tt, msg))
#        except (RuntimeError, SystemError, IOError, TypeError, ValueError):
#            f.write('runtime error etc in writing to debug.log\n')
