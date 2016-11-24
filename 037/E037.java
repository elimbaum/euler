import java.util.BitSet;


/* Euler 037
 * Truncatable Primes
 */
public class E037
{
	static BitSet notPrime;
	static int[] power10;
	
	public static boolean isTruncatablePrime(int n)
	{
		int d = numDigits(n);
		
		/* preliminary checks
		 * Last digit must be 3 or 7
		 * First digit must be prime (2, 3, 5, 7)
		 */
		int temp = n % 10;
		if(! (temp == 3 || temp == 7)) return false;

		temp = n / power10[d - 1];
		if(!(temp == 2 || temp == 3 || temp == 5 || temp == 7)) return false;
		
		// First digit was already checked above.
		temp = n / 10;
		// Check right to left first
		while(temp > 0)
		{
			if(notPrime.get(temp))
			{
				return false;
			}
			temp /= 10;
		}
		
		// Left to right
		while(n > 0)
		{
			if(notPrime.get(n))
			{
				return false;
			}
			n %= power10[--d];
		}
		
		return true;
	}
	
	public static int numDigits(int n)
	{
		int digits = 0;
		while(n > 0)
		{
			n /= 10;
			digits++;
		}
		return digits;
	}

	public static void main(String[] args)
	{
		long startTime = System.nanoTime();
		
		final int UPPER_BOUND = 800000; // Arbitrary.
		notPrime = new BitSet(UPPER_BOUND);
		
		notPrime.set(0);
		notPrime.set(1);
		
		int maxCheck = (int) Math.sqrt(UPPER_BOUND);
		for(int i = 2; i < maxCheck; i += 1)
		{
			if(! notPrime.get(i))
			{
				for(int j = i * i; j < UPPER_BOUND; j += i)
				{
					notPrime.set(j);
				}
			}
		}
		
		int d = numDigits(UPPER_BOUND);
		power10 = new int[d];
		power10[0] = 1;
		for(int i = 1; i < d; i++)
		{
			power10[i] = 10 * power10[i - 1];
		}

		
		// Problem says there will be 11.
		final int NUM_TPRIMES = 11;
		int count = 0;
		int sum = 0;
		for(int i = 11; count < NUM_TPRIMES; i += 2)
		{
			if(isTruncatablePrime(i))
			{
				//System.out.println(i);
				sum += i;
				count++;
			}
		}
		final long endTime = System.nanoTime();
		
		System.out.println("= " + sum + " (" + count + ")");
		System.out.println("[" + ((endTime - startTime) / 1000000.0) + " ms]");
	}


}
