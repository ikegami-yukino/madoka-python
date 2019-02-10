madoka
===========

|travis| |coveralls| |pyversion| |version| |license|

Madoka is an implementation of a Count-Min sketch data structure for summarizing data streams.

String-int pairs in a Madoka-Sketch may take less memory than in a standard Python dict, Counter, Redis.

Counting error rate is about 0.0911 %

More details are described in `Benchmark.ipynb`_

.. _Benchmark.ipynb: https://github.com/ikegami-yukino/madoka-python/blob/master/Benchmark.ipynb

This module is based on `madoka`_ C++ library.

.. _madoka: https://github.com/s-yata/madoka

NOTE: Madoka-Sketch does not have index of keys. so Madoka-Sketch can not dump all keys such as Python dict's `dict.keys()`. However, when set `k` parameter to costructer, `most_common` method (returns key and value as many as `k`) is available.

Contributions are welcome!

Installation
============

::

 $ pip install madoka

Class
============

Madoka has some classes having same interface. These classes are vary in value data type. So you can choose for your purpose.

For example, if you wants to count float data, it's preferable to choose CroquisFloat class or CroquisDouble class.

- Sketch
  - storing unsigned long long (64bit) and fast implementation
- CroquisFloat
  - storing float (32bit)
- CroquisDouble
  - storing double (64bit)
- CroquisUint8
  - storing unsigned char (8bit)
- CroquisUint16
  - storing unsigned short (16bit)
- CroquisUint32
  - storing unsigned int (32bit)
- CroquisUint64
  - storing unsigned long long (64bit)

Usage
=====

From here, I will describe about Sketch class.
But, Croquis classes have also same interfaces mostly.
So you can use other classes by the same way as Sketch class.
In that case, you should replace to intended class from "Sketch".


Create a new sketch
--------------------------------------------

.. code:: python

 >>> import madoka
 >>> sketch = madoka.Sketch()

- Sketch madoka.Sketch([width=1048576, max_value=35184372088831, path='', flags=0, seed=0, k=5])

  - `width` is a size of register. If you are worrying about gap, you should increase `width` value. The larger `width` is, the fewer mistakes madoka makes in estimating value. But, the larger `width` is, the larger memory consumption is.

  - Permission of `path` should be 644

  - `k` means Top-K used by `most_common` method. if you don't want to use `most_common` method, then I recommend to set `k=0` so it is slightly fast.

  - `madoka.Sketch()` calls `madoka.Sketch.create()`, so you don't have to explicitly call `create()` in initialization


Increment a key value
--------------------------------------------

.. code:: python

 >>> sketch['mami'] += 1

or

.. code:: python

 >>> sketch.inc('mami')


- int inc(key[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Add a value to the current key value
--------------------------------------------

.. code:: python

 >>> sketch['mami'] += 6

or

.. code:: python

 >>> sketch.add('mami', 6)


- int add(key, value[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.



Update a key value
--------------------------------------------

.. code:: python

 >>> sketch['mami'] = 6

or

.. code:: python

 >>> sketch.set('mami', 6)


- void set(key, value[, key_length=0])

  * Note that `set()` does nothing when the given value is not greater than the current key value.

  * Also note that the new value is saturated when the given value is greater than the upper limit.

  * Additionally note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.


Get a key value
--------------------------------------------

.. code:: python

 >>> sketch['mami']

or

.. code:: python

 >>> sketch.get('mami')


- int get(key[, key_length=0])

  - Note that `key_length` is automatically determined when not giving `key_length`. Thus, the order of parameters differs from original madoka C++ library.

Get all values
--------------------------------------------

.. code:: python

 >>> sketch.values()


- generator<int> values()

  - Note that processing time increases according to sketch's width. But this method may be slow, so I recommend setting width to less than 1000000 when creating sketch.

Save a sketch to a file
--------------------------------------------

.. code:: python

 >>> sketch.save('example.madoka')

- void save(path)

  - Permission of `path` should be 644

Load a sketch from a file
--------------------------------------------

.. code:: python

 >>> sketch.load('example.madoka')

- void load(path)

  - Permission of `path` should be 644

Clear a sketch
--------------------------------------------

.. code:: python

 >>> sketch.clear()

- void clear()

  * Delete all key-value pairs. It differs from `create()` in maintaining current settings.


Initialize a sketch with settings change
--------------------------------------------

.. code:: python

 >>> sketch.create()

- void create([width=0, max_value=0, path=NULL, flags=0, seed=0])

  - Permission of file given to `path` should be 644

Copy a sketch
--------------------------------------------

.. code:: python

 >>> sketch.copy(othersketch)

- void copy(Sketch)


Merge two sketches
--------------------------------------------

.. code:: python

 >>> sketch += other_sketch

or

.. code:: python

 >>> sketch.merge(othersketch)

- void merge(Sketch[, lhs_filter=None, rhs_filter=None])

  - lhs_filter is applied for self.sketch, rhs_filter is applied for given sketch


Shrink a sketch
--------------------------------------------

.. code:: python

 >>> sketch.shrink(sketch, width=1000)

- void shrink(Sketch[, width=0, max_value=0, filter=None, path=None, flags=0])

  - When width > 0, width must be less than source sketch

  - Permission of `path` should be 644


Get summed sketch
-----------------------

.. code:: python

 >>> summed_sketch = sketch + other_sketch

- Create summed sketch, So it does not break original sketches

Get summed sketch by dict
--------------------------

.. code:: python

 >>> summed_sketch = sketch + {'mami': 1, 'kyoko': 2}

- Create summed sketch, So it does not break original sketches


Check whether sketch contains key value
-----------------------------------------

.. code:: python

 >>> 'mami' in sketch


Get inner product of two sketches
--------------------------------------------

.. code:: python

 >>> sketch.inner_product(other_sketch)

- list<float> inner_product(Sketch)

  - Returns [inner product, square length of left hands sketch (float), square length of right hands sketch (float)]

Get median value
--------------------------------------------

.. code:: python

 >>> sketch['madoka'] = 1
 >>> sketch['mami'] = 2
 >>> sketch['sayaka'] = 3
 >>> sketch['kyouko'] = 4
 >>> sketch['homura'] = 5
 >>> sketch.median()  # => 3

- int or float median()

Apply filter into all values
--------------------------------------------

.. code:: python

 >>> sketch.filter(lambda x: x + 1)

- void filter(Callable[, apply_zerovalue=False])

  - If apply_zerovalue = True, filter_method is applied also 0 values (It may be slow) (from version 0.6 or later)

  - Note that processing time increases according to sketch's width. If you feel this method is slow, I recommend setting width to less than 1000000 when creating sketch

Set values from dict
--------------------------------------------

.. code:: python

 >>> sketch.fromdict({'mami': 14, 'madoka': 13})

or

.. code:: python

 >>> sketch += {'mami': 14, 'madoka': 13}


- void fromdict(dict)

Get most common keys
--------------------------------------------

.. code:: python

 >>> sketch.most_common()

- generator most_common([k=5])

  - returns key-value pair as many as `k`

  - Note that this method is required to set `k` parameter in constructer.

License
=========

- Wrapper code is licensed under New BSD License.
- Bundled `madoka`_ C++ library is licensed under the Simplified BSD License.


.. |travis| image:: https://travis-ci.org/ikegami-yukino/madoka-python.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/madoka-python
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/madoka-python/badge.svg
    :target: https://coveralls.io/r/ikegami-yukino/madoka-python
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/madoka.svg

.. |version| image:: https://img.shields.io/pypi/v/madoka.svg
    :target: http://pypi.python.org/pypi/madoka/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/madoka.svg
    :target: http://pypi.python.org/pypi/madoka/
    :alt: license
