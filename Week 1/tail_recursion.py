def sum_to(n, acc=0):
    if n==0:
      return acc
    return sum_to(n-1, acc+n)
    
def sum_iter(n):
    acc = 0
    for i in range(1, n+1):
        acc += i
    return acc
    
print(sum_to(100))
print(sum_iter(100))
