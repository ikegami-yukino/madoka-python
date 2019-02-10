CHANGES
========

0.7.1 (2018-02-11)
------------------

- Fix bug for Python 2.7


0.7 (2018-02-11)
----------------

- Support Python 3.5 - 3.7
- Unsupport Python 2.6
- Add `most_common()` function (requiring to give `k=n` parameter to constructer)
- Add `median()` function
- Fixed a bug that madoka::FILE_PRELOAD does not work

0.6 (2014-11-23)
----------------

- Support Python 3.4
- Improve processing time of `inner_product()`
- Fix `shrink()` method bug
- Change `filter()` methods param
- Support with-statement
- Implement increment-add from dict
  - (e.g.) summed_sketch = sketch + dict; sketch += dict


0.5 (2014-04-08)
----------------

- Add Croquis classes handling some data types (e.g., float, uint8)
- Given length=True to inner product method, returns also square length of both left hands and right hands sketch
- Add fromdict method

0.4 (2014-03-30)
----------------

- Implement dict-like interface (e.g., sketch['key'])
- Add filter() method
- Add values() method for dumping all values

0.3 (2014-03-14)
----------------

- Key length is automatically determined when it is not given
- Remove filter function
- Slightly decreasing amount of memory usage

0.2 (2013-10-12)
----------------

Simplify the step of creating new sketch.

0.1 (2013-10-11)
----------------

Initial release.

