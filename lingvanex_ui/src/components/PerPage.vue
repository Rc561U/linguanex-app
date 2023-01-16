<template>
    <div class="selcet-per-page" style="width: 100px">
        <v-select
            v-model="select"
            :hint="`${select.state}, ${select.abbr}`"
            :items="items"
            item-title="state"
            item-value="abbr"
            label="Select"
            persistent-hint
            return-object
            single-line

        ></v-select>
    </div>

</template>
<script>
export default {
    data() {
        return {
            select: {state: '10', abbr: 'Items per page'},
            items: [
                {state: '10', abbr: 'items per page'},
                {state: '20', abbr: 'items per page'},
            ],
        }
    },
}
</script>