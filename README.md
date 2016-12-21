## sandbook

This is a Jupyter Notebook to visualize and analyze system architecture as a network.

See a presentation from [Windy City GraphDB](https://github.com/bobbyno/windy-city-graphdb-9-22-16/blob/master/windy_city_graphdb_presentation.ipynb) for a more detailed introduction to the concept.

The Notebooks leverage [Cytoscape's RESTful API](http://apps.cytoscape.org/apps/cyrest) and [python-igraph](http://igraph.org/python/).


## Getting Started

[Install Cytoscape](http://cytoscape.org/)

Start it up and close the welcome screen. You probably want to check "Don't show again" in the lower left.

Start Jupyter in the `sandbook` directory:

```bash
git clone git@github.com:bobbyno/sandbook.git
cd sandbook
pip install -r requirements.txt
jupyter notebook
```

Use the [Iteration Workflow](./iteration_workflow.ipynb) to build a visualization that can be easily updated as new vertices and edges are added over time.

The project contains an example using data from [lein-topology](https://github.com/testedminds/lein-topology). Produce an edgelist of dependencies in the same format to use these notebooks for your own analysis.
