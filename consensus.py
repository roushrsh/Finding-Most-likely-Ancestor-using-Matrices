#Consensus and profile
import sys #todisplayonsame line
#readfromfile,findoutmatrixproperties
textfile = "rosalind_cons2.txt"  #as it's needed to write twice
s = open(textfile)

count = 0
leng = 0
height = 0
##get width and height
for x in s:
    if (x[0] == '>'): #move passed Rosalind lines
        height = height +1 #gets height
        leng = count
        count = 0
    if (x[0] == 'T' or x[0] == 'G' or x[0]=='C' or x[0] == 'A'):
        for y in x:
            if (y == 'T' or y == 'G' or y=='C' or y == 'A'):
                count = count +1
width = leng

#setup our two matrices

Matrix = [['e' for x in range(width)] for y in range(height)]
Matrixnum = [[0 for x in range(width)] for y in range(4)]


##matrix setup ##########
s = open(textfile)
a=-1 #as First line is always Rosalind
for x in s: #placing into first matrices
        if (x[0] == '>'):
            a= a+1
            b=0
        if (x[0] == 'T' or x[0] == 'G' or x[0]=='C' or x[0] == 'A'):
            for y in x:
                if (y == 'T' or y == 'G' or y=='C' or y == 'A'):
                    Matrix[a][b] = y
                    b = b + 1
#based on first matrix, creating second
##creating Matrix for ATCG letters in it 4 by width
i=-1
for y in range(0, width):
    i = i+1
    ACount = 0;
    GCount = 0;
    TCount = 0;
    CCount = 0;
    for x in range(0, height):
        if Matrix[x][y] == 'G':
            GCount= GCount+1
        if Matrix[x][y] == 'A':
            ACount= ACount+1
        if Matrix[x][y] == 'C':
            CCount= CCount+1
        if Matrix[x][y] == 'T':
            TCount= TCount+1
    Matrixnum[0][i] = ACount
    Matrixnum[1][i] = CCount
    Matrixnum[2][i] = GCount
    Matrixnum[3][i] = TCount

#using sys to print on same line clean. 
for u in range(width):
    if ((Matrixnum[0][u] >= Matrixnum[1][u]) and (Matrixnum[0][u] >= Matrixnum[2][u]) and (Matrixnum[0][u] >= Matrixnum[3][u])):
        sys.stdout.write('A')
    elif ((Matrixnum[1][u] >= Matrixnum[0][u]) and (Matrixnum[1][u] >= Matrixnum[2][u]) and (Matrixnum[1][u] >= Matrixnum[3][u])):
        sys.stdout.write('C')
    elif ((Matrixnum[2][u] >= Matrixnum[0][u]) and (Matrixnum[2][u] >= Matrixnum[1][u]) and (Matrixnum[2][u] >= Matrixnum[3][u])):
        sys.stdout.write('G')
    elif ((Matrixnum[3][u] >= Matrixnum[0][u]) and (Matrixnum[3][u] >= Matrixnum[1][u]) and (Matrixnum[3][u] >= Matrixnum[2][u])):
        sys.stdout.write('T')

print ''
print 'A:', (" ".join(str(x) for x in Matrixnum[0])) #have to us join to remove brackets and commas
print 'C:', (" ".join(str(x) for x in Matrixnum[1]))
print 'G:', (" ".join(str(x) for x in Matrixnum[2]))
print 'T:', (" ".join(str(x) for x in Matrixnum[3]))
