import java.util.ArrayList;


public class E040
{	
	// indices are the base-10 logarithm of that section
	static ArrayList<Integer> sectionLength = new ArrayList<Integer>();
	
	public static void main(String[] args)
	{	
		sectionLength.add(0, 9);
		// up to 1 million
		System.out.println(cd(1) * cd(10) * cd(100) * cd(1000) * cd(10000) * cd(100000) * cd(1000000));
	}
	
	/* Returns the nth digit of the champernowne constant,
	 * starting at the first digit (d = 1) after the decimal.
	 */
	public static int cd(int d)
	{
		int i = 0;
		while(i < sectionLength.size())
		{
			if(d > sectionLength.get(i))
			{
				d -= sectionLength.get(i);
			}
			i++;
		}
		
		// fill up the next slots in the array
		while(true)
		{
			i++;
			int v = i * 9 * power10(i - 1);
			
			if(d <= v) break;
			
			sectionLength.add(i - 1, v);
			d -= v;
		}
		
		/* Get which number d is in.
		 * i is the length of the number because of the i++ above
		 */
		int n = d / i + power10(i - 1);
		
		/* adjust d to be the digit within the number
		 * right-aligned such that digit #0 = ones place
		 */
		d = numDigits(n) - d % i;
		
		while(d > 0)
		{
			n /= 10;
			d--;
		}
		
		return n % 10;
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
	
	public static int power10(int n)
	{
		int r = 1;
		while(n > 0)
		{
			r *= 10;
			n--;
		}
		
		return r;
	}
}
