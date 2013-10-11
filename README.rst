madoka
===========

Madoka is an implementation of a Count-Min sketch, a data structure for summarizing data streams.

String-int pairs in a Madoka-Sketch may take less memory than in a standard Python dict.

Based on `madoka`_ C++ library.

.. _madoka: https://github.com/s-yata/madoka

Installation
============

::

    pip install madoka

Usage
=====

Create a new sketch::

    >>> import madoka
    >>> sketch = madoka.Sketch()
    >>> sketch.create()

create(width = 0, max_value = 0, path = NULL, flags = 0, seed = 0)


Increment a key value::

    >>> sketch.inc('mami', 6)

inc(key, byte_size)
In this example, the value of the key 'mami' is 4 at this time.


Add a value to current key value::

    >>> sketch.add('mami', 6, 3)

add(key, byte_size, value)
The byte_size argument is a range of a value.
In this example, the value of the key 'mami' is 3.


Update a key value::

    >>> sketch.set('mami', 6, 2)

set(key, byte_size, value)
Note that set() does nothing when the given value is not greater than the current key value.
Also note that the new value is saturated when the given value is greater than the upper limit.


Get a key value::

    >>> sketch.get('mami', 6)

get(key, byte_size)
In this example, return 4 as the value of the key 'mami'.


Save a sketch to a file::

    >>> sketch.save('example.madoka')

save(filename)


Load a sketch from a file::

    >>> sketch.save('example.madoka')

save(filename)


Clear a sketch::

    >>> sketch.clear()


Copy a sketch::

    >>> sketch.copy(othersketch)

copy(Sketch)

Merge two sketches::

    >>> sketch.merge(othersketch)

merge(Sketch)


Get inner product of two sketches::

    >>> sketch.inner_product(othersketch)

inner_product(Sketch)


Current limitations
===================

* ``Sketch.filter()`` doesn't work;

Contributions are welcome!

License
=======

Wrapper code is licensed under New BSD License.
Bundled `madoka`_ C++ library is licensed under the Simplified BSD License.

