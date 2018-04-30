<style scoped>

.layout{
    border: 1px solid #d7dde4;
    background: #FFFFFF;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}

.layout-nav{
    width: 120px;
    margin: 0 auto;
    margin-right: 20px;
    
}
.layout-footer-center{
    text-align: center;
    margin-top:2em;
}
.layout-Content{
    width:740px;
    height: 700px;
    margin:0 auto;
    background: #ffffff;
    padding: 1px 100px;
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
.hr {
    height: 0;
    font-size: 1em;
    line-height: 0;
    text-transform: uppercase;
    text-align: center;
    border-bottom: 1px solid #A7ADBA;
    margin-top: 3em;
    margin-bottom: 1.2em;
    cursor: default;
    user-select: none;
}
.hr span {
    background-color: #fff;
    padding-left: .5em;
    padding-right: .5em;
    color: #A7ADBA;
}
.about_me{
    font-size: 14px;
    color:black;
}
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
                        <a href="/">About me</a>
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