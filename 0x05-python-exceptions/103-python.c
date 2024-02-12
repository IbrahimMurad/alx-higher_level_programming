#include <python3.10/Python.h>
#include <stdio.h>
#include <string.h>


void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t mysize, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *) p)->ob_sval;
	mysize = PyBytes_Size(p);
	printf("  size: %ld\n", mysize);
	printf("  trying string: %s\n", str);
	if (mysize > 9)
	{
		mysize = 9;
	}
	printf("  first %ld bytes: ", mysize + 1);
	for (i = 0; i < mysize; i++)
	{
		printf("%02hhx ", str[i]);
	}
	if (i == 9)
	{
		printf("%02hhx\n", str[i]);
	}
	else
	{
		printf("%02hhx\n", '\0');
	}
}


void print_python_float(PyObject *p)
{
	double my_float;

	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	else
	{
		my_float = (((PyFloatObject *)(p))->ob_fval);
		if (my_float == (int) (my_float))
		{
			printf("  value: %.1f\n", my_float);
		}
		else
		{
			printf("  value: %.16g\n", my_float);
		}
	}
}

void print_python_list(PyObject *p)
{
	Py_ssize_t i, list_size;
	const char *mytype;

	fflush(stdout);
	list_size = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < list_size; i++)
	{
		mytype = ((PyListObject *)(p))->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, mytype);
		if (PyBytes_Check(((PyListObject *)(p))->ob_item[i]))
		{
			print_python_bytes(((PyListObject *)(p))->ob_item[i]);
		}
		if (PyFloat_CheckExact(((PyListObject *)(p))->ob_item[i]))
		{
			print_python_float(((PyListObject *)(p))->ob_item[i]);
		}
	}
}
