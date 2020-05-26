
# :dolphin:	 DTVis-master
[![Vue](https://img.shields.io/badge/Vue-2.5.2-yellow)](https://img.shields.io/badge/Vue-2.5.2-yellow)
[![Python](https://img.shields.io/badge/Python-3.8-blue)](https://img.shields.io/badge/Python-3.8-blue)
[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
> Author: Lee ZChuan\Qin Yangxin

> E-mail: cdutlzc@gmail.com

> PreDate: 2020-02-29

> StartDate: 2020-03-15

> EndDate: 2020-04-30

>Description: 基于Vue框架的交通流量时空演变特征可视分析系统

>UI设计：自己手写设计的UI、弹窗、时间选取工具以及提示窗使用的element-ui组件、



## 结果展示

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

## 代码结构
```
DTVis-master
│
├── build  # 存放最终发布的代码的存放位置
│ 
├── config # 存放配置路径、端口号等一些信息
│ 
├── node_modules：#npm 加载的项目依赖模块,（整个项目需要的依赖资源）
│ 
├── src：#这里是我们开发的主要目录，里面包含了几个目录及文件：
│   ├── assets  # 包含了css页面情况
│   ├── components # 页面的各个模块分布，各自介绍在README中有所介绍
│   ├── utils # 页面的可能需要的工具
│   ├── views # 跳转页面的布局情况
│   └── router # 页面Vue路由管理，用于进行网页链接
│
├── static # 该目录下的文件不会被WebPack处理：会被直接复制到最终的打包目录下 （绝对路径）
│   ├── data  # 包含了可视化页面所用到的数据
│   │    |──  Forecast # 订单预测
│   │    |──  ForecastPointChart # 订单预测结果数据源-散点图
│   │    |──  StartHeatMapChart # 起点订单分布热力图
│   │    |──  EndHeatMapChart # 终点订单分布热力图
│   │    |──  CalendarChart # 订单情况日历热力图
│   │    |──  TadpoleChart # 街道情况流量蝌蚪图
│   │    |──  multiputeMap # 订单预测结果
│   │    |──  MoveToChart # 订单情况整体区域迁徙图
│   │    |──  ChordChart # 订单情况整体街道和弦图（用在弹窗部分展示）
│   │    |──  RateLineChart #订单整体情况变化率折线图（用在弹窗展示部分）
│   │    |──  OrderNumLineChart #订单的出行距离与该订单出行距离数量组合折线图（用在弹窗展示部分）
│   │    |──  LineCharts #订单情况变化折线图
│   │    |──  PreBarChart # 订单整体预测柱状图
│   │    |──  wordCloud # 订单热门地点词云图
│   │    |──  DailyBarChart # 订单预测视图，整体预测柱状图
│   ├── img # 页面所需要的背景图片
│   ├── script # 数据处理所需要的代码
│   └── js # 作图所需要的库文件
│
├── DT-Vis.html # 测试效果样例网页
│
│
└── README.md # 此说明文件
```

## 系统截图

![Image text](https://github.com/LeeZChuan/DTVis-master/blob/master/static/img/README/%E8%8D%89%E5%9B%BE.bmp)


## 环境

* `Python 3.8 `

* 依赖：`Echarts` `D3.js`

* 系统支持：`Win10` 

* 编程环境:`pycharm、Vscode`

