<style scoped>
 @import '../assets/style/main.css';

</style>
<template>
          <div style="height: 100%;">
            <Content class="layout-Content" >
                <div>
                    <span v-html="htmlData">
                    </span>
                </div>
            </Content>
          </div>
    
</template>


<script>

import axios from 'axios'
export default {
    data () {
        return {
            articleID : -1,
            htmlData :null
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
                this.htmlData = response.data
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