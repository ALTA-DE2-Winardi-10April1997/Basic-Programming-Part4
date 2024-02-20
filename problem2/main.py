def draw_xyz(N):
    x = 1
    pattern = ""
    for i in range(1, N+1):
        row = ""
        for j in range(1, N+1):
            nilai = str(x)
            if int(nilai) % 3 == 0:
                row += "X "
            elif int(nilai) % 2 == 0:
                row += "Z "
            else:
                row += "Y "
            x += 1
        pattern += row + "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """