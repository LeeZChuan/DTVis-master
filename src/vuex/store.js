import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
         TimeDate : "2017-10-1",//日期存储
         TimeHour :0,
         
    },
    mutations:{
        updateTimeDate(state,num)
        {
            state.TimeDate=num;
        },
        updateTimeHour(state,num)
        {
            state.TimeHour=num;
        }

    }
})

export default store