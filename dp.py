import importlib
import sys

def run():
    argc = len(sys.argv)
    if argc < 3:
        print('Usage: dp <operation> <sub-command> <options>')
        return
    
    operation = sys.argv[1]
    pkg = importlib.import_module(operation)
    pkg.handle(sys.argv[2:])
    print("Done!")