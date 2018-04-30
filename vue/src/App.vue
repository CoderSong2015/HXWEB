<style scoped>
 @import 'assets/style/main.css';

</style>

<template>
  <div id="app">
    <header>
            <div class = "head">
                <img class = "circle" src="./assets/touxiang2.jpg">
                <p class = "name">Leo Song</p>
                <p class = "desc">Software Engineer. Blogging about life and tech.</p>
            </div>
            <nav>
                <ul class="nav">
                    <li class="nav-item">
                        <a  href="/" >Blog</a>
                    </li>
                    <li class="nav-item">
                        <a href="/">Timeline</a>
                    </li>
                    <li class="nav-item">
                        <a href="/about">About me</a>
                    </li>
                </ul>
            </nav>
      </header>
            
    <router-view/>
    <Footer class="layout-footer-center">2015-2018 &copy; Leo's Blog</Footer>
  </div>
 
</template>

<script>
export default {
  name: 'App'
}
</script>


