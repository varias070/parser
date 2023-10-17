from extractor import get_data
from writer import write_csv

# у каждого магазина свой id, извлек из запросов id магазинов из Москвы и Санкт-Петербурга
piter = 10
moscow = 15

moscow_data = get_data(moscow)
piter_data = get_data(piter)

write_csv(moscow_data, "moscow")
write_csv(piter_data, "piter")
