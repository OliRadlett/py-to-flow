class Parser:

    KEYWORD = ("if", "else", "elif", "while", "for", "def")
    source = []

    def load_source(self, path):

        lines = []

        with open(path) as file:

            for line in file:

                if not line == "\n" and not line.lstrip().startswith("#"):

                    lines.append(line.strip("\n"))

        self.source = lines

    def indent_level(self, line):

        length_full = len(line)
        length_no_white = len(line.lstrip())
        white = length_full - length_no_white
        white = white / 4
        return white


    def parse_conditional(self, data, line_number, indent):

        block = [data[line_number].lstrip()]

        for i in range(line_number, len(data)):

            line = data[i]
            curr_indent = self.indent_level(line)

            if curr_indent == indent + 1:

                line = line.lstrip()

                if not line.startswith(self.KEYWORD):

                    block.append(line)

                else:

                    break
            else:

                if not i == line_number:

                    break

        return block

    def parse(self):

        parsed_data = []
        blocked = []

        for i in range(0, len(self.source)):

            if i not in blocked:

                if self.source[i].lstrip().startswith(self.KEYWORD):

                    indent = self.indent_level(self.source[i])
                    block = self.parse_conditional(self.source, i, indent)
                    parsed_data.append(block)

                    for x in range(i + 1, i + len(block)):
                        blocked.append(x)

                else:

                    parsed_data.append(self.source[i].lstrip())

        return parsed_data
