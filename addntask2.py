fname="stringSimilarityInput.txt"   
with open(fname) as reader:
    S1=reader.readline()
    S2=reader.readline()

m=len(S1)
n=len(S2)
D=[[0 for i in range(n+1)] for j in range(m+1)]
P=[[None for i in range(n+1)] for j in range(m+1)]

#Initialize values for row zero and column zero here.
for i in range(m+1):
    D[i][0] = i
for j in range(n+1):
    D[0][j] = j

for i in range(1,m+1):
    for j in range(1,n+1):
        if (S1[i-1]==S2[j-1]):
            D[i][j] = D[i-1][j-1]
            P[i][j] = (i-1, j-1)
        else:
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            substitute = D[i-1][j-1] + 1
            min_distance = min(insert, delete, substitute)
            D[i][j] = min_distance
            if min_distance == insert:
                P[i][j] = (i, j-1)
            elif min_distance == delete:
                P[i][j] = (i-1, j)
            else:
                P[i][j] = (i-1, j-1)

# Print the optimal edit transcript
transcript = []
i, j = m, n
while True:
    if P[i][j] is None:
        break
    pi, pj = P[i][j]
    if pi == i-1 and pj == j-1:
        if S1[i-1] == S2[j-1]:
            transcript.append('M')
        else:
            transcript.append('S')
    elif pi == i and pj == j-1:
        transcript.append('I')
    else:
        transcript.append('D')
    i, j = pi, pj


for i in range(1,m+1):
    print('\n')
    for j in range(1,n+1):
        print(D[i][j],end=' ')
        
        print('\nOptimal edit transcript:', ''.join(reversed(transcript)))
