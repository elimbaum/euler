/*	Project Euler  18
 *	Maximum path sum I
 *
 *	Dynamic Programming approach
 *
 *	Single execution time ~ 5 ms.
 *	However I looped just the algorithm 60,000 times and it ran it 66 ms.
 *	Average time per loop: 1.1 microseconds.
 *	That would be about 3400 clock cycles... cool!
 */
 
#include <stdio.h>


/* Number of rows. */
#define SIZE 15

/*	Two dimensional array to hold the triangle.
 *	Regrettably, uses twice as much memory as needed...
 *  Zero values are not part of actual triangle.
 */
int T[SIZE][SIZE] =
	{{75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {95, 64,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {17, 47, 82,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {18, 35, 87, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {20,  4, 82, 47, 65,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {19,  1, 23, 75,  3, 34,  0,  0,  0,  0,  0,  0,  0,  0,  0},
	 {88,  2, 77, 73,  7, 63, 67,  0,  0,  0,  0,  0,  0,  0,  0},
	 {99, 65,  4, 28,  6, 16, 70, 92,  0,  0,  0,  0,  0,  0,  0},
	 {41, 41, 26, 56, 83, 40, 80, 70, 33,  0,  0,  0,  0,  0,  0},
	 {41, 48, 72, 33, 47, 32, 37, 16, 94, 29,  0,  0,  0,  0,  0},
	 {53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,  0,  0,  0,  0},
	 {70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,  0,  0,  0},
	 {91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,  0,  0},
	 {63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,  0},
	 { 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23}};
	 
/*	Two dimensional mirror array
 *	Holds the maximum sum to that node.
 *	Initialized to all zero.
 */
int S[SIZE][SIZE] = {0};

int main() {
	printf("Project Euler 018\n");

	/*	Set the first value to the triangle's apex. Here, 75 */
	S[0][0] = T[0][0];

	/*	Loop through rows (starting @ 1) & columns. */
	for(int r = 1; r < SIZE; r++) {
		/*	Calculate the leftmost number (special case).
		 *	Number directly above.
		 */
		S[r][0] = T[r][0] + S[r-1][0];

		/* Now do internal numbers. */
		for(int c = 1; c < r; c++) {
			/* The greatest path is the maximum of the two above it. */
			if(S[r-1][c-1] > S[r-1][c]) {
				S[r][c] = T[r][c] + S[r-1][c-1]; // up and to the left
			} else {
				S[r][c] = T[r][c] + S[r-1][c]; // directly above
			}
		}

		/*	And the rightmost number (special case).
		 *	Up and to the left.
		 */
		S[r][r] = T[r][r] + S[r-1][r-1];

	}

	/*	Now get the maximum in the last row. */
	int maximum = 0;
	for(int i = 0; i < SIZE; i++) {
		if(S[SIZE-1][i] > maximum) {
			maximum = S[SIZE-1][i];
		}
	}
	printf("%d\n", maximum);
	
	return(0);
}
	
	