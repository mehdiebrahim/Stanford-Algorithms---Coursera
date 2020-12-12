
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x,y):
    
    if len(str(x))<3 or len(str(y))<3:
        #base case, can also set len(str(x))==1 and same for len(str(y))==1 but takes more iterations
        return x*y
    
    n_x = len(list(str(x))) #no. of digits 
    n_y = len(list(str(y))) #no. of digits 
    n = max(n_x,n_y) #the longest integer, with most digits 
    n_2 = n//2 #deals with the problem of having odd digits, so ignores remainder
    
    a = x//10**(n_2) #first half of x
    b = x%10**(n_2) #second half of x
    c = y//10**(n_2) #first half of y
    d = y%10**(n_2) #second half of y
    
    ac = karatsuba(a,c) #recursively compute ac, as a and c can be very long
    bd = karatsuba(b,d) #recursively compute bd, as b and d can be very long
    ab_dc = karatsuba(a+b,c+d) #recursively compute a+b
    ad_bc = ab_dc - ac - bd #computes ad+bc using Gauss's trick
    
    xy = (10**(2*n_2))*ac + 10**(n_2)*(ad_bc)+bd #computes the xy which it then returns. if the 
                                                 # length of x and y meets certain condition, if stateent is triiggered
    return xy
        
karatsuba(x,y)