## SAND
### Python code and notebooks to model System Architecture as a Network of Dependencies

SAND uses Python and Jupyter Notebooks to explore applications of representing system architecture as a directed graph,
or network, of engineered artifacts and their relationships to one another.

Engineered artifacts are vertices in the graph. For a software library, the artifacts are functions and the dependencies
are function calls. For RESTful microservices, an artifact is a service and the dependencies are API calls.

Directed edges represent the dependencies and their transpose, impact.

Imagine we have two microservices, A and B.

If B calls A, then B has a dependency on A. The creator of A might not know that B is a client, so the dependency relationship
is directed.

The transpose of this relationship is that A impacts or influences B: Non backwards-compatible changes in A's interface that
B calls can break B. Changes in B do not impact A, so once again, the edge is directed.

This simple model proves to be extremely powerful in describing arbitrarily complicated system architectures. The SAND library
and accompanying Jupyter Notebooks provide working examples of visualization and analysis.


## Installing

1. You'll also need a working Jupyter installation running on Python 3.

2. Start Jupyter in the `sandbook` directory:

```bash
git clone git@github.com:testedminds/sand.git
cd sand
pip install -r requirements.txt
cd docs
jupyter notebook
```

3. [Install Cytoscape](http://cytoscape.org/).
Start Cytoscape up and close the welcome screen.
You probably want to check "Don't show again" in the lower left.


## Getting Started

* [Loading Network Data](./docs/Loading%20network%20data.ipynb)
* [Matrix Visualization with Bokeh](./docs/Matrix%20visualization%20with%20Bokeh.ipynb)
* [Network Visualization with Cytoscape](./docs/Visualization%20with%20Cytoscape.ipynb)


## Learn More

See a presentation from Bobby Norton at [Windy City GraphDB][wcgdb] for a more detailed introduction to the concept.

The Notebooks leverage [Cytoscape's RESTful API](http://apps.cytoscape.org/apps/cyrest) and [python-igraph](http://igraph.org/python/).


[wcgdb]: https://github.com/bobbyno/windy-city-graphdb-9-22-16/blob/master/windy_city_graphdb_presentation.ipynb


## License

Copyright © Bobby Norton and [Tested Minds, LLC](http://www.testedminds.com).

Released under the [Apache License, Version 2.0](./LICENSE.txt)
