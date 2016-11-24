import java.util.ArrayList;
import java.util.List;

/* Euler 023
 * Non-abundant Sums
 * 
 */
public class E023
{
	

	
	public static void main(String[] args)
	{
		
		System.out.println("Euler 023");
		
		// TIMING
		final long startTime = System.currentTimeMillis();
		
		/* First, generate a list of abundant numbers. */
		List<Integer> abundants = new ArrayList<Integer>();
		
		final int MAX = 28123;
		
		for(int n = 12; n < MAX; n ++)
		{
			int sumDivisors = 1; // every number starts with 1
			
			final int MAX_DIVISOR = (int) Math.sqrt(n);
			
			for(int i = 2; i <= MAX_DIVISOR; i++)
			{
				if (n % i == 0)
				{
					/* i is a divisor!
					 * 
					 * Add in both i and n/i
					 * (this is why only up to sqrt(n) is tested)
					 * UNLESS i is the sqrt of n... in which case only add it in once.
					 */
					if(i * i == n)
					{
						sumDivisors += i;
					}
					else
					{
						sumDivisors += i + n / i;
					}
				}
			}
			
			// sumDivisors contains the sum of n's divisors.
			if(sumDivisors > n)
			{
				abundants.add(n);
			}
		}
		
		// TIMING
		final long middleTime = System.currentTimeMillis();
		
		// Compile a list of abundant sums, to check against later.
		boolean isSumOfAbundants[] = new boolean[MAX];
		
		for (int a = 0; a < abundants.size(); a++)
		{
			int aValue = abundants.get(a);
			
			for (int b = 0; b < abundants.size(); b++)
			{
				int bValue = abundants.get(b);
				
				/* Only add it to the array if it's below MAX
				 * (the greatest index)
				 * Otherwise, move on to the next a.
				 */
				if ((aValue + bValue) < MAX)
				{
					isSumOfAbundants[aValue + bValue] = true;
				}
				else
				{
					break;
				}
				
			}
		}
		
		/* Since 12 is the smallest abundant, the smallest number
		 * that can be made from two abundants is 12 + 12 = 24.
		 * So 1 through 23 can be added in at the beginning.
		 * 
		 * We know 24 works.
		 * 
		 * So start at 25.
		 */
		
		int sum = (23 * (23 + 1)) / 2;
		
		for(int n = 25; n < MAX; n++)
		{
			if (! isSumOfAbundants[n])
			{
				sum += n;
				//System.out.println(n);
			}
		}
		
		final long endTime = System.currentTimeMillis();
		
		System.out.println("Result: " + sum);
		System.out.println("found in " + (endTime - startTime) + " (" + (middleTime - startTime) + " + " + (endTime - middleTime) + ")");
		
	}
}
