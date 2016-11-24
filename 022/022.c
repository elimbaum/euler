/* Euler 022
 * Names scores
 *
 * Sort a lot of names (alphabetically) and assign them a score.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
	
	/* Open the file */
	FILE *namesFile;
	namesFile = fopen("names.txt", "r");
	
	/* Start reading the file
	 * Format is "NAME","NAME","NAME"
	 * So quotations can be ignored, treat it as CSV.
	 */
	
	char **nameList = NULL;
	size_t nameListSize = 0;
	
	char c;
	do {
		char *name = NULL; // This will hold each name (new instance each loop)
		size_t nameSize = 0;
		
		/* Read the next character.
		 * Comma will move on to the next name, while
		 * EOF will end input (thanks to parent do...while)
		 */
		while (c = fgetc(namesFile), c != ',' && c != EOF) {
			
			// Skip "quotation marks"
			if(c == '"') {
				continue;
			}
			
			// Now we have a letter... add it to the name, and increase the size.
			name = realloc(name, ++nameSize * sizeof(char*));
			name[nameSize - 1] = c;
		}
		name[nameSize] = '\0'; // Null termination
		
		/* At this point, `name` contains a null-terminated name.
		 * Add it to the list.
		 */
		
		nameList = realloc(nameList, ++nameListSize * sizeof(char*));
		nameList[nameListSize - 1] = name;
		
		//printf("%s\n", name); // Print each name as it is read
		
	} while (c != EOF);


	/* Entire name list has been loaded. Sorting may commence.
	 * Using insertion sort (not terribly efficient, but simple)
	 */
	
	for(int i = 1; i < nameListSize; i++) {
		/* Now move the element around until it is in position. */
		for(int k = i; k > 0; k--) {
			if(strcmp(nameList[k], nameList[k-1]) >= 0) {
				// Element is sorted.
				break; // (and move on to next i)
			}
			
			// Element is not in position. Swap.
			char *temp = nameList[k];
			nameList[k] = nameList[k - 1];
			nameList[k - 1] = temp;
		}
	}
	
	/* Names are sorted. Now compute name scores.
	 * Note that my program is zero-indexed, while Euler is using one-indexes.
	 */
	 
	unsigned long sum = 0;
	
	for(int i = 0; i < nameListSize; i++) {
		unsigned int nameScore = 0;
		
		for(int k = 0; k < strlen(nameList[i]); k++) {
			nameScore += nameList[i][k] - 'A' + 1; // Convert to alpha position
		}
		
		//printf("%s\t%i\n", nameList[i], nameScore);
		
		sum += nameScore * (i + 1);
	}
	
	printf("%lu\n", sum);
}