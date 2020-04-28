#include "lists.h"

/**
 * insert_node - inserts a node into a sorted list
 * @head: a pointer to the first node
 * @number: int inside of the node
 * Return: the list with the node it, or 0 if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux, *ptr;

	if (head == NULL)
		return (0);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);
	ptr = *head;
	new->n = number;
	while (ptr != NULL && ptr->n < number)
	{
		aux = ptr;
		ptr = ptr->next;
	}
	new->next = ptr;
	if (aux == NULL)
	{
		*head = new;
	}
	else
	{
		aux->next = new;
	}
	return (new);
}
