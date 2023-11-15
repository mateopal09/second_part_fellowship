<template>
    <div id="app">
        <header>
            <h1 class="title-header">Query Lab</h1>
        </header>
        <main>
            <div class="control-section">
                <div class="col-lg-12 querybuilder-control">
                    <ejs-querybuilder>
                        <e-columns>
                            <!--Fields to filter all the tables-->
                            <e-column field='country_code' label="Country code" type="boolean" :values="country_code_array"/>
                            <e-column field="series_code" label="Series code" type="boolean" :values="series_code_array"/>
                            <e-column field='year' label='Year' type='date' format="yyyy" />
                            <e-column field='value' label='Value' type='number'/>
                        </e-columns>
                    </ejs-querybuilder>
                    <button class="e-query-builder_runquery" @click="runQuery">Run Query</button>

                </div>
            </div>
        </main>
        <footer>
            <p>El footer</p>
        </footer>
    </div>
</template>

<script>
import { QueryBuilderComponent, ColumnDirective, ColumnsDirective } from "@syncfusion/ej2-vue-querybuilder";

export default {
    name: "App",
    components: {
        "ejs-querybuilder": QueryBuilderComponent,
        "e-columns": ColumnsDirective,
        "e-column": ColumnDirective
    },
    data: function () {
        return {
            country_code_array: [
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
            query: {}
        };
    },
    methods: {
        runQuery() {
            // Aquí debes implementar la lógica para enviar la consulta al backend
        }
    },
}
</script>

<style>
/*
    Styles for Query Builder
    */
@import "../node_modules/@syncfusion/ej2-base/styles/material.css";
@import "../node_modules/@syncfusion/ej2-buttons/styles/material.css";
@import "../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
@import "../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
@import "../node_modules/@syncfusion/ej2-inputs/styles/material.css";
@import "../node_modules/@syncfusion/ej2-lists/styles/material.css";
@import "../node_modules/@syncfusion/ej2-popups/styles/material.css";
@import "../node_modules/@syncfusion/ej2-calendars/styles/material.css";
@import "../node_modules/@syncfusion/ej2-vue-querybuilder/styles/material.css";

/*Root for variables*/
:root {
    --with-size-page: 100%;
}

/**
    Setting reset CSS
    */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/**-------------
    Body styles
    ---------------*/
body {
    background-color: white;
    margin: 0;
    padding: 0;
    width: var(--with-size-page);

}

/**------------------
    Styles for ID app
    ----------------------*/
#app {
    display: block;
    margin: 0;
    padding: 0;
}

/**---------------------------------------------
    Changing the font size in 10px so I can use REM
    ----------------------------------------------*/
html {
    font-size: 62.5%;
}

/**----------------
    Styles for header
    -----------------*/
header {
    background-color: #0A192F;
    width: var(--with-size-page);
    height: 5.6rem;
    position: fixed;
    top: 0;
    left: 0;
}

.title-header {
    text-align: center;
    font-family: 'Good Times', sans-serif;
    font-size: 3rem;
    letter-spacing: 0.2rem;
    color: #FFC300;
    text-shadow: 0.2rem 0.15rem #B8B8D1;
}

/** -------------
    Styles for main
    ---------------*/
main {
    background-color: white;
    width: var(--with-size-page);
    position: absolute;
    top: 5.6rem;
    /* Esto coloca el main justo debajo del header */
    bottom: 4rem;
    /* Esto coloca el main justo encima del footer */
    min-height: calc(100vh - 5.6rem - 4rem);
    /* Esto hace que el main tenga al menos la altura del espacio restante, pero se expanda si tiene más contenido */
    margin: 0;
    padding: 0;
    display: flex;
    /* border: 1rem solid blue; */
}

.control-section {
    width: 20%;
    margin: 3rem;
}

.e-group-container {
    width: 100%;
}

.e-query-builder_runquery {
    margin-top: 2rem;
    width: 40%;
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

.e-query-builder_runquery:hover {
    background-color: #FFC300;
    /* Color de fondo del botón cuando el mouse está encima */
}

/**------------
    Styles for footer
    ---------------*/
footer {
    background-color: #0A192F;
    position: fixed;
    bottom: 0;
    width: var(--with-size-page);
    height: 4rem;
}
</style>
