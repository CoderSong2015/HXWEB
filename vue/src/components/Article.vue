<style scoped>
 @import '../assets/style/main.css';

</style>
<template>
          <div style="height: 100%;">
            <Content class="layout-Content" >
                <div>
                    
                </div>
            </Content>
          </div>
    
</template>


<script>

import axios from 'axios'
export default {
    data () {
        return {
            articleInfo: [{ 'name':'song',id:1},{'name':'test',id:2}],
            articleID : -1
        }
    },

    methods: {
        getArticleInfo() {
            const path = 'http://localhost:5000/api/article'
            axios.get(path,{
                params:{
                        articleid: this.articleID
                }
            }
                
            )
            .then(
                response => {
                this.articleInfo = response.data.articleInfo 
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
        this.articleID = this.$route.params.articleId,
        this.getArticleInfo(),
        console.log(this.$route)
    }

}

</script>