def reverse_p(*a):
    reverse = a[::-1]
    for arg in reverse:
        print(arg)

reverse_p(1, 2, 3, 4, 5)
#2
def ad(p1, p):

    result = eval(p) + eval(p1)
    print(result)
   
ad( "5","3")