
-- start with five articles 2-5 are references of 1
INSERT INTO articles VALUES (1, 'A physical, genetic and functional sequence assembly of the barley genome', '10.1038/nature11543', 23075845, NULL, 1;
INSERT INTO articles VALUES (2, 'An improved method to identify BAC clones using pooled overgos', '10.1093/nar/gkl920', 17151072, 'PMC1761434', 2);
INSERT INTO articles VALUES (3, 'Development of high-density genetic maps for barley and wheat using a novel two-enzyme genotyping-by-sequencing approach', '10.1371/journal.pone.0032253', 22389690, 'PMC3289635', 3);
INSERT INTO articles VALUES (4, 'Unlocking the barley genome by chromosomal and comparative genomics', '10.1105/tpc.110.082537', 21467582, 'PMC3101540', 4);
INSERT INTO articles VALUES (5, 'TEnest: automated chronological annotation and visualization of nested plant transposable elements', '10.1104/pp.107.110353', 18032588, 'PMC2230558', 5);

-- insert into article_refs table
INSERT INTO article_refs VALUES (1,2);
INSERT INTO article_refs VALUES (1,2);
INSERT INTO article_refs VALUES (1,3);
INSERT INTO article_refs VALUES (1,4);
INSERT INTO article_refs VALUES (1,5);

--gkl920
INSERT INTO articles VALUES (6, 'Uprobe: a genome-wide universal probe resource for comparative physical mapping in vertebrates.', '10.1101/gr.3066805', 15590945, 'PMC540286', 6);
INSERT INTO articles VALUES (7, 'Gene enrichment in maize with hypomethylated partial restriction (HMPR) libraries.', '10.1101/gr.3362105', 16204197, 'PMC1240087', 7);
INSERT INTO articles VALUES (8, 'OligoSpawn: a software tool for the design of overgo probes from large unigene datasets.', '10.1186/1471-2105-7-7', 16401345, 'PMC1361790', 8);
INSERT INTO articles VALUES (9, 'Anchoring 9,371 maize expressed sequence tagged unigenes to the bacterial artificial chromosome contig map by two-dimensional overgo hybridization.', '10.1104/pp.103.034538', 15020742, 'PMC419808', 9);
INSERT INTO articles VALUES (10, 'Comparative physical mapping links conservation of microsynteny to chromosome structure and recombination in grasses.', '10.1073/pnas.0502365102', 16141333, 'PMC1201573', 10);

INSERT INTO article_refs VALUES (2,6);
INSERT INTO article_refs VALUES (2,7);
INSERT INTO article_refs VALUES (2,8);
INSERT INTO article_refs VALUES (2,9);
INSERT INTO article_refs VALUES (2,10);


CREATE TABLE articles(article_id INTEGER NOT NULL,
title TEXT,
doi TEXT,
pmid INTEGER,
pmcid TEXT NULL,
article_ref_id INTEGER NOT NULL,
PRIMARY KEY (article_id, article_ref_id));

CREATE TABLE article_refs(
article_ref_id INTEGER NOT NULL REFERENCES articles,
article_id INTEGER NOT NULL REFERENCES articles,
PRIMARY KEY (article_ref_id, article_id)
);

-- find an article and its references

SELECT article.title, article_ref.article_id, reference_title.title FROM articles AS article 
JOIN article_refs AS article_ref on article.article_ref_id = article_ref.article_ref_id  
JOIN articles AS reference_title
ON reference_title.article_id = article_ref.article_id 
WHERE article.article_ref_id = 2;

