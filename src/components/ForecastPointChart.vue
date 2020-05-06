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
  },
  methods: {
    drawChart() {
      // 读取的时间
      var data = "2017-05-13"
      var timeindex = "15";
      var name1 = ['chezhan','daxue','guangchang','jiudian','renmin','shangchang','yiyuan','youyi','zhengfu'] //yiyuan_fushu
      var name = ['Station','University','Square','Hotal','Hospital2','Market','Hospital1','Friendship','Government']
                // 坐标经纬度
          var geoCoordMap = {
              "Market": [110.32354199623335, 20.02158601280024],                                                              // 商场
              "Hospital1": [110.33388648979098, 20.029357312123295],                                                          // 附属医院
              "Station": [110.34600449319761, 19.982437787047544],                                                            // 车站
              "Square": [110.3419978414701, 20.028707619877615],                                                              // 广场
              "Government": [110.3486952530797, 20.01874102105557],                                                           // 政府
              "University": [110.34134652693201, 19.99932256358843],                                                           // 大学
              "Friendship": [110.34064896567928, 20.039496528046975],                                                          // 友谊商城
              "Hotal": [110.3003359682968, 20.02209205730502],                                                                 // 酒店
              "Hospital2": [110.28733273053196, 20.004736626542677]                                                            // 医院
          };
      // var geoCoordMap = [
      //       [110.32354199623335, 20.02158601280024],                                                           // 商场
      //       [110.33388648979098, 20.029357312123295],                                                          // 附属医院
      //       [110.34600449319761, 19.982437787047544],                                                          // 车站
      //       [110.3419978414701, 20.028707619877615],                                                           // 广场
      //       [110.3486952530797, 20.01874102105557],                                                            // 政府
      //       [110.34134652693201, 19.99932256358843],                                                           // 大学
      //       [110.34064896567928, 20.039496528046975],                                                          // 友谊商城
      //       [110.3003359682968, 20.02209205730502],                                                            // 酒店
      //       [110.28733273053196, 20.004736626542677]                                                           // 医院
      //     ];
      for(var j=0;j<=0;j++){
        this.$axios.get("../../static/data/yuce/"+ name1[j] +"/2017-05-13.json").then(res => {
          // chezhan
          points[j] = res.data[prasInt(timeindex)];
          });
      }

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
          /*** 添加内容
           * {时间 24h
           * 个数 traVal
           * 预测值 proVal}
           * ***/

          // 颜色(需要修改)
          var colors = ['#9fd0d5','#f68e57','#eed5eb','#a65bc2','#9ecfd4','#f8ba7f','#a9e2cb','#eda3b8','#eff3b8']
          // 构造矢量圆形
          var circles=[];
          for(var i=0;i<=0;i++){
              circles[i] = new AMap.Circle({
                center: new AMap.LngLat(geoCoordMap.get(nmae[i])[0],geoCoordMap.get(nmae[i])[1]), // 圆心位置
                radius: points[i].get('traVal'),//500,  //半径 
                strokeColor:  colors[i],  //线颜色
                strokeOpacity: 0.5,  //线透明度
                strokeWeight: 1,  //线粗细度
                fillColor: colors[i],  //填充颜色
                fillOpacity: 0.5, //填充透明度
                content: "<div class='info'>此处有问题，需要修改</div>"
            });
          } 

          // // 构造标记
          // var markers=[];
          // for (var i = 0;i<=8;i++) {
          //   markers[i] = new AMap.Marker({
          //     map: map,
          //     position: [geoCoordMap[i][0],geoCoordMap[i][1]],    
          //     offset: new AMap.Pixel(-13, -30),
          //     content: "<div class='info'>我是 marker 的 label 标签</div>"
          //   });
  
          // }
          // markers.push(markers);
          // //   markers.setLabel({
          // //       offset: new AMap.Pixel(20, 20),  //设置文本标注偏移量
          // //       content: "<div class='info'>我是 marker 的 label 标签</div>", //设置文本标注内容
          // //       direction: 'right' //设置文本标注方位
          // // });

          //3D罗盘控制添加
          AMap.plugin(["AMap.ControlBar"], function() {
            // 添加 3D 罗盘控制
            map.addControl(new AMap.ControlBar());
            map.add(circles);
          });

          var Opts = {
            //3d 相关的参数
            '3d': {
              //热度转高度的曲线控制参数，可以利用左侧的控制面板获取
              heightBezier: [0.465, 0.115, 0.8, 0.36],
              //取样精度，值越小，曲面效果越精细，但同时性能消耗越大
              gridSize: 2,
              heightScale: 1
            },
          };
          //初始化heatmap对象
          var thismap = new AMap.Map(map, Opts);
          //设置数据集
          thismap.setDataSet({
            data: thisData,   
            resizeEnable: true,
            max: 20
          });
        }
      }
    }
          // 坐标经纬度
          // var geoCoordMap = {
          //     "Market": [110.32354199623335, 20.02158601280024],                                                              // 商场
          //     "Hospital1": [110.33388648979098, 20.029357312123295],                                                          // 附属医院
          //     "Station": [110.34600449319761, 19.982437787047544],                                                            // 车站
          //     "Square": [110.3419978414701, 20.028707619877615],                                                              // 广场
          //     "Government": [110.3486952530797, 20.01874102105557],                                                           // 政府
          //     "University": [110.34134652693201, 19.99932256358843],                                                           // 大学
          //     "Friendship": [110.34064896567928, 20.039496528046975],                                                          // 友谊商城
          //     "Hotal": [110.3003359682968, 20.02209205730502],                                                                 // 酒店
          //     "Hospital2": [110.28733273053196, 20.004736626542677]                                                            // 医院
          // };
</script>
<style>
 .info{
    position: relative;
    top: 0;
    right: 0;
    min-width: 0;
  }
</style>