import sys
from python.cli import cli

def main(argv):
    parser = cli.create_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
