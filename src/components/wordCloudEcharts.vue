<template>
  <div class="hello">
    <div id="app">
      <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :color="myColors"
        :showTooltip="false"
        :wordClick="wordClickHandler"
      ></wordcloud>
    </div>
  </div>
</template>
<script>
import wordcloud from "vue-wordcloud";

var wordData1 = require("../../static/data/wordCloud/2017-5-13.json"); //加载本地数据文件
var wordData2 = require("../../static/data/wordCloud/2017-5-14.json"); //加载本地数据文件
var wordData3 = require("../../static/data/wordCloud/2017-5-15.json"); //加载本地数据文件
var wordData4 = require("../../static/data/wordCloud/2017-5-16.json"); //加载本地数据文件
var wordData5 = require("../../static/data/wordCloud/2017-9-30.json"); //加载本地数据文件
var wordData6 = require("../../static/data/wordCloud/2017-10-01.json"); //加载本地数据文件
export default {
  name: "app",
  components: {
    wordcloud
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      if (true) {
        if (curVal) {
          this.data(curVal, this.$store.state.TimeHour);
        } else {
          this.data(oldVal, this.$store.state.TimeHour);
        }
      }
    }
  },

  methods: {
    wordClickHandler(name, value, vm) {
      console.log("wordClickHandler", name, value, vm);
    }
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      defaultWords: [
        {
          name: "琼山区云龙镇",
          value: 1
        },
        {
          name: "琼山区凤翔街道",
          value: 7
        },
        {
          name: "琼山区国兴街道",
          value: 42
        },
        {
          name: "琼山区府城街道",
          value: 33
        },
        {
          name: "琼山区旧州镇",
          value: 36
        },
        {
          name: "琼山区滨江街道",
          value: 1
        },
        {
          name: "琼山区滨江街道琼山区府城镇",
          value: 36
        },
        {
          name: "琼山区龙塘镇",
          value: 1
        },
        {
          name: "秀英区丘海大道",
          value: 5
        },
        {
          name: "秀英区东山镇",
          value: 4
        },
        {
          name: "秀英区永兴镇",
          value: 1
        },
        {
          name: "秀英区海秀街道",
          value: 14
        },
        {
          name: "秀英区海秀镇",
          value: 34
        },
        {
          name: "秀英区白水塘路",
          value: 31
        },
        {
          name: "秀英区石山镇",
          value: 7
        },
        {
          name: "秀英区秀英街道",
          value: 15
        },
        {
          name: "秀英区秀英街道苏南村镇",
          value: 30
        },
        {
          name: "秀英区西秀镇",
          value: 1
        },
        {
          name: "秀英区长流镇",
          value: 25
        },
        {
          name: "美兰区三江镇",
          value: 31
        },
        {
          name: "美兰区人民路街道",
          value: 1
        },
        {
          name: "美兰区博爱南路",
          value: 32
        },
        {
          name: "美兰区博爱街道",
          value: 1
        },
        {
          name: "美兰区和平南街道",
          value: 31
        },
        {
          name: "美兰区国营桂林洋农场",
          value: 29
        },
        {
          name: "美兰区新埠街道",
          value: 24
        },
        {
          name: "美兰区新民西路",
          value: 27
        },
        {
          name: "美兰区海府街道",
          value: 12
        },
        {
          name: "美兰区海甸街道",
          value: 33
        },
        {
          name: "美兰区海秀东路",
          value: 32
        },
        {
          name: "美兰区演丰镇",
          value: 4
        },
        {
          name: "美兰区灵山镇",
          value: 29
        },
        {
          name: "美兰区白沙街道",
          value: 38
        },
        {
          name: "美兰区白沙街道板桥横路东园镇",
          value: 27
        },
        {
          name: "美兰区白沙街道板桥路43东园镇",
          value: 1
        },
        {
          name: "美兰区白沙街道板桥路45东园镇",
          value: 1
        },
        {
          name: "美兰区白沙街道板桥路70号东园镇",
          value: 21
        },
        {
          name: "美兰区白沙街道板桥路东园镇",
          value: 5
        },
        {
          name: "美兰区白沙街道海口市美兰板桥海鲜广场(板桥路)东园镇",
          value: 11
        },
        {
          name: "美兰区白沙街道海轮宿舍北区东园镇",
          value: 0
        },
        {
          name: "美兰区白龙街道",
          value: 1
        },
        {
          name: "美兰区蓝天街道",
          value: 30
        },
        {
          name: "龙华区东湖路",
          value: 35
        },
        {
          name: "龙华区中山街道",
          value: 10
        },
        {
          name: "龙华区城西镇",
          value: 30
        },
        {
          name: "龙华区大同街道",
          value: 37
        },
        {
          name: "龙华区海垦街道",
          value: 33
        },
        {
          name: "龙华区滨海街道",
          value: 33
        },
        {
          name: "龙华区白坡里东一街",
          value: 32
        },
        {
          name: "龙华区金宇街道",
          value: 6
        },
        {
          name: "龙华区金贸街道",
          value: 35
        },
        {
          name: "龙华区龙昆南路",
          value: 33
        },
        {
          name: "龙华区龙桥镇",
          value: 1
        },
        {
          name: "龙华区龙泉镇",
          value: 28
        }
      ]
    };
  }
};
</script>