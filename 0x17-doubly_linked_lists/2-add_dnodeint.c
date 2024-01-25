#include "lists.h"

/**
 *add_dnodeint - add an element to a list
 *@head: pointer to the head of the list
 *@n: integer
 *
 *Return: address to new node
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *newNode = NULL;
	dlistint_t *h = NULL;

	newNode = malloc(sizeof(dlistint_t));
	if (newNode == NULL)
        	return (NULL);

	newNode->n = n;
	newNode->prev = NULL;
	h = *head;

	if (h != NULL)
	{
		while (h->prev != NULL)
			h = h->prev;
	}

	newNode->next = h;

        if (h != NULL)
		h->prev = newNode;

	*head = newNode;

        return (newNode);
}

