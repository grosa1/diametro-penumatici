import sys

h = int(sys.argv[1])
c = int(sys.argv[2])
r = int(sys.argv[3])

diametro = (((h * c)/100 * 2) + (r * 25.4))/10
print('diameter = ' + str(round(diametro, 2)) + 'cm')