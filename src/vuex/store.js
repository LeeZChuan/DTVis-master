import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
         TimeDate : "2017-10-1",//日期存储
         TimeHour :0,
         
    },
    mutations:{
        updateCount(state,num)
        {
            state.count=num;
        }

    }
})

export default store