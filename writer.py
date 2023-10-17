import csv


def write_csv(entitys, filename):
    with open(f'{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'Название', 'Ссылка', 'Бренд', 'Цена', 'Промо цена']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for entity in entitys:
            writer.writerow({
                'id': entity["id"],
                'Название': entity["name"],
                'Ссылка': entity["link"],
                'Бренд': entity["manufacturer"],
                'Цена': entity["normal_price"],
                'Промо цена': entity["promo_price"],
            })
