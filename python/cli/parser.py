import argparse
from python.cmd.clean import clean
from python.cmd.build import build
from python.cmd.fetch import fetch

def create_parser():
    parser = create_root_parser()
    subparsers = parser.add_subparsers()
    add_clean_parser(subparsers)
    add_build_parser(subparsers)
    add_fetch_parser(subparsers)
    return parser

def create_root_parser():
    description = "Project commands."
    prog='main.py'
    root_parser = argparse.ArgumentParser(prog=prog, description=description)
    root_parser.set_defaults(func=lambda args: root_parser.print_help())
    return root_parser

def add_clean_parser(subparsers):
    name = "clean"
    help_ = "Removes generated files and folders."
    parser = subparsers.add_parser(name, description=help_, help=help_)
    parser.set_defaults(func=clean)

def add_build_parser(subparsers):
    name = "build"
    help_ = "Builds the project."
    parser = subparsers.add_parser(name, description=help_, help=help_)
    parser.set_defaults(func=build)

def add_fetch_parser(subparsers):
    name = "fetch"
    help_ = "Fetches dependencies."
    parser = subparsers.add_parser(name, description=help_, help=help_)
    parser.set_defaults(func=fetch)
