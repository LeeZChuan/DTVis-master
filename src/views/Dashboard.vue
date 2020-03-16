<template>
  <section>
    <mu-appbar title="后台管理" :zDepth="2">
      <mu-icon value="settings_input_svideo" color="#0091ea" slot="left">
      </mu-icon>
      <mu-chip backgroundColor="rgba(0, 0, 0, 0)" slot="right">
        <mu-avatar src="https://avatars1.githubusercontent.com/u/22613580?v=4&s=40" :size="32">
        </mu-avatar><span class="bar-name">jawei</span>
      </mu-chip>
    </mu-appbar>
    <mu-row>
      <mu-col width="20" tablet="20" desktop="20" class="row-left ">
        <mu-list class="list-menu">
          <mu-list-item title="仪表盘" describeText="交通流量可视化" class="menu-active">
            <mu-icon value="av_timer" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="文章" :toggleNested="true">
            <mu-icon value="art_track" slot="left">
            </mu-icon>
            <mu-list-item title="写文章" slot="nested">
              <mu-icon value="border_color" slot="left">
              </mu-icon>
            </mu-list-item>
            <mu-list-item title="分类" slot="nested">
              <mu-icon value="folder" slot="left">
              </mu-icon>
            </mu-list-item>
          </mu-list-item>
          <mu-list-item title="多媒体">
            <mu-icon value="image" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="页面">
            <mu-icon value="pages" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="评论">
            <mu-icon value="comment" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="外观">
            <mu-icon value="format_paint" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="插件">
            <mu-icon value="settings_input_hdmi" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="用户">
            <mu-icon value="people" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="工具">
            <mu-icon value="build" slot="left">
            </mu-icon>
          </mu-list-item>
          <mu-list-item title="设置">
            <mu-icon value="settings" slot="left">
            </mu-icon>
          </mu-list-item>
        </mu-list>
      </mu-col>
      <mu-col width="80" tablet="80" desktop="80">
        <mu-row :gutter="true">
          <mu-col width="100" tablet="100" desktop="100">
            <mu-sub-header>
              仪表盘
            </mu-sub-header>
          </mu-col>
          <mu-col width="100" tablet="50" desktop="50" class="board-left">
            <mu-paper class="paper-draft">
              <mu-sub-header>
                概览
              </mu-sub-header>
              <mu-chip backgroundColor="rgba(0, 0, 0, 0)" class="overview-chip">
                <mu-avatar backgroundColor="rgba(0, 0, 0, 0)" color="#000000" icon="art_track" :size="32">
                </mu-avatar><span>16篇文章</span>
              </mu-chip>
              <mu-chip backgroundColor="rgba(0, 0, 0, 0)" class="overview-chip">
                <mu-avatar backgroundColor="rgba(0, 0, 0, 0)" color="#000000" icon="restore_page" :size="32">
                </mu-avatar><span>1个页面</span>
              </mu-chip>
              <mu-chip backgroundColor="rgba(0, 0, 0, 0)" class="overview-chip">
                <mu-avatar backgroundColor="rgba(0, 0, 0, 0)" color="#000000" icon="comment" :size="32">
                </mu-avatar><span>20条评论</span>
              </mu-chip>
              <br /><span>&nbsp;&nbsp;Vue-Layout 1.0.0，由jawei创建。</span>
              <mu-raised-button label="检查更新">
              </mu-raised-button>
            </mu-paper>
          </mu-col>
          <mu-col width="100" tablet="50" desktop="50" class="board-right">
            <mu-paper class="paper-draft">
              <mu-sub-header>
                快速草稿
              </mu-sub-header>
              <mu-text-field type="text" hintText="标题" :fullWidth="true">
              </mu-text-field>
              <mu-text-field type="text" hintText="在想些什么？" :fullWidth="true" :multiLine="true" :rows="5" :rowsMax="5" :maxLength="1024">
              </mu-text-field>
              <mu-raised-button label="保存草稿">
              </mu-raised-button>
            </mu-paper>
          </mu-col>
          <mu-col width="100" tablet="50" desktop="50" class="board-left">
            <mu-paper class="paper-draft">
              <mu-sub-header>
                活动
              </mu-sub-header><span>近期发布</span>
              <mu-row>
                <mu-col width="30" tablet="30" desktop="30">
                  <span>08-14 0:47</span>
                </mu-col>
                <mu-col width="70" tablet="70" desktop="70">
                  <span>Vue-Layout 1.0发布</span>
                </mu-col>
                <mu-col width="30" tablet="30" desktop="30">
                  <span>08-15 1:21</span>
                </mu-col>
                <mu-col width="70" tablet="70" desktop="70">
                  <span>我生前，也是做前端的</span>
                </mu-col>
                <mu-col width="30" tablet="30" desktop="30">
                  <span>昨天 7点</span>
                </mu-col>
                <mu-col width="70" tablet="70" desktop="70">
                  <span>！@#￥%……&*（）</span>
                </mu-col>
                <mu-col width="30" tablet="30" desktop="30">
                  <span>前天 6点</span>
                </mu-col>
                <mu-col width="70" tablet="70" desktop="70">
                  <span>！@#￥%……&*（）</span>
                </mu-col>
              </mu-row>
            </mu-paper>
          </mu-col>
        </mu-row>
      </mu-col>
    </mu-row>
  </section>
</template>
<style scoped>
  .bar-name {
    color: white;
  }
  .row-left {
    border-right: 1px dashed rgba(0, 0, 0, 0.1);
  }
  .menu-active {
    border-left: 2px solid lightblue;
  }
  .board-left,
  .board-right {
    padding: 5px;
  }
  .paper-draft {
    padding: 10px;
  }
  .list-menu {
    background: #eeeeee;
  }
</style>
