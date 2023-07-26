<script lang="js">
import search1 from '../assets/image/search1.png'
import human4 from '../assets/image/human4.png'
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
      if (typeof (item) === "string" && item.length > 0) {
        console.log(item, typeof (item))
        this.setRecent(item)
        router.push(`productsearch/${String(item)}`)
      }
      else {
        alert("empty item")
      }
    },
    setRecent(item) {
      const recentData = localStorage.getItem('productgh_recent')

      if (recentData === null || typeof (recentData) === 'undefined') {
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
      else {
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
  <main class="w-screen min-h-screen bg-gray-100 font-montserrat">
    <div
      class="navbar w-full p-8 flex flex-row items-center justify-between bg-yellow-100"
    >
      <div class="tracking-tighter font-bold md:text-2xl text-xl">
        Productgh
      </div>
    </div>
    <div
      class="w-full flex flex-row items-center justify-center space-x-8 bg-yellow-100 p-12"
    >
      <div class="flex flex-col space-y-4">
        <div
          class="md:text-5xl text-2xl font-medium tracking-wide max-w-2xl w-full leading-9 md:text-left text-center md:leading-snug md:pl-4"
        >
          Search and browse best ecommerce
          <span class="bg-orange-200 font-semibold p-2 pl-4 pr-4 rounded-full"
            >products</span
          >
          deals in ghana
        </div>
        <div>
          <form
            class="search_bar_box focus:border-2 focus:border-yellow-100 hover:border-2 hover:border-orange-300 transition ease-in duration-200"
            @submit.prevent="handleSearch(product)"
          >
            <input
              class="search_bar"
              v-model="product"
              placeholder="enter product to search for"
            />
            <span @click.prevent="handleSearch(product)">
              <img :src="searchimg" alt="search logo" class="logo" />
            </span>
          </form>
        </div>
      </div>
      <div class="md:flex hidden">
        <img alt="human" :src="humann" class="human" />
      </div>
    </div>

    <div
      class="w-full bg-gray-100 p-10 flex flex-col lg:flex-row flex-wrap items-center justify-center lg:space-y-0 space-y-8"
    >
      <div class="lg:p-4">
        <div
          class="bg-white p-6 rounded-xl space-y-4 w-full lg:max-w-md cursor-pointer transition duration-150 ease-in hover:text-orange-300 scale-100 hover:scale-105"
        >
          <div class="font-semibold text-xl md:text-2xl tracking-wide">
            For reviewers
          </div>
          <div class="font-medium text-md md:text-xl leading-7 md:leading-8">
            Incididunt irure id et commodo deserunt consectetur anim.Elit ipsum
            minim in ea Lorem velit irure adipisicing veniam culpa ipsum in.
          </div>
        </div>
      </div>

      <div class="lg:p-4">
        <div
          class="bg-white p-6 rounded-xl space-y-4 w-full lg:max-w-md cursor-pointer transition duration-150 ease-in hover:text-orange-300 scale-100 hover:scale-105"
        >
          <div class="font-semibold text-xl md:text-2xl tracking-wide">
            For Business
          </div>
          <div class="font-medium text-md md:text-xl leading-7 md:leading-8">
            Incididunt irure id et commodo deserunt consectetur anim.Elit ipsum
            minim in ea Lorem velit irure adipisicing veniam culpa ipsum in.
          </div>
        </div>
      </div>

      <div class="lg:p-4">
        <div
          class="bg-white p-6 rounded-xl space-y-4 w-full lg:max-w-md cursor-pointer transition duration-150 ease-in hover:text-orange-300 scale-100 hover:scale-105"
        >
          <div class="font-semibold text-xl md:text-2xl tracking-wide">
            Help & Support
          </div>
          <div class="font-medium text-md md:text-xl leading-7 md:leading-8">
            Incididunt irure id et commodo deserunt consectetur anim.Elit ipsum
            minim in ea Lorem velit irure adipisicing veniam culpa ipsum in.
          </div>
        </div>
      </div>
    </div>

    <!--creators-->
    <!-- <div
      class="flex flex-row items-center bg-yellow-100 rounded-t-lg p-8 justify-between w-full"
    >
      <div class="tracking-tighter text-md font-semibold">Productgh</div>
    </div> -->
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap");

/* Apply Montserrat font to specific elements */
.font-montserrat {
  font-family: "Montserrat", sans-serif;
}

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
  background-color: #ffc93c;
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
  padding: 15px;
}

/* .search_bar_box:hover,
.search_bar_box:focus {
  border: 3px solid #362fd9;
} */

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
  color: #ececec;
}

.logo {
  width: 25px;
  height: 25px;
}

.logo:hover {
  transform: scale(1.09, 1.09);
}
</style>
