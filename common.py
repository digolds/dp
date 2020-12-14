
class MiddleData:
    def __init__(self, *args):
        arg_count = len(args)
        self.df = args[0]
        self.file_name = ''
        if arg_count > 1:
            self.file_name = args[1]

if __name__ == '__main__':
    md = MiddleData('abc','llllll')
    print(md.df)