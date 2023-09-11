#include <stdlib.h>
#include "lists.h"


/**
 * list_len - counts the number of elements in a linked list
 * @h: the head of the list
 *
 * Return: the number of elements in the list
 */

size_t list_len(listint_t *h)
{
	size_t count = 0;
	listint_t *temp = h;

	while (temp)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}

/**
 * int_arr_palendrome - checks if an array of integers is a palindrome.
 * @p: a pointer to the array
 * @len: the length of the array
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */


int int_arr_palendrome(int *p, int len)
{
	int i;

	for (i = 0; i < len / 2; i++)
	{
		if (p[i] != p[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to a pointer to teh first node (the head of the list)
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	size_t len;
	listint_t *temp;
	int *p, i = 0, is_arr_palendrome;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	len = list_len(*head);
	p = (int *) malloc(sizeof(int) * len);
	if (p == NULL)
	{
		return (0);
	}
	temp = *head;
	while (temp)
	{
		p[i] = temp->n;
		i++;
		temp = temp->next;
	}
	is_arr_palendrome = int_arr_palendrome(p, len);
	free(p);
	return (is_arr_palendrome);
}
