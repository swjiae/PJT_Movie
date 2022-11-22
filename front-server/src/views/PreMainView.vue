<template>
    <div class="background">
        <h1>TWEEDLES</h1>
        <NavBarView/>
        <img src="@/assets/tt.png">
    </div>
    
</template>


<script>
import NavBarView from '@/components/NavBarView'
export default {
  name: 'PreMainView',
  components: {
    NavBarView,
  }
}
</script>

<style>
/* .background {
    background-image: url("../assets/Dee-dum.webp");
    height: 90vh;
    overflow: hidden;
    background-repeat: no-repeat;
    background-size: 100%;
} */
</style>


