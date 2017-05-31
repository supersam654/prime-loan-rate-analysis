import csv
from datetime import datetime

from tabulate import tabulate

data = []

def parse_row(row):
    if len(row) != 3:
        return None

    date_string, rate, _ = row
    if len(date_string) == 0 or len(rate) == 0:
        return None

    try:
        date = datetime.strptime(date_string, '%d-%b-%y')
        # Fix ambiguous 1900/2000 2-digit dates.
        if date.year > datetime.now().year:
            date = date.replace(year=date.year - 100)
        rate = float(rate)
    except TypeError:
        return None

    return date, rate

def load_data():
    data = []
    with open('prime.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            parsed_row = parse_row(row)
            if parsed_row is not None:
                data.append(parsed_row)
    return data

def avg(rows):
    values = [r[1] for r in rows]
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

    # Fill in missing rows.
    really_normal_data = [normal_data[0]]
    i = 1
    while i < len(normal_data):
        while really_normal_data[-1][0].year + 1 != normal_data[i][0].year:
            really_normal_data.append(list(really_normal_data[-1]))
            new_date = really_normal_data[-1][0].replace(year=really_normal_data[-1][0].year + 1)
            really_normal_data[-1][0] = new_date
        really_normal_data.append(normal_data[i])
        i += 1
    return really_normal_data

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

def main():
    YEARS = 5
    data = load_data()
    data.sort()
    data = normalize_dates(data)
    averages = calc_moving_averages(data, YEARS)

    max_average = max_averages(averages)

    for avg in averages:
        avg['Start Date'] = avg['Start Date'].year
        avg['End Date'] = avg['End Date'].year

    print(tabulate(averages, headers='keys', floatfmt=".2f"))
    print()
    print('Max %d-year positive difference: %.2f%% (from %d to %d)' % (YEARS, max_average['Difference'], max_average['Start Date'], max_average['End Date']))



if __name__ == '__main__':
    main()
