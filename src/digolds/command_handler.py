import logging
import importlib
import os
import glob

class CommandHandler:
    def __init__(self, sub_command):
        self.sub_command = sub_command

    def __call__(self, args):
        sub_command = args[0]
        sub_command_map = self.sub_command
        if sub_command in sub_command_map:
            handler = sub_command_map[sub_command]
            handler(args[1])
        else:
            logging.warning(f'sub command {sub_command} is not found')

def create_handler(folder):
    folder_name = os.path.basename(folder)
    package_name = os.path.basename(os.path.dirname(folder))
    files = [f for f in glob.glob(os.path.join(folder, '*.py'))]
    sub_command_map = {}
    for f in files:
        f = os.path.basename(f)
        if f == '__init__.py':
            continue
        f_without_extension = os.path.splitext(f)[0]
        m = importlib.import_module(f'{package_name}.{folder_name}.{f_without_extension}')
        sub_command_map[getattr(m, 'name')] = getattr(m, 'handler')
    
    return CommandHandler(sub_command_map)