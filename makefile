slides:
	jupyter nbconvert *.ipynb --to slides --post serve

dsm-example:
	./edgelist_to_dsm \
		./data/lein-topology-57af741.csv \
		"lein-topology 57af741" \
		"Each row shows a function's dependencies. Each column shows callers impacted by the function. Color depicts group membership. Darker cells indicate a larger number of interactions. Foo!" \
		800 \
		"`pwd`/figure" > /tmp/$@

open-dsm-example: dsm-example
	cd `cat /tmp/dsm-example` && \
	open http://localhost:8000 && \
	python -m http.server
