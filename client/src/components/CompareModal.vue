<!-- Modal.vue -->
<template>
     <div class="fixed inset-0 flex items-center justify-center z-50">
    <div class="fixed inset-0 bg-black opacity-50 transition-opacity"></div> <!-- Dark background -->
    <div class="modal-container bg-white w-4/5 lg:w-3/5 h-4/5 lg:h-3/5 p-6 shadow-lg rounded-lg transform scale-0 transition-transform">
      <div class="modal-content">
        <!-- Your modal content goes here -->
        {{ JSON.stringify(products) }}
        <slot></slot>
      </div>
      <div class="modal-actions mt-4 text-right">
        <button @click="closeModal" class="px-4 py-2 bg-gray-400 hover:bg-gray-600 text-white rounded-lg">Close</button>
      </div>
    </div>
  </div>
</template>
  
  <script>
  export default {
    props: {
        products: Array
    },
    methods: {
      closeModal() {
        this.$emit('close'); // Emit an event to close the modal
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your custom modal styles here */
  .modal-container {
  transition: transform 0.3s ease-in-out; /* Smooth transition for scaling */
  transform: scale(1); /* Initially hidden */
}

  </style>
  