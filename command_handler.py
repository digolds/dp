import logging

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