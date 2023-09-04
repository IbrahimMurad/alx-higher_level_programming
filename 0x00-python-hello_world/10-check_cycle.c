#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the first node in the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast && slow && slow->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
