#include <python3.4/Python.h>
#include <stdio.h>


void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_size;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}