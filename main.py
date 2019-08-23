import cherrypy
from datetime import datetime, timedelta
from random import randrange

cherrypy.config.update({'server.socket_port': 9090, 'server.socket_host':'0.0.0.0'})
VIENTO=['NORTE','NOR ESTE','ESTE','SUR ESTE', 'SUR','SUR OESTE','OESTE','NOR OESTE','NORTE']

def create_key_value():
    now = datetime.now()
    minute = int('{}0'.format(now.minute//10))
    now = now.replace(minute=minute, second=0, microsecond=0) 
    context = {}
    from_time = now - timedelta(hours=24)
    while now > from_time:
        context['{}'.format(now)]={'v':randrange(185,245)/10.0,
                                    'i':randrange(0,300)/10.0,
                                    'w_s':randrange(150,950)/10.0,
                                    'w_d':VIENTO[randrange(0,7)]}
        now = now - timedelta(minutes=10)
    return context

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return create_key_value()

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')
