# Selection_sort the Big O notation will be O(n(n+1)/2 ) best than Bubble sort
# Complixity = O(n(n+1)/2)

def selection_sort(x):
    for i in range(len(x)):
        index = i
        for j in range(i, len(x)):
            if x[j] < x[i]:
                index = j
        x[index], x[i] = x[i], x[index]
    return x


x = list(range(100, 0, -1))
print(selection_sort(x))
