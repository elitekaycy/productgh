<script lang="js">
import { useRoute } from 'vue-router';
import router from '../router';
import { useSetter, deleteSetter } from '../composables/getterSetter'

export default {
    name: 'ProfileCard',
    props: {
        img: String,
        title: String,
        price: String,
        link: String,
        location: String,
        tag: String
    },
    data() {
        return {
            active: false,
            randomColorClass: "bg-gradient-to-br from-green-100 via-blue-200 to-purple-300",
        }
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

    mounted() {
  },


    }

}
</script>

<template>
  <div
    @click="redirectToLinkUrl"
    :class="`p-8 rounded-md h-96 relative w-full overflow-hidden ${randomColorClass} hover:scale-105 transition duration-200 cursor-pointer ease-in scale-100`"
  >
    <div class="flex flex-row items-center justify-between">
      <div class="w-72 font-semibold text-lg hover:text-blue-300">
        {{ title }}
      </div>
      <div class="font-semibold text-yellow-700 text-lg">$ {{ price }}</div>
    </div>
    <img
      :src="img"
      class="object w-full bottom-0 top-10 rounded-t-2xl h-full hover:scale-110 transition duration-300 ease-in scale-100"
      alt="item image"
    />
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
