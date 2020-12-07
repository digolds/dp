import importlib
import sys

def list_to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def run():
    argc = len(sys.argv)

    if argc == 2 and sys.argv[1] == '--version':
        import pkg_resources
        version = pkg_resources.require('digolds-dp')[0].version
        print(f'dp(data pipeline) {version}')
        return

    if argc < 3:
        print('Usage: dp <operation> <sub-command> <options>')
        return
    
    operation = sys.argv[1]
    pkg = importlib.import_module(operation)
    combined_args = [sys.argv[2], list_to_dict(sys.argv[3:])]
    pkg.handle(combined_args)
    print("Done!")