"""
Given a String as input, count the number of times the substring "Java" appears in the string. Use recursion. Do not use loops.
Input-> "HelloJavaMaster"
Output-> 1
"""

def recur(st):
  ln = len(st)
  if ln == 0:
    return ""
  ch = st[0]
  count = 0
  if (ch=="Java"):
    count = count + 1
    return count
  else:
    return recur(st[1:])

st = "HelloJavaMaster"
print(recur(st))