scores = list(map(float, input().split()))
a1, b1, c1, a2, b2, a3 = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]
numerator = ( a1 + b1 + c1 ) + ( a2 + b2 )*2 + a3*3
average= numerator/10
print(f"{average:.2f}")