#========================
#== Function Recursion ==
#========================

#x="wwwoooorrrlldd"
#print(x[1:])

def cleanword(word):
    if len(word) == 1:
        return word
    if word[0] == word[1] :
        return cleanword(word[1:])
    return word[0] + cleanword(word[1:])

print(cleanword("woooorlld"))

# Function To Calculate Sumation
def sum_num(n):
    if n==1:
        return 1
    else:
        return n+sum_num(n-1)
print(sum_num(n=int(input("enter number to calculate sum\n"))))

# Function To Calculate Factorial
n=1
n=float(n)
def fact_num(n):
    if n==1:
        return 1
    else:
        return n*fact_num(n-1)

print(fact_num(n=int(input("enter number to calculate factorial\n"))))