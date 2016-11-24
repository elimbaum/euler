//
//  main.cpp
//  euler12
//
//  Created by Eli on 12/23/13.
//  Copyright (c) 2013 baum. All rights reserved.
//

#include <iostream>
using namespace std;

#include <math.h>
#include <vector>

/*  This is the lower bound of n;
 *  T_n is the lowest triangular number.
 *  See the txt file for derivation.
 */
#define LOWER_BOUND_N 11169

// Per the problem description.
#define MIN_TARGET_DIVISORS 500

int main(int argc, const char * argv[])
{
    // How many divisors the number has.
    unsigned int divisors = 0;
    
    // -1 to accomidate for the n++ at the top.
    unsigned int n = LOWER_BOUND_N - 1;
    
    unsigned int triangleNumber;
    
    cout<<"Project Euler 12"<<endl;
    
    while (divisors <= MIN_TARGET_DIVISORS) {
        
        // check the next triangle number.
        n++;
        
        // dynamic array to store the factorlist.
        vector<int> factors;
        
        // computer the triangle number
        triangleNumber = (n * (n + 1)) / 2;
        
        /*  now factor (trial division by odds).
         *  could be better by generating a list of primes.
         *  tempTri will get divided down.
         */
        unsigned int tempTri = triangleNumber;
        
        // first, check 2 (the only even)
        while ((tempTri % 2) == 0) {
            tempTri /= 2;
            factors.push_back(2);
            cout<<2<<endl;
        }
        
        // i is the divisor. conunt up every odd number.
        for (int i = 3; i < floor(sqrt(triangleNumber)); i += 2) {
            while (tempTri % i == 0) {
                tempTri /= i; // if i is a factor of n, divide.
                factors.push_back(i);
                cout<<i<<endl;
            }
            
        }
        
        if (tempTri != 1) {
            // tempTri is now the last factor... a prime
            factors.push_back(tempTri);
            cout<<tempTri<<endl;
        }
        
        cout<<"n = "<< n << "; T_n "<< triangleNumber << "; has " << factors.size() << " factors."<<endl;
        
        /* 'factors' now contains a list of all of the prime factors of triangleNumber.
         * now, count the number of duplicates (exponent on each factor)
         */
        int exponentArray[factors.size()]; // list of the exponents on the prime factors.
        
        // initialize array to all zeroes
        for(int i = 0; i<factors.size(); i++) {
            exponentArray[i] = 0;
        }

        // this stores the index of the array.
        int arrayCounter = 0;
        
        // the array is already sorted.
        for(int i=0; i<factors.size(); i++) {
            for (int j=i; j<factors.size(); j++) {
                if (factors.at(i) == factors.at(j)) {
                    // we have a duplicate!
                    exponentArray[arrayCounter]++;
                    i = j; // skip to next number.
                }
            }
            arrayCounter++;
        }
        
        
        // print the exponent array
        for(int i=0; i<factors.size(); i++) {
            cout<<exponentArray[i]<<" ";
        }
        cout<<endl<<endl;;
        
        
    }
    
    return 0;

}

