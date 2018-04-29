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
    height:700px;
}
.circle{
     width: 150px;    
     //margin-left: auto;
     //margin-right: auto;  
     height: 150px;      
     //background-color:red;      
     border-radius: 50%;      
     -moz-border-radius: 50%;      
     -webkit-border-radius: 50%;
     //left: 50%;
}
.img_div{
    width: 100px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 80px;  
}
</style>
<template>
    <div class="layout">
        <Layout>
          <div style="height: 1280px;">
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1" >
                    <div class="layout-nav">
                        <MenuItem name="4">
                            <Icon type="flash"></Icon>
                            Home
                        </MenuItem>
                    </div>
                </Menu>
            </Header>
            <Content :style="{padding: '0 100px'}">
                <div class="layout-Content">
                    <div class="img_div">
                        <img class = "circle" src="../assets/touxiang.png">
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