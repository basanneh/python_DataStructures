def fibonacci_recursion(num):
    if num < 0:
        print("please enter a positive number")
        return
    if num <= 1:
        return num
    else:
        return fibonacci_recursion(num -1) + fibonacci_recursion(num -2)


F = [-1]*50 #array to store fibonacci terms

def dynamic_fibonacci(n):
  if (F[n] < 0):
    if (n <=1):
      F[n] = n
    else:
      F[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
  return F[n]

print(dynamic_fibonacci(6))
print(fibonacci_recursion(6))

