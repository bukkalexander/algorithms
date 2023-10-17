#!/usr/bin/env python
import sys
from python.cli import parser

def main(argv):
    pars = parser.create_parser()
    args = pars.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
