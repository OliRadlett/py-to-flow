import os


KEYWORD = ("if", "else", "elif", "while", "for", "def")


def load_source(path):

    lines = []

    with open(path) as file:

        for line in file:

            if not line == "\n" and not line.lstrip().startswith("#"):

                lines.append(line.strip("\n"))

    return lines


def indent_level(line):

    length_full = len(line)
    length_no_white = len(line.lstrip())
    white = length_full - length_no_white
    white = white / 4
    return white


def parse_conditional(data, line_number, indent):

    block = [data[line_number].lstrip()]

    for i in range(line_number, len(data)):

        line = data[i]
        curr_indent = indent_level(line)

        if curr_indent == indent + 1:

            line = line.lstrip()

            if not line.startswith(KEYWORD):

                block.append(line)

            else:

                break
        else:

            if not i == line_number:

                break

    return block


def parse(data):

    parsed_data = []
    blocked = []

    for i in range(0, len(data)):

        if i not in blocked:

            if data[i].lstrip().startswith(KEYWORD):

                indent = indent_level(data[i])
                block = parse_conditional(data, i, indent)
                parsed_data.append(block)

                for x in range(i + 1, i + len(block)):
                    blocked.append(x)

            else:

                parsed_data.append(data[i].lstrip())

    return parsed_data


source_path = os.getcwd() + "/demo.py"
source = load_source(source_path)

parsed_source = parse(source)

print(parsed_source)
