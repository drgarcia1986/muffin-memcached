Muffin-Memcached
############

.. _description:

Muffin-Memcached -- A simple memcached plugin for muffin_ framework.

.. _badges:

.. image:: http://img.shields.io/travis/drgarcia1986/muffin-memcached.svg?style=flat-square
    :target: http://travis-ci.org/drgarcia1986/muffin-memcached
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/drgarcia1986/muffin-cache.svg?style=flat-square
    :target: https://coveralls.io/r/drgarcia1986/muffin-memcached
    :alt: Coverals

.. _requirements:

Requirements
=============

- python >= 3.4
- muffin >= 0.0.99

.. _installation:

Installation
=============

**Muffin-Memcached** should be installed using pip: ::

    pip install git+https://github.com/drgarcia1986/muffin-memcached.git

.. _usage:

Usage
=====

Add Muffin-Memcached_ and Muffin-Cache to muffin plugin list:

.. code-block:: python

    import muffin


    app = muffin.Application(
        'example',

        PLUGINS=(
            'muffin_memcached',
        )
    )

And use *memcached* plugin: 

.. code-block:: python

    @app.register('/cached')
    class Example(muffin.Handler):
        
        @asyncio.coroutine
        def get(self, request):
            value = yield from app.ps.memcached.get('foo')
            return value.decode()
    
.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/drgarcia1986/muffin-memcached/issues

.. _contributing:

Contributing
============

Development of Muffin-Memcached happens at: https://github.com/drgarcia1986/muffin-memcached


Contributors
=============

* drgarcia1986_ (Diego Garcia)

.. _license:

License
=======

Licensed under a `MIT license`_.

.. _links:


.. _muffin: https://github.com/klen/muffin
.. _drgarcia1986: https://github.com/drgarcia1986
.. _MIT license: http://opensource.org/licenses/MIT