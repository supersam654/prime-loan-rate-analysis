import csv
from datetime import datetime

from tabulate import tabulate

data = []

def parse_row(row):
    date_string, rate = row

    date = datetime.strptime(date_string, '%Y-%m-%d')
    rate = float(rate)

    return date, rate

def load_data(filename):
    data = []
    with open(filename) as f:
        reader = csv.reader(f)
        # Skip header
        next(reader)
        for row in reader:
            parsed_row = parse_row(row)
            if parsed_row is not None:
                data.append(parsed_row)
    return data

def avg(rows):
    values = [r[1] for r in rows]
    # Actually use the first value of every year instead of the average.
    # return sum(values) / len(values)
    return values[0]

def normalize_dates(data):
    if len(data) == 0:
        return data

    normal_data = []
    first_year = data[0][0].year
    same_year_rows = []
    for row in data:
        date, rate = row
        if date.year > first_year:
            normal_data.append((same_year_rows[0][0], avg(same_year_rows)))
            first_year = date.year
            same_year_rows = [row]
        else:
            same_year_rows.append(row)
    normal_data.append((same_year_rows[0][0], avg(same_year_rows)))

    return normal_data

def calc_moving_averages(data, years):
    if len(data) == 0:
        return

    averages = []
    for i in range(len(data) - years):
        start_date, start_rate = data[i]
        date, rate = data[i + years]
        averages.append({
            'Difference': rate - start_rate,
            'Start Date': start_date,
            'End Date': date,
            'Start Rate': start_rate,
            'End Rate': rate
        })
    return averages

def max_averages(averages):
    diffs = [(d['Difference'], i) for i, d in enumerate(averages)]
    diffs.sort(reverse=True)
    return averages[diffs[0][1]]

def main(filename, years):
    data = load_data(filename)
    data.sort()
    data = normalize_dates(data)
    averages = calc_moving_averages(data, years)

    max_average = max_averages(averages)

    for avg in averages:
        avg['Start Date'] = avg['Start Date'].year
        avg['End Date'] = avg['End Date'].year

    print(tabulate(averages, headers='keys', floatfmt=".2f"))

if __name__ == '__main__':
    main(argv[1], argv[2])
