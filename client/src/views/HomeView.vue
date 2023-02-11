<script lang="js">
import search1 from '../assets/image/search1.png'
import human from '../assets/image/human.png'
import human2 from '../assets/image/human2.png'
import router from '../router/index'
import RecentSearch from '@/components/RecentSearch.vue'

export default {
  components: {
    RecentSearch: RecentSearch
  },
  data() {
    return {
      product: '',
      searchimg: search1,
      human: human,
      human2: human2
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
      <div class="background">
        <img alt="human" :src="human" class="human"/>
        <img alt="human2" :src="human2" class="human2"/>
      </div>
    <div class="main">
    <form class="search_bar_box" @submit.prevent="handleSearch(product)">
        <input class="search_bar" v-model="product" placeholder="enter product to search for" />
        <span @click.prevent="handleSearch(product)">
          <img :src="searchimg" alt="search logo" class="logo"/>
        </span>
      </form>
      <RecentSearch />
    </div>
  </main>
</template>


<style scoped>
.human {
  margin-top: 3.05%;
}

.background {
  position: absolute;
  width: 100vw;
  height: 100%;
  max-height: 70vh;
  border-radius: 30px;
  padding: 20px;
  border: 10px solid white;
  background-color: #FFC93C;
}

.main {
  width: 100vw;
  height: 100vh;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.search_bar_box {
  max-width: 800px;
  width: 100%;
  /* box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 56px; */
  border-radius: 50px;
  display: flex;
  align-items: center;
  background-color: white;
  padding: 15px
}

.search_bar_box:hover, .search_bar_box:focus {
  border: 3px solid #362FD9;
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
  font-weight: 400;
  color: #ECECEC
}

.logo {
   width: 25px;
   height: 25px;
}

.logo:hover {
  transform: scale(1.09, 1.09);
}


</style>
