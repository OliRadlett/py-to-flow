import argparse
from _parser import Parser
from graph import Graph

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("source", help="the python file you want to create a flowchart for")
args = arg_parser.parse_args()
source_path = args.source

parser = Parser()
parser.load_source(source_path)
parsed_source = parser.parse()

graph = Graph(parsed_source)