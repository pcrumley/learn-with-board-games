<template>
  <div id="app">
    <MyHeader
      :navState = "navState"
      @change-state="navState=$event"/>
      <section class="hero is-medium is-bold">
        <div class="hero-body">
          <div class="container" id='main-title'>
            <h1 class="title is-1" >
              Gaming with kids
            </h1>
            <h2 class="subtitle" id='sub-title'>
              More board games. Fewer boring games.
            </h2>
          </div>
        </div>
      </section>
    <HelloWorld :navState ="navState"/>

    <MyFooter/>
  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyFooter from './components/MyFooter.vue'
import MyHeader from './components/MyHeader.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    MyFooter,
    MyHeader
  },
  data () {
    return {
      navState: 'overall'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  --accent-color:#f3f3f3ff;
  --links-color: #3966bfff;
  --secondary-color: #D7D7D9;
  margin-top: 10px;

}
.hero {
  background: #f3f3f3ff;
  top: 0px;
}
#sub-title {
  text-align:  right;
}
#main-title {
  float: left;
  padding-left: 2rem;
}
.noselect {
  cursor: pointer;
  -webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
     -khtml-user-select: none; /* Konqueror HTML */
       -moz-user-select: none; /* Old versions of Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
            user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Opera and Firefox */
}
</style>
