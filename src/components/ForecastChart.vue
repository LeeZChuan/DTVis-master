<template>
  <div id="app">
    <div id="ForecastChart" style="width: 800px;height:600px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//ForecastChart (预测视图，分为整体预测柱状图，订单具体细化预测花型散点图）用于展示海口市订单整体分布情况
//尚未完成
var echarts = require("echarts/lib/echarts");


export default {
  name: "ForecastChart",
  data() {
    return {
      ThreeDhotChart: "",
      hotChartOption: {}
    };
  },
  components: {},
  computed: {},
  mounted() {
    //页面初始化函数
    this.drawForecastChart();
  },
  methods: {
    drawForecastChart(){
      let myYuce = echarts.init(document.getElementById('ForecastChart'));
      var geoCoordMap = {
        //预测地点具体坐标情况
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


    function yuceFun(yuceVal) {
        var dataFile_shangchang = new Array();                                                                           // 商场数据读取
        $.ajax({
            url: 'data/yuce/shangchang/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_shangchang = data;
            }
        })

        var dataFile_fushuyiyuan = new Array();                                                                          // 附属医院数据读取
        $.ajax({
            url: 'data/yuce/yiyuan_fushu/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_fushuyiyuan = data;
            }
        })

        var dataFile_chezhan = new Array();                                                                              // 车站数据读取
        $.ajax({
            url: 'data/yuce/chezhan/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_chezhan = data;
                console.log(dataFile_chezhan)
            }
        })

        var dataFile_guangchang = new Array();                                                                           // 明珠广场数据读取
        $.ajax({
            url: 'data/yuce/guangchang/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_guangchang = data;
            }
        })

        var dataFile_zhengfu = new Array();                                                                              // 政府数据读取
        $.ajax({
            url: 'data/yuce/zhengfu/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_zhengfu = data;
            }
        })

        var dataFile_daxue = new Array();                                                                                // 大学数据读取
        $.ajax({
            url: 'data/yuce/daxue/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_daxue = data;
            }
        })

        var dataFile_youyi = new Array();                                                                                // 友谊商城数据读取
        $.ajax({
            url: 'data/yuce/youyi/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_youyi = data;
            }
        })

        var dataFile_jiudian = new Array();                                                                              // 酒店数据读取
        $.ajax({
            url: 'data/yuce/jiudian/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_jiudian = data;
            }
        })

        var dataFile_renmin = new Array();                                                                               // 人民医院数据读取
        $.ajax({
            url: 'data/yuce/renmin/' + yuceVal + '.json',
            async: false,
            success: function (data) {
                dataFile_renmin = data;
            }
        })

        function getParamValues(name, dataFile) {
            var ret = [];
            for (var i = 0, len = dataFile.length; i < len; i++) {
                ret.push(dataFile[i][name])
            }
            return ret
        }

        var valueTest = [
            { name: 'Market', value: getParamValues('proVal', dataFile_shangchang).map(Number) },
            { name: 'Hospital1', value: getParamValues('proVal', dataFile_fushuyiyuan).map(Number) },
            { name: 'Station', value: getParamValues('proVal', dataFile_chezhan).map(Number) },
            { name: 'Square', value: getParamValues('proVal', dataFile_guangchang).map(Number) },
            { name: 'Government', value: getParamValues('proVal', dataFile_zhengfu).map(Number) },
            { name: 'University', value: getParamValues('proVal', dataFile_daxue).map(Number) },
            { name: 'Friendship', value: getParamValues('proVal', dataFile_youyi).map(Number) },
            { name: 'Hotal', value: getParamValues('proVal', dataFile_jiudian).map(Number) },
            { name: 'Hospital2', value: getParamValues('proVal', dataFile_renmin).map(Number) }
        ];

        var convertData = function (data) {
            var res = [];
            var resArr = [];
            for (var i = 0; i < 24; i++) {
                for (var j = 0; j < data.length; j++) {
                    var geoCoord = geoCoordMap[data[j].name];
                    console.log(geoCoordMap[0])
                    res.push(geoCoord.concat(data[j].value[i]));
                }
            }
            for (var k = 0; k < res.length; k += 9) {
                resArr.push(res.slice(k, k + 9))
            }
            return resArr;
        };

        var convert = new Object();
        convert = convertData(valueTest);
        var optionYuceDitu = {
            baseOption: {
                title: {
                    text: "海口市区域订单预测",
                    left: 'center',
                    top: 20,
                    textStyle: {
                        color: '#cdddf7',
                        fontSize: 20
                    },
                    subtextStyle: {
                        color: 'white',
                        fontSize: 16
                    }
                },
                timeline: {
                    autoPlay: true,
                    data: ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
                    axisType: 'category',
                    padding: [5, 5, 5, 5],
                    playInterval: 2000,
                    lineStyle: { color: 'white' },
                    label: {
                        normal: {
                            textStyle: {
                                color: 'white',
                                fontSize: 13
                            }
                        }
                    }
                },
                tooltip: {
                    trigger: 'item',
                    position: 'top',
                    formatter: function (item) {
                        // if(item.data[2]>=300 && item.data[0]===110.3419978414701){
                        //     alert("明珠广场车流预警");
                        // }
                        // if(item.data[2]>=300 && item.data[0]===110.32354199623335){
                        //     alert("商场车流预警");
                        // }
                        // if(item.data[2]>=300 && item.data[0]===110.33388648979098){
                        //     alert("附属医院车流预警");
                        // }
                        // if(item.data[2]>=300 && item.data[0]===110.3486952530797){
                        //     alert("海南省政府车流预警");
                        // }
                        // if(item.data[2]>=300 && item.data[0]===110.34134652693201){
                        //     alert("海南师范大学车流预警");
                        // }
                        // return '预测车流量：'+ '\r\n'+ Math.round(item.data[2]);
                    }
                },
                amap: {                                                                                                 // 高德地图支持的初始化地图配置
                    center: [110.33835483551025, 20.01096791722277],                                                    // 高德地图初始中心经纬度
                    zoom: 13.3,                                                                                         // 高德地图初始缩放级别
                    resizeEnable: true,                                                                                 // 是否开启resize
                    mapStyle: "amap://styles/grey",                                                                     // 自定义地图样式主题
                    echartsLayerZIndex: 2019,                                                                           // 高德地图自定义EchartsLayer的zIndex，默认2000
                    // 说明：如果想要添加卫星、路网等图层
                    // 暂时先不要使用layers配置，因为存在Bug
                    // 建议使用amap.add的方式，使用方式参见最下方代码
                    viewMode: '3D',                                                                                     //开启3D视图,默认为关闭
                    buildingAnimation: true,                                                                            //楼块出现是否带动画
                },
                visualMap: {
                    min: 0,
                    max: 400,
                    splitNumber: 4,
                    inRange: {
                        color: ['rgba(154,255,194,0.5)', 'rgba(41,255,26,0.5)', 'rgba(255,112,11,0.5)', 'rgba(166,0,0,0.5)']
                    },
                    textStyle: {
                        color: '#fff'
                    },
                    bottom: 30
                },
                series: [{
                    name: '预测',
                    type: 'effectScatter',
                    coordinateSystem: 'amap',
                    showEffectOn: 'render',
                    rippleEffect: {
                        brushType: 'stroke'
                    },
                    hoverAnimation: true,
                    label: {
                        normal: {
                            formatter: '{b}',
                            position: 'right',
                            show: true
                        }
                    },
                    itemStyle: {
                        opacity: '0.6'
                    },
                    symbolSize: function (val) {
                        if (val[2] <= 30)
                            return Math.round(val[2]);
                        else return Math.round(val[2] / 3);
                    }
                },
                ]

            },
            options: []
        };

        var faultByHourIndex = []
        var faultByHourTime = setInterval(function () {
            myYuce.dispatchAction({                                                                                     //使得tootip每隔三秒自动显示
                type: 'showTip',                                                                                        // 根据 tooltip 的配置项显示提示框。
                seriesIndex: 0,
                dataIndex: faultByHourIndex % 9
            });
            faultByHourIndex++;
        }, 3000);
        for (var i = 0; i < 24; i++) {
            optionYuceDitu.options.push({
                series: [{ data: convert[i] }]
            })
        }
        myYuce.setOption(optionYuceDitu, true);
    }

    



    }

    
  },
};
</script>