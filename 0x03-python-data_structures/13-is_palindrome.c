#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *backwards(listint_t **head)
{
	listint_t *tmp = NULL;
	listint_t *next;

	if (*head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = tmp;
		tmp = *head;
		*head = next;
	}
	*head = tmp;
	return (*head);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointet to a pointer to the head of the list
 * Return: 1 if paindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *half, *tmp;


	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	else
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;
		}
		if (fast == NULL)
			half = slow;
		else
			half = slow->next;
		half = backwards(&half);
		tmp = *head;
		while (half != NULL)
		{
			if (tmp->n == half->n)
			{
				tmp = tmp->next;
				half = half->next;
			}
			else
				return (0);
		}
		return (1);
	}
}
