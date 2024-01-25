#include "lists.h"

/**
 *dlistint_len - get lenght of a list
 *@h: head
 *
 *Return: number of items
 */

size_t dlistint_len(const dlistint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
