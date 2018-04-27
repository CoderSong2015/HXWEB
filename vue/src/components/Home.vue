<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
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
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
.layout-footer-center{
    text-align: center;
}
</style>
<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo"></div>
                    <div class="layout-nav">
                        <MenuItem name="1">
                            <Icon type="ios-navigate"></Icon>
                            Item 1
                        </MenuItem>
                        <MenuItem name="2">
                            <Icon type="ios-keypad"></Icon>
                            Item 2
                        </MenuItem>
                        <MenuItem name="3">
                            <Icon type="ios-analytics"></Icon>
                            Item 3
                        </MenuItem>
                        <MenuItem name="4">
                            <Icon type="ios-paper"></Icon>
                            Item 4
                        </MenuItem>
                    </div>
                </Menu>
            </Header>
            <Content :style="{padding: '0 50px'}">
                <Breadcrumb :style="{margin: '20px 0'}">
                    <BreadcrumbItem>Home</BreadcrumbItem>
                    <BreadcrumbItem>Components</BreadcrumbItem>
                    <BreadcrumbItem>Layout</BreadcrumbItem>
                </Breadcrumb>
                <Card>
                    <div style="min-height: 200px;">
                        Content
                    </div>
                </Card>
            </Content>
            <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
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