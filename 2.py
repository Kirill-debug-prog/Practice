fibonacci = lambda n: [0, 1] + [fibonacci(i-1) + fibonacci(i-2)
                                for i in range(2, n+1) 
                                if fibonacci(i-1) + fibonacci(i-2) <= n]
print(fibonacci(50))
