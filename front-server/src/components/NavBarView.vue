<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" >Tweedles</a>
        </div>
        <SignUpView/>
        <LogInView/>
    </nav>
  </div>
</template>

<script>
import SignUpView from '@/components/SignUpView'
import LogInView from '@/components/LogInView'

export default {
    name: 'NavBarView',
    components: {
      SignUpView,
      LogInView
    },
}
</script>

<style>

</style>
