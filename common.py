
class MiddleData:
    def __init__(self, *args):
        arg_count = len(args)
        self.df = args[0]
        self.file_name = ''
        if arg_count > 1:
            self.file_name = args[1]

class Operator:
    def __init__(self, in_df, in_args, callable_core):
        self.in_df = in_df
        self.in_args = in_args
        self.callable_core = callable_core
        self.out_df = None

    def __call__(self):
        self.out_df = self.callable_core(self.in_df, self.in_args)
        return self.out_df

if __name__ == '__main__':
    md = MiddleData('abc','llllll')
    print(md.df)