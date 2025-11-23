import argparse

def hello(name="World"):
    return "Hello %s!" % name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    print(hello(args.name))
