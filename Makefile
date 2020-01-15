
ss: self_study/data_handling.pdf \
self_study/data_retrieval.pdf \
self_study/machine_learning.pdf

self_study/%.pdf: self_study/%.markdown
	pandoc --pdf-engine=xelatex $< -o $@
