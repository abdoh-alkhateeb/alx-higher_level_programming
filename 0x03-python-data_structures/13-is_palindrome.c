#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - a function that reverses the linked list in-place.
 * @head: pointer to the head of the linked list.
 *
 * Return: pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - a function that checks if a singly linked list
 * is a palindrome.
 * @headptr: pointer to pointer to first node in list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **headptr)
{
	listint_t *head = *headptr;
	listint_t *slow = head, *fast = head, *prevSlow = NULL, *middle = NULL;
	listint_t *p1, *p2, *second_half;
	int palindrome = 1;

	if (headptr == NULL || head == NULL || head->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prevSlow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	p1 = head;
	p2 = second_half;
	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			palindrome = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	second_half = reverse_list(second_half);
	if (middle != NULL)
	{
		prevSlow->next = middle;
		middle->next = second_half;
	}
	else
		prevSlow->next = second_half;
	return (palindrome);
}
