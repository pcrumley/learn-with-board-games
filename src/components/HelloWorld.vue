<template>
  <div class="hello">
    <div class="container">
    <GameList :navState="navState"/>
    </div>
  </div>
</template>

<script>
import GameList from  './GameList.vue'

export default {
  name: 'HelloWorld',
  props: ['navState'],
  components: {
    GameList
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  /*display: inline-block;*/
  margin: 0 10px;
}
a {
  color: #42b983;
}
.hello {
  margin-top: 50px;
  margin-right: 250px;
  margin-left: 250px;
}
</style>
