#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number into a
 * sorted singly linked list.
 * @head: pointer to pointer to first node in list.
 * @number: number to insert.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL)
	{
		*head = (listint_t *)malloc(sizeof(listint_t));

		(*head)->n = number;
		(*head)->next = NULL;

		return (*head);
	}
	else if ((*head)->n > number)
	{
		listint_t *p = (listint_t *)malloc(sizeof(listint_t));

		p->n = number;
		p->next = *head;
		*head = p;

		return (p);
	}
	else
		return (insert_node(&((*head)->next), number));
}
