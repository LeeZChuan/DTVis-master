<template>
  <transition name="dialog">
    <div class="dialog-wrap" v-show='showWin' @mousedown='down' @mouseup='up' @mousemove='move' ref='dialogArea'>
      <div class="modal"></div>
      <div class="dialog" ref='dialog' :style='{top:top+"px",left:left+"px",width:curWidth+"px",height:curHeight+"px"}'>
        <div class="title-wrap">
          <slot name='title'>标题</slot>
          <div class="title" data-type='move'></div>
        </div>
        <div class="content-wrap">
          <div class="content">
            <slot name='content'/>
          </div>
        </div>
        <div class="submit" @click='submit'>确定</div>
        <div class="max-win" :class='max?"restore":""' @click='maxWin'></div>
        <div class="close" @click="closeWin"></div>
        <div class="resize" data-type='resize'></div>
      </div>
    </div>  
  </transition>
</template>

<script>
export default {
  props:{
    showWin:{
      type:Boolean
    },
    width:{
      type:[String,Number],
      default:500
    },
    height:{
      type:[String,Number],
      default:300
    }
  },
  data() {
    return {
    startX:0,
    startY:0,
    Otop:0,
    Oleft:0,
    top:0,
    left:0,
    Owidth:this.width,
    Oheight:this.height,
    curWidth:this.width,
    curHeight:this.height,
    minWidth:240,
    minHeight:150,
    canMove:false,
    canResize:false,
    max:false
    }
  },
  components: {

  },
  methods: {
  	submit(){
      this.closeWin();
      this.$emit('submit', false)
    },
    closeWin(){
      this.$emit('update:showWin', false)
    },
    up(e){
      this.canMove=false;
      this.canResize=false;
      if(e.target.dataset.type=='move'){
        this.setTandL(e);
      }else if(e.target.dataset.type=='resize'){
        this.setWandH(e);
      }
    },
    down(e){
      e.preventDefault();
      if(this.max){
        return;
      }
      if(e.target.dataset.type=='move'){
        this.setXandY(e);
        this.setTandL(e);
        this.canMove=true;
      }else if(e.target.dataset.type=='resize'){
        this.setXandY(e);
        this.setWandH(e);
        this.canResize=true;
      }
    },
    move(e){
      e.preventDefault();
      if(this.canMove){
        this.left=e.pageX-this.startX+this.Oleft;
        this.top=e.pageY-this.startY+this.Otop;
      }else if(this.canResize){
        var w=e.pageX-this.startX+this.Owidth;
        var h=e.pageY-this.startY+this.Oheight;
        this.curWidth=w<this.minWidth?this.minWidth:w;
        this.curHeight=h<this.minHeight?this.minHeight:h;
      }
    },
    setXandY(e){
      this.startX=e.pageX;
      this.startY=e.pageY;
    },
    setTandL(e){
      this.Otop=this.$refs.dialog.offsetTop;
      this.Oleft=this.$refs.dialog.offsetLeft;
    },
    setWandH(e){
      this.Owidth=this.$refs.dialog.offsetWidth;
      this.Oheight=this.$refs.dialog.offsetHeight;
    },
    maxWin(){
      this.max=!this.max;
      if(this.max){
        var h=this.$refs.dialogArea.offsetHeight;
        var w=this.$refs.dialogArea.offsetWidth;
        this.curWidth=w;
        this.curHeight=h;
        this.top=0;
        this.left=0;
      }else{
        this.curWidth=this.Owidth;
        this.curHeight=this.Oheight;
        this.top=this.Otop;
        this.left=this.Oleft;
      }
    },
    initSize(){
      var refs=this.$refs;
      var top=(document.documentElement.clientHeight-this.height)/2;
      var left=(document.documentElement.clientWidth-this.width)/2;
      this.top=this.Otop=top;
      this.left=this.Oleft=left;
    }
  },
  watch:{
    
  },
  mounted(){
    this.initSize();
  }
}
</script>

<style scoped>
.dialog-wrap{
  text-align: left;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 999;
}
.modal{
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.3);
}
.dialog{
  min-width: 240px;
  background: white;
  position: absolute;
  margin: 0 auto;
}
.title-wrap{
  width: 100%;
  height: 40px;
  line-height: 40px;
  padding: 0 80px 0 15px;
  background: #f1f1f1;
  position: absolute;
  top: 0;
  left: 0;
  box-sizing: border-box;
}
.title{
  width: calc(100% - 80px);
  height: 100%;
  cursor: move; 
  user-select: none;
  position: absolute;
  top: 0;
  left: 0;
}
.content-wrap{
  padding: 60px 15px;
  height: 100%;
  box-sizing: border-box;
}
.content{
  height: 100%;
  box-sizing: border-box;
  overflow: auto;
}
.submit{
  background: rgb(55, 173, 255);
  color: #fff;
  width: 70px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border-radius: 3px;
  cursor: pointer;
  position: absolute;
  bottom: 0;
  right: 0;
  margin: 10px;
  font-size: 14px;
}
.submit:hover{
  opacity: 0.7;
}
.close,
.max-win{
  width: 20px;
  height: 20px;
  text-align: center;
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}
.close:hover,
.max-win:hover{
  opacity: 0.7;
}
.max-win{
  right: 45px;
  background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAqUlEQVQ4T9XTMQ4BQRiG4WcP4AAKrQtoaByAXiFRcQKFSyhcQCkatQOIRBRcQCkStROQTbaYYiUbQzKmnv/N+33zT4YTWr5z9hmeaOAWycwZ1ySAM/SCNEusipQfGQ7RLIAdPDCIAYZVT9FOGthHHXmP6bzyu3X9U8MJ7th+8A1LI29wwCJpYA3HwvCCdUXb0sgjjANA3uU8BlhxtvTa7/Zwh26MWjB7fgHwRkuR58BbzAAAAABJRU5ErkJggg==');
}
.restore{
  background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAmUlEQVQ4T2NkoDJgRDOPnYGBwZICO+6gGyjLwMDwiIGB4SAZhmoxMDC04zIQXZwY81czMDAco4mBRQwMDL3EOAGHGlAwPWFgYIC7EGSgBQMDQxgZhv5nYGAYNZCBYTQMSUo8NEk2yC4oAmU9akUK2GCaGVjBwMBwjaTQgyi2R8p6cBfKMDAwqJBhGEzLcQYGhp8wDjnlHl67ATeRPO4mAG3EAAAAAElFTkSuQmCC');
}
.close{
  background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAA10lEQVQ4T73UMQ9BMRDA8f/7GBLfxm4hMZEYmdhYBAsbE5vJ4Cvw6eSkJw2v7WlfdHt57a937fUqoAV0gCtlYwjcK2AA3IAzMM00T8AE6AkoYwcsMlHFNsBawVxUsT2wFMQH5fsAzIAjME+kr3PfWB1oRYMbf0aoQdXu7n5GswiBsvbrfLzLCx5JDPRRuUGZu0pVQgoU9AKMXbrJWrWAmrqYxaBiWxdhUcqxSwlG+peysbwWc2FbsGjx+yn/gikabA6Ntq8mG2xfUm4DXfd2Mxv2a9kIeDwBWWVE6C9M+OEAAAAASUVORK5CYII=');
}
.resize{
  width: 20px;
  height: 20px;
  position: absolute;
  bottom: -10px;
  right: -10px;
  cursor: nw-resize;
}
.dialog-enter-active,
.dialog-leave-active{
  transition: all 0.2s;
}
.dialog-enter-active .dialog,
.dialog-leave-active .dialog{
  transition: all 0.2s;
}
.dialog-enter .dialog,
.dialog-leave-to .dialog{
  transform: scale3d(.1, .1, .1);
}
.dialog-enter,
.dialog-leave-to{
  opacity: 0;
}
</style>