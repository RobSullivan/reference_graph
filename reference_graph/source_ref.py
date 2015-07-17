# -*- coding: utf-8 -*-

from collections import Counter, namedtuple

from pymongo import MongoClient

def db_conn():
	
	try:
	    client = MongoClient('localhost', 27017)
	    db = client.test
	    return db['articlemodels']	
	except Exception as err:
		print(err)

def load_seed_reference_data(doi):

		articles_helper = db_conn()
		seed_refs = articles_helper.find({'doi':doi}, \
		{'references': 1, 'title':1}) #returns a pymongo cursor
		return seed_refs	
	


class AncestorRef:

	"""
	Accepts a list of references
	Retrieves the references for a list of references
	Does some list processing and then instantiates a Counter class
	https://docs.python.org/3.4/library/collections.html#collections.Counter

	params: seed_doi - doi of seed article
			seed_reference_list - the references of the seed_doi article
			in this example the seed_reference_list will be MongoDB's ObjectIds

	"""
	
	def __init__(self, seed_doi, seed_reference_list, db_conn, top=None):
		self.seed_doi = seed_doi
		self.seed_refs = seed_reference_list 
		self.db_conn = db_conn()
		self.ancestor_refs = self.load_ancestor_refs()
		self.counter = Counter


	def load_ancestor_refs(self):
		"""procedure...does stuff"""
		ancestor_refs = self.db_conn.find({'_id':{'$in': self.seed_refs}},\
		 					{'references':1})
		ancestor_refs = [i for i in ancestor_refs]

		return ancestor_refs # the results as a list of dictionaries

	
	def flatten(self, ancestor_refs):
		"""procedure...does stuff"""
		super_long_list = [i['references'] for i in ancestor_refs]#get the reference lists out
		super_long_list = [i for i in super_long_list for i in i]# flattens lists of lists
		return super_long_list

	def ancestors_counter(self, single_list):
		"""return a value"""
		return self.counter(single_list)

	def seed_ref_match_common_ans(self, ancestor_references_list, top_common_ancestors):
		"""create and return a data structure that gives you the top n most_common, 
		the frequency and a list of the references that cite the most_common.

		params: ancestor_references_list
				top_common_ancestors
		"""
		
		results = {'doi': seed_doi, 'super_ancestors':[]}

		for top in top_common_ancestors:
			index = 0
			citing_seed_refs = []
			TopCommonAncestor = namedtuple('TopCommonAncestor', ['id', 'frequency', 'citing_references'])
			for seed_reference in ancestor_references_list:
				if top[index] in seed_reference['references']:
					citing_seed_refs.append(seed_reference['_id'])		
			index += 1
			top_namedtuple = TopCommonAncestor(top[0], top[1], citing_seed_refs)
			results['super_ancestors'].append(top_namedtuple)

		return results
		


if __name__ == "__main__":
	#prep
	seed_doi = "10.1038/nature11543"
	seed_article = load_seed_reference_data(seed_doi)
	seed_reference_list = [i['references'] for i in seed_article][0]
	#init class
	ancestor_references = AncestorRef(seed_doi, seed_reference_list, db_conn)
	#get the list of ancestor references
	seed_ancestor_references_list = ancestor_references.ancestor_refs
	#flatten the list
	all_the_refs = ancestor_references.flatten(seed_ancestor_references_list)
	print("Total number of ancestor references: ", len(all_the_refs))
	
	#init a counter
	common_ancestor = ancestor_references.ancestors_counter(all_the_refs)

	top_common_ancestors = common_ancestor.most_common(5)

	results = ancestor_references.seed_ref_match_common_ans(seed_ancestor_references_list, top_common_ancestors)
	
	for i in results['super_ancestors']:
		print(i)

	#now hand off results to a database to populate title, pmid, doi fields


