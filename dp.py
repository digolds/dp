import importlib
import sys
import logging

from common import create_operator

def list_to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def visit_digolds():
    import webbrowser
    url = 'https://www.digolds.cn/article/0016124413347014dd0efcd3edc44cc8e182c864ee8e0ca000'
    webbrowser.open_new_tab(url)

def show_version():
    import pkg_resources
    version = pkg_resources.require('digolds-dp')[0].version
    print(f"""dp(data pipeline) {version}
Visit the site: digolds.cn, if you want to learn more""")

commands_with_2_args = {
    '--version' : show_version,
    '--help' : visit_digolds
}

def run():
    argc = len(sys.argv)

    if argc == 2:
        commands_with_2_args.get(sys.argv[1], show_version)()
        return

    if argc < 3:
        print('Usage: dp <operation> <sub-command> <options>')
        return
    
    operation = sys.argv[1]
    pkg = importlib.import_module(operation)
    combined_args = [sys.argv[2], list_to_dict(sys.argv[3:])]
    pkg.handle(combined_args)
    logging.info('Done!')

if __name__ == "__main__":
    visit_digolds()
    show_version()