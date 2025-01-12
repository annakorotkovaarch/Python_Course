# TODO Найдите количество книг, которое можно разместить на дискете

d_volume_mb = 1.44
page_count = 100
line_count = 50
symbol_count = 25
symbol_weight = 4
d_volume_kb = d_volume_mb * 1024
d_volume_b = d_volume_kb * 1024

book_total = page_count * line_count * symbol_count
book_total_weight = book_total * symbol_weight

book_count = d_volume_b / book_total_weight
book_count = int(book_count)

print("Количество книг, помещающихся на дискету:", book_count)
