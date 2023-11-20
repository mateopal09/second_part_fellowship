<template>
    <!-- The main container for the save query feature -->
    <div id="save-query">
        <main>
            <!-- Button to open the save query dialog -->
            <button class="savequery" @click="dialog = true">Save Query</button>

            <!-- The dialog for saving a query -->
            <div class="queryinformation" :class="{ dialog: dialog }" v-if="dialog">
                <div class="dialog-content">
                    <!-- Title of the dialog -->
                    <h2>Information to Save the Query</h2>

                    <!-- Input field for the name -->
                    <label for="name">Name:</label>
                    <input id="name" v-model="name" required>
                    <!-- Error message if the name field is empty -->
                    <div class="errors" v-if="nameError" style="color:red;">Field necessary</div>

                    <!-- Input field for the comment -->
                    <label for="comment">Comment:</label>
                    <input id="comment" v-model="comment" required>
                    <!-- Error message if the comment field is empty -->
                    <div class="errors" v-if="commentError" style="color:red;">Field necessary</div>

                    <!-- Input field for the username -->
                    <label for="username">Username:</label>
                    <input id="username" v-model="username" required>
                    <!-- Error message if the username field is empty -->
                    <div class="errors" v-if="usernameError" style="color:red;">Field necessary</div>

                    <!-- Container for the Save and Close buttons -->
                    <div class="button_container">
                        <!-- Button to save the query -->
                        <button class="save" @click="saveQuery">Save</button>
                        <!-- Button to close the dialog -->
                        <button class="close" @click="dialog = false">Close</button>
                    </div>

                    <!-- Message displayed when the query is successfully saved -->
                    <div v-if="requestStatus === 'success'" class="message success">Query succesfully saved</div>
                    <!-- Message displayed when there is an error saving the query -->
                    <div v-else-if="requestStatus === 'error'" class="message error">Error to save the query: It is
                        necessary to create a query</div>
                </div>
            </div>
        </main>
    </div>
</template>
<script>
// Importing the axios library for making HTTP requests
import axios from 'axios';

export default {
    // Props are custom attributes you can register on a component
    props: ['query'],
    // The data function returns an object that holds all the data for the component
    data() {
        return {
            dialog: false,
            name: '',
            username: '',
            comment: '',
            nameError: false,
            commentError: false,
            usernameError: false,
            selectedCountry: null,
            selectedSeries: null,
            year: 0,
            value: 0,
            requestStatus: null
        }
    },
    // Methods for the component
    methods: {
        // Method to save the query
        saveQuery() {
            // Check if the fields are empty
            this.nameError = this.name === '';
            this.commentError = this.comment === '';
            this.usernameError = this.username === '';
            this.queryError = !this.query;

            // If all fields are filled, make the query and save the query
            if (!this.nameError && !this.commentError && !this.usernameError && !this.queryError) {
                // First, make the query
                axios.post('http://127.0.0.1:8000/api/query-builder/', this.query)
                    .then(response => {
                        // Then, save the query
                        axios.post('http://127.0.0.1:8000/api/saved-queries/', {
                            name: this.name,
                            comment: this.comment,
                            username: this.username,
                            query: response.data.id // Use the ID of the query
                        })
                            .then(() => {
                                this.requestStatus = 'success';
                                // Delay the closing of the dialog by 2.5 seconds to show the success message
                                setTimeout(() => {
                                    this.dialog = false;
                                }, 2500);
                                this.$emit('query-saved');
                            })
                            .catch(error => {
                                console.error('Error saving the query:', error);
                                this.requestStatus = 'error' + error;
                            });
                    })
                    .catch(error => {
                        console.error('Error making the query:', error);
                    });
            } else {
                // If the query is empty, set the requestStatus to 'error'
                if (this.queryError) {
                    this.requestStatus = 'error';
                }
            }
        }
    }
}
</script>
<style scoped>
/* Define global custom properties */
:root {
    --font-family: var(--font-family);
    --font-color: aliceblue;
}

/* Apply a box-sizing rule to all elements and remove default margins and padding */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Set the base font size for the document */
html {
    font-size: 62.5%;
}

/* Reset all styles for the save-query component */
#save-query {
    all: initial;
}

/* Styles for the save query button */
.savequery {
    width: 100%;
    padding: 0.5rem;
    background-color: #113140;
    color: aliceblue;
    transition-duration: 0.5s;
    cursor: pointer;
}

/* Change the background color of the save query button on hover */
.savequery:hover {
    background-color: #8D00FF;
}

/* Styles for the query information dialog */
.queryinformation {
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
    display: none;
    /* Hide by default */
}

/* Show the dialog when the .dialog class is present */
.queryinformation.dialog {
    display: flex;
}

/* Styles for the dialog content */
.queryinformation .dialog-content {
    background-color: #113140;
    padding: 2rem;
    border-radius: 1rem;
    width: 100%;
    max-width: 60rem;
}

/* Styles for the button container */
.queryinformation .dialog-content .button_container {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
}

/* Styles for the close and save buttons */
.close,
.save {
    width: 10rem;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* Styles for the close button */
.close {
    background-color: #7D1531;
    color: white;
}

/* Styles for the save button */
.save {
    background-color: #32CD32;
    color: white;
}

/* Change the background color and text color of the buttons on hover */
.close:hover,
.save:hover {
    background-color: #ddd;
    color: black;
}

/* Styles for the success and error messages */
.message {
    text-align: center;
    padding: 1rem;
    margin: 1rem;
    background-color: #1E4A60;
    border-radius: 1rem;
}

.success {
    background-color: #1E4A60;
    color: white;
}

.error {
    background-color: #1E4A60;
    color: white;
}
</style>