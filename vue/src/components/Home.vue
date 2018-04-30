<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #5b6270;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 120px;
    margin: 0 auto;
    margin-right: 20px;
    
}
.layout-footer-center{
    text-align: center;
}
.layout-Content{
    height:780px;
    background: #ffffff;
}
.header{
    
}
.circle{
     margin:0 auto;
     width: 128px;     
     height: 128px;       
     border-radius: 50%;
     margin-top: 6em;
}
.img_div{
    width: 70px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 50px;  
}
.head{
    text-align: center;
    background: #ffffff;

}
.name{
    font-family: -apple-system, BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;
    font-size: 16px;
    font-weight: bold;
    margin-top: 1em;
}
.desc{
    font-family: sans-serif;
    font-size: 14px;
    margin-top: 1em;
    opacity: .8;
}
nav {
    padding: 3em;
    background: #ffffff;
}

nav .nav{
    list-style-type: none;
    margin: 0;
    padding: 0;
    text-align: center;
}
nav .nav .nav-item{
    display: inline-block;
    background: #ffffff;
    list-style-type: none;
    margin: 0;
    padding: 0;
    font-size: 14px;
    margin-right: .5em
}
a {
    color:black;
    text-decoration: underline;
}
li {
    
    display: list-item;
    text-align: -webkit-match-parent;
}
</style>
<template>
    <div class="layout">
        <Layout>
          <div style="height: 100%;">
            <header>
            <div class = "head">
                <img class = "circle" src="../assets/touxiang2.jpg">
                <p class = "name">Leo Song</p>
                <p class = "desc">Software Engineer. Blogging about life and tech</p>
            </div>
            <nav>
                <ul class="nav">
                    <li class="nav-item">
                        <a  href="/" >Blog</a>
                    </li>
                    <li class="nav-item">
                        <a href="/">Timeline</a>
                    </li>
                </ul>
            </nav>
            </header>
            <Content class="layout-Content" :style="{padding: '1px 100px'}">
                <div >
                    <div class="img_div">
                        
                   </div>
                </div>
            </Content>
            <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
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