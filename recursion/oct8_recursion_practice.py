


def countdown(n):
    #Breaking condition
    if n<=0:
        print("Done")
        return
    print(n)
    countdown(n-1)

# sum of the number using recursion
def countdown(n):
    #Breaking condition
    if n==0:
        return 0

    return n + countdown(n-1)
# return 1 + countdown(1-1) 이 될때까지 countdown(n-1)의 값을 알수없으니
# 끝까지 가서 countdown(1-1) = 0이고 Breaking condition에 걸려서 리턴 0이되는순간 값을알게되서 다시 거슬러올라간다.

countdown(5)

def palindrome(s):
    """
    /Assuming that the input is case sensitive and there are no white space
    """
    #Breaking condition 1
    if len(s) <= 1:
        return True     #meaning it is palindreome
    #Breaking condition 2
    #check the first and the last
    if s[0] != s[-1]:
        return False    #meaning it is not palindreome

    return palindrome(s[1:-1])  #substring sending everything first letter to the last letter

print(palindrome("Hello World"))
print("racecaR",palindrome("racecaR"))
print(palindrome(" racecar"))
print(palindrome("Racecar"))

#edge case: White space / Case sensitive


def sum_nested_list(lst):
    total = 0
    for item in lst:
        if type(item) == int:
            total += item
        elif type(item) == list:
            total += sum_nested_list(item)
    return total


print(sum_nested_list([1, [2, [3, 4], 5], 6]))


def count_vowels(s):
    if s == "":
        return 0
    first_char = s[0].lower()
    rest = s[1:]

    if first_char in "aeiou":
        return 1 + count_vowels(rest)
    else:
        return count_vowels(rest)

print(count_vowels("Recursion is neat!"))
