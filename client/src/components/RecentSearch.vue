<script>

export default {
    data() {
        return {
            recents: []
        }
    },
    methods: {
        getRecents() {
            console.log("get recents running...")
            const data = localStorage.getItem('productgh_recent')

            if (typeof(data) === 'undefined' || data === null ) {
                this.recents = []
                return
            }
            this.recents = Array.from(JSON.parse(localStorage.getItem('productgh_recent')))

        },
        deleteRecent(item) {
            // method to delete particular recent
            const getData =  Array.from(JSON.parse(localStorage.getItem('productgh_recent')))
            this.recents = getData.filter(data => String(data) !== String(item))
            localStorage.setItem('productgh_recent', JSON.stringify(this.recents))
            return
        },
        clearRecents() {
            //method to clear all recent
            localStorage.setItem('productgh_recent', JSON.stringify([]))
            this.recents = []
            return
        }
    },
    mounted() {
        this.getRecents()
        console.log('this recents is ', this.recents)
    }
}
</script>

<template>
  <div class="recent_main">
    <div class="item-spacing">
        <div class="recent-heading">Recent search</div>
        <div>
            <font-awesome-icon class="item-addon" @click="clearRecents()" icon="fa-solid fa-delete-left" />
        </div>
    </div>

    <div v-for="(item) in recents"> 
        <div class="item-spacing">
            <div class="item-title">{{ item }}</div>
            <font-awesome-icon class="item-addon" @click="deleteRecent(item)" icon="fa-solid fa-xmark" />
        </div>
    </div>
  </div>
</template>

<style scoped>
.item-addon {
    transition: 100ms ease-in-out 100ms;
    cursor: pointer;
}
.item-addon:hover {
    transform: scale(1.09, 1.09);
}
.item-title {
    font-weight: 500;
}
.recent_main {
    margin-top: 10%;
    color: black;
    max-width: 40vw;
    width: 100%;
    display: flex;
    flex-direction: column;
    background-color: white;
    padding: 10px;
    border-radius: 10px;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}

.item-spacing {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    justify-content: space-between;
    padding: 5px;
}

.item-spacing:hover {
    cursor: pointer;
    background-color: aliceblue;
}

.recent-heading {
    font-weight: bold;
    font-size: large;
}

</style>