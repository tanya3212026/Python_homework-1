def square(side):

    side_round = int(side) + (side % 1 > 0)
    print('Площадь квадрата = ' + str(side_round * side_round))


square(198.1)
