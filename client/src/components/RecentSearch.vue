<script>
</script>

<template>
  <div class="recent_main">
    <div class="item-spacing">
        <div class="recent-heading">Recent search</div>
        <div>
            <font-awesome-icon icon="fa-solid fa-delete-left" />
        </div>
    </div>
  </div>
</template>

<style scoped>
.recent_main {
    margin-top: 15%;
    color: black;
    max-width: 40vw;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.item-spacing {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    justify-content: space-between;
}

.recent-heading {
    font-weight: bold;
    font-size: large;
}

</style>