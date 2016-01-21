import muffin
import pytest


@pytest.fixture(scope='session')
def app(loop):
    return muffin.Application(
        'memcached_app', loop=loop,
        PLUGINS=('muffin_memcached',)
    )


def test_plugin_register(app):
    assert 'memcached' in app.ps
    assert app.ps.memcached.conn


@pytest.mark.async
def test_memcached_set_get(app):
    key = 'key'
    value = 'value'
    yield from app.ps.memcached.set(key, value)
    value_returned = yield from app.ps.memcached.get(key)
    assert value_returned == value


@pytest.mark.async
def test_memcached_set_get_with_dict(app):
    key = 'key'
    value = {'value': 'test'}
    yield from app.ps.memcached.set(key, value)
    value_returned = yield from app.ps.memcached.get(key)
    assert value_returned == value


@pytest.mark.async
def test_memcached_set_get_with_list(app):
    key = 'key'
    value = ['value', 'test']
    yield from app.ps.memcached.set(key, value)
    value_returned = yield from app.ps.memcached.get(key)
    assert value_returned == value
