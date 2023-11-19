<template>
    <div id="app">
        <header>
            <h1 class="title-header">Query Lab</h1>
        </header>
        <main>
            <!-- The QueryBuilder component is used to build the query. 
                 When the data is obtained, the "updateData" method is called with the new data. -->
            <QueryBuilder @data-obtained="updateData"/>
            
            <!-- The VisualQuery component is used to visualize the data.
                 The "responseData" prop is passed to it. -->
            <VisualQuery :data="responseData"/>


        </main>
        <footer>
            <p>Made by Mateo Palomá</p>
        </footer>
    </div>
</template>

<script>
import QueryBuilder from './components/QueryBuilder.vue';
import VisualQuery from './components/VisualQuery.vue';


export default{
    name:"App",
    components: {
    // Importing the QueryBuilder and VisualQuery components
    QueryBuilder,
    VisualQuery
},
    data(){
        return {
            // The responseData data property is used to store the data obtained from the query
            responseData: null
        }
    },
    methods: {
        // The updateData method is used to update the responseData property with the new data
        updateData(newData){
            this.responseData = newData;
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
    display:flex;
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
    background-color: white;
    width: var(--with-size-page);
    height: auto;
    flex: 1 0 auto;
    
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
    height:5.6rem;
    letter-spacing: 0.2rem;
    color: #FFC300;
    text-shadow: 0.1rem 0.1rem #B8B8D1;
    flex-shrink: 0;
}
</style>
