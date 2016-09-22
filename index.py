# -*- coding: utf-8 -*-

import web

import logging

logging.basicConfig(filename='webpy.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')

urls = (
        '/', 'index',
	'/upload_callback', 'index'
        )


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class index:
    def GET(self):
        return "Hello, world!"
    def POST(self):
	data = web.input()
	return "received post %s" % data

if __name__ == '__main__' :
    app = web.application(urls, globals())
    app.run()


