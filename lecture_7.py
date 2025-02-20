#Lecture 7
#Function

def is_even(i):
    """
    Input:i, a positive int
    Returns True if i is even, otherwise False
    """
    if i%2 ==0:
        return True
    else:
        return False

print(is_even(3))
print(is_even(8))

def is_even(i):
    """
    Input:i, a positive int
    Returns True if i is even, otherwise False
    """
    return i%2 ==0

def div_by(n, d):
    """

    :param n: n is a positive integer
    :param d: d is another positive integer
    :return: Bool, True if d divides n , else return false
    """
    return n%d == 0

print(div_by(51,3))
print(div_by(6,4))

for i in range(1,10):
    if is_even(i):
        print(i, "Even")
    else:
        print(i, "Odd")

def sum_odd(a,b):
    """

    :param a: Lower limit for starting to sum the odd numbers
    :param b: Upper limit for ending to sum the odd numbers
    :return: Sum of odd numbers between a and b
    """
    ans = 0
    for j in range(a,b+1):
        if not is_even(j):
            ans += j
    return ans

print(sum_odd(1,9))

#to find whether a string is palindrome or not
def pali_1(str):
  if (str[::-1]==str):
      return True
  else:
      return False

str1 = input("enter a palindrome")
sr = pali_1(str1)
print(sr)