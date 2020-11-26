import csv
import iso8601

def print_summary():
    sales_sum = 0  # Сума на продажбите
    min_ts = None  # Начало на периода за отчитане
    max_ts = None  # Край на периода за отчитане
    with open("sales.csv") as f:
        reader = csv.reader(f)
        for n, column in enumerate(reader, 1):
            sales_sum += float(column[4])
            if max_ts is None or max_ts < column[3]:
                max_ts = column[3]
            if min_ts is None or min_ts > column[3]:
                min_ts = column[3]
    print(''' \t Обобщение
    ---------------------------------------------
        ''')
    print(f" \t Общ брой продажби: {n}")
    print(f" \t Обща сума на продажбите: {sales_sum} €")
    print(f" \t Средна цена на продажбите: {(sales_sum / n):.3f} €")
    print(f" \t Начало на периода: {min_ts}")
    print(f" \t Край на периода: {max_ts}")
    print('''
        ''')
    f.close()

def print_sale_hour():
    sale_by_hour = {}
    with open("sales.csv") as f:
        reader = csv.reader(f)
        for column in reader:
            # Часове
            price = float(column[4])
            dt = iso8601.parse_date(column[3])
            ts_hour = dt.replace(minute=0, second=0, microsecond=0)
            hour = ts_hour.hour
            # Продажби в съответния час
            if sale_by_hour.get(hour) is None:
                sale_by_hour[hour] = price
            else:
                sale_by_hour[hour] = sale_by_hour.get(hour) + price
        amounts_by_hour_sorted = []
        for h, total_amount in sale_by_hour.items():
            amounts_by_hour_sorted.append((total_amount, h))
        amounts_by_hour_sorted.sort(reverse=True)
        print(''' \t Сума на продажби по часове
    ---------------------------------------------
            ''')
        for total_amount, h in amounts_by_hour_sorted[:3]:
            print(f"\t {h}: {total_amount:.2f} €")

        f.close()


print_summary()
print_sale_hour()