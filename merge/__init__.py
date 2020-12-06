from merge import csv_to_xlsx
from merge import multi_csv_to_single_csv

def handle(args):
    sub_command = args[0]
    if sub_command == 'csv2csv':
        multi_csv_to_single_csv.multiple_csv_to_single_csv(args[1], args[2], args[3])