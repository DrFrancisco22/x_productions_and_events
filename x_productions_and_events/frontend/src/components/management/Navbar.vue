<template>
<div id="">
  <nav class="navbar is-link" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <!-- <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a> -->
      </div>

      <div class="navbar-menu">

        <div class="navbar-start">
          <router-link :to="{ name: 'Management'}" class="navbar-item">
            Administración
          </router-link>
          <router-link target="_blank" :to="{ name: 'LandingPage'}" class="navbar-item">
            Página principal
          </router-link>
        </div>
      </div>

    </div>
  </nav>
</div>
</template>

<script>
export default {
  name: "Navbar",
}
</script>
<style lang="scss" scoped>
</style>
