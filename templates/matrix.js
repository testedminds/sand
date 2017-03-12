function matrix(json_file) {
  d3.json(json_file, function(network) {
    d3.select("#title").text(network.title);
    d3.select("#generatedDate").text("Generated " + network.date);

    var scale = network.scale;
    var svg = createSvg(scale, scale);

    var nodes = network.nodes;
    var edges = network.edges;
    var matrix = initializeMatrix(nodes);
    edgesToMatrix(nodes, edges, matrix);
    var sortOrder = setSortOrder(svg, nodes, scale);
    addRows(svg, matrix, sortOrder, nodes, scale);
    addColumns(svg, matrix, sortOrder, nodes, scale);
  });
};

function edgesToMatrix(nodes, edges, matrix) {
  edges.forEach(function(edge) {
    matrix[edge.source][edge.target].z = edge.weight + maxWeight - 1;
    matrix[edge.source][edge.source].z = 1;
    matrix[edge.target][edge.target].z = 1;
  });
};

function initializeMatrix(nodes) {
  var matrix = [];

  // Compute index per node.
  nodes.forEach(function(node) {
    matrix[node.id] = d3.range(nodes.length).map(function(j) { return {x: j, y: node.id, z: 0}; });
  });
  return matrix;
};

function setSortOrder(svg, nodes, width) {
  // https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#ordinal_rangeBands
  var sortOrder = d3.scale.ordinal().rangeBands([0, width]);
  var orders = precomputeOrders(nodes);

  // The default sort order.
  sortOrder.domain(orders.group);

  d3.select("#order").on("change", function() {
    sortOrder.domain(orders[this.value]);
    order(this.value, sortOrder, svg);
  });

  return sortOrder;
};

function precomputeOrders(nodes) {
    return {
      name:      d3.range(nodes.length).sort(function(a, b) { return d3.ascending(nodes[a].name, nodes[b].name); }),
      indegree:  d3.range(nodes.length).sort(function(a, b) { return nodes[b].indegree - nodes[a].indegree; }),
      outdegree: d3.range(nodes.length).sort(function(a, b) { return nodes[b].outdegree - nodes[a].outdegree; }),
      group:     d3.range(nodes.length).sort(function(a, b) { return nodes[b].group - nodes[a].group; })
    };
};

function addRows(svg, matrix, sortOrder, nodes, width) {
  var row = svg.selectAll(".row")
        .data(matrix)
        .enter().append("g")
        .attr("class", "row")
        .attr("transform", function(d, i) { return "translate(0," + sortOrder(i) + ")"; })
        .each(function(r) {
          var cell = d3.select(this);
          buildRow(cell, r, sortOrder, nodes)
        });

  row.append("line")
    .attr("x2", width);

  row.append("text")
    .attr("x", -6)
    .attr("y", sortOrder.rangeBand() * 0.5)
    .attr("dy", ".32em")
    .attr("text-anchor", "end")
    .text(function(d, i) { return nodes[i].name; });
};

function buildRow(cell, r, sortOrder, nodes) {
  cell.selectAll(".cell")
    .data(r.filter(function(d) { return d.z; }))
    .enter().append("rect")
    .attr("class", "cell")
    .attr("x", function(d) { return sortOrder(d.x); })
    .attr("width", sortOrder.rangeBand())
    .attr("height", sortOrder.rangeBand())
    .style("fill-opacity", function(d) { return opacity(d.z); })
    .style("fill", function(d) { return nodes[d.x].group == nodes[d.y].group ? colors(nodes[d.x].group) : null; })
    .on("mouseover", mouseover)
    .on("mouseout", mouseout);
};

function addColumns(svg, matrix, sortOrder, nodes, width) {
  var column = svg.selectAll(".column")
        .data(matrix)
        .enter().append("g")
        .attr("class", "column")
        .attr("transform", function(d, i) { return "translate(" + sortOrder(i) + ")rotate(-90)"; });

  column.append("line")
    .attr("x1", -width);

  column.append("text")
    .attr("x", 6)
    .attr("y", sortOrder.rangeBand() / 2)
    .attr("dy", ".32em")
    .attr("text-anchor", "start")
    .text(function(d, i) { return nodes[i].name; });
};

function mouseover(cell) {
  d3.selectAll(".row text").classed("active", function(d, i) { return i == cell.y; });
  d3.selectAll(".column text").classed("active", function(d, i) { return i == cell.x; });
};

function mouseout() {
  d3.selectAll("text").classed("active", false);
};

function createSvg(width, height) {
  var margin = {top: 300, right: 0, bottom: 10, left: 300};

  var svg = d3.select("#matrix")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg.append("rect")
    .attr("class", "background")
    .attr("width", width)
    .attr("height", height);

  return svg;
};

function order(value, sortOrder, svg) {
  var delay = 1.5
  var t = svg.transition().duration(500);

  t.selectAll(".row")
    .delay(function(d, i) { return sortOrder(i) * delay; })
    .attr("transform", function(d, i) { return "translate(0," + sortOrder(i) + ")"; })
    .selectAll(".cell")
    .delay(function(d) { return sortOrder(d.x) * delay; })
    .attr("x", function(d) { return sortOrder(d.x); });

  t.selectAll(".column")
    .delay(function(d, i) { return sortOrder(i) * delay; })
    .attr("transform", function(d, i) { return "translate(" + sortOrder(i) + ")rotate(-90)"; });
};

// TODO: Assumes a set maximum edge weight, which might not be valid.
var maxWeight = 5;

// Create a new ordinal scale with a range of ten categorical colors:
// https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category10
var colors = d3.scale.category10().domain(d3.range(10));

// https://github.com/d3/d3-3.x-api-reference/blob/master/Quantitative-Scales.md#linear_domain
var opacity = d3.scale.linear().domain([0, maxWeight]).clamp(true);
