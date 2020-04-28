# Components组件用途解释
使用说明及命名规则

## 使用说明
1. vue文件用于组件开发，制作相关可视化网页组件
2. 其中css样式都在static文件中
3. 其中所有外部引用的js文件也在static文件中


## 可视化组件内容详细介绍

其中Pre文件是未定型的可视化组件文件

0. exp.vue 例子模块部分代码（作为参考项目）√-finsh
1. ForecastChart 预测的订单整体情况折线图界面 √-finsh
   ForecastChart 预测界面包含整体订单预测与局部订单预测（散点花图）
2. TadpoleChart 蝌蚪图（热力图）√-finsh
3. StartHeatMapChart (3D热力图）后续还可以添加一些交互功能 √-finsh
   EndHeatMapChart 终点订单情况热力图 √-finsh
4. Control 控制面板  unfinsh
5. multiputeMap 用于展示海口市地区订单情况散点雷达图
6. LineChart 出行距离与出行次数折线图√-finsh
7. map 出行订单数量散点图（花弦图）
8. CalendarChart 订单情况日期热力图√-finsh
9. MoveToChart 区域迁徙图 √-finsh
10. ChordChart 和弦图--用于展示该天整体订单街道流向情况 √-finsh
11. RateLineChart订单整体情况变化率折线图（用在弹窗展示部分）√-finsh
12. OrderNumLineChart 订单的出行距离与该订单出行距离数量组合折线图（用在弹窗展示部分） √-finsh
13. ParallelChart 平行坐标系--分析多个因素对出行量的影响（日期x1、天气x2、距离x3、时间x4、地区x5、订单数量x6）
14. FinishChart （柱状/折线图）--订单完成率，以周/月为单位，分析不同时间的订单完成率
15. 




## 特殊要求图使用说明
### 图名
1. 图例使用说明，需要进行图例规范命名，例如：xxxx_xxxx.vue
2. DTVis_xxx.vue xxx:代表的这个图的使用功能
3. 使用英文或者中文描述性词语对组件进行命名


## 颜色搭配

整体配色属于深蓝色色调，相对沉稳，符合商业用途。