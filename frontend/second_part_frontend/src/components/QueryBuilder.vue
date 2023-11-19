<template>
    <!-- Main container for the component -->
    <div id="query-builder">
        <!-- Main content of the component -->
        <main>
            <!-- Form for user input -->
            <div class="form-group">
                <!-- Dropdown for selecting country code -->
                <label for="country_code">Country Code:</label><br>
                <select id="country_code" v-model="selectedCountry" required>
                    <option v-for="country in country_code_array" :value="country">
                        {{ country }}
                    </option>
                </select><br>
                <!-- Error message for country code -->
                <div class="errors" v-if="countryError" style="color:red;">Field necessary</div>

                <!-- Dropdown for selecting series code -->
                <label for="series_code">Series Code:</label><br>
                <select id="series_code" v-model="selectedSeries" required>
                    <option v-for="series in series_code_array" :value="series">
                        {{ series }}
                    </option>
                </select><br>
                <!-- Error message for series code -->
                <div class="errors" v-if="seriesError" style="color:red;">Field necessary</div>

                <!-- Input for entering year -->
                <label for="year">Year:</label><br>
                <input type="number" id="year-text" name="year-text" min="1985" max="2100" step="1" v-model="year"><br>
                <!-- Error message for year -->
                <p class="errors">{{ errorYearMessage }}</p>
                <!-- Range input for selecting year -->
                <input type="range" id="year" name="year" min="1985" max="2100" step="1" v-model="year"><br>
                
                <!-- Input for entering value -->
                <label for="value">Value:</label><br>
                <input type="number" id="value" name="value" step="any" v-model="value"><br>
                <!-- Button for running query -->
                <button class="runquery" v-on:click="runquery">Run Query</button>
            </div>
        </main>
    </div>
</template>

<script>
// Importing the axios library for making HTTP requests
import axios from 'axios';

export default {
    name: "App",
    // Defining the data properties for the component
    data: function () {
        return {
            // Data properties for form inputs
            selectedCountry: null,
            selectedSeries: null,
            year: 2000,
            value: 0,
            // Data properties for error messages
            errorYearMessage: null,
            countryError: false,
            seriesError: false,
            // Data property for storing the response data from the API
            responseData: null,
            // Arrays for the dropdown options
            country_code_array: [
                "ALB",
                "AUS",
                "AZE",
                "BLR",
                "BMU",
                "CAN",
                "CHN",
                "FRA",
                "GBR",
                "GEO",
                "GRL",
                "HKG",
                "HRV",
                "ISR",
                "JPN",
                "KAZ",
                "KGZ",
                "KOR",
                "LKA",
                "LUX",
                "MDA",
                "MDV",
                "MNE",
                "MUS",
                "NCL",
                "NZL",
                "PRI",
                "PSE",
                "RUS",
                "SDN",
                "SGP",
                "SRB",
                "SYC",
                "UKR",
                "USA",
                "UZB",
                "VEN",
                "VIR",
                "VNM",
                "XKX",
                "ZAF",
                "TZA",
                "AUT",
                "BEL",
                "BGR",
                "CHE",
                "CZE",
                "DEU",
                "DNK",
                "ESP"],
            series_code_array: [
                "SP.POP.TOTL",
                "SP.POP.GROW",
                "SP.POP.0014.TO.ZS",
                "SP.POP.1564.TO.ZS",
                "SP.POP.TOTL.FE.ZS",
                "SP.POP.TOTL.MA.ZS",
                "NY.GNP.PCAP.CD",
                "NY.GDP.PCAP.CD",
                "NY.GDP.PCAP.KD",
                "NY.GDP.PCAP.PP.CD",
                "NY.GNP.PCAP.PP.CD",
                "NY.GDP.PCAP.PP.KD",
                "NY.GDP.MKTP.PP.KD",
                "NY.GNP.MKTP.PP.CD",
                "NY.GDP.MKTP.PP.CD",
                "SP.POP.1564.MA.IN",
                "SP.POP.0014.TO",
                "SP.POP.1564.TO",
                "SP.POP.1564.FE.IN",
                "SP.POP.0014.MA.IN",
                "SP.POP.0014.FE.IN"],

        };
    },
    methods: {
        // Method for running the query when the form is submitted
        runquery() {
            // Check if the country and series fields are filled out
            this.countryError = !this.selectedCountry;
            this.seriesError = !this.selectedSeries;

            // If either field is not filled out, stop the function
            if (this.countryError || this.seriesError) {
                return;
            }
            
            // Check if the year is between 1985 and 2100
            if(this.year < 1985 || this.year > 2100){
                this.errorYearMessage = 'Please, enter a year between 1985 and 2100';
                return;
            } else {
                this.errorYearMessage = null;
            }

            // Make a POST request to the API with the form inputs
            axios.post('http://127.0.0.1:8000', {
                country_code: this.selectedCountry,
                series_code: this.selectedSeries,
                year: this.year,
                value: this.value
            })
            .then(response => {
                // If the request is successful, store the response data
                this.responseData = response.data;
                this.$emit('data-obtained', this.responseData);

            })
            .catch(error => {
                // If the request fails, log the error to the console
                console.error(error);
            })
        }
    }
}
</script>

<style>
:root{
    /* Define a custom property for the font family */
    --font-family: var(--font-family);
}

* {
    /* Apply a box-sizing rule to all elements */
    box-sizing: border-box;
    /* Remove default margins from all elements */
    margin: 0;
    /* Remove default padding from all elements */
    padding: 0;
}

html {
    /* Set the base font size for the document */
    font-size: 62.5%;
}

.form-group {
    /* Style rules for the form group */
    display: flex;
    flex-direction: column;
    margin: 1rem;
    border: 0.001rem solid #113140;
    border-radius: 0.5rem;
    width: 25rem;
}

.form-group label {
    /* Style rules for the labels in the form group */
    margin: 0.5rem 2rem;
    font-size: 1.5rem;
    font-family: var(--font-family);
    color: black;
}

.errors {
    /* Style rules for error messages */
    margin:0rem 0rem 1.5rem 1rem;
    color: red;
    width: 20.5rem;
    font-family: var(--font-family);
}

.form-group select,.form-group input {
    /* Style rules for select and input elements in the form group */
    width: 80%;
    padding: 0.5rem;
    font-size: 1rem;
    margin-left: 1.5rem;
    border: 0.01rem solid gray;
    border-radius: 1rem;
}

.runquery {
    /* Style rules for the query button */
    margin: 2rem;
    width: 60%;
    background-color: #113140; /* Background color of the button */
    color: #FFFFFF; /* Text color */
    padding: 0.5rem; /* Internal spacing */
    text-decoration: none; /* Remove text decoration */
    font-size: 1.4rem; /* Font size */
    transition-duration: 0.5s; /* Transition duration */
    cursor: pointer; /* Change the cursor to a pointer */
    border: 0.1rem solid #8D00FF; /* Neon purple border */
    border-radius: 0.5rem;
}

.runquery:hover {
    /* Style rules for the query button when the mouse is over it */
    background-color: #FFC300; /* Background color when the mouse is over */
}

.responseData{
    /* Style rules for the response data container */
    display: inline-block;
    justify-content: right;
    align-items: right;
}
</style>