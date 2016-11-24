/* Euler 036
 * Double-base palindromes
 */

#include <stdio.h>
#include <time.h>

#define MAX 1000000

int _log2(int n);
int reverse_bits(int n);
int isPalindrome(int n);

int main() 
{
	clock_t start = clock();
	
	const int MAX_LENGTH = _log2(MAX) + 1;
	const int MAX_VALUE = 1 << (MAX_LENGTH / 2);
	
	long sum = 0;

	for(int i = 1; i < MAX_VALUE; i += 2)
	{
		int rb = reverse_bits(i);
		for(int L = _log2(i); L < MAX_LENGTH; L++)
		{
			int v = (i << L) | rb;
		
			if (v < MAX && isPalindrome(v))
			{
				sum += v;
			}
		}
	}
	clock_t end = clock();
	printf("= %ld\n", sum);
	printf("[%f ms]\n", (end - start) * 1000.0 / CLOCKS_PER_SEC);
}

/* floored log2
 * returns the "length" of a binary number, by finding the highest-order
 * set bit.
 * underscore prevents clashing with actual log2
 */
int _log2(int n)
{
	int loc = 0;
	
	while(n >>= 1)
	{
		loc++;
	}
	
	return loc;
}

/* Reverses the bits in n, starting from the highest set bit.
 * Ex:
 * 1110 =>  111
 * 1011 => 1101
 */
int reverse_bits(int n)
{
	int loc = _log2(n);
	
	// all bits from 0 to loc have to be reversed.
	int ret = 0;
	for(int i = 0; i <= loc; i++)
	{
		// if a bit is set, also set it's flipped-position
		if (n & (1 << (loc - i)))
		{
			ret |= 1 << i;
		}
	}
	return ret;
}

/* isPalindrome (base 10)
 * algorithm works by checking if n = reversed(n).
 */
int isPalindrome(int n)
{
	int rev = 0;
	int t = n;
	while (t > 0)
	{
		rev *= 10;
		rev += t % 10;
		t /= 10;
	}
	return rev == n;
}
