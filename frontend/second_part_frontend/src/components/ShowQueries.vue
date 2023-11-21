<template>
  <div id="ShowQueries">
    <!-- Table for displaying the queries -->
    <table class="showtable">
      <caption>
        The Query Comedy Table: Laughs Guaranteed!
      </caption>
      <thead>
        <!-- Table headers -->
        <tr>
          <th>Name</th>
          <th>Comment</th>
          <th>Username</th>
          <th>Country Code</th>
          <th>Series Code</th>
          <th>Year</th>
          <th>Value</th>
          <th>Comment</th>
        </tr>
      </thead>
      <tbody v-for="(query, index) in queries" :key="'query-' + index">
        <!-- Table rows for displaying the queries -->
        <tr>
          <td>{{ query.name }}</td>
          <td>{{ query.comment }}</td>
          <td>{{ query.username }}</td>
          <td>{{ query.country_code }}</td>
          <td>{{ query.series_code }}</td>
          <td>{{ query.year }}</td>
          <td>{{ query.value }}</td>
          <td class="column_comment">
            <!-- Button for opening the comment dialog -->
            <button class="comment" @click="selectedQuery = query; showDialog = true">Comment</button>
          </td>
        </tr>
        <!-- Table rows for displaying the comments -->
        <tr class="comment_user" v-for="(comment, commentIndex) in query.comments"
          :key="'comments-' + index + '-' + commentIndex">
          <td colspan="8">
            <ul style="list-style-type: none;">
              <li>
                <!-- Display the username and comment -->
                <strong style="font-size: 1.1rem;">User:</strong> {{ comment.username }},
                <strong style="font-size: 1.1rem;">Comment:</strong>{{ comment.comment }}
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Dialog for adding a comment -->
    <div v-if="showDialog" class="queryinformation dialog">
      <div class="dialog-content">
        <h2>Add a comment</h2>
        <!-- Input fields for the username and comment -->
        <label for="username">Username</label>
        <input id="username" v-model="newComment.username">
        <div class="errors" v-if="usernameError" style="color:red;">Field necessary</div>

        <label for="comment">Comment</label>
        <input id="comment" v-model="newComment.comment">
        <div class="errors" v-if="commentError" style="color:red;">Field necessary</div>

        <!-- Buttons for saving the comment and closing the dialog -->
        <div class="button_container">
          <button class="save" @click="addComment">Save</button>
          <button class="close" @click="showDialog = false">Close</button>
        </div>
        <!-- Messages for displaying the request status -->
        <div v-if="requestStatus === 'success'" class="message success">Comment succesfully saved</div>
        <div v-else-if="requestStatus === 'error'" class="message error">Error to save the comment</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // Importing axios for making HTTP requests

export default {
  data() {
    return {
      queries: [], // Data property for storing the queries
      selectedQuery: null, // Data property for storing the selected query
      newComment: { // Data property for storing the new comment
        username: '',
        comment: '',
      },
      showDialog: false, // Data property for controlling the visibility of the dialog
      usernameError: false, // Data property for storing the username error state
      commentError: false, // Data property for storing the comment error state
      requestStatus: false, // Data property for storing the request status
    };
  },
  methods: {
    async loadQueries() { // Method for loading the queries
      const response = await axios.get('http://localhost:8000/show_queries/'); // Making a GET request to the server to fetch the queries
      this.queries = response.data; // Storing the response data in the queries array
    },
    async addComment() { // Method for adding a comment
      let selectedQueryId = this.selectedQuery.id; // Getting the id of the selected query
      this.usernameError = this.newComment.username === ''; // Checking if the username is empty
      this.commentError = this.newComment.comment === ''; // Checking if the comment is empty

      // Validation of username and comment
      if (!this.usernameError && !this.commentError) { // If both username and comment are not empty
        try {
          // Making a POST request to the server to create a new comment
          await axios.post(`http://127.0.0.1:8000/api/saved-queries/${selectedQueryId}/create_comment/`, this.newComment);
          this.loadQueries(); // Reloading the queries
          this.requestStatus = 'success'; // Setting the request status to success
          // Delay the closing of the dialog by 2.5 seconds to show the success message
          setTimeout(() => {
            this.showDialog = false;
          }, 2000);
        } catch (error) { // If there's an error
          console.error(error); // Log the error
          this.requestStatus = 'error' + error; // Set the request status to error
        }
      } else { // If either username or comment is empty
        console.log("required fields") // Log a message indicating that fields are required
      }
    }
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
  margin-top: 10rem;
}

#ShowQueries caption {
  /* Apply the custom font family and size to the caption of ShowQueries */
  font-family: var(--font-family);
  font-size: 3rem;
  /* Set the margin around the caption */
  margin: 1rem;
  /* Set the text color to white and apply a multi-color text shadow */
  color: #FFFFFF;
  text-shadow: 0 0 5px #32CD32, 0 0 10px #32CD32, 0 0 15px #FFD700, 0 0 20px #FFD700;
  /* Set the background color to a dark blue, apply padding, and set the border style */
  background-color: #152D44;
  padding: 10px;
  border: 2px solid #FFFFFF;
  border-radius: 15px;
  /* Apply a box shadow for a 3D effect */
  box-shadow: 5px 10px #888888;
}

#ShowQueries td,
#ShowQueries th {
  /* Apply a thin solid border, padding, and font size to the table cells and headers */
  border: 0.01rem solid #152D44;
  padding: 8px;
  font-size: 1.2rem;
}

#ShowQueries tr:nth-child(even) {
  /* Set a different background color for even rows */
  background-color: #ACC8E5;
}

#ShowQueries tr:hover {
  /* Change the background color of a row when it's hovered over */
  background-color: #DAE7F3;
}

#ShowQueries th {
  /* Apply padding, text alignment, background color, and text color to the table headers */
  padding-top: 1.2rem;
  padding-bottom: 1.2rem;
  text-align: left;
  background-color: #152D44;
  color: white;
}

.column_comment {
  /* Center the content of the column_comment class */
  display: flex;
  justify-content: center;
  align-items: center;
}

.comment {
  /* Style the comment class with a specific width, padding, background color, text color, transition duration, cursor style, font size, and border radius */
  width: 85%;
  padding: 0.5rem;
  background-color: #113140;
  color: aliceblue;
  transition-duration: 0.5s;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 0.5rem;
}

.showtable {
  /* Apply the custom font family, collapse borders, set the width to 100%, set a maximum width, set the text color, center the table, and set the top margin for the showtable class */
  font-family: var(--font-family);
  border-collapse: collapse;
  width: 100%;
  max-width: 90rem;
  color: #0A192F;
  margin: 0 auto;
  margin-top: 5rem;
}

/* Change the background color of the comment button on hover */
.comment:hover {
  background-color: #8D00FF;
}

.queryinformation {
  /* Style the queryinformation class with a fixed position, full width and height, semi-transparent black background color, centered content, padding, box sizing, and a high z-index */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  box-sizing: border-box;
  z-index: 1000;
}

.queryinformation.dialog {
  /* Display the dialog class within the queryinformation class as a flex container */
  display: flex;
}

.queryinformation .dialog-content {
  /* Style the dialog-content class within the queryinformation class with a flex container, column direction, specific background color, padding, border radius, full width, maximum width, text color, custom font family, and font size */
  display: flex;
  flex-direction: column;
  background-color: #113140;
  padding: 2rem;
  border-radius: 1rem;
  width: 100%;
  max-width: 60rem;
  color: aliceblue;
  font-size: var(--font-family);
  font-size: 1.5rem;
}

.dialog-content label {
  /* Set the margin around the labels within the dialog-content class */
  margin: 1rem 0;
}

.dialog-content input {
  /* Set the width and border radius of the input fields within the dialog-content class */
  width: 50%;
  border-radius: 0.5rem;
}

.dialog-content #username {
  /* Set the height of the username input field within the dialog-content class */
  height: 3rem;
}

.dialog-content #comment {
  /* Set the height of the comment input field within the dialog-content class */
  height: 6rem;
}

.queryinformation .dialog-content .button_container {
  /* Display the button_container class within the dialog-content class as a flex container, justify the content to the end, and set the gap between the buttons */
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.close,
.save {
  /* Style the close and save buttons with a specific width, padding, no border, rounded corners, font size, pointer cursor, and transition for the background color */
  width: 10rem;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.close {
  /* Set the background color and text color of the close button */
  background-color: #7D1531;
  color: white;
}

.save {
  /* Set the background color and text color of the save button */
  background-color: #32CD32;
  color: white;
}

.close:hover,
.save:hover {
  /* Change the background color and text color of the close and save buttons when they're hovered over */
  background-color: #ddd;
  color: black;
}

/* Styles for the success and error messages */
.message {
  /* Center the text, apply padding and margin, set the background color, and round the corners for the message class */
  text-align: center;
  padding: 1rem;
  margin: 1rem;
  background-color: #1E4A60;
  border-radius: 1rem;
}

.success {
  /* Set the background color and text color of the success class */
  background-color: #1E4A60;
  color: white;
}

.error {
  /* Set the background color and text color of the error class */
  background-color: #1E4A60;
  color: white;
}
</style>