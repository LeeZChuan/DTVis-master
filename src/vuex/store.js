import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
         TimeDate : "2017-10-1",//日期存储
         TimeHour :"0",
         
    },
    //存放同步函数方法
    mutations:{
        updateTimeDate(state,num)
        {
            state.TimeDate=num;
        },
        updateTimeHour(state,num)
        {
            state.TimeHour=num;
        }

    },
    //getters可以认为是store的计算属性
	getters:{
		NowTime(state){
				return state.TimeHour;
        }
    }
})

export default store