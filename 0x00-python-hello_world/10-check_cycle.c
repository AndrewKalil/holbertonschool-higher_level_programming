#include "lists.h"

/**
 * check_cycle - checks if a singly linked list is a cycle or not
 * @list: pointer to the list
 * Return: 1 if there is a cycle, 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node, *nodeahead;

	if (list == NULL || list == NULL)
		return (0);

	node = list;
	nodeahead = list;
	while (nodeahead != NULL && node != NULL && nodeahead->next != NULL)
	{
		node = node->next;
		nodeahead = nodeahead->next->next;
		if (node == nodeahead)
			return (1);
	}
	return (0);
}
