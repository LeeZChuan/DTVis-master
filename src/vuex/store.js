import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
         TimeDate : "2017-10-1",//日期存储
         Timehour :0
    }
})

export default store