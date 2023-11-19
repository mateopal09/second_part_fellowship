<template>
  <div id="visual-query">
    <!-- The Bar component is rendered if 'loaded' is true. The data and options for the chart are passed as props -->
    <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
// Import the Bar component from vue-chartjs and various elements from chart.js
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Register the imported elements with Chart.js
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  // Declare the Bar component in the 'components' option
  components: { Bar },
  // The 'data' prop is used to receive the data from the parent component
  props: ['data'],
  data: () => ({
    // 'loaded' is used to control the rendering of the BarChart component
    loaded: true,
    // 'chartData' is used to store the data for the bar chart
    chartData: {
      labels: [],
      datasets: []
    },
    // 'chartOptions' is used to store the options for the bar chart
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
      //Adding the title and its font for the chart title
      plugins: {
        title: {
          display: true,
          text: 'Query visualization',
          font: {
            size: 24,
          }
        }
      },
      scales: {
        x: {
          stacked: true,  // Configures the x-axis to be stacked
          title: {
            display: true,
            text: 'Tables'  // Adds a title to the x-axis
          }
        },
        y: {
          stacked: true,  // Configures the y-axis to be stacked
          title: {
            display: true,
            text: 'Percentage by field on each table (%)'  // Adds a title to the y-axis
          },
          ticks: {
            callback: function (value, index, values) {
              return value + '%'; // Converts the y-axis labels to percentage
            }
          }
        }
      }
    }
  }),
  watch: {
    // Watch the "responseData" prop for changes
    data: {
      // Call the handler immediately after the component is created, and every time the prop changes
      immediate: false,
      handler(newData) {
        if (newData) {
          // Format the new data for the bar chart and assign it to "chartData"
          this.chartData = this.formatDataForBarChart(newData);
          // Set "loaded" to true to render the BarChart component
          this.loaded = true;
        }
      }
    }
  },
  methods: {
    // The "formatDataForBarChart" method is used to format the data for the bar chart
    formatDataForBarChart(data) {
      try {
        // Define the fields that will be used to create the datasets for the chart
        const fields = ['country_code', 'series_code', 'year', 'value'];
        // Define the tables that will be used as labels for the chart
        const tables = ['country_summary', 'series_summary', 'International Education', 'country_series_definitions'];
        // Define the colors that will be used for the datasets in the chart
        const colors = ['#f87979', '#7acbf9', '#f8e879', '#79f8f2'];
        // Map over the fields to create the datasets for the chart
        const datasets = fields.map((field, index) => {
          return {
            label: field,
            backgroundColor: colors[index % colors.length],
            data: tables.map(table => {
              // Filter the data for the current table
              const tableData = data.filter(item => item.Tables === table);
              // Calculate the count for the current field in the current table
              const fieldCount = tableData.reduce((count, item) => item[field] !== 0 ? count + item[field] : count, 0);
              // Calculate the total count for all fields in the current table
              const totalCount = tableData.reduce((count, item) => {
                let fieldSum = 0;
                fields.forEach(field => {
                  if (item[field] !== 0) {
                    fieldSum += item[field];
                  }
                });
                return count + fieldSum;
              }, 0);
              // Calculate the percentage for the current field in the current table
              return totalCount === 0 ? 0 : (fieldCount / totalCount) * 100;
            })
          };
        });
        // Return the labels and datasets for the chart
        return { labels: tables, datasets };
      } catch (error) {
        console.error('An error occurred while formatting the data for the bar chart:', error);
      }
    }
  }
}
</script>
<style>
#visual-query {
  height: 42.5rem;
  width: 70rem;
  position: relative;
  right: 0;
  border: 0.001rem solid #113140;
  border-radius: 0.5rem;
  margin: 1.5rem 5rem;
}
</style>