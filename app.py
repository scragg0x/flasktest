from gevent import monkey, pywsgi 
monkey.patch_all()
import logging
from lastdb import app

if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    pywsgi.WSGIServer(('', 8000), app).serve_forever()
