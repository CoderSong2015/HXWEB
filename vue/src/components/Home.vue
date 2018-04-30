<style scoped>
 @import '../assets/style/main.css'

</style>
<template>
    <div class="layout">
        <Layout class="layout">
          <div style="height: 100%;">
            <header>
            <div class = "head">
                <img class = "circle" src="../assets/touxiang2.jpg">
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
            
                
           
            <Content class="layout-Content" >
                <h2 class="hr">
                    <span>About Me</span>
                </h2>   
                <p class="about_me">
                    My name is Leo Song(宋昊霖). I was born in 1994. I used C/C++, Java, Python and Go. Now I focus on
                    distributed database development and currently work at <b>Esgyn.inc</b>
                </p>
                <h2 class="hr">
                    <span>Posts</span>
                </h2>           
            </Content>
            <Footer class="layout-footer-center">2015-2018 &copy; Leo's Blog</Footer>
          </div>
        </Layout>
    </div>
</template>


<script>

import axios from 'axios'
export default {
data () {
return {
    single: true,
    randomNumber: 0
}
},

methods: {
    getRandomInt (min, max) {
        min = Math.ceil(min) 
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min + 1)) + min
    },

    getRandom () {
    //this.randomNumber = this.getRandomInt(1, 100)
        this.randomNumber = this.getRandomFromBackend()
    },
    
    getRandomFromBackend(){
        const path = 'http://localhost:5000/api/random'
        axios.get(path)
        .then(
          response => {
            this.randomNumber = response.data.randomNumber 
          })
          .catch(
            error => {
              console.log(error)
            }
          )
    }

},

created () {
this.getRandom()
}

}

</script>