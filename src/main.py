import os
import re
# Resolve the problem!!


def run():
    # Start coding here
    with open(os.getcwd() + '/src/encoded.txt', 'r', encoding='utf-8') as f:
        read_data = f.read()
        f.close()
    text = re.split("[^a-zA-Z]*", read_data)
    print(''.join(text))


if __name__ == '__main__':
    run()
