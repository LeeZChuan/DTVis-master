<template>
  <div>
    <el-amap id="Chart" style="width: 980px; height: 400px;"></el-amap>
  </div>
</template>

<script>
import { lazyAmapApiLoaderInstanse } from "vue-amap";
var echarts = require("echarts");
export default {
  name: "Chart",
  data() {
    return {};
  },
  mounted() {
    this.drawChart();
    this.readata();
  },
  methods: {
    drawChart() {
      var geoCoordMap = [
        [110.34600449319761, 19.982437787047544],                                                          // 车站
        [110.34134652693201, 19.99932256358843],                                                           // 大学
        [110.3419978414701, 20.028707619877615],                                                           // 广场
        [110.3003359682968, 20.02209205730502],                                                            // 酒店
        [110.28733273053196, 20.004736626542677],                                                          // 医院
        [110.32354199623335, 20.02158601280024],                                                           // 商场
        [110.33388648979098, 20.029357312123295],                                                          // 附属医院
        [110.34064896567928, 20.039496528046975],                                                          // 友谊商城 
        [110.3486952530797, 20.01874102105557],                                                            // 政府  
      ];
      var colors = ['#9fd0d5','#f68e57','#eed5eb','#a65bc2','#9ecfd4','#f8ba7f','#a9e2cb','#eda3b8','#eff3b8'] // 颜色(需要修改)
      var rads = this.readata()
      var map = new AMap.Map("Chart", {
        viewMode: "3D",
        pitch: 0,//俯仰角度，默认0，[0,83]，2D地图下无效 。
        resizeEnable: true,//是否监控地图容器尺寸变化，默认值为false
        center: [110.32835483551025, 20.01996791722277],
        zoom: 13,
        mapStyle: "amap://styles/grey", // 自定义地图样式主题
        // echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
        buildingAnimation: true,
        rotateEnable:true,
        pitchEnable:true
      });

      // 构造矢量圆形 circles[] 9个地点
      
      console.log(rads)
      console.log(rads.points)
      // var t = rads.points.forEach(item =>{
      //   return item
      //   console.log(t)
      // });
      // console.log(rads.points.value)
      // console.log(rads.points.value[2])
      console.log(rads.points[2])
      // console.log(rads.points.forEach(v=>{v}))
      // console.log(parseInt(rads.points[i]))
      // console.log(geoCoordMap[5][0])
      var circles = []
      for(var i=0;i<=8;i++){
        //  console.log(rads.points)
          circles[i] = new AMap.Circle({
          // 数据读取
          center: new AMap.LngLat(geoCoordMap[i][0],geoCoordMap[i][1]), // 圆心位置
          // 半径 数据读取 
          radius: parseInt(rads.points[i]),//500,  
          strokeColor: colors[i],  //线颜色
          strokeOpacity: 0.5,  //线透明度
          strokeWeight: 1,  //线粗细度
          fillColor: colors[i],  //填充颜色
          fillOpacity: 0.5, //填充透明度
          // content: "<div class='info'>此处有问题，需要修改</div>"
        });
      } 
      // 添加覆盖物
      map.add(circles);
      var Opts = {
      };
      //初始化heatmap对象
      var thismap = new AMap.Map(map, Opts);
      //设置数据集
      thismap.setDataSet({
        data: rads.points,//thisData,   
        resizeEnable: true,
        max: 20
      });
    },
    readata(){
      // 读取的时间
      var data = "2017-05-13"
      var timeindex = "15";
      var name = ['Station','University','Square','Hotal','Hospital2','Market','Hospital1','Friendship','Government']
      var points = []
      // console.log("tempdata");
      for(var j=0;j<=8;j++){
        this.$axios.get("../../static/data/yuce/"+ name[j] +"/" + data + ".json").then(res => {
          // 从9个文件中读取数据：对应日期、地点和时间的 {} 对象，将其存入points数组
          var tempdata = res.data
          // console.log(tempdata);
          // points.push(tempdata[timeindex]);
          var radius = tempdata[timeindex].proVal
          points.push(radius);
          // points[j] = radius
        });
      }
      return{
        points
      }
    }
  }
}
</script>
<style>
 .info{
    position: relative;
    top: 0;
    right: 0;
    min-width: 0;
  }
</style>