<template>
  <div id="app">
    <div class="top">
      <Nav>Nav</Nav>
      <div></div>

    
  </div>
</template>



<script>
import Tadpole from './components/Tadpole/Tadpole chart.vue'//蝌蚪图
import Forecast from'./components/Forecast/Forecast.vue'//预测界面
import HeatMap from'./components/3Dhot/3Dhot chart.vue'//热力图界面

export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
