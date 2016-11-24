/* Euler 034
 * Digit factorials
 */

#include <stdio.h>
#include <time.h>

// See notes; at this point n grows too fast for the digits to catch up.
#define MAX 999999

int main() {
	clock_t start = clock();

	// Holds the factorial of each digit
	int dp[10];
	dp[0] = 1;
	
	for(int i = 1; i < 10; i++)
	{
		dp[i] = i * dp[i - 1];
	}
	
	// Loop through
	long sum = 0;
	for(int n = 10; n < MAX; n++)
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
	
	clock_t end = clock();
	
	printf("---\n%ld\n", sum);
	printf("%f ms\n", (end - start) * 1000.0 / CLOCKS_PER_SEC);

}