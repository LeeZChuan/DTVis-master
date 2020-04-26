<template>
  <div class="gis">
    <Alert banner class="top-banner" show-icon v-show="isMonitorMode" type="error">
      <Icon type="ios-alert-outline" size="24" slot="icon"></Icon>温馨提示,您目前正在选择监测路线,请单击鼠标左键选择多个地点构建成一条线路,单击右下键按扭退出选择模式
    </Alert>
    <div class="monitor-button" v-show="isMonitorMode">
      <Button type="info" style="margin-right:15px;" size="large" @click="saveMonitorLine">构建路线</Button>
      <Button type="info" style="margin-right:15px;" size="large" @click="reMonitor">重新构建</Button>
      <Button type="success" style="margin-right:15px;" size="large" @click="reDrawLine(4)">轨迹回放</Button>
      <Button type="default" size="large" @click="quitMonitorMode">退出</Button>
    </div>
    <Alert banner class="top-banner" show-icon v-show="isRewriteMode" type="success">
      <Icon type="ios-alert-outline" size="24" slot="icon"></Icon>正在轨迹回放您最近一次构建的路线
    </Alert>
    <div class="monitor-button" v-show="isRewriteMode">
      <Button type="info" style="margin-right:15px;" size="large" @click="startAnimation">开始回放</Button>
      <Button type="info" style="margin-right:15px;" size="large" @click="pauseAnimation">暂停动画</Button>
      <Button type="info" style="margin-right:15px;" size="large" @click="resumeAnimation">继续动画</Button>
      <Button type="default" size="large" style="margin-right:15px;" @click="endAnimation">结束动画</Button>
      <Button type="default" size="large" @click="closeRewriteMode">退出</Button>
    </div>

    <div class id="gis-sidebar" v-show="!isMonitorMode&&!isRewriteMode">
      <div
        v-for="(item,index) of sidebarList"
        :key="index"
        class="gis-menubar-item"
        @mouseover="showMunuList(index)"
        @mouseout="hideMenuList"
      >
        <img
          :src="index!=0?item.normallPicture:item.activePicture"
          width="36"
          height="36"
          class="item-picture"
        >
        <div class="menubar-item-detail" v-if="index===0">
          <ul class="gis-item0">
            <li @click="closeOilLine(index)">关闭输油管道</li>
            <li @click="showOilLine(index)">显示输油管道</li>
          </ul>
        </div>
        <div class="menubar-item-detail" v-if="index===1">
          <ul class="gis-item1">
            <li @click="toSearchDialog(index)">查询油田</li>
          </ul>
        </div>
        <div class="menubar-item-detail" v-if="index===2">
          <ul class="gis-item2">
            <li @click="toLocateDialog(index)">我要定位</li>
          </ul>
        </div>
        <div class="menubar-item-detail" v-if="index===3">
          <ul class="gis-item3">
            <li @click="toShowDialog(index)">统计信息功能</li>
          </ul>
        </div>
        <div class="menubar-item-detail" v-if="index===4">
          <ul class="gis-item4">
            <li @click="monitorLine(index)">监测路线</li>
            <li @click="reDrawLine(index)">轨迹回放</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="gis-menu-bar">
      <div class="gis-back">
        <Button type="info" size="large" @click="toExit">关闭
          <Icon type="md-close"/>
        </Button>
      </div>
    </div>
    <div class="map-content">
      <div class="map" id="map-container" ref="mymap"></div>
    </div>
    <i-dialog :isShow="dialogShow" @on-close="closeDialog">
      <div class="m-title">油田信息统计</div>
      <div class="m-content">
        <p v-for="item of lal.oil" :key="item.id">
          <span>{{item.id}}:</span>
          <span>{{item.name}}</span>
        </p>
      </div>
      <div class="m-tail">共6座油田处于监控中.....</div>
    </i-dialog>
    <i-dialog :isShow="searchDialogShow" @on-close="closeSearchDialog">
      <div class="search">
        <span>请选择要查找的油田</span>
        <Select v-model="searchOilInfo" filterable @on-change="openOilInfo">
          <Option v-for="item of lal.oil" :value="item.id" :key="item.id">{{ item.name }}</Option>
        </Select>
      </div>
    </i-dialog>
    <i-dialog :isShow="locateDialogShow" @on-close="closeLocateDialog">
      <div class="location">
        <span>定位到</span>
        <input type="text" id="tipInput" v-model="locatePlace" @input="autoCompletePlace">
      </div>
    </i-dialog>
  </div>
</template>
 


<script>
import iDialog from "../../components/dialog";
export default {
  props: {},
  components: {
    iDialog
  },
  data() {
    return {
      //右键菜单
      contextMenu: null,
      contextMenuPositon: null,
      //历史标记线路二维数组
      lineArr: [],
      //历史轨迹标注
      historyMarker: null,
      historyStartMarker: null,
      historyEndMarker: null,
      //历史轨迹路线
      tempPolyline: null,
      passedPolyline: null,
      //历史轨迹路线
      historyLine: null,
      //是否处于轨迹回放路线
      isRewriteMode: false,
      //三种图标
      startIcon: null,
      viaIcon: null,
      endIcon: null,
      moveIcon: null,
      //构建路线需要存储的点数据组
      monitorPolyLine: [],
      monitorLineList: [],
      saveMonitorLineList: [],
      //是否处于键控状态
      isMonitorMode: false,
      //搜索对话框显示
      searchDialogShow: false,
      locateDialogShow: false,
      //当前菜单栏
      currentMenuIndex: 0,
      //五个侧边栏
      item0: null,
      item1: null,
      item2: null,
      item3: null,
      item4: null,
      //油管路线是否显示
      lineShow: true,
      //左侧菜单数据
      sidebarList: [
        {
          normallPicture: require("../../assets/images/sidebar1.png"),
          activePicture: require("../../assets/images/sidebar1-active.png"),
          item1: "显示油管路线",
          item2: "隐藏油管路线"
        },
        {
          normallPicture: require("../../assets/images/sidebar2.png"),
          activePicture: require("../../assets/images/sidebar2-active.png"),
          item1: "查询已有油田"
        },
        {
          normallPicture: require("../../assets/images/sidebar3.png"),
          activePicture: require("../../assets/images/sidebar3-active.png"),
          item1: "我要定位"
        },
        {
          normallPicture: require("../../assets/images/sidebar4.png"),
          activePicture: require("../../assets/images/sidebar4-active.png"),
          item1: "统计信息"
        },
        {
          normallPicture: require("../../assets/images/sidebar5.png"),
          activePicture: require("../../assets/images/sidebar5-active.png"),
          item1: "检测路线",
          item2: "轨迹回放"
        }
      ],
      //中心标记点
      centerMaker: null,
      dialogShow: false,
      //定义11条线
      line: null,
      line1: null,
      line2: null,
      line3: null,
      line4: null,
      line5: null,
      line6: null,
      line7: null,
      line8: null,
      line9: null,
      line10: null,
      //定义11条路径

      //要定位的位置
      locatePlace: null,
      searchPlace: null,
      locatePlaceList: null,
      //搜索的油田信息
      searchOilInfo: null,
      roadSwitch: true,
      //唯一实例化的地图
      map: null,
      //地图上的油田标注
      maker: null,
      //选中的油田标注
      targetOil: null,
      //选中的消息窗体
      infoWindow: null,
      //机场拐点
      airPoint: {
        x: 108.7481690673828,
        y: 34.38310419514892
      },
      airPoint1: {
        x: 108.7701417236328,
        y: 34.38877075187437
      },
      airPoint2: {
        x: 108.83468640136718,
        y: 34.41369904458776
      },
      airPoint3: {
        x: 108.8390596923828,
        y: 34.44654771738653
      },

      airPoint4: {
        x: 108.9360596923828,
        y: 34.43654771738653
      },

      //长安拐点

      caPoint: {
        x: 108.80413067626952,
        y: 34.306568155083355
      },
      caPoint1: {
        x: 108.80413067626952,
        y: 34.291819859883894
      },

      //湿地公园拐点

      sdPoint1: {
        x: 108.97441876220702,
        y: 34.43012499468482
      },
      sdPoint: {
        x: 108.96480572509765,
        y: 34.43635468325383
      },

      //汉长安-未央区
      wyPoint: {
        x: 108.85597241210937,
        y: 34.31096378052061
      },
      wyPoint1: {
        x: 108.86215222167968,
        y: 34.31096378052066
      },
      wyPoint2: {
        x: 108.88824475097655,
        y: 34.30075423253784
      },
      wyPoint3: {
        x: 108.89408123779296,
        y: 34.30075423253784
      },

      //西安北站
      railWay: {
        x: 108.93116009521484,
        y: 34.37091979955785
      },
      railWay1: {
        x: 108.94145977783202,
        y: 34.36751918675531
      },

      //京昆高速

      speedWay: {
        x: 108.83777630615234,
        y: 34.16266188386401
      },
      speedWay1: {
        x: 108.85631573486327,
        y: 34.163798201326586
      },

      speedWay2: {
        x: 108.93047344970702,
        y: 34.17686475279816
      },
      speedWay3: {
        x: 108.96137249755859,
        y: 34.185953334574926
      },
      //莲湖区
      lh: {
        x: 108.8521958618164,
        y: 34.29323807771724
      },

      lh2: {
        x: 108.82267010498046,
        y: 34.28359372437714
      },

      lh1: {
        x: 108.96068585205077,
        y: 34.275083081654074
      },

      lh3: {
        x: 108.82816326904296,
        y: 34.291536213445134
      },

      lh4: {
        x: 108.91536724853515,
        y: 34.2722460092673
      },

      //最后一条
      last2: {
        x: 109.03312695312499,
        y: 34.2469918479261
      },
      last3: {
        x: 109.00978100585937,
        y: 34.2345038442171
      },

      last4: {
        x: 109.02076733398437,
        y: 34.210657966177614
      },

      last5: {
        x: 108.97544873046874,
        y: 34.22428500877778
      },
      last6: {
        x: 108.94386303710937,
        y: 34.23109770351319
      },

      point1: {
        x: 108.78524792480468,
        y: 34.19589284974892
      },
      point2: {
        x: 108.7591553955078,
        y: 34.317344117641554
      },
      point3: {
        x: 108.85665905761718,
        y: 34.408034175668504
      },
      point4: {
        x: 109.04068005371093,
        y: 34.38197083778134
      },
      point5: {
        x: 109.22332775878905,
        y: 34.30032880776794
      },
      point6: {
        x: 109.02145397949218,
        y: 34.28557941702164
      },
      lal: {
        //地图中心坐标
        center: {
          x: 108.95004284667968,
          y: 34.310538407470524
        },
        //油田坐标及信心
        oil: [
          {
            x: 108.78524792480468,
            y: 34.19589284974892,
            id: 1,
            name: "长青油田",
            description:
              "勘探区域主要在陕甘宁盆地，勘探总面积约37万平方公里。油气勘探开发建设始于1970年，先后找到油气田22个，其中油田19个。",
            image: require("../../assets/images/oil1.png")
          },
          {
            x: 108.7591553955078,
            y: 34.317344117641554,
            id: 2,
            name: "江汉油田",
            description:
              "先后发现24个油气田，探明含油面积139.6平方公里、含气面积71.04平方公里，累计生产原油2118.73万吨、天然气9.54亿立方米。1995年年产原油85万吨。",
            image: require("../../assets/images/oil2.png")
          },
          {
            x: 108.85665905761718,
            y: 34.408034175668504,
            id: 3,
            name: "塔里油田",
            description:
              "经过7年的勘探，已探明9个大中型油气田、26个含油气构造，累计探明油气地质储量3.78亿吨，具备年产500万原油。",
            image: require("../../assets/images/oil3.png")
          },
          {
            x: 109.04068005371093,
            y: 34.38197083778134,
            id: 4,
            name: "胜利油田",
            description:
              "主要工作范围约4.4万平方公里。1995年年产原油3000万吨，是我国第二大油田",
            image: require("../../assets/images/oil4.png")
          },
          {
            x: 109.22332775878905,
            y: 34.30032880776794,
            id: 5,
            name: "麻衣油田",
            description:
              "开发了15个油气田，建成792万吨原油配套生产能力(稀油603.1万吨，稠油188.9万吨)，3.93亿立方米天然气生产能力。",
            image: require("../../assets/images/oil5.png")
          },
          {
            x: 109.02145397949218,
            y: 34.28557941702164,
            id: 6,
            name: "大港油田",
            description:
              "现已在大港探区建成投产15个油气田24个开发区，形成年产原油430万吨和天然气3.8亿立方米生产能力。",
            image: require("../../assets/images/oil6.png")
          }
        ]
      }
    };
  },
  computed: {},
  created() {},
  mounted() {
    this.initMap();
    this.initContainer();
    this.initAllMaker();
    this.drawOilLine();
    this.openOilInfo(6);

    //监听窗口调整,改变地图大小
  },
  methods: {
    //进入轨迹回放模式
    reDrawLine(index) {
      let historyLineString = localStorage.getItem("historyLine");
      console.log(historyLineString);
      if (historyLineString === null) {
        this.$Message.error({
          content: "你暂时无可用的监控路线回放,请先选择监控路线构建路线!",
          duration: 10
        });
        return false;
      }
      this.isMonitorMode = false;
      this.changeAcitveIcon(index);
      this.isRewriteMode = true;
      //获取上一次构建的路线数据

      this.historyLine = JSON.parse(historyLineString);
      this.infoWindow.close();

      this.startIcon = new AMap.Icon({
        image: require("../../assets/images/starticon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(64, 64)
      });
      this.endIcon = new AMap.Icon({
        image: require("../../assets/images/endicon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(64, 64)
      });

      this.moveIcon = new AMap.Icon({
        image: require("../../assets/images/moveicon.png"),
        size: new AMap.Size(32, 32),
        imageSize: new AMap.Size(72, 71)
      });

      this.endIcon = new AMap.Icon({
        image: require("../../assets/images/endicon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(64, 64)
      });

      this.historyStartMarker = new AMap.Marker({
        map: this.map,
        position: [this.historyLine[0]["O"], this.historyLine[0]["P"]],
        icon: this.startIcon,
        autoRotation: true
      });

      this.historyEndMarker = new AMap.Marker({
        map: this.map,
        position: [
          this.historyLine[this.historyLine.length - 1]["O"],
          this.historyLine[this.historyLine.length - 1]["P"]
        ],
        icon: this.endIcon,
        autoRotation: true
      });

      //定义移动点

      this.historyMarker = new AMap.Marker({
        position: [this.historyLine[0]["O"], this.historyLine[0]["P"]],
        icon: this.moveIcon,
        autoRotation: true
      });

      this.map.add(this.historyEndMarker);
      this.map.add(this.historyMarker);
      this.map.setFitView();

      this.lineArr = [];
      for (let i = 0; i < this.historyLine.length; i++) {
        let arr = [this.historyLine[i]["O"], this.historyLine[i]["P"]];
        this.lineArr.push(arr);
      }

      // 绘制轨迹
      this.tempPolyline = new AMap.Polyline({
        map: this.map,
        path: this.lineArr,
        showDir: true,
        strokeColor: "rgba(255,255,255,0)", //线颜色
        // strokeOpacity: 1,     //线透明度
        strokeWeight: 1 //线宽
        // strokeStyle: "solid"  //线样式
      });

      this.passedPolyline = new AMap.Polyline({
        map: this.map,
        // path: lineArr,
        strokeColor: "#AF5", //线颜色
        // strokeOpacity: 1,     //线透明度
        strokeWeight: 10 //线宽
        // strokeStyle: "solid"  //线样式
      });

      this.historyMarker.on("moving", e => {
        this.passedPolyline.setPath(e.passedPath);
      });
    },
    //开始动画
    startAnimation() {
      this.map.add(this.historyMarker);
      this.map.add(this.passedPolyline);
      this.historyMarker.moveAlong(this.lineArr, 18000);
    },
    pauseAnimation() {
      this.historyMarker.pauseMove();
    },
    resumeAnimation() {
      this.historyMarker.resumeMove();
    },
    endAnimation() {
      this.historyMarker.stopMove();
      this.map.remove(this.historyMarker);
      this.map.remove(this.passedPolyline);
    },
    closeRewriteMode() {
      //关闭三个标注
      this.historyMarker.stopMove();
      this.map.remove(this.historyStartMarker);
      this.map.remove(this.historyEndMarker);
      //关掉线
      this.map.remove(this.tempPolyline);
      this.endAnimation();
      this.isRewriteMode = false;
    },
    //画线
    drawMonitorLine(list) {
      let path = [];
      for (let i = 0; i < list.length; i++) {
        let point = new AMap.LngLat(list[i].O, list[i].P);
        path.push(point);
      }
      // 创建折线实例
      let polyline = new AMap.Polyline({
        path: path,
        borderWeight: 10, // 线条宽度，默认为 1
        strokeColor: "#22d855", // 线条颜色
        lineJoin: "round" // 折线拐点连接处样式
      });
      this.monitorPolyLine.push(polyline);
      this.map.add(this.monitorPolyLine);
    },
    //重新构建
    reMonitor() {
      this.map.on("click", this.mapClickHandle);
      this.map.remove(this.monitorLineList);
      this.map.remove(this.saveMonitorLineList);
      this.map.remove(this.monitorPolyLine);
      this.monitorPolyLine = [];
      this.saveMonitorLineList = [];
      this.monitorLineList = [];
      localStorage.setItem("hello", JSON.stringify(this.saveMonitorLineList));
    },
    //保存构建的路线
    saveMonitorLine() {
      if (
        this.saveMonitorLineList.length < 2 ||
        this.monitorLineList.length < 2
      ) {
        this.$Modal.info({
          title: "操作有误",
          content: "选择的地点数量不能小于2,点击确定继续选择"
        });
        return false;
      }
      this.map.off("click", this.mapClickHandle);
      this.monitorLineList[this.monitorLineList.length - 1].setIcon(
        this.endIcon
      );
      this.drawMonitorLine(this.saveMonitorLineList);

      localStorage.setItem(
        "historyLine",
        JSON.stringify(this.saveMonitorLineList)
      );
    },

    //检测路线
    monitorLine(index) {
      this.changeAcitveIcon(index);
      this.isMonitorMode = true;
      this.infoWindow.close();
      //初始化图标
      //开始监听点击地图事件
      this.map.on("click", this.mapClickHandle);
    },
    //map板顶的时间
    mapClickHandle(ev) {
      let Obj = {
        O: "",
        P: ""
      };
      this.startIcon = new AMap.Icon({
        image: require("../../assets/images/starticon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(48, 48)
      });
      this.viaIcon = new AMap.Icon({
        image: require("../../assets/images/viaicon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(48, 48)
      });
      this.endIcon = new AMap.Icon({
        image: require("../../assets/images/endicon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(48, 48)
      });
      // 触发事件的对象
      let target = ev.lnglat;
      console.log(target["O"]);
      console.log(target["P"]);
      Obj.O = target["O"];
      Obj.P = target["P"];
      let icon;

      if (this.monitorLineList.length === 0) {
        icon = this.startIcon;
      } else {
        icon = this.viaIcon;
      }
      let marker = new AMap.Marker({
        position: [target["O"], target["P"]],
        icon: icon
      });

      this.monitorLineList.push(marker);
      this.map.add(marker);
      this.saveMonitorLineList.push(Obj);
    },
    //退出监测路线模式
    quitMonitorMode() {
      this.map.off("click", this.mapClickHandle);
      this.map.remove(this.monitorLineList);
      this.map.remove(this.monitorPolyLine);
      this.saveMonitorLineList = [];
      this.monitorLineList = [];
      this.isMonitorMode = false;
    },
    //定位对话框的相关方法
    toLocateDialog(index) {
      this.changeAcitveIcon(index);
      this.locateDialogShow = true;
    },
    closeLocateDialog() {
      this.locateDialogShow = false;
    },
    //搜索框的相关方法
    toSearchDialog(index) {
      this.changeAcitveIcon(index);
      this.searchDialogShow = true;
    },
    closeSearchDialog() {
      this.searchDialogShow = false;
    },
    //显示所有的管道
    showOilLine(index) {
      this.changeAcitveIcon(index);
      this.showRoad();
      this.$Message.success("输油管道显示成功!");
    },
    //关闭所有的管道
    closeOilLine(index) {
      this.changeAcitveIcon(index);
      this.hideRoad();
      this.$Message.success("输油管道隐藏成功!");
    },
    changeAcitveIcon(index) {
      let el;
      for (let index = 0; index < 5; index++) {
        el = document.getElementsByClassName("item-picture")[index];
        el.src = require("../../assets/images/sidebar" + (index + 1) + ".png");
      }
      let el1 = document.getElementsByClassName("item-picture")[index];
      el1.src = require("../../assets/images/sidebar" +
        (index + 1) +
        "-active.png");

      this.currentMenuIndex = index;
    },
    //隐藏侧边栏的子菜单
    hideMenuList() {
      for (let index = 0; index < 5; index++) {
        this["item" + index] = document.getElementsByClassName(
          "gis-item" + index
        )[0];
        this["item" + index].style.display = "none";
      }
    },
    //显示侧边栏的子菜单

    showMunuList(index) {
      for (let index = 0; index < 5; index++) {
        this["item" + index] = document.getElementsByClassName(
          "gis-item" + index
        )[0];
        this["item" + index].style.display = "none";
      }
      this["item" + index].style.display = "flex";
    },
    //自动获取列表
    autoCompletePlace() {
      let that = this;
      AMap.plugin(["AMap.Autocomplete"], function() {
        let autocomplete = new AMap.Autocomplete({
          city: "", //默认全国
          input: "tipInput"
        });
        AMap.event.addListener(autocomplete, "select", e => {
          console.log(e.poi);
          if (!e.poi.location["lng"]) {
            that.$Message.info(
              "关键字 " + that.locatePlace + " 范围偏大,请选择更小的行政区"
            );
            return false;
          }
          that.map.setCenter([e.poi.location["lng"], e.poi.location["lat"]]);
          that.centerMaker.setPosition([
            e.poi.location["lng"],
            e.poi.location["lat"]
          ]);
          that.locateDialogShow = false;
        });
      });
    },

    //初始化地图
    initMap() {
      this.map = new AMap.Map("map-container", {
        zoom: 11, //级别
        center: [this.lal.center.x, this.lal.center.y], //中心点坐标
        viewMode: "3D", //使用3D视图
        mapStyle: "amap://styles/df95df063dea9d024331dd5091367335" //自定义风格
      });

      AMap.plugin(
        [
          "AMap.ControlBar",
          "AMap.Scale",
          "AMap.OverView",
          "AMap.MapType",
          "AMap.Geolocation",
          "AMap.ToolBar"
        ],
        e => {
          // 添加 3D 罗盘控制
          this.map.addControl(
            new AMap.ControlBar({
              position: {
                top: "200px",
                right: "0px"
              }
            })
          );
          this.map.addControl(new AMap.Scale());
          // 在图面添加类别切换控件，实现默认图层与卫星图、实施交通图层之间切换的控制
          this.map.addControl(new AMap.MapType());
          // 在图面添加定位控件，用来获取和展示用户主机所在的经纬度位置
        }
      );

      //构建右键菜单

      //创建右键菜单
      this.contextMenu = new AMap.ContextMenu();

      //右键放大
      this.contextMenu.addItem(
        "放大一级",
        e => {
          this.map.zoomIn();
        },
        0
      );

      //右键缩小
      this.contextMenu.addItem(
        "缩小一级",
        e => {
          this.map.zoomOut();
        },
        1
      );
      this.contextMenu.addItem(
        "一键还原",
        e => {
          this.map.setZoom(11);
          this.map.setCenter([this.lal.center.x, this.lal.center.y]);
        },
        1
      );

      //右键显示全国范围
      this.contextMenu.addItem(
        "缩放至全国范围",
        e => {
          this.map.setZoomAndCenter(4, [108.946609, 34.262324]);
        },
        2
      );

      //右键添加Marker标记
      this.contextMenu.addItem(
        "添加标记",
        e => {
          let marker = new AMap.Marker({
            map: this.map,
            position: this.contextMenuPositon //基点位置
          });
        },
        3
      );
      //地图绑定鼠标右击事件——弹出右键菜单
      this.map.on("rightclick", e => {
        this.contextMenu.open(this.map, e.lnglat);
        this.contextMenuPositon = e.lnglat;
      });
    },
    //自定义菜单类

    //调整地图大小
    initContainer() {
      let el = document.getElementById("map-container");
      el.style.width = this.getViewPortWidth() - 10 + "px";
      el.style.height = this.getViewPortHeight() - 65 + "px";
    },
    // 获取浏览器窗口的可视区域的宽度
    getViewPortWidth() {
      return document.documentElement.clientWidth || document.body.clientWidth;
    },
    // 获取浏览器窗口的可视区域的高度
    getViewPortHeight() {
      return (
        document.documentElement.clientHeight || document.body.clientHeight
      );
    },
    //添加标注
    initAllMaker() {
      //中心地点
      let centerIcon = new AMap.Icon({
        image: require("../../assets/images/locationicon.png"),
        size: new AMap.Size(128, 128),
        imageSize: new AMap.Size(42, 42)
      });
      this.centerMaker = new AMap.Marker({
        position: [this.lal.center.x, this.lal.center.y],
        icon: centerIcon
      });
      this.map.add(this.centerMaker);

      let myIcon = new AMap.Icon({
        image: require("../../assets/images/oil.png"),
        size: new AMap.Size(36, 36)
      });

      this.maker = new Array(6);
      let i = 0;
      for (const oilInfo of this.lal.oil) {
        this.maker[i++] = new AMap.Marker({
          position: [oilInfo.x, oilInfo.y], //位置
          icon: myIcon,
          title: i + "号油田"
        });
      }
      //绑定click事件
      this.map.add(this.maker);
      for (let i = 0; i < this.maker.length; i++) {
        this.maker[i].on("click", this.onMarkerClick);
      }
    },
    //为每个标注添加时间

    //显示单个油田信息
    onMarkerClick(e) {
      //console.log(e.target.F.title);
      let oilTitle = e.target.F.title;
      let id = parseInt(oilTitle.slice(0, 1));

      for (const oilInfo of this.lal.oil) {
        if (oilInfo.id === id) {
          this.targetOil = oilInfo;
          break;
        }
      }
      //实例化该窗体
      this.infoWindow = new AMap.InfoWindow({
        //创建信息窗体
        isCustom: true, //使用自定义窗体
        content:
          '<div class="info"><img id="closePic" width="36px" height="36px" class="info-close" src="./static/close.png" alt="close"><div class="info-title">' +
          this.targetOil.name +
          '</div><div class="info-content"><img src="' +
          this.targetOil.image +
          '" alt="油田图片"><div class="real-content">' +
          this.targetOil.description +
          "</div></div>",
        offset: new AMap.Pixel(16, -45)
      });
      this.infoWindow.open(this.map, e.target.getPosition()); //打开信息窗体
      //e.target就是被点击的Marker
      this.$refs.mymap.onclick = this.closeOilInfo;
    },
    //打开某个特定的油田信息
    openOilInfo(index = -1) {
      if (index === -1) {
        index = this.searchOilInfo;
      }
      //console.log(e.target.F.title);
      for (const oilInfo of this.lal.oil) {
        if (oilInfo.id === index) {
          this.targetOil = oilInfo;
          break;
        }
      }
      //实例化该窗体
      this.infoWindow = new AMap.InfoWindow({
        //创建信息窗体
        isCustom: true, //使用自定义窗体
        content:
          '<div class="info"><img id="closePic" width="36px" height="36px" class="info-close" src="./static/close.png" alt="close"><div class="info-title">' +
          this.targetOil.name +
          '</div><div class="info-content"><img src="' +
          this.targetOil.image +
          '" alt="油田图片"><div class="real-content">' +
          this.targetOil.description +
          "</div></div>",
        offset: new AMap.Pixel(16, -45)
      });
      //打开窗体/关闭对话框
      this.searchDialogShow = false;
      this.infoWindow.open(this.map, this.maker[index - 1].getPosition()); //打开信息窗体
      //e.target就是被点击的Marker
      this.$refs.mymap.onclick = this.closeOilInfo;
    },
    //关闭油田信息窗体
    closeOilInfo(e) {
      if (e.target.className === "info-close") {
        this.infoWindow.close();
      }
    },

    //开始画油管线
    drawOilLine() {
      //定义划线的数据
      let path = [
        [[this.point2.x, this.point2.y]],
        [
          [this.airPoint.x, this.airPoint.y],
          [this.airPoint1.x, this.airPoint1.y]
        ],
        [[this.point3.x, this.point3.y]]
      ];
      let path1 = [
        [[this.point2.x, this.point2.y]],
        [[this.caPoint.x, this.caPoint.y], [this.caPoint1.x, this.caPoint1.y]],
        [[this.point1.x, this.point1.y]]
      ];

      let path2 = [
        [[this.point3.x, this.point3.y]],
        [[this.sdPoint.x, this.sdPoint.y], [this.sdPoint1.x, this.sdPoint1.y]],
        [[this.point4.x, this.point4.y]]
      ];
      let path3 = [
        [[this.point2.x, this.point2.y]],
        [[this.wyPoint.x, this.wyPoint.y], [this.wyPoint1.x, this.wyPoint1.y]],
        [
          [this.wyPoint2.x, this.wyPoint2.y],
          [this.wyPoint3.x, this.wyPoint3.y]
        ],
        [[this.lal.center.x, this.lal.center.y]]
      ];
      let path4 = [
        [[this.point3.x, this.point3.y]],
        [[this.railWay.x, this.railWay.y], [this.railWay1.x, this.railWay1.y]],
        [[this.lal.center.x, this.lal.center.y]]
      ];
      let path5 = [
        [[this.point5.x, this.point5.y]],
        [[this.point6.x, this.point6.y]]
      ];
      let path6 = [
        [[this.lal.center.x, this.lal.center.y]],
        [[this.point6.x, this.point6.y]]
      ];
      let path7 = [
        [[this.point4.x, this.point4.y]],
        [[this.point6.x, this.point6.y]]
      ];
      let path8 = [
        [[this.point1.x, this.point1.y]],
        [
          [this.speedWay.x, this.speedWay.y],
          [this.speedWay1.x, this.speedWay1.y]
        ],
        [[this.speedWay2.x, this.speedWay2.y]],
        [[this.speedWay3.x, this.speedWay3.y]]
      ];
      let path9 = [
        [[this.point1.x, this.point1.y]],
        [[this.lh3.x, this.lh3.y], [this.lh.x, this.lh.y]],
        [[this.lh4.x, this.lh4.y], [this.lh1.x, this.lh1.y]],
        [[this.point6.x, this.point6.y]]
      ];
      let path10 = [
        [[this.point6.x, this.point6.y]],
        [[this.last2.x, this.last2.y], [this.last3.x, this.last3.y]],
        [[this.last4.x, this.last4.y], [this.last5.x, this.last5.y]],
        [[this.last6.x, this.last6.y]]
      ];

      //开始画线

      this.line = new AMap.BezierCurve({
        path: path, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line);

      this.line1 = new AMap.BezierCurve({
        path: path1, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line1);

      this.line2 = new AMap.BezierCurve({
        path: path2, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line2);

      this.line3 = new AMap.BezierCurve({
        path: path3, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line3);

      this.line4 = new AMap.BezierCurve({
        path: path4, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line4);

      this.line5 = new AMap.BezierCurve({
        path: path5, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line5);

      this.line6 = new AMap.BezierCurve({
        path: path6, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line6);

      this.line7 = new AMap.BezierCurve({
        path: path7, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line7);

      this.line8 = new AMap.BezierCurve({
        path: path8, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line8);

      this.line9 = new AMap.BezierCurve({
        path: path9, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line9);

      this.line10 = new AMap.BezierCurve({
        path: path10, //设置线覆盖物路径
        strokeColor: "#ff6600", //线颜色
        strokeWeight: 5, // 线条宽度
        borderWeight: 5 // 描边宽度
      });
      this.map.add(this.line10);
    },
    //隐藏输油管道
    hideRoad() {
      this.map.remove(this.line);
      this.map.remove(this.line1);
      this.map.remove(this.line2);
      this.map.remove(this.line3);
      this.map.remove(this.line4);
      this.map.remove(this.line5);
      this.map.remove(this.line6);
      this.map.remove(this.line7);
      this.map.remove(this.line8);
      this.map.remove(this.line9);
      this.map.remove(this.line10);
    },
    showRoad() {
      this.map.add(this.line);
      this.map.add(this.line1);
      this.map.add(this.line2);
      this.map.add(this.line3);
      this.map.add(this.line4);
      this.map.add(this.line5);
      this.map.add(this.line6);
      this.map.add(this.line7);
      this.map.add(this.line8);
      this.map.add(this.line9);
      this.map.add(this.line10);
    },

    //打开对话框
    toShowDialog(index) {
      this.changeAcitveIcon(index);
      this.dialogShow = true;
    },
    closeDialog() {
      this.dialogShow = false;
    },
    //返回主页面
    toExit() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>
<style scoped>
html,
body {
  margin: 0px !important;
  padding: 0;
}
.monitor-button {
  position: fixed;
  right: 30px;
  bottom: 30px;
  z-index: 99999;
}
.top-banner {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 50px;
  line-height: 40px;
  z-index: 9999999;
  display: flex;
  font-size: 14px;
  justify-content: center;
  align-items: center;
}
.gis-back {
  margin-right: 20px;
}
#gis-sidebar {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 60px;
  box-sizing: border-box;
  min-height: 100vh;
  background: rgba(255, 255, 255, 0.2);

  font-size: 16px;
  z-index: 99999;
}
.map-content {
  margin-top: -42px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.gis-menubar-item {
  position: relative;
  top: 0;
  left: 0;
  box-sizing: border-box;
  padding: 15px 12px;

  cursor: pointer;
}
.menubar-item-detail {
  position: absolute;
  left: 60px;
  width: 160px;
  box-shadow: 2px 4px 10px #030303;
  top: 0;
  color: #fff;
}

.menubar-item-detail ul {
  padding: 0;
  margin: 0;
  background: #0c1730;

  display: none;
  padding: 5px;
  font-size: 14px;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
}

.menubar-item-detail ul li {
  margin: 0;
  padding: 20px 10px;
  text-align: left;
  list-style-type: none;
}

.gis-menubar-item:hover {
  background: #0c1730;
}
.gis-menubar-item + .gis-menubar-item {
  border-top: 1px solid #0c170c;
}
#tipInput {
  outline: none;
  padding: 3px;
  position: relative;
  z-index: 10000;
}
.amap-sug-result {
  z-index: 99999;
}
.auto-item {
  font-size: 14px;
}
.gis-menu-bar {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  height: 60px;
  position: absolute;
  width: 100%;
  top: -100px;
  left: 0;
  z-index: 1000;
  color: #fff;
  background: #0c1730;
  box-shadow: 0px 2px 50px rgba(255, 255, 255, 0.1);
}

.gis-menu-bar .location {
  display: flex;
  flex-direction: row;
  margin-right: 30px;
  justify-content: center;
  align-items: center;
}

.gis-menu-bar .location span {
  margin-right: 10px;
}
.search {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  width: 60%;
  margin-left: 20%;
  height: 300px;
}
.gis-menu-bar .total {
  margin-left: 30px;
}
.search span {
  display: block;
  margin-bottom: 10px;
}
.search span {
  display: block;
  width: 200px;
}
.gis {
  z-index: 999;
  border-top: 1px solid #0c1730;
}
#map-container {
  width: 1600px;
  height: 780px;
}

.m-title {
  font-size: 16px;
  color: #0c1730;
  text-align: center;
  margin: 10px;
}
.m-content {
  text-align: center;
  font-size: 14px;
}
.m-tail {
  text-align: right;
  font-size: 12px;
  margin-right: 10px;
}
.gis {
  display: flex;
  flex-direction: column;
  top: -42px;
  left: 0;
}

@media screen and (max-width: 720px) {
  .gis {
    display: flex;
    flex-direction: column;
    margin-top: -350px;
  }
  .gis-menu-bar {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    height: auto;
    position: absolute;
    width: 100%;
    top: -350px;
    left: 0;
    padding: 10px 0;
    z-index: 1000;
    color: #fff;
    background: #0c1730;
  }

  .gis-menu-bar .location {
    display: flex;
    flex-direction: row;
    margin: 2px;
    justify-content: center;
    align-items: center;
  }

  .gis-menu-bar .location span {
    margin-right: 10px;
  }
  .search {
    display: flex;
    flex-direction: row;
    margin: 0px;
    justify-content: flex-start;
    align-items: center;
    width: 260px;
  }
  .total {
    margin-left: 10px;
  }
  .search span {
    display: block;
    width: 200px;
    margin-right: 0px;
  }
}
</style>