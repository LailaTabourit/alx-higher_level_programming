#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it.
*
* by: laila
* Return: 0  if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t first_tmp = list;
	listint_t last_tmp = list;

	while (last_tmp != NULL && first_tmp != NULL && last_tmp->next != NULL)
	{
		first_tmp = first_tmp->next;
		last_tmp = last_tmp->next->next;
		if(first_tmp == last_tmp)
			return (1);
	}
	return (0);
}
