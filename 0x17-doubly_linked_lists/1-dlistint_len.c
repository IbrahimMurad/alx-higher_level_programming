#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list.
 * @h: the head of the list
 *
 * Return: the number of elements in the list
*/

size_t dlistint_len(const dlistint_t *h)
{
	size_t len = 0;
	const dlistint_t *temp = h;

	while (temp)
	{
		len++;
		temp = temp->next;
	}
	return (len);
}
