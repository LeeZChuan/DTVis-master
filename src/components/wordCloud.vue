<template>
  <div style="width: 1000px;height: 800px;">
    <div id="container"></div>
  </div>
</template>

<script>
import Highcharts from "highcharts/highcharts";
import wordcloud from "highcharts/modules/wordcloud";

wordcloud(Highcharts);

export default {
  name: "wordCloud",
  data() {
    return {
      wordCloudData: [
        { id: 0, content: "琼山区云龙镇" },
        { id: 1, content: "琼山区凤翔街道" },
        { id: 2, content: "琼山区国兴街道" },
        { id: 3, content: "琼山区府城街道" },
        { id: 4, content: "琼山区旧州镇" },
        { id: 5, content: "琼山区滨江街道" },
        { id: 6, content: "琼山区滨江街道琼山区府城镇" },
        { id: 7, content: "琼山区龙塘镇" },
        { id: 8, content: "秀英区丘海大道" },
        { id: 9, content: "秀英区东山镇" },
        { id: 10, content: "秀英区永兴镇" },
        { id: 11, content: "秀英区海秀街道" },
        { id: 12, content: "秀英区海秀镇" },
        { id: 13, content: "秀英区白水塘路" },
        { id: 14, content: "秀英区石山镇" },
        { id: 15, content: "秀英区秀英街道" },
        { id: 16, content: "秀英区秀英街道苏南村镇" },
        { id: 17, content: "秀英区西秀镇" },
        { id: 18, content: "秀英区长流镇" },
        { id: 19, content: "美兰区三江镇" },
        { id: 20, content: "美兰区人民路街道" },
        { id: 21, content: "美兰区博爱南路" },
        { id: 22, content: "美兰区博爱街道" },
        { id: 23, content: "美兰区和平南街道" },
        { id: 24, content: "美兰区国营桂林洋农场" },
        { id: 25, content: "美兰区新埠街道" },
        { id: 26, content: "美兰区新民西路" },
        { id: 27, content: "美兰区海府街道" },
        { id: 28, content: "美兰区海甸街道" },
        { id: 29, content: "美兰区海秀东路" },
        { id: 30, content: "美兰区演丰镇" },
        { id: 31, content: "美兰区灵山镇" },
        { id: 32, content: "美兰区白沙街道" },
        { id: 33, content: "美兰区白沙街道板桥横路东园镇" },
        { id: 34, content: "美兰区白沙街道板桥路43东园镇" },
        { id: 35, content: "美兰区白沙街道板桥路45东园镇" },
        { id: 36, content: "美兰区白沙街道板桥路70号东园镇" },
        { id: 37, content: "美兰区白沙街道板桥路东园镇" },
        {
          id: 38,
          content: "美兰区白沙街道海口市美兰板桥海鲜广场(板桥路)东园镇"
        },
        { id: 39, content: "美兰区白沙街道海轮宿舍北区东园镇" },
        { id: 40, content: "美兰区白龙街道" },
        { id: 41, content: "美兰区蓝天街道" },
        { id: 42, content: "龙华区东湖路" },
        { id: 43, content: "龙华区中山街道" },
        { id: 44, content: "龙华区城西镇" },
        { id: 45, content: "龙华区大同街道" },
        { id: 46, content: "龙华区海垦街道" },
        { id: 47, content: "龙华区滨海街道" },
        { id: 48, content: "龙华区白坡里东一街" },
        { id: 49, content: "龙华区金宇街道" },
        { id: 50, content: "龙华区金贸街道" },
        { id: 51, content: "龙华区龙昆南路" },
        { id: 52, content: "龙华区龙桥镇" },
        { id: 53, content: "龙华区龙泉镇" }
      ]
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.dealData();
    }, 1000);
  },
  methods: {
    dealData() {
      let data = this.wordCloudData.reduce(function(arr, word) {
        let obj = {
          name: word.content,
          itemData: word,
          weight: Math.floor(Math.random() * 3 + 1) //控制加粗,随机数取1~3
        };
        arr.push(obj);
        return arr;
      }, []);
      this.drawPic(data);
    },
    drawPic(data) {
      Highcharts.chart("container", {
        //highcharts logo
        credits: { enabled: false },
        //导出
        exporting: { enabled: false },
        //提示关闭
        tooltip: { enabled: false },
        //颜色配置
        colors: [
          "#ffffff",
          "#00c0d7",
          "#2594ce",
          "#de4c85",
          "#ff7f46",
          "#ffb310",
          "#e25c52"
        ],
        //图形配置
        chart: {
          spacingBottom: 15,
          spacingTop: 12,
          // spacingLeft: 5,
          // spacingRight: 5,
          backgroundColor: "rgba(0, 0, 0,0.5)"
        },

        series: [
          {
            type: "wordcloud", // 类型
            data: data,
            rotation: 15, //字体不旋转
            maxFontSize: 36, //最大字体
            minFontSize: 12, //最小字体
            style: {
              fontFamily: "微软雅黑",
              fontWeight: "500"
            }
          }
        ],
        //点击事件方法
        plotOptions: {
          series: {
            cursor: "pointer",
            events: {
              click: function(e) {
                // 单条数据
                // console.log(e.point.options.itemData);
              }
            }
          }
        },

        //标题配置
        // title: {
        //   text: "REC ●",
        //   // x: 5,
        //   // y: 15,
        //   align: "left",
        //   style: {
        //     color: "red",
        //     fontSize: "16px",
        //     fontWeight: "bold",
        //     lineHeight: "1.2"
        //   }
        // }

      });
    }
  }
};
</script>
