import logging

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
)

from config import Config
from app import create_app

if __name__ == '__main__':
    app = create_app()
    print(f'Proxy service starting on 0.0.0.0:{Config.PROXY_PORT}')
    print(f'Target: {Config.PROXY_TARGET_URL}')

    from gevent.pywsgi import WSGIServer
    server = WSGIServer(
        ('0.0.0.0', Config.PROXY_PORT),
        app,
    )
    server.serve_forever()
