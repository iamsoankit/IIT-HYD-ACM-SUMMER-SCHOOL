fname="stringSimilarityInput.txt"   
with open(fname) as reader:
    S1=reader.readline().strip()
    S2=reader.readline().strip()

m=len(S1)
n=len(S2)
D=[[0 for i in range(n+1)] for j in range(m+1)]

#Initialize values for row zero and column zero here.
for i in range(m+1):
    D[i][0] = i
for j in range(n+1):
    D[0][j] = j

for row in range(1, m+1):
    for col in range(1, n+1):
        if S1[row-1] == S2[col-1]:
            D[row][col] = D[row-1][col-1]
        else:
            D[row][col] = min(D[row-1][col], D[row][col-1], D[row-1][col-1]) + 1

for i in range(1,m+1):
    print('\n')
    for j in range(1,n+1):
        print(D[i][j],end=' ')