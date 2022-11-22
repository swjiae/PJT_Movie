<template>
  <div>
    <div class="col-1">
      <LogInView/>
    </div>
    <div class="col-1">
      <SignUpView/>
    </div>
  </div>
</template>

<script>
import SignUpView from '@/components/SignUpView'
import LogInView from '@/components/LogInView'

  export default {
    name: 'NavBarView',
    components: {
      LogInView,
      SignUpView,
  }
  }
</script>