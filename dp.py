import importlib
import sys

def list_to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def run():
    argc = len(sys.argv)
    if argc < 3:
        print('Usage: dp <operation> <sub-command> <options>')
        return
    
    operation = sys.argv[1]
    pkg = importlib.import_module(operation)
    combined_args = [sys.argv[2], list_to_dict(sys.argv[3:])]
    pkg.handle(combined_args)
    print("Done!")