<template>
    <div class="mt-4 flex justify-between items-center">
      <button 
        @click="$emit('change-page', prevPage)" 
        :disabled="!prevPage"
        class="px-4 py-2 bg-gray-300 rounded disabled:opacity-50"
      >
        Previous
      </button>
  
      <span>Page {{ currentPage }}</span>
  
      <button 
        @click="$emit('change-page', nextPage)" 
        :disabled="!nextPage"
        class="px-4 py-2 bg-gray-300 rounded disabled:opacity-50"
      >
        Next
      </button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      currentPage: Number,
      nextPage: Number,
      prevPage: Number,
    }
  };
  </script>
  