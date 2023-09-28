<!-- Modal.vue -->
<template>
  <div class="fixed inset-0 flex items-center justify-center z-50">
    <div class="fixed inset-0 bg-black opacity-50 transition-opacity"></div>
    <!-- Dark background -->
    <div
      class="modal-container w-full max-w-[70vw] min-w-[700px] h-[90vh] overflow-scroll bg-white p-6 shadow-lg rounded-lg transform scale-0 transition-transform"
    >
      <div class="modal-content w-full">
        <div>
          <div
            v-if="loading"
            class="text-center w-100 flex flex-col items-center p-4 loading"
          >
            <img :src="loader" alt="loadingAnimation" />
          </div>
        </div>

        <div v-if="productsArray.length > 0">
          <div class="flex flex-row gap-16 p-4">
            <!-- Use v-for to loop through the productsArray -->
            <div
              class="flex flex-row w-full"
              v-for="product in productsArray"
              :key="product.title"
            >
              <div class="max-w-sm w-full space-y-3">
                <div class="text-xs max-w-[500px] font-bold">
                  {{ product.title }}
                </div>
                <div class="">
                  <img
                    :src="product.img"
                    class="w-full max-h-[300px] h-full rounded-md gb"
                  />
                </div>

                <div class="space-y-1">
                  <div class="text-xs font-bold text-black">description</div>
                  <div
                    class="p-4 w-full h-auto bg-gray-100 text-dark rounded-md"
                  >
                    <div class="text-xs font-normal">
                      {{ product.description }}
                    </div>
                  </div>
                </div>

                <div
                  class="p-2 border-b-2 w-full border-gray-100 space-y-1 flex flex-col"
                >
                  <span class="font-bold text-black text-xs">seller</span>
                  <div class="font-medium text-sm text-gray-400">
                    {{ product.seller }}
                  </div>
                </div>

                <div
                  class="p-2 border-b-2 w-full border-gray-100 space-y-2 flex flex-col"
                >
                  <span class="font-bold text-black text-xs">views</span>
                  <div class="font-medium text-sm text-gray-400">
                    {{ product.views }}
                  </div>
                </div>

                <div
                  class="p-2 border-b-2 w-full border-gray-100 space-y-2 flex flex-col"
                >
                  <span class="font-bold text-black text-xs">ratings</span>
                  <div class="font-medium text-sm text-gray-400">
                    {{ product.get_ratings }}
                  </div>
                </div>

                <div class="max-w-sm w-full space-y-4 mt-2">
                  <div class="font-bold text-xs border-b-2 pb-2 border-b-gray-100">
                    Tags
                  </div>
                  <div
                    class="flex flex-col items-start justify-start bg-gray-50 p-2 rounded-md w-full max-w-sm gap-2 flex-wrap"
                  >
                    <div class="flex flex-row gap-2 items-center" v-for="(value, key) in product.types" :key="key">
                      <div class="text-xs font-bold">{{ key }}</div>
                      <div class="font-medium text-sm"> {{ value }}</div>
                    </div>
                  </div>
                </div>


                <div
                    class="p-2 border-b-2 w-full border-gray-100 space-y-2 flex flex-col"
                  >
                    <span class="font-bold text-black text-xs">location</span>
                    <div class="font-medium text-sm text-gray-400">
                      {{ product.location }}
                    </div>
                  </div>
              </div>

            </div>
          </div>
        </div>
      </div>
      <div class="modal-actions mt-4 text-right">
        <button
          @click="closeModal"
          class="px-4 py-2 bg-gray-400 hover:bg-gray-600 text-white rounded-lg"
        >
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import loader from "../assets/image/loader.gif";

export default {
  props: {
    products: Array,
  },
  data() {
    return {
      loading: false,
      productsArray: [],
      loader: loader,
    };
  },
  mounted() {
    this.loadCompareProducts();
  },

  methods: {
    // method to load data
    async loadCompareProducts() {
      this.loading = true;
      fetch(`http://127.0.0.1:5000/product/newProduct`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.products),
      })
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(
            "data from load compare products -> CompareModal.vue ",
            data
          );
          this.productsArray = data;
          this.loading = false;
        })
        .catch((err) => {
          console.warn("error on line 58 ", err);
          this.loading = false;
        });
    },
    closeModal() {
      this.$emit("close"); // Emit an event to close the modal
    },
  },
};
</script>

<style scoped>
/* Add your custom modal styles here */
.modal-container {
  transition: transform 0.3s ease-in-out; /* Smooth transition for scaling */
  transform: scale(1); /* Initially hidden */
}
</style>
