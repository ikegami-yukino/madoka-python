# -*- coding: utf-8 -*-
import numbers
import os
import tempfile

import pytest

import madoka


@pytest.fixture
def target_classes():
    return [madoka.Sketch, madoka.CroquisUint8, madoka.CroquisUint16,
            madoka.CroquisUint32, madoka.CroquisUint64,
            madoka.CroquisFloat, madoka.CroquisDouble]


class TestMadoka():

    def test___len__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            assert isinstance(len(sketch), numbers.Integral)

    def test___contains__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.add('mami', 1)
            assert 'mami' in sketch

    def test___setitem__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] += 20
            assert sketch.get('mami') == 20
            sketch['mami'] *= 2
            assert sketch.get('mami') == 40

    def test___getitem__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.set('mami', 1)
            assert sketch['mami'] == 1

    def test___add__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.inc('mami')
            other_sketch = cls(width=100)
            other_sketch.inc('mami')
            new_sketch = sketch + other_sketch
            assert new_sketch['mami'] == 2

            new_sketch = sketch + {'mami': 1, 'madoka': 2}
            assert new_sketch['mami'] == 2

    def test___iadd__(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.inc('mami')
            other_sketch = cls(width=100)
            other_sketch.inc('mami')
            sketch += other_sketch
            assert sketch['mami'] == 2
            assert other_sketch['mami'] == 1

            sketch = cls(width=100)
            sketch.inc('mami')
            sketch += {'mami': 2}
            assert sketch['mami'] == 3

    def test_add(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.add('mami', 2)
            assert sketch['mami'] == 2
            sketch.add('mami', 8)
            assert sketch['mami'] == 10
            sketch['mami'] += 10
            assert sketch['mami'] == 20

    def test_set(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.set('mami', 14)
            assert sketch['mami'] == 14

    def test_inc(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.inc('mami')
            assert sketch['mami'] == 1
            sketch.inc('mami')
            assert sketch['mami'] == 2

    def test_clear(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 14
            sketch.clear()
            assert sketch['mami'] == 0

    def test_create(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch.create()
            sketch['mami'] = 14
            assert sketch['mami'] == 14

    def test_fromdict(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            src_dict = {'mami': 14, 'madoka': 13}
            sketch.fromdict(src_dict)
            assert sketch['mami'] == 14

    def test_save_and_load(self, target_classes):
        try:
            for cls in target_classes:
                sketch_file = tempfile.mktemp()

                sketch = cls(width=100)
                sketch['mami'] = 14
                sketch.save(sketch_file)
                assert os.path.exists(sketch_file)

                sketch = cls(width=100)
                sketch.load(sketch_file)
                assert sketch['mami'] == 14
                sketch = cls(width=100)
                sketch.open(sketch_file)
                assert sketch['mami'] == 14
        finally:
            del sketch
            os.remove(sketch_file)

    def test_copy(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 14

            new_sketch = cls(width=100)
            new_sketch.copy(sketch)
            assert new_sketch['mami'] == 14

    def test_inner_product(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 2
            sketch['homura'] = 1
            sketch['kyouko'] = 2

            new_sketch = cls(width=100)
            new_sketch['mami'] = 2
            new_sketch['kyouko'] = 3
            got = sketch.inner_product(new_sketch)
            assert got == [10, 9, 13]

    def test_median(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 1
            sketch['madoka'] = 2
            sketch['sayaka'] = 3
            sketch['kyouko'] = 4
            sketch['homura'] = 5
            assert sketch.median() == 3

    def test_filter(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 2
            filter_method = lambda x: x * 2
            sketch.filter(filter_method)
            assert sketch['mami'] == 4

            sketch = cls(width=100)
            sketch['mami'] = 2
            neg_sign = lambda x: 0 if x else 1
            sketch.filter(neg_sign, apply_zerovalue=True)
            assert sketch['mami'] == 0
            assert sketch['homura'] == 1

    def test_merge(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=1000)
            sketch['mami'] = 14
            new_sketch = cls(width=1000)
            new_sketch['mami'] = 14
            new_sketch.merge(sketch)
            assert new_sketch['mami'] == 28

    def test_shrink(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=10000)
            sketch['mami'] = 2
            sketch.shrink(sketch, width=1000)
            assert sketch['mami'] == 2
            assert sketch.width == 1000

    def test_values(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 2
            sketch['madoka'] = 3
            got = [i for i in sketch.values()]
            assert set(got) == set([2, 3])

    def test_most_common(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            sketch['mami'] = 14
            sketch['madoka'] = 13
            sketch['sayaka'] = 13
            got = list(sketch.most_common())
            assert got == [('mami', 14), ('sayaka', 13), ('madoka', 13)]

    def test_with_statement(self, target_classes):
        for cls in target_classes:
            opened = False
            with cls() as m:
                m['test'] += 1
                opened = True
            assert opened

    def test_width_mask(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            assert isinstance(sketch.width_mask, numbers.Integral)

    def test_value_size(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            assert isinstance(sketch.value_size, numbers.Integral)

    def test_table_size(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            assert isinstance(sketch.table_size, numbers.Integral)

    def test_flags(self, target_classes):
        for cls in target_classes:
            sketch = cls(width=100)
            assert isinstance(sketch.flags, numbers.Integral)


class Test_Sketch:

    def test_merge(self):
        sketch = madoka.Sketch(width=1000)
        sketch['mami'] = 14
        new_sketch = madoka.Sketch(width=1000)
        new_sketch['mami'] = 14
        new_sketch.merge(sketch)
        assert new_sketch['mami'] == 28

        filter_method = lambda x: x // 10
        new_sketch.merge(new_sketch, filter_method, filter_method)
        assert new_sketch['mami'] == 4

    def test_shrink(self):
        sketch = madoka.Sketch(width=10000)
        sketch['mami'] = 2
        sketch.shrink(sketch, width=1000, max_value=100)
        assert sketch['mami'] == 2
        assert sketch.width == 1000
        filter_method = lambda x: x * 2
        sketch.shrink(sketch, width=100, max_value=100,
                      filter_method=filter_method)
        assert sketch['mami'] == 4

    def test_value_mask(self):
        sketch = madoka.Sketch(width=100)
        assert isinstance(sketch.value_mask, numbers.Integral)

    def test_mode(self):
        sketch = madoka.Sketch(width=100)
        assert isinstance(sketch.mode, numbers.Integral)
