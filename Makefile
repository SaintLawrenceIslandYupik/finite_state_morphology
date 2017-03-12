test: yupik.pairs.tsv yupik.pairs.gold.tsv
	diff yupik.pairs.tsv yupik.pairs.gold.tsv

yupik.pairs ess.dot: ess.foma
	./ess.foma

yupik.pairs.tsv: yupik.pairs
	sort --ignore-case yupik.pairs > yupik.pairs.tsv	

ess.pdf: ess.dot
	dot -Tpdf ess.dot > ess.pdf

clean:
	rm -f ess.dot ess.pdf yupik.pairs yupik.pairs.tsv
