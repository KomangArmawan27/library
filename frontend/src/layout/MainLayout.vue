<template>
    <div class="flex h-screen">
      <Sidebar />
      <div class="flex-1 p-6">
        <slot />
      </div>
    </div>
  </template>
  
  <script>
  import Sidebar from "../components/Sidebar.vue";
  
  export default {
    components: { Sidebar },
  };
  </script>
  