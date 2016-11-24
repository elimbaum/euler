/* Euler 028
 *
 * I have reduced the problem to a single cubic...
 * so I probably don't need to do this.
 *
 * Doing it anyway for hahas.
 */

#include <stdio.h>
#include <time.h>

int main()
{
	// size of the grid
	long r = 1001;
	
	long sum = (r * (r * (4 * r + 3) + 8) - 9) / 6;
	
	printf("%ld\n", sum);
	
	/* === END OF PROGRAM ===
	 * Below is just benchmarking... useless but fun.
	 * Takes about 13 nanoseconds per iter.
	 */
	
	// Benchmarking... run a billion times
	clock_t start = clock();
	for(long i = 0; i < 1000000000; i++)
	{
		sum = (r * (r * (4 * r + 3) + 8) - 9) / 6;
	}	
	clock_t end = clock();
	
	printf("%lu %lu\n", start, end);
	
	long micros = (end - start) * 1000000 / CLOCKS_PER_SEC;
	printf("cps = %d\n", CLOCKS_PER_SEC);
	printf("%ld usec total; %f per iter\n", micros, (float)micros/1000000000);
}