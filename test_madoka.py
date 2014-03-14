# -*- coding: utf-8 -*-
from nose.tools import eq_, ok_
import madoka
import os


class Test_madoka(object):

    def test_inc(self):
        sketch = madoka.Sketch()
        sketch.inc('mami', 3)
        eq_(1, sketch.get('mami', 3))
        sketch.inc('mami', 3)
        eq_(2, sketch.get('mami', 3))

    def test_add(self):
        sketch = madoka.Sketch()
        sketch.add('mami', 3, 2)
        eq_(2, sketch.get('mami', 3))
        sketch.add('mami', 3, 8)
        eq_(10, sketch.get('mami', 3))

    def test_set(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 3, 14)
        eq_(14, sketch.get('mami', 3))

    def test_clear(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 3, 14)
        sketch.clear()
        eq_(0, sketch.get('mami', 3))

    def test_create(self):
        sketch = madoka.Sketch()
        sketch.create(max_value=4)
        sketch.set('mami', 3, 100)
        eq_(15, sketch.get('mami', 3))

    def test_copy(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 3, 14)

        new_sketch = madoka.Sketch()
        new_sketch.copy(sketch)
        eq_(14, new_sketch.get('mami', 3))

    def test_merge(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 3, 14)

        new_sketch = madoka.Sketch()
        new_sketch.set('mami', 3, 14)

        new_sketch.merge(sketch)
        eq_(28, new_sketch.get('mami', 3))

    def test_inner_product(self):
        sketch = madoka.Sketch()
        sketch.set('mami', 3, 2)
        sketch.set('homura', 3, 1)
        sketch.set('kyouko', 3, 2)
        sketch.set('sayaka', 3, 2)

        new_sketch = madoka.Sketch()
        new_sketch.set('mami', 3, 2)
        new_sketch.set('kyouko', 3, 3)
        new_sketch.set('sayaka', 3, 10)

        eq_(30, new_sketch.inner_product(sketch))

    def test_save_and_load(self):
        try:
            filename = 'test.madoka'
            sketch = madoka.Sketch()
            sketch.set('mami', 3, 14)
            sketch.save(filename)
            ok_(os.path.exists(filename))

            sketch = madoka.Sketch()
            sketch.load(filename)
            eq_(14, sketch.get('mami', 3))
        finally:
            os.remove(filename)
