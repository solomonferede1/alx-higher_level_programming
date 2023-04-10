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
        int *ptr = NULL;

        i = 0;
        listint_t *tmp = *head;

        while (tmp != NULL)
        {
                ptr = realloc(ptr, (i + 1) * sizeof(int));
                ptr[i] = tmp->n;
                tmp = tmp->next;
                i++;
        }

        while ((*head) != NULL || i == 0)
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