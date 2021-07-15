# :dolphin:	 DTVis-master
[![Vue](https://img.shields.io/badge/Vue-2.5.2-yellow)](https://img.shields.io/badge/Vue-2.5.2-yellow)
[![Python](https://img.shields.io/badge/Python-3.8-blue)](https://img.shields.io/badge/Python-3.8-blue)
[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)

> [🇨🇳 中文版](./README.zh_CN.md)


>Description: Visual analysis system of traffic flow spatio-temporal evolution based on Vue framework


## Results display

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

## Code structure

```
DTVis-master
│
├── build  # Where to store the final released code
│ 
├── config # Store some information such as configuration path and port number
│ 
├── node_modules：# Project dependent modules loaded by npm, (dependent resources required by the entire project)
│ 
├── src：# Here is the main directory we developed, which contains several directories and files:
│   ├── assets  # Contains css page situation
│   ├── components # The various modules of the page are distributed, and their respective introductions are introduced in the README.md
│   ├── utils # Tools that may be needed for the page
│   ├── pages # File saved by page jump
│   ├── views # Jump page layout
│   ├── vuex # Route management file save page
│   └── router # Page Vue routing management for web page links
│
├── static # Files in this directory will not be processed by WebPack: they will be copied directly to the final packaging directory (absolute path)
│   ├── data  # Contains the data used by the visualization page
│   │    |──  Forecast # Order forecast
│   │    |──  ForecastPointChart # Data source for order forecast results-scatterplot
│   │    |──  StartHeatMapChart # Heat map of distribution of starting orders
│   │    |──  EndHeatMapChart # Heat map of end order distribution
│   │    |──  CalendarChart # Order status calendar heat map
│   │    |──  TadpoleChart # Street situation flow tadpole map
│   │    |──  multiputeMap # Order forecast results
│   │    |──  MoveToChart # Order situation overall regional migration map
│   │    |──  ChordChart # Order situation Overall street chord diagram (used in the pop-up window)
│   │    |──  RateLineChart # Line chart of the overall order change rate (used in the popup display section)
│   │    |──  OrderNumLineChart # Line chart of the combination of the travel distance of the order and the travel distance of the order (used in the pop-up window display section)
│   │    |──  LineCharts # Line chart of order changes
│   │    |──  PreBarChart # Histogram of overall order forecast
│   │    |──  wordCloud # Word Cloud Map of Popular Places for Orders
│   │    |──  DailyBarChart # Order forecast view, overall forecast histogram
│   ├── img # The background image required by the page
│   ├── script # Code required for data processing
│   └── js # Library files required for drawing
│
│
│
└── README.md 
```

## System screenshot

![Image 1](static/img/README/草图.bmp)

![Image 2](static/img/README/蝌蚪图.bmp)

![Image 3](static/img/README/预测.bmp)

![Image 4](static/img/README/天气情况分析.bmp)

## Environment 

* Data processing：`Python 3.8 `

* Dependency：`Echarts` `HighCharts` 

* System support：`Win10` 

* Programming environment:`pycharm、Vscode`

## About

* Those who are interested can pay attention to my personal official account, which will share relevant technologies and experience from time to time.

* 公众号名称：当生活遇上Coding

![公众号](static/img/README/微信公众号.jpg)