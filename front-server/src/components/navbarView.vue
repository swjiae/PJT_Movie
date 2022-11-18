<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" >Tweedles</a>
        </div>
        <loginModal/>
    </nav>
  </div>
</template>

<script>
import loginModal from '@/components/loginModal.vue'
export default {
    name : 'navbarView',
    components: {
        loginModal,
    }

}
</script>

<style>

</style>