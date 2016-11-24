/* Euler 030
 * Digit fifth powers
 *
 * This one *should* be more efficient, but it's not.
 */

#include <stdio.h>
#include <time.h>

#define MAX 999999

// Holds the fifth power of each digit
int dp[10];

/* Get digit sum
 * End early if digitSum has already passed n, 
 * or if the digits are not loosely decreasing.
 */
int firstDigitSum(int n)
{
	int t = n;
	int digitSum = 0;
	int lastDigit = 0;
	while(t > 0)
	{
		int d = t % 10;
		if (d < lastDigit)
		{
			return -1;
		}
		lastDigit = d;
		digitSum += dp[d];
		
		if(digitSum > n)
		{
			return -1;
		}
		
		t /= 10;
	}
	
	return digitSum;
}

int fastDigitSum(int n)
{
	int t = n;
	int digitSum = 0;
	while(t > 0)
	{
		digitSum += dp[t % 10];
		
		if(digitSum > n)
		{
			return -1;
		}
		t /= 10;
	}
	
	return digitSum;
}

int main() {
	clock_t start = clock();
	
	for(int i = 0; i < 10; i++)
	{
		int sq = i * i;
		dp[i] = sq * sq * i;
	}
	
	// Loop through
	long sum = 0;
	for(int n = 500000; n < MAX; n++)
	{
		int first = firstDigitSum(n);
		
		// Don't count -1 (error) or 1
		if(first > 1)
		{
			if(fastDigitSum(first) == first)
			{
				sum += first;
				printf("%d\n", n);
			}
		}
	}
	
	clock_t end = clock();
	
	printf("---\n%ld\n", sum);
	printf("%f ms\n", (end - start) * 1000.0 / CLOCKS_PER_SEC);

}