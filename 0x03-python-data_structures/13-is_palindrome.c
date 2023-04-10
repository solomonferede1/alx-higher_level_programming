#include "lists.h"
#include <stdlib.h>
/**
  * is_palindrome - checks if a singly linked list is palindrome
  * @head: head of linked list
  * Return: 0 if not palindrone, 1 if palindrone
  */

int is_palindrome(listint_t **head)
{
        int i;
        int *ptr;
        int capacity = 100;
        listint_t *tmp;

        ptr = malloc(capacity * sizeof(int));
        i = 0;
        tmp = *head;

        while (tmp != NULL)
        {
                if (i > capacity)
                {
                        capacity = 2 * capacity;
                        ptr = realloc(ptr, capacity * sizeof(int));
                }
                ptr[i] = tmp->n;
                tmp = tmp->next;
                i++;
        }

        while ((*head) != NULL)
        {
                i--;
                if ((*head)->n != ptr[i])
                {
                            return (0);
                }
                (*head) = (*head)->next;
        }
    return (1);
}