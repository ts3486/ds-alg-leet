n = 0

def inception():
    global n
    print(n)
    if n > 3:
        return "done!"
    n+=1
    return inception()
    
inception()

# base case 
# recursive case
# return value for recursive case and base case in most cases

#find factorial iteratively O(n)
def find_factorial_iterative(number):
    answer = 1
    for i in range(2, number + 1):
        answer *= i
    return answer

print(find_factorial_iterative(5))

#find factorial recursively O(n)
def find_factorial_recursive(number):
    if number == 2:
        return 2
    return number * find_factorial_recursive(number - 1)

print(find_factorial_recursive(5))

#find fibonacci iteratively O(n)
def find_fibonacci_iterative(number):
    if number < 2:
        return number
    fib = [0, 1]
    for i in range(2, number + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[number]

#find fibonacci recursively O(2^n)
def find_fibonacci_recursive(number):
    if number < 2:
        return number
    return find_fibonacci_recursive(number - 1) + find_fibonacci_recursive(number - 2)

#Anything that you can program recursively, you can program iteratively. Hence there are always two options and the choice depends on the problem, constraints, readability, complexity, etc.

#When using a tree, consider using recursion.





