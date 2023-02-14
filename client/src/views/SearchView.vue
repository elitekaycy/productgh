<script lang="js">
import { useRoute } from 'vue-router'
import search1 from '../assets/image/search1.png'
import router from '../router/index'
import ProfileCardSkeleton from '@/components/ProfileCardSkeleton.vue'
import ProfileCard from '../components/ProfileCard.vue'

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
            productList: []
        }
    },
    mounted() {
        const route = useRoute()
        console.log("route params are ", route.params)
        this.product = route.params.product
        this.loadMetaData(String(route.params.product))
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
                
                console.log("data is ", data)
                this.productList = data
                this.error = false
                this.loading = false
                console.log(this.productList)
                return
            })
            .catch(err => {
                this.error = true
                this.loading = false
                this.productList = []
                return
            })
        },
       clear(){ return this.product = '' },
       returnHome(){
        const router = useRoute()
        router.  
        return
       }
    }
    
}

</script>

<template>
    <main>
        <div class="search_bar_box_container">
            <!-- <font-awesome-icon class="item-active" icon="fa-sharp fa-regular fa-arrow-left" @click="returnHome" size="2x" inverse/> -->
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
                    <!-- <img :src="searchimg" alt="search logo" class="logo"/> -->
                </span>
                <span>
                    <font-awesome-icon icon="fa-bookmark" />
                </span>
            </span>
        </form>
        </div>

        <div class="main_box">
        <div class="info">
           showing search results for "<span>{{ product }}</span>"
        </div>
        
        <div v-if="loading" class="products_list_main">
            <div class="profileCard" v-for="(item, index) in [1,2,3,4,5,6,7,8]" :key="index">
                <ProfileCardSkeleton />
            </div>
        </div>
        <div v-if="!loading && productList.length > 0" class="products_list_main">
            <div v-for="(item, index) in productList" :key="index" class="product_list">
                <ProfileCard 
                :img="String(item?.img)" 
                :title="String(item?.title)"
                :price="String(item?.price)"
                :link="String(item?.link)"
                :location="String(item?.location)"
                :tag="String(item?.tag)"
                /> 
            </div>
        </div>
        </div>
        
    </main>

</template>

<style scoped>

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
    padding: 20px;
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
    justify-content:space-around;
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
    background-color: #F9F9F9;
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
    background-color: #FFC93C;

}

.search_bar_box:hover, .search_bar_box:focus {
  border: 3px solid #362FD9;
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
    padding: 20px;
}

</style>