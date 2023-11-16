<template>
    <div id="query-builder">
        <main>
            <div class="form-group">
                <label for="country_code">Country Code:</label><br>
                <select id="country_code" v-model="selectedCountry" requiered>
                    <option v-for="country in country_code_array" :value="country">
                        {{ country }}
                    </option>
                </select><br>
                <label for="series_code">Series Code:</label><br>
                <select id="series_code" v-model="selectedSeries" required>
                    <option v-for="series in series_code_array" :value="series">
                        {{ series }}
                    </option>
                </select><br>
                <label for="year">Year:</label><br>
                <input type="number" id="year-text" name="year-text" min="1985" max="2100" step="1" v-model="year"><br>
                <p class="year_error">{{ errorYearMessage }}</p>
                <input type="range" id="year" name="year" min="1985" max="2100" step="1" v-model="year"><br>
                
                <label for="value">Value:</label><br>
                <input type="number" id="value" name="value" step="any" v-model="value"><br>
                <button class="runquery" v-on:click="runquery">Run Query</button>
            </div>
        </main>
    </div>
</template>

<script>
//Axios to make requests
import axios from 'axios';

export default {
    name: "App",
    data: function () {
        return {
            selectedCountry: null,
            selectedSeries: null,
            year: 2000,
            value: 0,
            errorYearMessage: null,
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
            // query: {}
        };
    },
    methods: {
        runquery() {
            console.log(this.selectedCountry);
            console.log(this.selectedSeries);
            console.log(this.year);
            console.log(this.value);
            
            if(this.year < 1985 || this.year > 2100){
                this.errorYearMessage = 'Please, enter a year between 1985 and 2100';
                return;
            }else {
                this.errorYearMessage = null;
            }

            axios.post('http://127.0.0.1:8000/api/query-builder/', {
                country_code: this.selectedCountry,
                series_code:this.selectedSeries,
                year: this.year,
                value: this.value
            })
            .then(response =>{
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            })

        }
    }
}
</script>

<style>
:root{
    --font-family: var(--font-family);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 62.5%;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin: 1rem;
    border: 0.001rem solid #113140;
    border-radius: 0.5rem;
    width: 25rem;
}

.form-group label {
    margin: 0.5rem 2rem;
    font-size: 1.5rem;
    font-family: var(--font-family);
    color: black;

    
}

.year_error {
    margin-left: 1rem;
    color: red;
    width: 20.5rem;
    font-family: var(--font-family) ;
}

.form-group select,.form-group input {
    width: 80%;
    padding: 0.5rem;
    font-size: 1rem;
    margin-left: 1.5rem;
    border: 0.01rem solid gray;
    border-radius: 1rem;
}

.runquery {
    margin: 2rem;
    width: 60%;
    background-color: #113140;
    /* Color de fondo del botón */
    color: #FFFFFF;
    /* Color del texto */
    padding: 0.5rem;
    /* Espaciado interno */
    text-decoration: none;
    /* Remueve la decoración del texto */
    font-size: 1.4rem;
    /* Tamaño de la fuente */
    transition-duration: 0.5s;
    /* Duración de la transición */
    cursor: pointer;
    /* Cambia el cursor a un puntero */
    border: 0.1rem solid #8D00FF;
    /* Borde púrpura neón */
    border-radius: 0.5rem;

}

.runquery:hover {
    background-color: #FFC300;
    /* Color de fondo del botón cuando el mouse está encima */
}
</style>