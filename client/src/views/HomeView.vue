<script lang="js">
import search1 from '../assets/image/search1.png'
import humann from '../assets/image/humann.png'
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
      humann: humann,
      human2: human2
    }
  },
  methods: {
    handleSearch(item) {
      if (typeof(item) === "string" && item.length > 0) {
        console.log(item, typeof(item))
        this.setRecent(item)
        router.push(`productsearch/${String(item)}`)
      }
      else {
        alert("empty item")
      }
    },
    setRecent(item) {
        const recentData = localStorage.getItem('productgh_recent')

        if(recentData === null || typeof(recentData) === 'undefined') {
          const data = [item]
          localStorage.setItem('productgh_recent', JSON.stringify(data))
          return
        }

        const getCurrentData = Array.from(JSON.parse(recentData))
        console.log("get current data ", getCurrentData, getCurrentData.length)
        if (getCurrentData.length < 3) {
             const isItemExist = getCurrentData.filter(data => String(data) === String(item))
             console.log("is item exists ", isItemExist)
             if (isItemExist.length === 0) {
                 let new_items = [...getCurrentData, item]
                 localStorage.setItem('productgh_recent', JSON.stringify(new_items))
                 return
             }
        }
        else{
            let editData = [...getCurrentData]
            editData.pop(0)
            editData.push(item)
            localStorage.setItem('productgh_recent', JSON.stringify(editData))
            return

        }




    }
  }
}

</script>

<template>
  <main>
      <div class="background">
        <img alt="humann" :src="humann" class="human"/>
        <!-- <img alt="human2" :src="human2" class="human2"/> -->
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


.background {
  position: absolute;
  width: 100vw;
  height: 100%;
  max-height: 70vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
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
