/* Euler 030
 * Digit fifth powers
 */

#include <stdio.h>
#include <time.h>

// See notes; at this point n grows too fast for the digits to catch up.
#define MAX 354294

int main() {
	clock_t start = clock();

	// Holds the fifth power of each digit
	int dp[10];

	for(int i = 0; i < 10; i++)
	{
		int sq = i * i;
		dp[i] = sq * sq * i;
	}
	
	// Loop through
	long sum = 0;
	for(int n = 0; n < MAX; n++)
	{
		int t = n;
		
		/* Get digit sum
		 * End early if digitSum has already passed n, 
		 */
		int digitSum = 0;

		while(digitSum <= n && t > 0)
		{
			digitSum += dp[t % 10];
			t /= 10;	
		}
		
		if(digitSum == n)
		{
			sum += n;
		}
	}
	
	sum -= 1; // 1 doesn't count/
	
	clock_t end = clock();
	
	printf("---\n%ld\n", sum);
	printf("%f ms\n", (end - start) * 1000.0 / CLOCKS_PER_SEC);

}