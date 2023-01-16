<template>
    <v-app-bar
        color="teal-darken-4"
        image="https://picsum.photos/1920/1080?random"

    >
        <template v-slot:image>
            <v-img
                gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
            ></v-img>
        </template>
        <v-app-bar-title>Django API</v-app-bar-title>
<v-btn icon @click="scrapData" value="recent">
            <v-icon>mdi-database-plus</v-icon>

        </v-btn>

        <v-btn icon href="http://localhost:8000/api" value="recent">
            <v-icon>mdi-keyboard-return</v-icon>

        </v-btn>
    </v-app-bar>
</template>

<script>
import axios from "axios";

export default {
    name: "NavBar",
    methods: {
        async scrapData() {
            try {
                await axios.get("http://localhost:8000/", {});
            } catch (e) {
                this.alert_text = `Server is not available`;
                this.snackbar = true;
            }
        },
    }
}
</script>
<style scoped>
.nav-bar-items {
    text-align: center;
}
</style>