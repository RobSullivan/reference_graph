from itertools import zip_longest

from source_ref import *

import networkx as nx
import pylab

"""
use ipython --matplotlib

and import pylab

HOWTO: http://matplotlib.org/faq/installing_faq.html#windows-installer

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

nx.draw(MDG, pos=nx.spring_layout(MDG)) # a mess

