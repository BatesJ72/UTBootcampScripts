console.log("Hello")

let svg = d3.select("svg")
    .attr("width", 700)
    .attr("height", 700)

svg.append("circle")
    .attr("cx", 300)
    .attr("cy", 300)
    .attr("r", 300)
    .attr("fill", "blue")
    .attr("stroke", "#000000")
    .attr("stroke-width", "10")

svg.append("circle")
    .attr("cx", 300)
    .attr("cy", 300)
    .attr("r", 225)
    .attr("fill", "#000000")
    .attr("stroke", "#000000")
    .attr("stroke-width", "10")

svg.append("circle")
    .attr("cx", 300)
    .attr("cy", 300)
    .attr("r", 150)
    .attr("fill", "blue")
    .attr("stroke", "#000000")
    .attr("stroke-width", "10")

svg.append("circle")
    .attr("cx", 300)
    .attr("cy", 300)
    .attr("r", 75)
    .attr("fill", "#000000")
    .attr("stroke", "#000000")
    .attr("stroke-width", "10")