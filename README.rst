madoka
===========
.. image:: https://badge.fury.io/py/madoka.png
    :target: http://badge.fury.io/py/madoka
.. image:: https://travis-ci.org/ikegami-yukino/madoka-python.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/madoka-python

Madoka is an implementation of a Count-Min sketch data structure for summarizing data streams.

String-int pairs in a Madoka-Sketch may take less memory than in a standard Python dict.

Based on `madoka`_ C++ library.

.. _madoka: https://github.com/s-yata/madoka

NOTE: Madoka-Sketch does not have index of keys. so Madoka-Sketch can not dump all keys such as Python dict's `dict.keys()`.


Installation
============

::

 $ pip install madoka


Usage
=====

Create a new sketch
--------------------------------------------

::

 >>> import madoka
 >>> sketch = madoka.Sketch()


- Sketch madoka.Sketch([width=0, max_value=0, path='', flags=0, seed=0])

  - `madoka.Sketch()` calls `madoka.Sketch.create()`, so you don't have to explicitly call `create()`


Increment a key value
--------------------------------------------

::

 >>> sketch['mami'] += 1
 
or

:: 

 >>> sketch.inc('mami')


- int inc(key[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Add a value to the current key value
--------------------------------------------

::

 >>> sketch['mami'] += 6
 
or

::

 >>> sketch.add('mami', 6)


- int add(key, value[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Update a key value
--------------------------------------------

::

 >>> sketch['mami'] = 6
 
or

::

 >>> sketch.set('mami', 6)


- void set(key, value[, key_length=0])

  * Note that `set()` does nothing when the given value is not greater than the current key value.

  * Also note that the new value is saturated when the given value is greater than the upper limit.

  * Additionally note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Get a key value
--------------------------------------------

::

 >>> sketch['mami']
 
or

::

 >>> sketch.get('mami')


- int get(key[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.

Get all values
--------------------------------------------

::

 >>> sketch.values()


- generator<int> values()

  - Note that processing time increases according to sketch's width. If you feel slow, I recommend setting width to less than 1000000 when creating sketch.

Save a sketch to a file
--------------------------------------------

::

 >>> sketch.save('example.madoka')

- void save(filename)


Load a sketch from a file
--------------------------------------------

::

 >>> sketch.load('example.madoka')

- void load(filename)


Clear a sketch
--------------------------------------------

::

 >>> sketch.clear()

- void clear()

  * Delete all key-value pairs. It differs from create() in maintaining current settings.


Initialize a sketch with settings change
--------------------------------------------

::

 >>> sketch.create()

- void create([width=0, max_value=0, path=NULL, flags=0, seed=0])


Copy a sketch
--------------------------------------------

::

 >>> sketch.copy(othersketch)

- void copy(Sketch)


Merge two sketches
--------------------------------------------

::

 >>> sketch += other_sketch

or

::

 >>> sketch.merge(othersketch)

- void merge(Sketch[, lhs_filter=None, rhs_filter=None])

  - lhs_filter is applied for self.sketch, rhs_filter is applied for given sketch


Shrink a sketch
--------------------------------------------

::

 >>> sketch.shrink(sketch, width=1000)

- void shrink(Sketch[, width=0, max_value=0, filter=None, path=None, flags=0])

  - When width > 0, width must be less than source sketch


Get summed sketch
-----------------------

::

 >>> summed_sketch = sketch + other_sketch

- It does not break original sketches

Check whether sketch contains key value
-----------------------------------------

::

 >>> 'mami' in sketch


Get inner product of two sketches
--------------------------------------------

::

 >>> sketch.inner_product(other_sketch)

- int inner_product(Sketch)

Apply filter into all values
--------------------------------------------

::

 >>> sketch.filter(lambda x: x + 1)

- void filter(Callable[, only_nonzero=False])

  - Note that processing time increases according to sketch's width. If you feel this method is slow, I recommend setting width to less than 1000000 when creating sketch

Set values from dict
--------------------------------------------

::

 >>> sketch.fromdict({'mami': 14, 'madoka': 13})

- void fromdict(dict)

TODO
=========

- Implement getting sketch length on inner_product method
- Support storing float or double value by Croquis class

Contributions are welcome!


License
=========

- Wrapper code is licensed under New BSD License.
- Bundled `madoka`_ C++ library is licensed under the Simplified BSD License.


