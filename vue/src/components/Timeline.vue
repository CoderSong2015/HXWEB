<style scoped>
    .time{
        font-size: 14px;
        font-weight: bold;
    }
    .content{
        padding-left: 5px;
    }
    .div{

    }
    .layout-Content{
        width:740px;
        height: 700px;
        margin:0 auto;
        background: #ffffff;
        padding: 1px 100px;
    }
</style>
<template>
    <div style="height: 100%;">
        <Content class="layout-Content" >
            <Timeline>
                <TimelineItem>
                    <p class="time">1994年8月</p>
                    <p class="content">宋昊霖 问世</p>
                </TimelineItem>
                <TimelineItem>
                    <p class="time">2014年9月</p>
                    <p class="content">遇见我的HX</p>
                </TimelineItem>
                <TimelineItem>
                    <p class="time">2016年7月1号</p>
                    <p class="content">HX升级为我的产品经理</p>
                </TimelineItem>
                <TimelineItem>
                    <p class="time">2016年10月</p>
                    <p class="content">进入Oracle深造</p>
                </TimelineItem>
                <TimelineItem>
                    <p class="time">2017年6月</p>
                    <p class="content">发布 Haolin 1.0</p>
                </TimelineItem>
                <TimelineItem color = "red">
                    <p class="time">至今</p>
                    <p class="content">Esgyn 打磨产品</p>
                </TimelineItem>
            </Timeline> 
        </Content>
    </div>
</template>
<script>
    export default {
        
    }
</script>
