#include "lists.h"
/**
  * print_dlistint - print elements of doubly linked list
  * @h: head
  * Return: The number of nodes
  */
size_t print_dlistint(const dlistint_t *h)
{
	int counter;

	counter = 0;
	while (h)
	{
		printf("%d\n", h->n);
		counter++;
		h = h->next;
	}
	return (counter);
}
