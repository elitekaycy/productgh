<script lang="js">
import { useRoute } from 'vue-router';
import router from '../router';
import { useSetter, deleteSetter } from '../composables/getterSetter'
import loader from '../assets/image/loader.gif'

export default {
    name: 'ProfileCard',
    props: {
        img: String,
        title: String,
        price: String,
        link: String,
        location: String,
        tag: String,
        tagName: String
    },
    data() {
        return {
            active: false,
            randomColorClass: "bg-gradient-to-br from-green-100 via-blue-200 to-purple-300",
            showMore: false,
            detail: {},
            loader: loader,
            loadingDetail: false
        }
    },

      watch: {
      // Watch the 'showMore' property
      showMore(newShowMoreValue) {
        if (newShowMoreValue) {
          // When 'showMore' becomes true, call the 'fetchDetail' function
          this.fetchDetail();
        }
      },
    },

    methods: {
        checkBookmark(data) {
            console.log("check bookmark is called ", data)
            if (this.active === false) {
                useSetter(data, 'product_bookmark', 7)
            }
            else {
                deleteSetter(data, 'product_bookmark')
            }

            this.active = !this.active
            return
        },

        async redirectToLinkUrl(){
          console.log("requst body ", JSON.stringify(this.title))
          fetch(`http://127.0.0.1:5000/update`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                  },
                body: JSON.stringify({
                  title: this.title
                }),
             }).then(response => {
                  return response.json()
                })
                .then(data => {
                  console.log("data is ", data)
                  window.location.href = this.link
                })
                .catch(err => {
                  console.warn("error on line 50 ", err)
                })

        },
        async fetchDetail() {
          this.loadingDetail = true
          fetch(`http://127.0.0.1:5000/product/newProduct`,{
            method: 'POST',
            headers: {
                    'Content-Type': 'application/json',
                  },
            body: JSON.stringify([
              {
                "tag": this.tagName,
                "link": this.link
              }
            ]),
          })
          .then(response => {
            return response.json()
          })
          .then(data =>  {
            console.log("data from a single product ", data)
            this.detail = data[0]
            this.loadingDetail = false
          })
          .catch(err => {
            console.warn("error on line 76 ", err)
            this.loadingDetail = false
          })

        },
         toggleValue() {
           // Toggle the value between true and false on click
           this.showMore = !this.showMore;
         },

    mounted() {
  },


    }

}
</script>

<template>
  <div
    :class="`rounded-md h-auto relative w-full ${randomColorClass} hover:scale-105 transition duration-200 cursor-pointer ease-in scale-100 ${
      showMore ? 'rounded-b-2xl' : ''
    }`"
  >
    <div :class="`p-8 overflow-hidden`">
      <div class="flex flex-row items-center justify-between">
        <div 
        @click="redirectToLinkUrl"
        class="w-72 font-semibold text-sm hover:text-blue-300">
          {{ title }}
        </div>
        <div class="font-semibold text-yellow-700 text-sm">GH₵ {{ price }}</div>
      </div>

      <div class="w-full h-64 overflow-hidden rounded-t-2xl rounded-b-2xl">
        <img
          :src="img"
          class="object w-full bottom-0 top-5 rounded-t-2xl h-full hover:scale-110 transition duration-300 ease-in scale-100"
          alt="item image"
        />
      </div>
    </div>
    <div
      @click="toggleValue"
      class="bg-gray-800 text-dark flex flex-row items-center justify-between p-2 px-5 h-20 w-full z-20 rounded-t-2xl"
    >
      <div class="text-white font-bold text-xs">{{ tagName }}</div>
      <div
        class="p-2 bg-gray-600 rounded-full text-white text-xs transform scale-90 font-bold"
      >
        more
      </div>
    </div>

    <div
      v-if="showMore"
      class="z-80 w-full h-64 rounded-b-2xl px-6 pt-2 bg-gray-800 transition ease-in-out duration-200"
    >

    <div
        v-if="loadingDetail"
        class="text-center w-100 flex flex-col items-center p-4 loading"
      >
        <img :src="loader" alt="loadingAnimation" />
      </div>

    <div v-if="!loadingDetail" class="flex flex-row items-center gap-2">
      <span class="text-gray-300 text-xs font-medium">ratings</span>
      <span class="text-white font-medium text-lg">{{ detail['get_ratings'] }}</span>
    </div>

    <div v-if="!loadingDetail" class="flex flex-row items-center gap-2">
      <span class="text-gray-300 text-xs font-medium">views</span>
      <span class="text-white font-medium text-lg">{{ detail['views'] }}</span>
    </div>
  
    <div v-if="!loadingDetail" class="flex flex-row items-center gap-2">
      <span class="text-gray-300 text-xs font-medium">seller</span>
      <span class="text-white font-medium text-lg">{{ detail['seller'] }}</span>
    </div>

    <div v-if="!loadingDetail" class="p-4 mt-4 rounded-md gap-2 bg-gray-700">
      <span class="text-gray-300 text-xs font-medium">description</span>
      <div class="text-xs text-white max-h-[50px] overflow-hidden">
        {{ detail['description'] }}
      </div>

    </div>
  
  
  
  </div>
  </div>
</template>

<style scoped>
.bookmark-icon {
  color: #2192ff;
}

.product_fav:hover {
  transform: scale(1.09, 1.09);
}
.product_fav {
  transition: 100ms ease-in-out 100ms;
  position: absolute;
  cursor: pointer;
  z-index: 100;
  margin-left: 70%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  padding: 10px;
  background-color: white;
  border-radius: 100%;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}
.product_tag {
  font-weight: bold;
  line-height: -10px;
  word-spacing: -1px;
  letter-spacing: -0.5px;
  font-size: small;
}
.product_content {
  padding: 15px;
  margin-top: 5px;
  background-color: white;
}
.product_meta {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.footer-text {
  font-weight: bold;
  color: white;
  cursor: pointer;
}
.footer-text:hover {
  text-decoration: underline;
  background-color: #2192ff;
}
.footer {
  padding: 20px;
  background-color: #2192ff;
  color: white;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.product_link {
  display: inline;
}
.product_price {
  font-weight: bolder;
  font-size: large;
  word-spacing: -1px;
}

.product_location {
  font-weight: 700;
  font-size: small;
}

.product_title {
  font-size: small;
  font-weight: 800;
  letter-spacing: -0.5px;
  font-family: Arial, Helvetica, sans-serif;
}
.item_image_box {
  border-radius: 15px;
  background-color: #f5f5f5;
  width: 100%;
  height: auto;
  max-height: 400px;
  display: flex;
  place-content: center;
}
.item_image {
  width: 100%;
  height: 100%;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.product_main {
  position: relative;
}
</style>
