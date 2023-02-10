<script lang="js">
import search1 from '../assets/image/search1.png'
import router from '../router/index'

export default {
  data() {
    return {
      product: '',
      searchimg: search1
    }
  },
  methods: {
    handleSearch(item) {
      if (typeof(item) === "string" && item.length > 0) {
        console.log(item, typeof(item))
        router.push(`productsearch/${String(item)}`)
      }
      else {
        alert("empty item")
      }
    }
  }
}

</script>

<template>
  <main>
    <div class="main">
    <form class="search_bar_box" @submit.prevent="handleSearch(product)">
        <input class="search_bar" v-model="product" placeholder="enter product to search for" />
        <span @click.prevent="handleSearch(product)">
          <img :src="searchimg" alt="search logo" class="logo"/>
        </span>
      </form>
    </div>

  </main>
</template>


<style scoped>

.main {
  width: 100vw;
  height: 100vh;
  padding: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.search_bar_box {
  max-width: 800px;
  width: 100%;
  box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 56px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  padding: 15px
}

.search_bar {
  padding: 15px;
  width: 100%;
  height: 100%;
  border: none;
  font-size: larger;
}

.search_bar:focus {
  outline: none;
  border: none;
}

.search_bar:placeholder-shown {
  font-size: larger;
  color: rgba(17, 17, 26, 0.1) 0px 4px 16px;
}

.logo {
   width: 25px;
   height: 25px;
}

.logo:hover {
  transform: scale(1.09, 1.09);
}


</style>
