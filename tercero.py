from random import randint
def play(y):
    return y + 1

def dot_it(x):

    return play (x*x)

def random_number():
    data = randint(0, 100)
    return data, dot_it(data)

ans = random_number()
print(f"Value: {ans[0]}")
print(f"Do_it: {ans[1]}")