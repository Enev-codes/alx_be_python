import sys

def main():
    """Show split array of argv values"""
    sys_args = sys.argv
    command, *params = sys_args[1].split(':')
    print(params)


if __name__ == '__main__':
    main()
