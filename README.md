## sandbook
### Notebooks for System Architecture as Network Data

This work uses Jupyter Notebooks to explore applications of representing system architecture as a network of engineered
artifacts and their interactions. For a software library, the artifacts are functions and the interactions are function
calls. For RESTful microservices, an artifact is a service and the interactions are API calls.

Since A calls or sends a message to B, A has a dependency on B. Anthropomorphizing helps build some intuition for this:
A knows about B and sent a message for some reason, whereas B might not know anything about A. Transitively, the
designer of A needs to understand the work of the designer of B, but the designer of B need not understand A assuming
the interface for B already exists.

The transpose of this relation is that B impacts or influences A: Non backwards-compatible changes in the interface of B
will break A. Changes in the semantics of B will change the behavior of A unless the relationship is redundant.


## Installing

1. [Install Cytoscape](http://cytoscape.org/).
Start Cytoscape up and close the welcome screen.
You probably want to check "Don't show again" in the lower left.

1. You'll also need a working Jupyter installation running on Python 3.

1. Start Jupyter in the `sandbook` directory:

```bash
git clone git@github.com:bobbyno/sandbook.git
cd sandbook
pip install -r requirements.txt
jupyter notebook
```

## Getting Started

Use the [Iteration Workflow](./iteration_workflow.ipynb) to build a visualization that can be easily updated as new vertices and edges are added over time.

The project contains an example using data from [lein-topology](https://github.com/testedminds/lein-topology).
Produce dependency data in the same format to use these notebooks for your own analysis.


## Learn More

See a presentation from Bobby Norton at [Windy City GraphDB][wcgdb] for a more detailed introduction to the concept.

The Notebooks leverage [Cytoscape's RESTful API](http://apps.cytoscape.org/apps/cyrest) and [python-igraph](http://igraph.org/python/).


[wcgdb]: https://github.com/bobbyno/windy-city-graphdb-9-22-16/blob/master/windy_city_graphdb_presentation.ipynb
