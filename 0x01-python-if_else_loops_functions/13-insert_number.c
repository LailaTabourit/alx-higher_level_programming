#include "lists.h"
/**
 * insert_node - inserts a new node
 * @head: head of a list.
 * @number: index of the list where the new node
 * by: Mega Mega
 * Return: the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd;
	listint_t *h;
	listint_t *n_prv;

	h = *head;
	nd = malloc(sizeof(listint_t));

	if (nd == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		n_prv = h;
		h = h->next;
	}

	nd->n = number;

	if (*head == NULL)
	{
		nd->next = NULL;
		*head = nd;
	}
	else
	{
		nd->next = h;
		if (h == *head)
			*head = nd;
		else
			n_prv->next = nd;
	}

	return (nd);
}
