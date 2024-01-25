#include "lists.h"

/**
 *print_dlistint - prints element in a list
 *@h: head
 *
 *Return: number of items
 */

size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (count);
}
