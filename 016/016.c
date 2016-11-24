/*	Project Euler 16
 *	Digit sum of 2^1000
 *
 *	need to do "custom" multiplication to handle the huge number
 *	starting with 2, build the number backwards until done (like
 *	school multiplication).
 *
 *	note that python, with arbitrary precision ints, can calculate
 *	2**1000 just fine.
 *	
 *	This is a test in C, for comparison against python. essentially the same logic.
 *
 *	Results:
 *	Python takes ~ 0.130 sec
 *	C takes ~.006 sec, fully optimized: ~.004 sec 
 *	22 [32.5 optimized] times faster.
 */
 
#include <stdio.h>
 
#define ARRAY_SIZE 302
#define TARGET_EXPONENT 1000

int main() {
	int bigNumList[ARRAY_SIZE] = {0}; // log10(2^1000) is slightly less than 302
	bigNumList[0] = 2; // start off with 2

	int currentExponent = 1;

	while (currentExponent < TARGET_EXPONENT) {
		// run through the number and multiply by 2
		// start at the end
		int carry = 0;
		for(int position = 0; position < ARRAY_SIZE; position++) {
			int digit = bigNumList[position];
		
			bigNumList[position] = digit * 2 + carry;
		
			carry = 0; // reset carry
			if(digit >= 5) {
				// carry multiply, subtract 10
				bigNumList[position] -= 10;
			
				// mark the carry variable.
				carry = 1;
			}
		}
		// multiply it again
		currentExponent++;
	}
	// now we have calculated the number.
	

	// now sum the number (it's backwards, whatever)
	int sum = 0;
	for(int i=0; i<ARRAY_SIZE; i++) {
		sum += bigNumList[i];
	}
	printf("%d\n", sum);
	
	return(0);
		
}

