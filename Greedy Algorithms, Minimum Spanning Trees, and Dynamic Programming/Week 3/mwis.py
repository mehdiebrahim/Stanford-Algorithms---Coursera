os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')

def mwis(weights , n):
    book_keeper = [0,weights[1]]
    #mwis for first i vertices in graph. First 0 vertices, total weight of MWIS
    # is 0. Then until first vertices we have only that vertice being sum of MWIS
    for i in range(2,n+1):
        book_keeper.append(0)
        #initialise to 0 
    for i in range(2,n+1):
        book_keeper[i] = max(book_keeper[i-1],book_keeper[i-2]+ weights[i])
        #the book_keeper[i-1] term is if vi is not in the MWIS of graph Gi, 
        #so A[i]=A[i-1] if book_keeper[i-2]+ weights[i] is less than A[i-1]. Otherwise 
        #vi is in A[i] 
        
    IS = set()
    j = n     
    #second pass to reconstruct 
    while(j >= 1):
        if book_keeper[j-1] >= (book_keeper[j-2] + weights[j]):
            j -=1
        else:
            IS.add(j)
            j -= 2
    return IS 



weights = [0]
with open('mwis.txt') as f:
    n = int(f.readline())
    data = f.readlines()
    for line in data:
        weights.append(int(line[:-1]))

IS = mwis(weights , n)

ans = ""
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    if i in IS:
        ans += '1'
    else:
        ans += '0'
print(ans)