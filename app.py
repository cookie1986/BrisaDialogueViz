import json
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plth

# load json file containing dialogue data
with open('data/test_dialogue.vf') as f:
    data = json.load(f)


def parse_diagrams(json_string):
    for diagram_id, diagram in data["diagrams"].items():
        print(f'Diagram ID: {diagram_id}, Name: {diagram["name"]}')
        # for node_id, node in diagram["nodes"].items():
        #     print(f'  Node ID: {node_id}, Type: {node["type"]}')
        #     if 'data' in node:
        #         print(f'    Data: {node["data"]}')

parse_diagrams(data)