import anytree
import anytree.exporter

class Parser:

    # maybe change output from list to tree

    KEYWORD = ("if", "else", "elif", "while", "for", "def")
    source = []
    tree = None
    last_node = None

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
        parent = anytree.Node(data[line_number].lstrip(), parent=self.last_node)
        self.last_node = parent
        reset = True

        for i in range(line_number, len(data)):

            line = data[i]
            curr_indent = self.indent_level(line)

            if curr_indent == indent + 1:

                line = line.lstrip()

                if not line.startswith(self.KEYWORD):

                    block.append(line)
                    anytree.Node(data[i].lstrip(), parent=parent)

                else:

                    reset = False
            else:

                if not i == line_number:

                    if self.indent_level(data[i + 1]) < curr_indent:

                        # agghhhh
                        # might need to make the parser again

                    break

        return block, reset

    def parse(self):

        parsed_data = []
        blocked = []

        for i in range(0, len(self.source)):

            if i not in blocked:

                if self.source[i].lstrip().startswith(self.KEYWORD):

                    # CONDITIONAL

                    original_node = self.last_node
                    indent = self.indent_level(self.source[i])
                    block, reset = self.parse_conditional(self.source, i, indent)
                    parsed_data.append(block)

                    if reset:
                        self.last_node = original_node

                    # parent = None
                    #
                    # for ii in range(0, len(block)):
                    #
                    #     line = block[ii]
                    #
                    #     if not ii == len(block) - 1:
                    #
                    #         # breaking because multidimensional array
                    #
                    #         parent = anytree.Node(self.source[i].lstrip(), parent=self.last_node)
                    #
                    #     else:
                    #
                    #         anytree.Node(self.source[i].lstrip(), parent=parent)

                    for x in range(i + 1, i + len(block)):
                        blocked.append(x)

                else:

                    # LINEAR

                    parsed_data.append(self.source[i].lstrip())

                    if i == 0:

                        self.tree = anytree.Node(self.source[i].lstrip())
                        self.last_node = self.tree

                    else:

                        self.last_node = anytree.Node(self.source[i].lstrip(), parent=self.last_node)

        for pre, fill, node in anytree.RenderTree(self.tree):

            print("%s%s" % (pre, node.name))

        anytree.exporter.DotExporter(self.tree).to_picture("tree.png")

        return parsed_data
