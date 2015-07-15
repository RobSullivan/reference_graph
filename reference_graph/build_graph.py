from itertools import zip_longest

from source_ref import load_seed_reference_data

import networkx as nx

seed_doi = "10.1038/nature11543"

edges = []

G = nx.DiGraph()

seed = load_seed_reference_data(seed_doi)

seed_node = seed.next()

for i in zip_longest(seed_node['references'], [seed_node['_id']],\
		fillvalue=seed_node['_id']):
	edges.append(i)

G.add_edges_from(edges)

print("predecessors: ",G.predecessors(seed_node['_id']))

