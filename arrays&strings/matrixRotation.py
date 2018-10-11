

def rotateMax(m):
    print('--------original--------')
    printMatrix(m)
    #return if maxtix len is zero
    if not len(m):
        return

    top = 0
    bottom = len(m) - 1

    left = 0
    right= len(m[0]) - 1

    while left < right and top < bottom:

        first = m[top+1][left]

        #move elements from top row to right column
        for i in range(left,right+1):
            curr = m[top][i]
            m[top][i] = first
            first = curr

        print('----first iteration---')
        printMatrix(m)
        #increment top once done

        top +=1
        #move right olumn elemnets to bottom
        for i in range(top,bottom+1):
            curr = m[i][right]
            m[i][right] = first
            first = curr

        right -= 1

        #move bottom to left
        for i in range(right, left-1 , -1):
            curr = m[bottom][i]
            m[bottom][i] = first
            first = curr

        bottom -= 1

        #move left to top
        for i in range(bottom, top-1, -1):
            curr= m[i][left]
            m[i][left] = first
            first = curr

        left += 1

    return m

def printMatrix(m):
    for row in m:
        print(row)


matrix =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
m  = rotateMax(matrix)
print('------final----------')
printMatrix(m)


