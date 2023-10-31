#include <stdlib.h>
#include "lists.h"
/**
*check_cycle - Checks if a singly-linked list contains a cycle.
*@list: A singly-linked list.
*Return: If there is no cycle - 0 if there is a cycle - 1.
*/
int check_cycle(listint_t *list)
{
listint_t *one, *two;
if (list == NULL || list->next == NULL)
return (0);
one = list->next;
two= list->next->next;
while (one != NULL && two != NULL && two->next != NULL)
{
if (one == two)
return (1);
one = one->next;
two = two->next->next;
}
return (0);
}
