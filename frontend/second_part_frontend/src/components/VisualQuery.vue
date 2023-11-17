<template>
    <!-- Main container for the component -->
    <div id="VisualQuery">
        <!-- Main content of the component -->
        <main>
            <div id="chart"></div>
        </main>
    </div>
</template>

<script>
// Importing the D3 library
import * as d3 from 'd3'

export default {
    // Defining the props that the component accepts
    props: ['data'],
    // When the component is created, it fetch the data
    mounted() {
        this.createBarChart()
        console.log('Componente montado');

    },
    // Watch for changes in the data prop
    watch: {
        data() {
            // If the data changes, recreate the bar chart
            this.createBarChart()
        }
    },
    methods: {
        // Method to create the bar chart
        createBarChart() {
            if (this.data) {
                d3.select('#chart').html('');

                // Getting the data from the component's props
                const data = this.data
                // Creating an SVG element in the chart container
                const svg = d3.select('#chart')
                    .append('svg')
                    .attr('width', 300)
                    .attr('height', 300)

                // Creating the bars of the chart
                svg.selectAll('rect')
                    .data(data)
                    .enter()
                    .append('rect')
                    .attr('x', (d, i) => i * 70) // Position on the X axis
                    .attr('y', d => 500 - 10 * (d.country_count || 1)) // Position on the Y axis
                    .attr('width', 65) // Width of the bar
                    .attr('height', d => (d.country_count || 1) * 10) // Height of the bar
                    .attr('fill', 'green'); // Color of the bar


            }

        }
    }
}
</script>

<style>
/* Styles for the component go here */

#chart {
    border: 1rem solid blue;
    width: 10rem;
    height: 20rem;
}
</style>