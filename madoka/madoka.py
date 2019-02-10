# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
import heapq
from collections import deque
from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_madoka')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_madoka')
    _madoka = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_madoka', [dirname(__file__)])
        except ImportError:
            import _madoka
            return _madoka
        try:
            _mod = imp.load_module('_madoka', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _madoka = swig_import_helper()
    del swig_import_helper
else:
    import _madoka
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


FILE_CREATE = 1 << 0
FILE_TRUNCATE = 1 << 1
FILE_READONLY = 1 << 2
FILE_WRITABLE = 1 << 3
FILE_SHARED = 1 << 4
FILE_PRIVATE = 1 << 5
FILE_ANONYMOUS = 1 << 6
FILE_HUGETLB = 1 << 7
FILE_PRELOAD = 1 << 8

cvar = _madoka.cvar
SKETCH_ID_SIZE = cvar.SKETCH_ID_SIZE
SKETCH_MAX_ID = cvar.SKETCH_MAX_ID
SKETCH_ID_MASK = cvar.SKETCH_ID_MASK
SKETCH_MIN_WIDTH = cvar.SKETCH_MIN_WIDTH
SKETCH_MAX_WIDTH = cvar.SKETCH_MAX_WIDTH
SKETCH_DEFAULT_WIDTH = cvar.SKETCH_DEFAULT_WIDTH
SKETCH_MAX_MAX_VALUE = cvar.SKETCH_MAX_MAX_VALUE
SKETCH_DEFAULT_MAX_VALUE = cvar.SKETCH_DEFAULT_MAX_VALUE
SKETCH_DEPTH = cvar.SKETCH_DEPTH
SKETCH_APPROX_VALUE_SIZE = cvar.SKETCH_APPROX_VALUE_SIZE
SKETCH_OWNER_OFFSET = cvar.SKETCH_OWNER_OFFSET
SKETCH_OWNER_MASK = cvar.SKETCH_OWNER_MASK

CROQUIS_HASH_SIZE = cvar.CROQUIS_HASH_SIZE
CROQUIS_ID_SIZE = cvar.CROQUIS_ID_SIZE
CROQUIS_MAX_ID = cvar.CROQUIS_MAX_ID
CROQUIS_ID_MASK = cvar.CROQUIS_ID_MASK
CROQUIS_MIN_WIDTH = cvar.CROQUIS_MIN_WIDTH
CROQUIS_MAX_WIDTH = cvar.CROQUIS_MAX_WIDTH
CROQUIS_DEFAULT_WIDTH = cvar.CROQUIS_DEFAULT_WIDTH
CROQUIS_MIN_DEPTH = cvar.CROQUIS_MIN_DEPTH
CROQUIS_MAX_DEPTH = cvar.CROQUIS_MAX_DEPTH
CROQUIS_DEFAULT_DEPTH = cvar.CROQUIS_DEFAULT_DEPTH

_COMMON_METHODS = ('open', 'load', 'close', 'save', 'clear', 'get',
                   'get__', 'set', 'set__', 'add', 'create', 'copy',
                   'swap', 'inner_product', 'median', 'merge', 'shrink',
                   'width', 'width_mask', 'depth', 'max_value',
                   'value_size', 'seed', 'table_size', 'file_size',
                   'flags')


class _Madoka(_object):
    __swig_setmethods__ = {}
    __swig_getmethods__ = {}
    __repr__ = _swig_repr

    def __setattr__(self, name, value):
        _swig_setattr(self, self.__class__, name, value)

    def __getattr__(self, name):
        _swig_getattr(self, self.__class__, name)

    def __init__(self, width=0, depth=0, path=None, flags=0, seed=0, k=5):
        self._rename_method()
        this = getattr(_madoka, 'new_%s' % self.__class__.__name__)()
        try:
            self.this.append(this)
        except:
            self.this = this
        self.k = k
        self.ranking = []
        heapq.heapify(self.ranking)
        self.dq = deque(maxlen=self.k)
        self.num = 0
        return self.create_method(self, width, depth, path, flags, seed)

    def __del__(self):
        self.close()

    def _rename_method(self):
        class_name = self.__class__.__name__
        for method_name in _COMMON_METHODS:
            method = getattr(_madoka, '%s_%s' % (class_name, method_name))
            method_name += '_method'
            setattr(self, method_name, method)

    def __enter__(self, *args, **kargs):
        self.create(*args, **kargs)
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __len__(self):
        return self.file_size

    def __getitem__(self, key):
        """
        Param:
            <str> key
        Return:
            <int> value
        """
        return self.get_method(self, key, len(key))

    def __setitem__(self, key, value):
        """
        Param:
            <str> key
            <int> value
        """
        if self.k:
            self._update(key, value)
        return self.set_method(self, key, len(key), value)

    def __contains__(self, key):
        """
        Param:
            <str> key
        Return:
            <bool>
        """
        return self.get_method(self, key, len(key)) > 0

    def __add__(self, given_data):
        """Get merged sketch
        summed_sketch = sketch + sketch
        or
        summed_sketch = sketch + dict
        Param:
            <Sketch> | <dict> given_data
        Return:
            <Sketch> summed_sketch
        """
        summed_sketch = self.__class__(width=self.width, depth=self.depth, seed=self.seed, k=self.k)
        summed_sketch.copy(self)
        return summed_sketch.__iadd__(given_data)

    def __iadd__(self, given_data):
        """Merge sketch
        sketch += sketch
        Param:
            <Sketch> | <dict> given_data
        Return:
            <Sketch> sketch
        """
        if hasattr(given_data, 'items'):
            self.fromdict(given_data, 'add')
        else:
            self.merge_method(self, given_data)
            if given_data.k:
                for (key, val) in given_data.most_common(given_data.k):
                    self._update(key, val)
        return self

    def create(self, width=0, depth=0, path=None, flags=0, seed=0):
        """Create new sketch
        Params:
            <int> width
            <str> path
            <int> flags
            <int> seed
        """
        return self.create_method(self, width, depth, path, flags, seed)

    def open(self, *args):
        """Load sketch from file

        open() uses memory mapped I/O instead of reading the whole sketch into memory

        file_flag as following:
            FILE_CREATE    1,
            FILE_TRUNCATE  2,
            FILE_READONLY  4,
            FILE_WRITABLE  8,
            FILE_SHARED    16,
            FILE_PRIVATE   32,
            FILE_ANONYMOUS 64,
            FILE_HUGETLB   128,
            FILE_PRELOAD   256

        Params:
            <str> filepath
            <int> file_flag
        """
        return self.open_method(self, *args)

    def close(self):
        return self.close_method(self)

    def load(self, *args):
        """Load sketch from file

        file_flag as following:
            FILE_CREATE    1,
            FILE_TRUNCATE  2,
            FILE_READONLY  4,
            FILE_WRITABLE  8,
            FILE_SHARED    16,
            FILE_PRIVATE   32,
            FILE_ANONYMOUS 64,
            FILE_HUGETLB   128,
            FILE_PRELOAD   256

        Params:
            <str> filepath
            <int> file_flag
        """
        return self.load_method(self, *args)

    def save(self, *args):
        """Save sketch to file

        file_flag as following:
            FILE_CREATE    1,
            FILE_TRUNCATE  2,
            FILE_READONLY  4,
            FILE_WRITABLE  8,
            FILE_SHARED    16,
            FILE_PRIVATE   32,
            FILE_ANONYMOUS 64,
            FILE_HUGETLB   128,
            FILE_PRELOAD   256

        Params:
            <str> filepath
            <int> file_flag
        """
        return self.save_method(self, *args)

    def _update(self, key, val):
        if key not in self.dq:
            if self.num < self.k:
                heapq.heappush(self.ranking, (val, key))
                self.dq.append(key)
                self.num += 1
            else:
                (min_val, min_key) = heapq.heappushpop(self.ranking, (val, key))
                if key != min_key:
                    self.dq.remove(min_key)
                    self.dq.append(key)

    def get(self, key, key_length=0):
        """Add key-value
        Params:
            <str> key
            <int> key_length
        Return:
            <int> key_value
        """
        if key_length < 1:
            key_length = len(key)
        return self.get_method(self, key, key_length)

    def set(self, key, value, key_length=0):
        """Set value to key-value
        Params:
            <str> key
            <int> value
            <int> key_length
        Return:
            <int> key_value
        """
        if key_length < 1:
            key_length = len(key)
        if self.k:
            self._update(key, value)
        return self.set_method(self, key, key_length, value)

    def add(self, key, value, key_length=0):
        """Add value to key-value
        Params:
            <str> key
            <int> value
            <int> key_length
        Return:
            <int> key_value
        """
        if key_length < 1:
            key_length = len(key)
        val = self.add_method(self, key, key_length, value)
        if self.k:
            self._update(key, value)
        return val

    def inc(self, key, key_length=0):
        """Add value to key-value
        Params:
            <str> key
            <int> value
            <int> key_length
        Return:
            <int> key_value
        """
        if key_length < 1:
            key_length = len(key)
        val = self.add_method(self, key, key_length, 1)
        if self.k:
            self._update(key, val)
        return val

    def clear(self):
        """Clear sketch"""
        self.ranking = []
        heapq.heapify(self.ranking)
        self.dq = deque(maxlen=self.k)
        self.num = 0
        return self.clear_method(self)

    def copy(self, *args):
        """Copy this sketch
        Return:
            <Sketch> sketch
        """
        return self.copy_method(self, *args)

    def swap(self, *args):
        """Swap sketches
        Params:
            <Sketch> sketch
        """
        return self.swap_method(self, *args)

    def shrink(self, src, width=0, path=None, flags=0):
        """Shrink sketch
        Params:
            <Sketch> src_sketch
            <int> width
            <str> path
            <int> flags
        """
        self.shrink_method(self, src, width, path, flags)

    def merge(self, rhs, lhs_filter=None, rhs_filter=None):
        """Merge two sketches
        Params:
            <Sketch> sketch
            <lambda> | <function> lhs_filter
            <lambda> | <function> rhs_filter
        """
        if lhs_filter or rhs_filter:
            get_ = self.get___method
            set_ = self.set___method
            max_value = _madoka.Sketch_max_value(self)
            for table_id in range(self.depth):
                for cell_id in range(self.width):
                    lhs_val = get_(self, table_id, cell_id)
                    rhs_val = get_(rhs, table_id, cell_id)
                    if lhs_filter:
                        lhs_val = lhs_filter(lhs_val)
                    if rhs_filter:
                        rhs_val = rhs_filter(rhs_val)
                    if (lhs_val >= max_value) or (rhs_val >= (max_value - lhs_val)):
                        lhs_val = self.max_value
                    else:
                        lhs_val += rhs_val
                    set_(self, table_id, cell_id, lhs_val)
        else:
            self.merge_method(self, rhs)
            if rhs.k:
                for (key, val) in rhs.most_common(rhs.k):
                    self._update(key, val)

    def inner_product(self, sketch):
        """Inner product of two sketches
        Params:
            <Sketch> sketch
        Return:
            <float> inner_product
            <float> lhs_square_length
            <float> rhs_square_length
        """
        return self.inner_product_method(self, sketch)

    def median(self):
        return self.median_method(self)

    def filter(self, given_filter, apply_zerovalue=False):
        """Apply filter into all values
        Params
            <lambda> | <function> given_filter
            <bool> only_nonzero
        """
        get_ = self.get___method
        set_ = self.set___method
        max_value = self.max_value
        for table_id in range(self.depth):
            for cell_id in range(self.width):
                val = get_(self, table_id, cell_id)
                if val or apply_zerovalue:
                    val = given_filter(val)
                    val = max_value if val > max_value else val
                    set_(self, table_id, cell_id, val)

    def values(self):
        """Dump all values
        Return:
            <generator> <int> val
        """
        table_id = 0
        get = self.get___method
        for cell_id in range(self.width):
            val = get(self, table_id, cell_id)
            if val:
                yield val

    def fromdict(self, src_dict, method='set'):
        """Set values from dict
        Params:
            <dict <str> <int>> src_dict
        """
        if method == 'set':
            _method = self.set_method
        else:
            _method = self.add_method
        if hasattr(src_dict, 'iteritems'):
            for (key, val) in src_dict.iteritems():
                _method(self, key, len(key), val)
                if self.k:
                    self._update(key, value)
        else:
            for (key, val) in src_dict.items():
                _method(self, key, len(key), val)
                if self.k:
                    self._update(key, val)

    def most_common(self, k=5):
        for (val, key) in heapq.nlargest(k, self.ranking):
            yield (key, val)

    @property
    def width(self):
        return self.width_method(self)

    @property
    def width_mask(self):
        return self.width_mask_method(self)

    @property
    def depth(self):
        return self.depth_method(self)

    @property
    def max_value(self):
        return self.max_value_method(self)

    @property
    def value_size(self):
        return self.value_size_method(self)

    @property
    def seed(self):
        return self.seed_method(self)

    @property
    def table_size(self):
        return self.table_size_method(self)

    @property
    def file_size(self):
        return self.file_size_method(self)

    @property
    def flags(self):
        return self.flags_method(self)


class Sketch(_Madoka):
    __swig_destroy__ = _madoka.delete_Sketch

    def __init__(self, width=0, max_value=0, path=None, flags=0, seed=0, k=5):
        this = _madoka.new_Sketch()
        try:
            self.this.append(this)
        except:
            self.this = this
        self._rename_method()
        self.k = k
        self.ranking = []
        heapq.heapify(self.ranking)
        self.dq = deque(maxlen=self.k)
        self.num = 0
        return _madoka.Sketch_create(self, width, max_value, path, flags, seed)

    def __add__(self, given_data):
        """Get merged sketch
        summed_sketch = sketch + sketch
        Param:
            <Sketch> | <dict> given_data
        Return:
            <Sketch> summed_sketch
        """
        summed_sketch = Sketch(width=self.width, max_value=self.max_value, seed=self.seed)
        summed_sketch.copy(self)
        return summed_sketch.__iadd__(given_data)

    def create(self, width=0, max_value=0, path=None, flags=0, seed=0):
        """Create new sketch
        Params:
            <int> width
            <int> max_value
            <str> path
            <int> flags
            <int> seed
        """
        return _madoka.Sketch_create(self, width, max_value, path, flags, seed)

    def inc(self, key, key_length=0):
        """Increment key-value
        Params:
            <str> key
            <int> key_length
        Return:
            <int> key_value
        """
        if key_length < 1:
            key_length = len(key)
        return _madoka.Sketch_inc(self, key, key_length)

    def shrink(self, src, width=0, max_value=0, filter_method=None,
               path=None, flags=0):
        """Shrink sketch
        Params:
            <Sketch> src_sketch
            <int> width
            <int> max_value
            <lambda> | <function> filter
            <str> path
            <int> flags
        """
        if filter_method:
            get_ = _madoka.Sketch_get__
            set_ = _madoka.Sketch_set__
            new_sketch = Sketch(width, max_value, path, flags, src.seed)
            for table_id in range(SKETCH_DEPTH):
                for offset in range(width, src.width, width):
                    for cell_id in range(width):
                        val = get_(src, table_id, offset + cell_id)
                        val = filter_method(val)
                        val = max_value if val > max_value else val
                        if val > get_(new_sketch, table_id, cell_id):
                            set_(new_sketch, table_id, cell_id, val)
            self.swap(new_sketch)
        else:
            _madoka.Sketch_shrink(self, src, width, max_value, None, path, flags)

    @property
    def value_mask(self):
        return _madoka.Sketch_value_mask(self)

    @property
    def mode(self):
        return _madoka.Sketch_mode(self)

Sketch_swigregister = _madoka.Sketch_swigregister
Sketch_swigregister(Sketch)


class CroquisUint8(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisUint8

CroquisUint8_swigregister = _madoka.CroquisUint8_swigregister
CroquisUint8_swigregister(CroquisUint8)


class CroquisUint16(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisUint16

CroquisUint16_swigregister = _madoka.CroquisUint16_swigregister
CroquisUint16_swigregister(CroquisUint16)


class CroquisUint32(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisUint32

CroquisUint32_swigregister = _madoka.CroquisUint32_swigregister
CroquisUint32_swigregister(CroquisUint32)


class CroquisUint64(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisUint64

CroquisUint64_swigregister = _madoka.CroquisUint64_swigregister
CroquisUint64_swigregister(CroquisUint64)


class CroquisFloat(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisFloat

CroquisFloat_swigregister = _madoka.CroquisFloat_swigregister
CroquisFloat_swigregister(CroquisFloat)


class CroquisDouble(_Madoka):
    __swig_destroy__ = _madoka.delete_CroquisDouble

CroquisDouble_swigregister = _madoka.CroquisDouble_swigregister
CroquisDouble_swigregister(CroquisDouble)

# This file is compatible with both classic and new-style classes.
