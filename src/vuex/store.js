import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        TimeDate: "2017-10-1",//日期存储
        TimeHour: "12",
        Recent: [["2017-05-13", "0.282%", "98.092%", "2.918%", "0.203%"],
        ["2017-05-14", "0.336%", "97.574%", "2.901%", "0.422%"],
        ["2017-05-15", "0.36%", "97.851%", "3.241%", "0.218%"],
        ["2017-05-16", "0.391%", "97.759%", "3.509%", "0.143%"],
        ["2017-05-17", "0.353%", "97.947%", "3.379%", "0.153%"],
        ["2017-09-30", "0.434%", "96.481%", "4.263%", "1.39%"],
        ["2017-10-01", "0.631%", "97.477%", "4.732%", "0.364%"]],
        Forecast:[],


    },
    //存放同步函数方法
    mutations: {
        updateTimeDate(state, num) {
            state.TimeDate = num;
        },
        updateTimeHour(state, num) {
            state.TimeHour = num;
        },
        updateForecast(state,num)
        {
            state.Forecast.push(num);
        }

    },
    //getters可以认为是store的计算属性
    getters: {
        NowTime(state) {
            return state.TimeHour;
        },
        GetNowRecentLong(state) {
            for (let i = 0; i < 7; i++) {
                if(state.TimeDate==state.Recent[i][0])
                {
                    return state.Recent[i][1];
                }
                else{
                }
            }
        },
        GetNowRecentFast(state) {
            for (let i = 0; i < 7; i++) {
                if(state.TimeDate==state.Recent[i][0])
                {
                    return state.Recent[i][2];
                }
                else{
                }
            }
        },
        GetNowRecentHigh(state) {
            for (let i = 0; i < 7; i++) {
                if(state.TimeDate==state.Recent[i][0])
                {
                    return state.Recent[i][3];
                }
                else{
                }
            }
        },
        GetNowRecentLongTime(state) {
            for (let i = 0; i < 7; i++) {
                if(state.TimeDate==state.Recent[i][0])
                {
                    return state.Recent[i][4];
                }
                else{
                }
            }
        },
        GetForecast(state) {
           return state.Forecast;
        },
    }
})

export default store