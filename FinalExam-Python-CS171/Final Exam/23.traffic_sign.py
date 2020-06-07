
def traffic_sign(n):
    while(n > 0):
        print('No parking')
        n = n - 1

def traffic_sign_recursion(n):
    if(n == 0):
        return None
    else:
        print(f'{n}: No parking')
        traffic_sign_recursion(n - 1)


#traffic_sign(0)
traffic_sign_recursion(100)