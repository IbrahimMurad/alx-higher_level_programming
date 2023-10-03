import ctypes
a = "SCHL"
a_id = id(a)
print(id(a), end=', ')
print(ctypes.cast(a_id, ctypes.py_object).value)
b = "SCHL"
b_id = id(b)
print(id(b), end=', ')
print(ctypes.cast(b_id, ctypes.py_object).value)
del a
del b
print(ctypes.cast(a_id, ctypes.py_object).value)
print(ctypes.cast(b_id, ctypes.py_object).value)
c = "SCHL"
c_id = id(c)
print(id(c), end=', ')
print(ctypes.cast(c_id, ctypes.py_object).value)