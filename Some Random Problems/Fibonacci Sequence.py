def fib(n):
  if n<=1:
    return n
  else:
    return (fib(n-1)+fib(n-2))
if __name__ == "__main__":
  terms = int(input("Input the number of Terms: \n"))
  print([fib(s) for s in range(terms)])
