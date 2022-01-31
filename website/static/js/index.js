const svgWidth = 1400, svgHeight = 500;

const svg = d3.select('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight);

const lineChart = data => {

    const grouped_data = d3.group(data, d => d.city_id);
    const xAxisLabel = 'Time';
    const yAxisLabel = 'Temperature (\xB0C)';

    const margin = {top: 40, right: 220, bottom: 90, left: 365};
    const innerWidth = svgWidth - margin.left - margin.right;
    const innerHeight = svgHeight - margin.top - margin.bottom;

    const colours = d3.scaleOrdinal()
        .range(['#001886', '#A10303', '#2AD304']);

    const xScale = d3.scaleTime()
        .domain(d3.extent(data, function(d) { return d.datetime; }))
        .range([0, innerWidth])
        .nice();

    console.log(d3.min(data, function(d) { return d.temperature; }));
    console.log(d3.max(data, function(d) { return d.temperature; }));
    console.log(d3.min(data, function(d) { return d.datetime; }));
    console.log(d3.max(data, function(d) { return d.datetime; }));

    const yScale = d3.scaleLinear()
        .domain(d3.extent(data, function(d) { return d.temperature; }))
        .range([innerHeight, 0])
        .nice();

    const g = svg.append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

    const xAxis = d3.axisBottom(xScale)
        .tickSize(-innerHeight)
        .tickPadding(15);

    const yAxis = d3.axisLeft(yScale)
        .tickSize(-innerWidth)
        .tickPadding(10);

    const yAxisG = g.append('g').call(yAxis);
    yAxisG.selectAll('.domain').remove();

    yAxisG.append('text')
        .attr('class', 'axis-label')
        .attr('y', -60)
        .attr('x', -innerHeight / 2)
        .attr('fill', 'black')
        .attr('transform', 'rotate(-90)')
        .attr('text-anchor', 'middle')
        .text(yAxisLabel);

    const xAxisG = g.append('g').call(xAxis)
        .attr('transform', 'translate(0,' + innerHeight + ')');

    xAxisG.select('.domain').remove();

    xAxisG.append('text')
        .attr('class', 'axis-label')
        .attr('y', 50)
        .attr('x', innerWidth / 2)
        .attr('fill', 'black')
        .text(xAxisLabel);

    g.selectAll('.line')
        .data(grouped_data)
        .enter()
        .append('path')
        .attr('fill', 'none')
        .attr('stroke', function(d) { return colours(d[0]); })
        .attr('stroke-width', 4)
        .attr('d', function(d){
            return d3.line()
                .x(function(d) { return xScale(d.datetime); })
                .y(function(d) { return yScale(d.temperature); })
                (d[1])
        });

    const legend_labels = d3.scaleOrdinal()
        .range(['Tallinn, Estonia', 'Riga, Latvia', 'Vilnius, Lithuania'])

    const legend = d3.select('svg')
        .selectAll('g.legend')
        .data(grouped_data)
        .enter()
        .append('g')
        .attr('class', 'legend');

    legend.append('circle')
        .attr('cx', 1240)
        .attr('cy', (d, i) => i * 30 + 50)
        .attr('r', 6)
        .style('fill', function(d) { return colours(d[0]); });

    legend.append('text')
        .attr('x', 1260)
        .attr('y', (d, i) => i * 30 + 55)
        .text(function(d) { return legend_labels(d[0]); });
};