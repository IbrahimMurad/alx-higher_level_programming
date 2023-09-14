#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: the head of the list
 *
 * Return: the number of nodes in the list
 */


size_t print_dlistint(const dlistint_t *h)
{
	size_t len = 0;
	const dlistint_t *temp = h;

	while (temp)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
		len++;
	}
	return (len);
}
