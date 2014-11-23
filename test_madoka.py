# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_true
import madoka
import os


class MadokaTest(object):

    def test___contains__(self):
        sketch = self.target_class(width=100)
        sketch.add('mami', 1)
        assert_true('mami' in sketch)

    def test___setitem__(self):
        sketch = self.target_class(width=100)
        sketch['mami'] += 20
        assert_equal(sketch.get('mami'), 20)
        sketch['mami'] *= 2
        assert_equal(sketch.get('mami'), 40)

    def test___getitem__(self):
        sketch = self.target_class(width=100)
        sketch.set('mami', 1)
        assert_equal(sketch['mami'], 1)

    def test___add__(self):
        sketch = self.target_class(width=100)
        sketch.inc('mami')
        other_sketch = self.target_class(width=100)
        other_sketch.inc('mami')
        new_sketch = sketch + other_sketch
        assert_equal(new_sketch['mami'], 2)
        assert_equal(sketch['mami'], 1)
        assert_equal(other_sketch['mami'], 1)

    def test___iadd__(self):
        sketch = self.target_class(width=100)
        sketch.inc('mami')
        other_sketch = self.target_class(width=100)
        other_sketch.inc('mami')
        sketch += other_sketch
        assert_equal(sketch['mami'], 2)
        assert_equal(other_sketch['mami'], 1)

    def test_add(self):
        sketch = self.target_class(width=100)
        sketch.add('mami', 2)
        assert_equal(sketch['mami'], 2)
        sketch.add('mami', 8)
        assert_equal(sketch['mami'], 10)
        sketch['mami'] += 10
        assert_equal(sketch['mami'], 20)

    def test_set(self):
        sketch = self.target_class(width=100)
        sketch.set('mami', 14)
        assert_equal(sketch['mami'], 14)

    def test_inc(self):
        sketch = self.target_class(width=100)
        sketch.inc('mami')
        assert_equal(sketch['mami'], 1)
        sketch.inc('mami')
        assert_equal(sketch['mami'], 2)

    def test_clear(self):
        sketch = self.target_class(width=100)
        sketch['mami'] = 14
        sketch.clear()
        assert_equal(sketch['mami'], 0)

    def test_create(self):
        sketch = self.target_class(width=100)
        sketch.create()
        sketch['mami'] = 14
        assert_equal(sketch['mami'], 14)

    def test_fromdict(self):
        sketch = self.target_class(width=100)
        src_dict = {'mami': 14, 'madoka': 13}
        sketch.fromdict(src_dict)
        assert_equal(sketch['mami'], 14)

    def test_save_and_load(self):
        try:
            filename = 'test.madoka'
            sketch = self.target_class(width=100)
            sketch['mami'] = 14
            sketch.save(filename)
            assert_true(os.path.exists(filename))

            sketch = self.target_class(width=100)
            sketch.load(filename)
            assert_equal(sketch['mami'], 14)
            sketch = self.target_class(width=100)
            sketch.open(filename)
            assert_equal(sketch['mami'], 14)
        finally:
            os.remove(filename)

    def test_copy(self):
        sketch = self.target_class(width=100)
        sketch['mami'] = 14

        new_sketch = self.target_class(width=100)
        new_sketch.copy(sketch)
        assert_equal(new_sketch['mami'], 14)

    def test_inner_product(self):
        sketch = self.target_class(width=100)
        sketch['mami'] = 2
        sketch['homura'] = 1
        sketch['kyouko'] = 2

        new_sketch = self.target_class(width=100)
        new_sketch['mami'] = 2
        new_sketch['kyouko'] = 3
        got = sketch.inner_product(new_sketch)
        assert_equal(got, [10, 9, 13])

    def test_filter(self):
        sketch = self.target_class(width=100)
        sketch['mami'] = 2
        filter_method = lambda x: x * 2
        sketch.filter(filter_method)
        assert_equal(sketch['mami'], 4)
        sketch.filter(filter_method, only_nonzero=True)
        assert_equal(sketch['mami'], 8)

    def test_merge(self):
        sketch = self.target_class(width=1000)
        sketch['mami'] = 14
        new_sketch = self.target_class(width=1000)
        new_sketch['mami'] = 14
        new_sketch.merge(sketch)
        assert_equal(new_sketch['mami'], 28)

    def test_shrink(self):
        sketch = self.target_class(width=10000)
        sketch['mami'] = 2
        sketch.shrink(sketch, width=1000)
        assert_equal(sketch['mami'], 2)
        assert_equal(sketch.width, 1000)

    def test_values(self):
        sketch = self.target_class(width=100)
        sketch['mami'] = 2
        sketch['madoka'] = 3
        got = [i for i in sketch.values()]
        assert_equal(set(got), set([2, 3]))

    def test_with_statement(self):
        with self.target_class() as m:
            m['test'] += 1
        assert_true(True)


class Test_Sketch(MadokaTest):

    def __init__(self):
        self.target_class = madoka.Sketch

    def test_merge(self):
        sketch = madoka.Sketch(width=1000)
        sketch['mami'] = 14
        new_sketch = madoka.Sketch(width=1000)
        new_sketch['mami'] = 14
        new_sketch.merge(sketch)
        assert_equal(new_sketch['mami'], 28)

        filter_method = lambda x: x // 10
        new_sketch.merge(new_sketch, filter_method, filter_method)
        assert_equal(new_sketch['mami'], 4)

    def test_shrink(self):
        sketch = madoka.Sketch(width=10000)
        sketch['mami'] = 2
        sketch.shrink(sketch, width=1000, max_value=100)
        assert_equal(sketch['mami'], 2)
        assert_equal(sketch.width, 1000)
        filter_method = lambda x: x * 2
        sketch.shrink(sketch, width=100, max_value=100,
                      filter_method=filter_method)
        assert_equal(sketch['mami'], 4)


class Test_CroquisUint8(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisUint8


class Test_CroquisUint16(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisUint16


class Test_CroquisUint32(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisUint32


class Test_CroquisUint64(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisUint64


class Test_CroquisFloat(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisFloat


class Test_CroquisDouble(MadokaTest):

    def __init__(self):
        self.target_class = madoka.CroquisDouble
