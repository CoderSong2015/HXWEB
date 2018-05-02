<template>
  <div id="app">
    <div>
    <p> About random number {{ randomNumber }}</p>
    </div>
    <div>
        <span v-html="htmlData">
        </span>
    </div>
  </div>
</template>



<script>

import axios from 'axios'
export default {
data () {
return {
    single: true,
    randomNumber: 0,
    htmlData:null,
}
},

methods: {
    getRandomInt (min, max) {
        min = Math.ceil(min) 
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getHtml(){
        this.htmlData = this.htmlTest()
    },
    getRandom () {
    //this.randomNumber = this.getRandomInt(1, 100)
        this.randomNumber = this.getRandomFromBackend()
    },
    htmlTest(){
        const path = 'http://localhost:5000/api/html'
        axios.get(path)
        .then(
          response => {
            this.htmlData = response.data;
            console.log("dsada " + response.data);
          })
          .catch(
            error => {
              console.log(error)
            }
          )
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
    this.getHtml()
}

}

</script>