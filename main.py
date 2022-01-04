# Problem ALG004r

def rotation0(n):
    magicsquare = [[0 for x in range(n)]
                   for y in range(n)]
    #    0 1 2 ... n
    # 0 [0,0,0];
    # 1 [0,0,0];
    # 2 [0,0,0];
    # ...
    # n

    num = 1
    rows, col = 0, n / 2
    while num <= (n * n):
        magicsquare[int(rows)][int(col)] = num
        num += 1
        new_row, new_col = (rows - 1) % n, (col + 1) % n
        if magicsquare[int(new_row)][int(new_col)]:
            rows += 1
        else:
            rows, col = new_row, new_col
    print(f"\nMagic Square for Rotation 0 with a Dimension of {n}")
    for rows in range(0, n):
        for col in range(0, n):
            print(f"{magicsquare[rows][col]}", end=" | ")
            if col == n - 1:
                print("")
    sum_const = n * (n ** 2 + 1) / 2
    print(f"\nConstant Sum of each row, column and diagonal is = {sum_const}")


def rotation1(n):
    magicsquare = [[0 for x in range(n)]
                   for y in range(n)]
    #    0 1 2 ... n
    # 0 [2,7,6];            #(-1,+1)
    # 1 [9,5,1]; index[1,2]
    # 2 [4,3,8];
    # ...
    # n
    num = 1
    rows, col = n / 2, n - 1
    while num <= (n * n):
        if rows == -1 and col == n:
            col = n - 2
            rows = 0
        else:
            if col == n:
                col = 0
            if rows < 0:
                rows = n - 1
        if magicsquare[int(rows)][int(col)]:
            col = col - 2
            rows = rows + 1
            continue
        else:
            magicsquare[int(rows)][int(col)] = num
            num = num + 1
        rows = rows - 1
        col = col + 1
    print(f"\nMagic Square for Rotation 1 with a Dimension of {n}")
    for rows in range(0, n):
        for col in range(0, n):
            print(f"{magicsquare[rows][col]}", end=" | ")
            if col == n - 1:
                print()
    sum_const = n * (n ** 2 + 1) / 2
    print(f"\nConstant Sum of each row, column and diagonal is = {sum_const}")


def rotation2(n):
    magicsquare = [[0 for x in range(n)]
                   for y in range(n)]
    num = 1
    rows, col = n - 1, n / 2
    while num <= (n * n):
        magicsquare[int(rows)][int(col)] = num
        num += 1
        new_row, new_col = (rows + 1) % n, (col + 1) % n
        if magicsquare[int(new_row)][int(new_col)]:
            rows -= 1
        else:
            rows, col = new_row, new_col
    print(f"\nMagic Square for Rotation 2 with a Dimension of {n}")
    for rows in range(0, n):
        for col in range(0, n):
            print(f"{magicsquare[rows][col]}", end=" | ")
            if col == n - 1:
                print()
    sum_const = n * (n ** 2 + 1) / 2
    print(f"\nConstant Sum of each row, column and diagonal is = {sum_const}")


def rotation3(n):
    magicsquare = [[0 for x in range(n)]
                   for y in range(n)]
    #       0 1 2                 +1;-1
    # 0    [8,3,4];    index[1,0]                =1
    # 1    [1,5,9];        *[2,-1] => [2,2]      =2
    # 2    [6,7,2];        *[3,1]  => [0,1]      =3
    #                      *[1,0]  => [0,2]      =4
    #                       [1,1]                =5
    #                       [2,0]                =6
    #                      *[3,-1]  => [2,1]     =7
    #                      *[3,0]   => [0,0]     =8
    #                      *[1,-1]  => [1,2]     =9
    num = 1
    rows, col = int(n / 2), n-n
    while num <= (n * n):
        if rows == n and col < 0:
            col = col + 2
            rows = n - 1
        else:
            if col < 0:
                col = n - 1
            if rows == n:
                rows = 0
        if magicsquare[int(rows)][int(col)]:
            col = col + 2
            rows = rows - 1
            continue
        else:
            magicsquare[int(rows)][int(col)] = num
            num = num + 1
        col = col - 1
        rows = rows + 1
    print(f"\nMagic Square for Rotation 3 with a Dimension of {n}")
    for rows in range(0, n):
        for col in range(0, n):
            print(f"{magicsquare[rows][col]}", end=" | ")
            if col == n - 1:
                print()
    sum_const = n * (n ** 2 + 1) / 2
    print(f"\nConstant Sum of each row, column and diagonal is = {sum_const}")


print("Magic Square generator\n")
r = int(input("Please input a Rotation\n"
              "- If rotation = 0, then the starting 1 is top middle\n"
              "- If rotation = 1, then the starting 1 is right middle\n"
              "- If rotation = 2, then the starting 1 is bottom middle\n"
              "- If rotation = 3, then the starting 1 is left middle\n\n"
              "Rotation = "))
number = int(input("\nPlease input an odd Dimension\nFor Example: '3', which will produce a 3x3 magic square\n"
                   "Dimension = "))
if r == 0:
    print(rotation0(number))
elif r == 1:
    print(rotation1(number))
elif r == 2:
    print(rotation2(number))
elif r == 3:
    print(rotation3(number))
else:
    print("Invalid input")
