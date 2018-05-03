<style scoped>
 @import '../assets/style/main.css';

</style>
<template>
          <div style="height: 100%;">
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
                <ul>
                    <li v-for="item in articleName">
                        <a :href=" item.url ">
                            <span>{{item.name}}</span>
                        </a>
                    </li>
                    
                </ul>          
            </Content>
          </div>
    
</template>


<script>

import axios from 'axios'
export default {
    data () {
        return {
            articleName: [{'name':'song','url':'about'},{'name':'test','url':'/'}]
        }
    },

    methods: {
    
    },

    created () {
    
    }

}

</script>