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
                    <li v-for="item in articleInfo">
                         
                        <router-link :to="{ name: 'article', params: { articleId: item.id }}">{{ item.name }}</router-link>
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
            articleInfo: [{ 'name':'song',id:1},{'name':'test',id:2}]
        }
    },

    methods: {
        select(event) {
            console.log(event.currentTarget);
            console.log(event.target);
        },
        getArticleInfo() {
            const path = 'http://localhost:5000/api/articleInfo'
            axios.get(path)
            .then(
                response => {
                this.articleInfo = response.data
                console.log(this.articleInfo)
            })
            .catch(
                error => {
                    console.log(error)
                }
            )
        }
    },

    created () {
        this.getArticleInfo(),
        console.log(this.$route)
    }

}

</script>