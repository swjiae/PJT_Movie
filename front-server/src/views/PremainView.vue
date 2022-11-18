<template>
    <div class="background">
        <!-- <h1>PremainView</h1> -->
        <navbarView/>
    </div>
    
</template>


<script>
import navbarView from '@/components/navbarView.vue'

export default {
  name: 'PremainView',
  components: {
    navbarView,
  }
}
</script>

<style>
.background {
    background-image: url("../assets/Dee-dum.webp");
    height: 90vh;
    overflow: hidden;
    background-repeat: no-repeat;
    background-size: 100%;
}
</style>