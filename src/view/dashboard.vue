<script>
//网页界面设计
import exp from '../components/exp.vue'
import Tadpole from '../components/Tadpole/Tadpole chart'//蝌蚪图
import Forecast from'../components/Forecast/Forecast'//预测界面
import HeatMap from'./components/3Dhot/3Dhot chart.vue'//热力图界面
import multiputeMap from'./components/multiputeMap.vue'//用于展示海口市地区订单情况散点雷达图
export default {
  components: {
    exp,
  },
};
</script>

<template>
    <exp></exp>
</template>