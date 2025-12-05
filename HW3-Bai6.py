a = int(input("hay nhap so a:"))
dem = 0
for i in range(1, a + 1):
    if a % i == 0:
       dem = dem + 1
print(dem)