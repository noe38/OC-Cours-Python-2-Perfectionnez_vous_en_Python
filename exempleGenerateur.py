""" def my_generator():
    i = 40
    while i <= 56:
        i += 2
        yield i """

def generator(start, end):

    print("    On commence !")
    cnt = start
    while cnt <= end:
        if start % 2 == 0:
            print("    On s'arrete au yield")
            yield float(cnt)
            print("   On reprend après le yield")
        else:
            print("     On s'arrete au yield")
            yield str(cnt)
            print("      On reprend après la yield")
        cnt += 1
    yield "C'est bientôt la fin"
    yield "C'est VRAIMENT bientôt la fin"
    yield "Là c'est la fin"

for i in generator(4, 8):
    print(i)
