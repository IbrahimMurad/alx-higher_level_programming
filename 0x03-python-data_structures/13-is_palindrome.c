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
 * reverse_listint - reverses a listint_t list
 * @head: a pointer to a pointer to the first node in the list (the head)
 *
 * Return: Nothing
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *before, *current, *after;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}
	before = *head;
	current = (*head)->next;
	if (current == NULL)
	{
		return (*head);
	}
	before->next = NULL;
	after = current->next;
	current->next = before;
	while (after)
	{
		before = current;
		current = after;
		after = after->next;
		current->next = before;
	}
	*head = current;
	return (*head);
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
	listint_t *daeh, *temp;
	int i;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	len = list_len(*head);
	temp = *head;
	for (i = 0; i < len / 2 + 1; i++)
	{
		temp = temp->next;
	}
	daeh = temp;
	daeh = reverse_listint(&daeh);
	temp = *head;
	for (i = 0; i < len / 2 + 1; i++)
	{
		if (daeh->n != temp->n)
		{
			return (0);
		}
	}
	return (1);
}
