<script lang="js">

</script>

<template>
<div class="product_lists"> 
                <div class="item_image_box">
                    <div class="item_image" alt="item image"></div>
                </div>
                <div class="product_content">
                    <div class="product_meta">
                        <div class="product_title"></div>
                        <div class="product_price"></div>
                    </div>
                    <div class="product_link">
                        <div class="product_a_link"></div>
                        <div class="product_a_link"></div>
                        <div class="product_a_link"></div>
                    </div>
                    <div class="product_location"></div>

                </div>
            </div>
</template>

<style scoped>
.product_content {
    padding: 15px;
    margin-top: 5px;
    height: 200px;
}
.product_meta {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.product_a_link {
width: 100%;
padding: 8px;
border-radius: 10px;
height: 10px;
background-color: #F5F5F5;
margin-bottom: 8px;
}

.product_link {
    width: 100%;
    padding-top: 25px;

}

.product_price {
    width: 100%;
    max-width: 90px;
    background-color: #F5F5F5;
    padding: 10px;
    height: 30px;
    border-radius: 7px;
}

.product_location {
    margin-top: 16px;
    width: 100%;
    max-width: 150px;
    background-color: #F5F5F5;
    padding: 5px;
    height: 20px;
    border-radius: 10px;
}

.product_title {
    width: 100%;
    max-width: 120px;
    background-color: #F5F5F5;
    padding: 10px;
    height: 30px;
    border-radius: 7px;

}
.item_image_box {
    border-radius: 15px;
    background-color: #F5F5F5;
    width: 100%;
    height: 300px;
    display: flex;
    place-content: center;
}
.item_image {
    width: 100%;
    height: 100%;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.product_lists {
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    border-radius: 15px;
    max-width: 300px;
    width: 100%;
    margin: 0px;
    margin-top: 40px;
    
}
</style>