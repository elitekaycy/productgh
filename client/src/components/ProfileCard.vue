<script lang="js">
import { useRoute } from 'vue-router';
import router from '../router';
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
    
  
}

</script>

<template>
    <div class="product_main">
         <div class="item_image_box">
                    <img :src="img" class="item_image" alt="item image"/>
                </div>
                <div class="product_content">
                    <div class="product_meta">
                        <div class="product_title">
                            {{ title }}
                        </div>

                        <div class="product_price">
                            ${{ price }}
                        </div>
                    </div>
                    <div class="product_link">
                       <a class="product_tag" :href="tag">{{ tag }}</a>
                    </div>
                    <!-- <div class="product_location">
                        {{ location }}
                    </div> -->
                    <div class="product_fav">
                        <font-awesome-icon icon="fa-bookmark" />
                    </div>
                </div>
                <div class="footer">
                    <a class="footer-text" :href="link">learn more</a>
                    <font-awesome-icon icon="fa-solid fa-chevron-right" />
                </div>
            </div>
</template>

<style scoped>
.product_fav {
    position: absolute;
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
    background-color: #2192FF;
}
.footer {
    padding: 20px;
    background-color: #2192FF;
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
    background-color: #F5F5F5;
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