test:
	./ess.foma && dot -Tpdf ess.dot > ess.pdf && sort --ignore-case yupik.pairs > yupik.pairs.tsv && diff yupik.pairs.tsv yupik.pairs.gold.tsv
