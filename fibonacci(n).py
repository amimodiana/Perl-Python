def fibonacci(n):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the sequence up to n numbers
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Return the sequence, truncated to n elements
    return fib_sequence[:n]
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
