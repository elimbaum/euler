# Does mod10 addition... experiments for 027

n = int(input("starting value? "))

i = 2

# divisibility
while n not in (0, 2, 4, 5, 6, 8):
   print(n)
   n = (n + i) % 10
   i += 2

print(n)