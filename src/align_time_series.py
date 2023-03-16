import argparse
import csv
from datetime import datetime
from os.path import basename, join, dirname
from time import strptime, struct_time, mktime


def first_non_null_value(csv_data, time_column, value_column, time_format) -> struct_time:
    for line in csv_data:
        str_val = line[value_column]
        val = float(str_val) if not str_val.endswith('%') else float(str_val.strip('%'))
        if val > 0.0:
            return strptime(line[time_column], time_format)


def process(arguments: argparse.Namespace):
    with open(arguments.filename1) as f1, open(arguments.filename2) as f2:
        csv1 = csv.reader(f1, delimiter=arguments.delimiter)
        csv2 = csv.reader(f2, delimiter=arguments.delimiter)
        t1 = first_non_null_value(csv1, arguments.time1-1, arguments.column1-1, arguments.format)
        t2 = first_non_null_value(csv2, arguments.time2-1, arguments.column2-1, arguments.format)

    delta = datetime.fromtimestamp(mktime(t1)) - datetime.fromtimestamp(mktime(t2))

    with open(arguments.filename2) as f2bis,\
         open(join(dirname(arguments.filename2), f'new-{basename(arguments.filename2)}'), 'w') as f2new:
        csv_writer = csv.writer(f2new, delimiter=arguments.delimiter)
        csv2 = csv.reader(f2bis, delimiter=arguments.delimiter)
        for csv_line in csv2:
            time_value = strptime(csv_line[arguments.time1-1], arguments.format)
            shifted_value = datetime.fromtimestamp(mktime(time_value)) + delta
            time_str = shifted_value.strftime(arguments.format)
            csv_writer.writerow([time_str] + csv_line[1:])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Align time series based on first non 0 values. '
                                                 'The second file will be copied with "new-" prefix '
                                                 'and time values aligned with the first CSV file')
    parser.add_argument('filename1', help='first CSV file')
    parser.add_argument('filename2', help='second CSV file')
    parser.add_argument('-t1', '--time1', default=1, type=int, help='number of the column in file 1 for the time')
    parser.add_argument('-t2', '--time2', default=1, type=int, help='number of the column in file 2 for the time')
    parser.add_argument('-c1', '--column1', default=2, type=int, help='number of the column in file 1 for the data')
    parser.add_argument('-c2', '--column2', default=2, type=int, help='number of the column in file 2 for the data')
    parser.add_argument('-f', '--format', default='%H:%M:%S', type=str, help='format of the time series')
    parser.add_argument('-d', '--delimiter', default=' ', type=str, help='CSV column delimiter')

    args = parser.parse_args()
    process(args)