#Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n
#example:>>> intreverse(783)
#o/p:387

def intreverse(n):
    str_n = str(n)
    reversed_str_n = str_n[::-1]
    reversed_n = int(reversed_str_n)
    return reversed_n
#by instructor
def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

#Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.
#>>> matched("zb%78")
#True
#>>> matched("(7)(a")
#False

def matched(s):
    balance = 0  
    
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        if balance < 0:
            return False
    
    return balance == 0
  
#by instructor
def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)

#Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.
#>>> sumprimes([3,3,1,13])
#19
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sumprimes(l):
    return sum(x for x in l if is_prime(x))
  
#by instructor
def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
  return(factors(n) == [1,n])


def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)
