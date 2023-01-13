<template>
    <v-card>
        <v-card-title>
            Business
            <v-spacer></v-spacer>
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
            ></v-text-field>
        </v-card-title>

        <v-data-table
            :headers="headers"
            :items="users"
            :search="search"
            calculate-widths

        ></v-data-table>
    </v-card>
</template>
<script>
export default {
    name: "UsersTable",
    props: {
        users: {
            required: true
        },
    },
    data() {
        return {

            search: '',
            headers: [
                {
                    align: 'start',
                    key: 'name',
                    sortable: false,
                },
                {key: 'title', title: 'Title'},
                {key: 'publisher', title: 'Publisher'},
                {key: 'publishedYear', title: 'Published Year'},
                {key: 'email', title: 'Email'},
            ],
        }
    },
}
</script>
<style scoped>
.post_list-move, /* apply transition to moving elements */
.post_list-enter-active,
.post_list-leave-active {
    transition: all 0.5s ease;
}

.post_list-enter-from,
.post_list-leave-to {
    opacity: 0;
    transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.post_list-leave-active {
    position: absolute;
}
</style>