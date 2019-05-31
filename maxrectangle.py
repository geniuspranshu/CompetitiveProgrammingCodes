def sumZero(temp, starti, endj, n):
    presum = {}
    sum = 0
    max_length = 0
    for i in range(0, n):
        sum += temp[i]
        if temp[i] == 0 and max_length == 0:
            starti = i
            endj = i
            max_length = 1
        if sum == 0:
            if max_length < i + 1:
                starti = 0
                endj = i
            max_length = i + 1

        if sum in presum:
            old = max_length
            max_length = max(max_length, i - presum[sum])
            if old < max_length:
                endj = i
                starti = presum[sum] + 1
        else:
            presum[sum] = i

    return max_length != 0, starti, endj


def sumZeroMatrix(a, row, col):
    fup = 0
    fdown = 0
    fleft = 0
    fright = 0
    maxl = -999999999
    up = 1
    down = 0
    for left in range(0, col):
        temp = [0] * row
        for right in range(left, col):
            for i in range(0, row):
                temp[i] += a[i][right]
            print(temp)
            c_sum, up, down = sumZero(temp, up, down, row)
            ele = (down - up + 1) * (right - left + 1)

            if c_sum and ele > maxl:
                fup = up
                fdown = down
                fleft = left
                fright = right
                maxl = ele

    print(abs(fdown- fup +1)*abs(fright-fleft+1))


if __name__ == '__main__':
    a = [[9, 7, 16, 5], [1, -6, -7, 3],
         [1, 8, 7, 9], [7, -2, 0, 10]]

    row = 4
    col = 4
    sumZeroMatrix(a, row, col)