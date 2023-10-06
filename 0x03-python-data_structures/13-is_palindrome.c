#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - a function that checks if a singly linked list
 * is a palindrome.
 * @head: pointer to pointer to first node in list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *array;
	int i, count;

	if (head == NULL || *head == NULL)
		return (1);

	for (count = 0; current != NULL; count++)
		current = current->next;

	array = (int *)malloc(sizeof(int) * count);

	if (array == NULL)
		return (0);

	current = *head;
	for (i = 0; i < count; i++)
	{
		array[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < count / 2; i++)
	{
		if (array[i] != array[count - 1 - i])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
