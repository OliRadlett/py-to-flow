import pydotplus


class Graph:

    graph_data = []
    node_index = 0
    source = []

    def __init__(self, parsed_source):

        self.source = parsed_source

        self.graph_data.append("digraph {\n")
        self.graph_data.append("Start [shape=rectangle, color=orange, fontcolor=navy];\n")
        self.generate_nodes(parsed_source)
        self.generate_node_links(parsed_source, parent=0)

        self.graph_data.append("}")

        #self.graph_file = open("graph.dot", "w+")

        for x in self.graph_data:

            print(x)
            #self.graph_file.write(x)

        #self.graph_file.close()

        graph = pydotplus.graph_from_dot_file('graph.dot')
        graph.write_png("graph.png")

    def generate_nodes(self, parsed_source):

        for i in range(0, len(parsed_source)):

            line = parsed_source[i]

            if isinstance(line, str):

                line = line.replace('"', "'")
                self.graph_data.append(str(self.node_index) + ' [label="' + line + '" shape=rectangle color=blue];\n')
                self.node_index += 1

            elif isinstance(line, list):

                self.generate_nodes(line)

    def generate_node_links(self, parsed_source, parent=None):

        for i in range(0, len(parsed_source)):

            line = parsed_source[i]

            if isinstance(line, str):

                if i == 0 and not parent:

                    self.graph_data.append("Start -> 0;\n")

                else:

                    self.graph_data.append(str(parent - 1) + " -> " + str(i + parent) + ";\n")
                    #print(line)
                    #print(parent + i)

            else:

                #self.generate_node_links(line, parent=self.source.index(line))
                self.generate_node_links(line, parent=0)
                #print(line)
                #print(self.source.index(line))
                #print("INDEX: " + str(self.calculate_node_index(line, parsed_source)))
