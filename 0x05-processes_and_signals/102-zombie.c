#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int infinite_while(void);
/**
 * main - Entry point
 *
 * Return: 0.
 */
int main(void)
{
	pid_t ZOMBIE_PID;
	int limit = 0;

	while (limit < 5)
	{
		ZOMBIE_PID = fork();

		if (ZOMBIE_PID > 0)
		{
			printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
			limit++;
		}
		else
		{
			exit (0);
		}

	}

	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite while loop
 *
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
