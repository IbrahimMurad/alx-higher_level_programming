import ctypes
a = 1024
a_id = id(a)
print(ctypes.cast(a_id, ctypes.py_object).value)
print("-----")
b = 1024
b_id = id(b)
print(ctypes.cast(b_id, ctypes.py_object).value)
print("-----")
del a
print(ctypes.cast(a_id, ctypes.py_object).value)
print("-----")
del b
print(ctypes.cast(b_id, ctypes.py_object).value)
print("-----")
c = 1024
c_id = id(c)
print(ctypes.cast(a_id, ctypes.py_object).value)
print(ctypes.cast(b_id, ctypes.py_object).value)
print(ctypes.cast(c_id, ctypes.py_object).value)