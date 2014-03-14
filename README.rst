madoka
===========

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
-----------------------------

::

 >>> import madoka
 >>> sketch = madoka.Sketch()


- madoka.Sketch(width=0, max_value=0, path=NULL, flags=0, seed=0)

  - `madoka.Sketch()` calls `madoka.Sketch.create()`, so you don't have to explicitly call `create()`


Increment a key value
-----------------------------

::

 >>> sketch.inc('mami')


- inc(key[, key_length])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Add a value to the current key value
---------------------------------

::

 >>> sketch.add('mami', 6)


- add(key, value[, key_length])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Update a key value
-----------------------------

::

 >>> sketch.set('mami', 6)


- set(key, value[, key_length])

  * Note that `set()` does nothing when the given value is not greater than the current key value.

  * Also note that the new value is saturated when the given value is greater than the upper limit.

  * Additionally note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Get a key value
-----------------------------

::

 >>> sketch.get('mami')


- get(key[, key_length])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Save a sketch to a file
-----------------------------

::

 >>> sketch.save('example.madoka')

- save(filename)


Load a sketch from a file
-------------------------------

::

 >>> sketch.save('example.madoka')

- save(filename)


Clear a sketch
-----------------------------

::

 >>> sketch.clear()

- clear()

  * Delete all key-value pairs. It differs from create() in maintaining settings.


Initialize a sketch with settings change
--------------------------------------------

::

 >>> sketch.create()

- create(width=0, max_value=0, path=NULL, flags=0, seed=0)


Copy a sketch
-----------------------------

::

 >>> sketch.copy(othersketch)

- copy(Sketch)

Merge two sketches
-----------------------------

::

 >>> sketch.merge(othersketch)

- merge(Sketch)


Get inner product of two sketches
----------------------------------------

::

 >>> sketch.inner_product(othersketch)

- inner_product(Sketch)


TODO
======================
* Filter function performing same behavior with original C++ madoka library

Contributions are welcome!

License
=========
- Wrapper code is licensed under New BSD License.
- Bundled `madoka`_ C++ library is licensed under the Simplified BSD License.

