# TODO Найдите количество книг, которое можно разместить на дискете
str = 100
stroki = 50
simvoli = 25
mesto = 4 # в байтах
book_mb = str*stroki*simvoli*mesto/1024/1024
disk = 1.44
print("Количество книг, помещающихся на дискету:", int(disk//book_mb))
