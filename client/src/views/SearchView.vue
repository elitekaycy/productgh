<script lang="js">
import { useRoute } from 'vue-router'
import search1 from '../assets/image/search1.png'
import loader from '../assets/image/loader.gif'
import router from '../router/index'
import ProfileCardSkeleton from '@/components/ProfileCardSkeleton.vue'
import ProfileCard from '../components/ProfileCard.vue'
import { useGetter } from '../composables/getterSetter'

export default {
    components: {
        ProfileCardSkeleton: ProfileCardSkeleton,
        ProfileCard: ProfileCard
    },
    data() {
        return {
            product: '',
            loading: true,
            error: false,
            input: true,
            searchimg: search1,
            loader: loader,
            productList: [],
            productListFilter: [],
            productSearch: "",
            isbookmark: false
        }
    },
    mounted() {
        const route = useRoute()
        console.log("route params are ", route.params)
        this.product = route.params.product
        this.loadMetaData(String(route.params.product))
        this.checkBookmark()
    },
    methods: {
         handleSearch(item) {
            const route = useRoute()
            if (item.length < 1) {
                console.log("stuck here...")
                return;
            }
            this.loadMetaData(item)
            router.push(`${String(item)}`)
            return
        },
        async loadMetaData(product){
            this.loading = true
            this.error = false
            console.log("running meta data", product)
            fetch(`http://127.0.0.1:5000/search?name=${product}`, {
                mode: 'cors',
                headers: {
                'Access-Control-Allow-Origin':'*'
                }
            }).then((response) =>{
                return response.json()
            })
            .then(data => {

                this.productList = data
                this.productListFilter = data
                this.error = false
                this.loading = false
                console.log(this.productList)
                return
            })
            .catch(err => {
                this.error = true
                this.loading = false
                this.productList = []
                this.productListFilter = []
                return
            })
        },
       clear(){ return this.product = '' },
       returnHome(){
        const router = useRoute()
        router.
        return
       },
       getFilteredProducts() {
            if (String(this.productSearch).length  <  1) {
                this.productListFilter = this.productList
                return
            }
            this.productListFilter = this.productList.filter(product => String(product?.title + product?.tag + product?.price).toLowerCase().includes(String(this.productSearch).toLowerCase()))
            return
            // this.productListFilter = productArray
            // return

         },
        checkBookmark() {
            const bookmarks =  useGetter('product_bookmark')
            if(bookmarks.length > 0) {
                this.isbookmark = true
            }
            else {
                this.isbookmark = false
            }
        }

    }

}
</script>

<template>
  <main class="flex flex-col w-screen min-h-screen font-montserrat">
    <!-- <div class="search_bar_box_container">
        <form class="search_bar_box" @submit.prevent="handleSearch(product)">
            <div class="header">
                <font-awesome-icon icon="fa-house-laptop" />
                <div class="header-text">Productsgh</div> 
                <div>|</div>
            </div>
            <input class="search_bar" type="text" v-model="product" placeholder="new product"/>

            <span class="options">
                <span v-if="product != ''" class="clear">
                    <font-awesome-icon icon="fa-solid fa-xmark" @click="clear" />
                </span>
                <span>
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                </span>
                <span>
                    <font-awesome-icon :class="{ 'bookmark-icon': isbookmark }" icon="fa-bookmark" />
                </span>
            </span>
        </form>
        </div> -->
    <div class="flex flex-col w-full relative p-10 items-center justify-center">
      <div
        class="sea rounded-full pr-5 items-center flex flex-row max-w-2xl w-full bg-yellow-100 z-50"
      >
        <input
          class="w-full bg-transparent h-full p-8 placeholder-gray-500 text-xl font-light focus:outline-none"
          type="text"
          v-model="product"
          placeholder="Enter search for new product"
        />
        <span v-if="product != ''" class="clear">
          <font-awesome-icon
            icon="fa-solid fa-xmark"
            size="2x"
            @click="clear"
          />
        </span>
      </div>
    </div>

    <div class="">
      <div
        v-if="loading"
        class="text-center w-100 flex flex-col items-center p-4 loading"
      >
        <img :src="loader" alt="loadingAnimation" />
      </div>

      <!-- <div class="filter-search-box">
        <div class="filter_input_box">
          <input
            class="filter_input"
            v-model="productSearch"
            v-on:input="getFilteredProducts"
            type="text"
            name="filter_search"
            placeholder="filter search results"
          />
          <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
        </div>
      </div> -->

      <div
        v-if="loading"
        class="flex flex-row items-center flex-wrap justify-center"
      >
        <div
          class="p-2 w-full md:max-w-md"
          v-for="(item, index) in [1, 2, 3, 4, 5, 6]"
          :key="index"
        >
          <ProfileCardSkeleton />
        </div>
      </div>
      <div
        v-if="!loading && productList.length > 0"
        class="flex flex-row items-center flex-wrap justify-center"
      >
        <div
          v-for="(item, index) in productListFilter"
          :key="index"
          class="p-2 w-full md:max-w-md"
        >
          <ProfileCard
            :img="String(item?.img)"
            :title="String(item?.title)"
            :price="String(item?.price)"
            :link="String(item?.link)"
            :location="String(item?.location)"
            :tag="String(item?.tag)"
            :id="String(index)"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap");

/* Apply Montserrat font to specific elements */
.font-montserrat {
  font-family: "Montserrat", sans-serif;
}

.searchLength {
  font-size: 10px;
  font-weight: lighter;
  background-color: #362fd9;
  color: white;
  padding: 8px;

  border-radius: 15px;
}
.bookmark-icon {
  color: #362fd9;
}
.filter_input {
  border: 0;
  width: 100%;
}

.filter_input:hover,
.filter_input:focus {
  outline: none;
}
.filter_input_box {
  background-color: white;
  padding: 2px;
  width: 100%;
  max-width: 200px;
  height: 100%;
  max-height: 50px;
  display: flex;
  flex-direction: row;
  align-items: center;
  border: 1px solid gray;
}
.filter_input_box:hover {
  border: 1px solid black;
}
.filter-search-box {
  display: flex;
  height: auto;
  width: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
  padding-right: 60px;
}
.loading {
  text-align: center;
}
.item-active {
  transform: scale(1.09, 1.09);
  transition: 100ms ease-in-out 100ms;
  cursor: pointer;
}

.options {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  padding: 2px;
  width: 100%;
  max-width: 70px;
}

.clear {
  cursor: pointer;
  margin-right: 4px;
}
.info {
  padding: 10px;
  font-weight: 400;
  font-size: x-large;
}

.info > span {
  font-weight: bolder;
}
.header {
  display: flex;
  padding: 3px;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-right: 2px;
}

.header-text {
  font-size: large;
  font-weight: bold;
  margin-left: 5px;
  margin-right: 5px;
}
.profileCard {
  width: 100%;
  max-width: 300px;
}

.products_list_main {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-around;
  padding: 10px;
}

.product_list {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  border-radius: 15px;
  max-width: 300px;
  width: 100%;
  margin: 0px;
  margin-top: 30px;
  z-index: 100;
  background-color: white;
}

/* .product_list:hover {
    transform: scale(1.1, 1.1);
    cursor: pointer;
    transition: 220ms ease-in-out;
} */

main {
  overflow: hidden;
  background-color: #f9f9f9;
  min-height: 100vh;
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
  transform: scale(0.8, 0.8);
}

.search_bar_box_container {
  padding: 15px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: #ffc93c;
}

.search_bar_box:hover,
.search_bar_box:focus {
  border: 3px solid #362fd9;
}
.search_bar {
  padding: 10px;
  width: 100%;
  height: 100%;
  border: none;
  font-size: large;
}

.search_bar:focus {
  outline: none;
}

.logo {
  width: 25px;
  height: 25px;
}

.logo:hover {
  transform: scale(1.09, 1.09);
}

.main_box {
  padding: 15px;
}
</style>
