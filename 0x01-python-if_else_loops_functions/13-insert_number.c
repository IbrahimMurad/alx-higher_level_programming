#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - nserts a number into a sorted singly linked list.
 * @head: a pointer to a pointer to the head of the list
 * @number: the number stored in the new node
 * Return: the address of the new node or NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	if (head == NULL)
	{
		return (NULL);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	temp = *head;
	if (temp == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (temp)
	{
		if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	new->next = NULL;
	temp->next = new;
	return (new);
}
