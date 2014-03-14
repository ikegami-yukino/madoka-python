# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_true
import madoka
import os


class Test_madoka(object):

    def test_inc(self):
        sketch = madoka.Sketch()
        sketch.inc('mami')
        assert_equal(1, sketch.get('mami'))
        sketch.inc('mami')
        assert_equal(2, sketch.get('mami'))

    def test_add(self):
        sketch = madoka.Sketch()
        sketch.add('mami', 2)
        assert_equal(2, sketch.get('mami'))
        sketch.add('mami', 8)
        assert_equal(10, sketch.get('mami'))

    def test_set(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 14)
        assert_equal(14, sketch.get('mami'))

    def test_clear(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 14)
        sketch.clear()
        assert_equal(0, sketch.get('mami'))

    def test_create(self):
        sketch = madoka.Sketch()
        sketch.create(max_value=4)
        sketch.set('mami', 100)
        assert_equal(15, sketch.get('mami'))

    def test_copy(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 14)

        new_sketch = madoka.Sketch()
        new_sketch.copy(sketch)
        assert_equal(14, new_sketch.get('mami'))

    def test_merge(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 14)

        new_sketch = madoka.Sketch()
        new_sketch.set('mami', 14)

        new_sketch.merge(sketch)
        assert_equal(28, new_sketch.get('mami'))

    def test_inner_product(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 2)
        sketch.set('homura', 1)
        sketch.set('kyouko', 2)
        sketch.set('sayaka', 2)

        new_sketch = madoka.Sketch()
        new_sketch.set('mami', 2)
        new_sketch.set('kyouko', 3)
        new_sketch.set('sayaka', 10)

        assert_equal(30, new_sketch.inner_product(sketch))

    def test_save_and_load(self):
        try:
            filename = 'test.madoka'
            sketch = madoka.Sketch()
            sketch.set('mami', 14)
            sketch.save(filename)
            assert_true(os.path.exists(filename))

            sketch = madoka.Sketch()
            sketch.load(filename)
            assert_equal(14, sketch.get('mami'))
            sketch = madoka.Sketch()
            sketch.open(filename)
            assert_equal(14, sketch.get('mami'))
        finally:
            os.remove(filename)
