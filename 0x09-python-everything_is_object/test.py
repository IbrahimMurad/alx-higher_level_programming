import ctypes
a = 'I'
a_id = id(a)
I_id = id('I')
print(a_id)
print("-----")
print(I_id)
print(ctypes.cast(I_id, ctypes.py_object).value)
