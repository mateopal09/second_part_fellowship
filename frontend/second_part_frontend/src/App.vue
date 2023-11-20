<template>
    <!-- Root div element for the application -->
    <div id="app">
        <!-- Header section -->
        <header>
            <!-- Title of the application -->
            <h1 class="title-header">Query Lab</h1>
        </header>
        <!-- Main section -->
        <main>
            <!-- The QueryBuilder component is used to build the query. 
                 When the data is obtained, the "updateData" method is called with the new data. -->
            <QueryBuilder class="querybuilder" @data-obtained="updateData" @query-made="querycreated" />

            <!-- The VisualQuery component is used to visualize the data.
                 The "responseData" prop is passed to it. -->
            <VisualQuery class="visualquery" :data="responseData" />

            <!-- The SaveQuery component is used to save the query.
                 The "query" prop is passed to it. When the query is saved, the "Updatequery" method is called. -->
            <SaveQuery class="savequery" :query="query" @query-saved="Updatequery" />

            <!-- The ShowQueries component is used to display the queries. -->
            <ShowQueries class="showqueries" ref="showQueries" />
        </main>
        <!-- Footer section -->
        <footer>
            <!-- Footer text -->
            <p>Made by Mateo Palomá</p>
        </footer>
    </div>
</template>

<script>
import QueryBuilder from './components/QueryBuilder.vue'; // Importing the QueryBuilder component
import VisualQuery from './components/VisualQuery.vue'; // Importing the VisualQuery component
import SaveQuery from './components/SaveQuery.vue'; // Importing the SaveQuery component
import ShowQueries from './components/ShowQueries.vue'; // Importing the ShowQueries component

export default {
    name: "App", // Name of the Vue component
    components: {
        // Registering the imported components
        QueryBuilder,
        VisualQuery,
        SaveQuery,
        ShowQueries,
    },
    data() {
        return {
            // The responseData data property is used to store the data obtained from the query
            responseData: null,
            // The query data property is used to store the created query
            query: null
        }
    },
    methods: {
        // The updateData method is used to update the responseData property with the new data
        updateData(newData) {
            this.responseData = newData;
        },
        // The querycreated method is used to update the query property with the created query
        querycreated(query) {
            this.query = query;
        },
        // The Updatequery method is used to reload the queries in the ShowQueries component
        Updatequery() {
            this.$refs.showQueries.loadQueries();
        }
    }
}
</script>
<style>
/*

/**
    Setting reset CSS
    */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/*Root for variables*/
:root {
    --with-size-page: 100%;
    --font-family: 'Good Times', sans-serif;
}

/**---------------------------------------------
    Changing the font size in 10px so I can use REM
    ----------------------------------------------*/
html {
    font-size: 62.5%;
}

/**------------------
    Styles for ID app
    ----------------------*/
body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/**----------------
    Styles for header
    -----------------*/
header {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #0A192F;
    width: var(--with-size-page);
    height: 5.6rem;

}

.title-header {
    font-family: var(--font-family);
    font-size: 3rem;
    letter-spacing: 0.2rem;
    color: #FFC300;
    text-shadow: 0.2rem 0.15rem #B8B8D1;
}

/** -------------
    Styles for main
    ---------------*/
main {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    background-color: white;
    width: var(--with-size-page);
    height: auto;
}

.savequery {
    /* Styles for  SaveQuery */
    position: relative;
    top: 40rem;

}

.showqueries {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

/**------------
    Styles for footer
    ---------------*/
footer {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #0A192F;
    font-family: var(--font-family);
    width: var(--with-size-page);
    height: 5.6rem;
    letter-spacing: 0.2rem;
    color: #FFC300;
    text-shadow: 0.1rem 0.1rem #B8B8D1;
}
</style>
