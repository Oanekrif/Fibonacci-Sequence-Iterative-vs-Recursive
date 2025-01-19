# Function to generate Fibonacci sequence iteratively
def fibonacci(n):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(n):  # Loop to generate the Fibonacci sequence up to n terms
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers

# Function to generate Fibonacci sequence recursively
def recfibonachi(n):
    if n < 2:  # Base case: return n if it's 0 or 1
        return n
    else:  # Recursive case: sum of the previous two Fibonacci numbers
        return recfibonachi(n - 1) + recfibonachi(n - 2)

# Taking input for the number of Fibonacci terms
n = int(input("Enter the number of terms: "))

# Print Fibonacci sequence using the iterative method
fibonacci(n)

print("\n")  # Print a newline for separation

# Print Fibonacci sequence using the recursive method
for i in range(n):  # Loop to print Fibonacci numbers recursively
    print(recfibonachi(i), "", end="")  # Print the i-th Fibonacci number recursively
git fetch origin git checkout main