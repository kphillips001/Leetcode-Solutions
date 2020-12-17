# Given a string S remove the vowels and return the new string

def removeVowels(s):
  # define emptry string:
  ans = ""
  # loop
  for c in s:
    if c in "aeiou":
      continue
    else:
      ans += c
  return ans

  def removeVowels(s):
    return ''.join(c for c in s if c not in 'aeiou')