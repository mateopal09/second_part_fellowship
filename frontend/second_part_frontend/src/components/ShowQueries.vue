<template>
  <!-- Root div element for displaying queries -->
  <div id="ShowQueries">
    <!-- Table for displaying query data -->
    <table>
      <!-- Table title  -->
      <caption>
        The Query Comedy Table: Laughs Guaranteed!
      </caption>
      <!-- Table header -->
      <thead>
        <tr>
          <!-- Column headers -->
          <th>Name</th>
          <th>Comment</th>
          <th>Username</th>
          <th>Country Code</th>
          <th>Series Code</th>
          <th>Year</th>
          <th>Value</th>
        </tr>
      </thead>
      <!-- Table body -->
      <tbody>
        <!-- Table row for each query in the queries array -->
        <!-- The 'v-for' directive is used for rendering a list of items based on an array -->
        <!-- The ':key' is a special attribute to give each node a unique id, improving Vue's rendering performance -->
        <tr v-for="query in queries" :key="query.name">
          <!-- Data cells displaying query properties -->
          <td>{{ query.name }}</td>
          <td>{{ query.comment }}</td>
          <td>{{ query.username }}</td>
          <td>{{ query.country_code }}</td>
          <td>{{ query.series_code }}</td>
          <td>{{ query.year }}</td>
          <td>{{ query.value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'; // Importing axios for making HTTP requests

export default {
  data() {
    return {
      queries: [], // Data property for storing the queries
    };
  },
  methods: {
    async loadQueries() { // Method for loading the queries
      const response = await axios.get('http://localhost:8000/show_queries/'); // Making a GET request to the server to fetch the queries
      this.queries = response.data; // Storing the response data in the queries array
    },
  },
  created() { // Vue lifecycle hook which will be called as soon as the Vue instance is created
    this.loadQueries(); // Calling the loadQueries method when the Vue instance is created
  },
};
</script>
<style>
:root {
  /* Define a custom property for the font family */
  --font-family: var(--font-family);
}

#ShowQueries {
  /* Apply the custom font family to the ShowQueries element */
  font-family: var(--font-family);
  /* Collapse borders for a cleaner look */
  border-collapse: collapse;
  /* Set the width to 100% to use the full width of the parent container */
  width: 100%;
  /* Set the text color to a dark blue */
  color: #0A192F;
}

#ShowQueries caption {
  font-family: var(--font-family);
  font-size: 3rem;
  margin: 1rem;
  /* Add a clear color for a fun look */
  color: #FFFFFF;
  /* Add a neon text shadow for a playful effect */
  text-shadow: 0 0 5px #32CD32, 0 0 10px #32CD32, 0 0 15px #FFD700, 0 0 20px #FFD700;
  /* Add a dark background color for contrast */
  background-color: #152D44;
  /* Add some padding */
  padding: 10px;
  /* Add a border with rounded corners */
  border: 2px solid #FFFFFF;
  border-radius: 15px;
  /* Add a box shadow for depth */
  box-shadow: 5px 10px #888888;
}

#ShowQueries td,
#ShowQueries th {
  /* Add a border to the table cells and headers */
  border: 1px solid #152D44;
  /* Add padding to the cells for better readability */
  padding: 8px;
}

#ShowQueries tr:nth-child(even) {
  /* Set a different background color for even rows for better readability */
  background-color: #ACC8E5;
}

#ShowQueries tr:hover {
  /* Set a different background color when hovering over a row */
  background-color: #DAE7F3;
}

#ShowQueries th {
  /* Add more padding to the headers */
  padding-top: 12px;
  padding-bottom: 12px;
  /* Align the text to the left */
  text-align: left;
  /* Set the background color of the headers to a dark blue */
  background-color: #152D44;
  /* Set the text color of the headers to white */
  color: white;
}
</style>