var("x y")
inp = [(26, 66, 70314326037540683861066), (175, 242, 1467209789992686137450970), (216, 202, 1514632596049937965560228), (13, 227, 485439858137512552888191), (1, 114, 112952835698501736253972), (190, 122, 874047085530701865939630), (135, 12, 230058131262420942645110), (229, 220, 1743661951353629717753164), (193, 81, 704858158272534244116883)]
xs = [i[0] for i in inp]
ys = [i[1] for i in inp]
s = [i[2] for i in inp]
A = matrix([[i^2 for i in xs], [i^2 for i in ys], [xs[i]*ys[i] for i in range(len(xs))], [i for i in xs], [i for i in ys], [1]*len(xs)]).transpose()
b = matrix(s).transpose()
c = list(A.solve_right(b).transpose()[0])
x1,y1 = 886191939093, 589140258545
f(x,y)=c[0]*x^2+c[1]*y^2+c[2]*x*y+c[3]*x+c[4]*y+c[5]
print(bytes.fromhex((hex(int(f(x1,y1))^^19440293474977244702108989804811578372332250))[2:]).decode('utf-8'))