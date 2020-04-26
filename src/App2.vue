<template>
  <div id="app">
    <div v-if="!isLogin" class="login-view">
      <v-login @on-login="loginSuccess"></v-login>
    </div>
    <div class="app-view" v-if="isLogin">
      <v-app></v-app>
    </div>
  </div>
</template>

<script>
import vLogin from "./pages/login/index";
import vApp from "./pages/app/index";
export default {
  name: "App",
  components: {
    vLogin,
    vApp
  },
  data() {
    return {
      isLogin: false,
      user: {
        name: "",
        id: ""
      }
    };
  },
  mounted() {},
  methods: {
    loginSuccess(value) {
      //登录成功做持久化处理
      console.log("chengong");
      this.user.name = value.name;
      this.user.password = value.password;
      this.user.id = value.id;
      sessionStorage.setItem("userInfo", JSON.stringify(this.user));
      this.user.name = value.name;
      this.isLogin = true;
    }
  }
};
</script>

<style>
body,
html {
  margin: 0;
  padding: 0;
}

.app-view {
  width: 100%;
  min-height: 100vh;
}
.info {
  box-sizing: border-box;
  background: #fff;
  color: #000;
  padding: 20px;
  z-index: 9998;
  max-width: 400px;
}

.info .info-title {
  text-align: left;
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 10px;
}

.info .info-content {
  display: flex;
  width: 300px;
  text-align: left;
  flex-direction: row;
}

.info .info-content img {
  flex: 1;
  width: 60px;
  height: 60px;
}

.info .info-content .real-content {
  width: 200px;
  margin-left: 10px;
  font-size: 12px;
}

.info .info-close {
  display: block;
  position: absolute;
  top: 0px;
  right: 0px;
  padding: 10px;
  cursor: pointer;
}

#app {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  justify-content: center;
  min-height: 100vh;
}

/* .home {
  background: url(./assets/images/background2.png) no-repeat top center !important;
} */

.time {
  font-size: 16px;
  color: rgba(15, 166, 255, 0.3);
  position: absolute;
  right: 15px;
  top: 15px;
}

.nav {
  flex: 1;
  align-self: flex-start;
  display: flex;
}

.navList {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 280px;
}


</style>
