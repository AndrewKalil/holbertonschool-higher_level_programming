#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check(listint_t **left, listint_t *right)
{
	if (right == NULL)
		return (1);
	check(left, right->next);
	if ((*left)->n == right->n)
	{
		(*left) = (*left)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointet to a pointer to the head of the list
 * Return: 1 if paindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check(head, *head));
}
