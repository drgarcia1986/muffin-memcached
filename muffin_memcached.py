import asyncio

import aiomcache
import jsonpickle
from muffin.plugins import BasePlugin


__version__ = "0.1.0"
__project__ = "muffin-memcached"
__author__ = "Diego Garcia <drgarcia1986@gmail.com>"
__license__ = "MIT"


class Plugin(BasePlugin):

    """ Connect to Memcached. """

    name = 'memcached'
    defaults = {
        'host': '127.0.0.1',
        'poolsize': 1,
        'port': 11211,
    }

    def __init__(self, *args, **kwargs):
        """ Initialize the Plugin. """
        super().__init__(*args, **kwargs)
        self.conn = None

    def setup(self, app):
        """ Setup self. """
        super().setup(app)
        self.cfg.port = int(self.cfg.port)
        self.cfg.poolsize = int(self.cfg.poolsize)

    @asyncio.coroutine
    def start(self, app):
        """ Connect to memcached. """
        self.conn = aiomcache.Client(
            host=self.cfg.host,
            port=self.cfg.port,
            pool_size=self.cfg.poolsize,
            loop=app.loop,
        )

    def finish(self, app):
        """ Close self connections. """
        self.conn.close()

    @asyncio.coroutine
    def get(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        value = yield from self.conn.get(key)
        if isinstance(value, bytes):
            return jsonpickle.decode(value.decode('utf-8'))
        return value

    @asyncio.coroutine
    def set(self, key, value, *args, **kwargs):
        if not isinstance(key, bytes):
            key = key.encode()
        value = jsonpickle.encode(value).encode()
        return (yield from self.conn.set(key, value, *args, **kwargs))

    def __getattr__(self, name):
        """ Proxy attribute to self connection. """
        return getattr(self.conn, name)
