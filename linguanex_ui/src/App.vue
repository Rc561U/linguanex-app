<template>
    <v-app>
        <div>
            <nav-bar/>
            <div v-if="users.length > 0">
                <v-card
                    class="mx-auto"
                    id="main_card"
                    width="max-content"
                    height="max-content"
                >

                    <!--            Main data table component -->
                    <v-row align="stretch">
                        <v-col
                            class="d-flex justify-center align-center"
                        >
                            <users-table
                                v-bind:users="users"
                            />
                        </v-col>
                    </v-row>

                </v-card>

            </div>

            <v-progress-circular v-else

                                 indeterminate
                                 class="progress_error"
                                 :size="80"
                                 :width="7"
                                 color="indigo darken-4"
            ></v-progress-circular>
        </div>

    </v-app>
</template>
<script>
import UsersTable from "@/components/UsersTable.vue";
import axios from "axios";

import NavBar from "@/components/NavBar.vue";


export default {
    name: 'App',
    components: {
        NavBar,UsersTable
    },
    data: () => ({
        users: [],
        page: 1,
        limit: 15,
        totalPages: 0,
        nextPage: 0,
        previousPage: 0,
        loading: false,
        dialog: false,
        options: {
            itemsPerPage: 100
        },


    }),
    methods: {


        async fetchUsers() {
            try {
                const response = await axios.get("http://localhost:8000/api/", {

                });
                this.totalPages = Math.ceil(response.data / this.limit)
                this.users = response.data;


            } catch (e) {
                this.alert_text = `Server is not available`;
                this.snackbar = true;
            }
        },
        async getRequst() {
            try {
                const response = await axios.get("http://localhost:8000/api/order-by/?limit=10", {});
                this.users = response.data.results;


            } catch (e) {
                this.alert_text = `Server is not available`;
                this.snackbar = true;
            }
        },

        changePage() {
            this.user = []
            this.fetchUsers()
        },
    },
    mounted() {
        this.fetchUsers();
    },

}
</script>
<style>
.label-header {
    display: flex;
    justify-content: space-between;
    padding-left: 10px;
    padding-top: 10px;
}

.actions-header {
    display: flex;
    justify-content: space-between;
    padding: 20px;
}

#main_card {
    margin-top: 100px;
}

.progress_error {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
}
</style>