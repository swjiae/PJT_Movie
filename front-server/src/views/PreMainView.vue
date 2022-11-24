<template>
    <div class="background">
        <NavBarView
        class="row d-flex justify-content-center"
        />
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
</style>