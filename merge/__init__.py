import logging

import command_handler

from merge import csv_to_xlsx
from merge import multi_csv_to_single_csv
from merge import multi_csv_to_single_xlsx

sub_command_map = {
    'multi-csv2xlsx' : multi_csv_to_single_xlsx.handler,
    'csv2csv' : multi_csv_to_single_csv.handler,
    'csv2xlsx' : csv_to_xlsx.handler
}

handle = command_handler.CommandHandler(sub_command_map)