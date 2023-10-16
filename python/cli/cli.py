import argparse
from python.cmd.clean import clean

def create_parser():
    parser = create_root_parser()
    subparsers = parser.add_subparsers()
    add_clean_parser(subparsers)
    return parser

def create_root_parser():
    description = "Project commands"
    prog='main.py'
    root_parser = argparse.ArgumentParser(prog=prog, description=description)
    return root_parser

def add_clean_parser(subparsers):
    clean_name = "clean"
    clean_help = "Removes generated files and folders"
    clean_parser = subparsers.add_parser(clean_name, description=clean_help, help=clean_help)
    clean_parser.set_defaults(func=clean)