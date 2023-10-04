def fact(n, m):
  if n == m:
    return n
  else :
    return n + fact(n + 1, m)
  
fact(1, 1000)