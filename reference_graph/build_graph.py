from bson import json_util
from itertools import zip_longest
import json

from source_ref import *

import networkx as nx
from networkx.readwrite import json_graph
import pylab

"""
use ipython 

I need to know titles and pmids of all articles at the very least.



"""


seed_doi = "10.1038/nature11543"

seed_edges = []
ancestor_edges = []

MDG = nx.MultiDiGraph()

seed = load_seed_reference_data(seed_doi)

seed_node = seed.next()

seed_reference_list = [i for i in seed_node['references']]

for i in zip_longest(seed_node['references'], [seed_node['_id']],\
		fillvalue=seed_node['_id']):
	seed_edges.append(i)

MDG.add_edges_from(seed_edges)

#print("predecessors: ",MDG.predecessors(seed_node['_id']))

"""

same process with seed_ancestor_references_list


"""

ancestor_references = AncestorRef(seed_doi, seed_reference_list, db_conn)

seed_ancestor_references_list = ancestor_references.ancestor_refs

for ref in seed_ancestor_references_list:
	for i in zip_longest(ref['references'], [ref['_id']],\
		fillvalue=ref['_id']):
	    ancestor_edges.append(i)


MDG.add_edges_from(ancestor_edges)

#nx.draw(MDG, pos=nx.spring_layout(MDG)) # a mess

"""
Find out degrees
Out degrees represent edges going out and represent "cited_by"
In edges represent "cites" relationship

"""

out_degrees = MDG.out_degrees()

highest_out_degrees = sorted(out_degrees.values(), reverse=True)

highest_out_degrees[:5]


"""
Find all_shorteset paths from source to target
source is one of highest_out_degree nodes
target is seed_node

Look up keys that have a value

store shortest paths in a list 

"""
shortest_paths = []

for key, value in out_degrees.items():
	if value in highest_out_degrees[:5]:
		shortest_paths.append(nx.all_shortest_paths(MDG, source=key, target=seed_node['_id']))
		

"""
Create subgraph from shortest_paths 
Create json for d3
Use as starting point for users as graph is less clutered 
and present useful information from the outset.
If the user wants to 'see all' then chuck up full graph


What data to add to nodes? 
http://networkx.github.io/documentation/latest/reference/generated/networkx.readwrite.json_graph.node_link_data.html?highlight=node_link_data#networkx.readwrite.json_graph.node_link_data


"""
subgraph_edges = []

for i in shortest_paths:
	subgraph_edges.append([p for p in i])

flattened_subgraph_nodes = nx.utils.misc.flatten(subgraph_edges)
common_references_subgraph = MDG.subgraph(flattened_subgraph_nodes)

subgraph_data = json_graph.node_link_data(common_references_subgraph)

with open('subgraph_data.json', 'w') as f:
	json.dump(subgraph_data, f, indent=4, default=json_util.default)


"""
Output graph to json for d3.js

"""



data = json_graph.node_link_data(MDG)

with open('another_data.json', 'w') as f:
	json.dump(data, f, indent=4, default=json_util.default)



