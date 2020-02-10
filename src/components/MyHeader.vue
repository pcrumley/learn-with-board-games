<template>
  <nav class="navbar sticky noselect" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
      <span class="logo">
    <img src="../assets/logo.png" alt="Bulma: Free, open source, and modern CSS framework based on Flexbox" width="112" height="28">
  </span>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>

  </div>
  <div class="navbar-item is-hoverable is-size-5"
      :class="{ isClicked: navState =='overall',
      notClicked: navState !='overall'}"
      v-on:click="$emit('change-state', 'overall')"
      ><!--", 'overall')" -->
      Overall
  </div>
  <div class="navbar-item is-hoverable is-size-5"
    :class="{ isClicked: navState =='co-op',
    notClicked: navState !='co-op'}"

      v-on:click="$emit('change-state', 'co-op')" >
      Co-op Games
  </div>
  <div class="navbar-item is-hoverable is-size-5"
    :class="{ isClicked: navState =='logic',
    notClicked: navState !='logic'}"
    v-on:click="$emit('change-state', 'logic')" >
      Logic Games
  </div>
  <div class="navbar-item is-hoverable is-size-5"
  :class="{ isClicked: navState =='reasoning',
  notClicked: navState !='reasoning'}"
    v-on:click="$emit('change-state', 'reasoning')" >
      Reasoning
  </div>
  <div class="navbar-item is-hoverable is-size-5"
  :class="{ isClicked: navState =='math',
  notClicked: navState !='math'}"
    v-on:click="$emit('change-state', 'math')" >
      Math Games
  </div>
  <div class="navbar-item is-hoverable is-size-5"
    :class="{ isClicked: navState =='pattern',
    notClicked: navState !='pattern'}"
      v-on:click="$emit('change-state', 'pattern')">
      Pattern Matching
  </div>
  <div class="navbar-item is-hoverable is-size-5"
  :class="{ isClicked: navState =='memory',
  notClicked: navState !='memory'}"
    v-on:click="$emit('change-state', 'memory')">
      Memory
  </div>
  <!--
  <div class="navbar-item is-hoverable is-size-5"
    :class="{ isClicked: navState =='dexterity',
    notClicked: navState != 'dexterity'}"
      v-on:click="$emit('change-state', 'dexterity')">
      Dexterity
  </div>
  -->
  <!--
  <div class="navbar-item is-hoverable is-size-5"
    :class="{ isClicked: navState =='learn',
    notClicked: navState != 'learn'}"
      v-on:click="$emit('change-state', 'learn')">
      Easy to Learn
  </div>
-->
  </nav>
  <!--<div class="header sticky is-secondary" id="myHeader">
   <h1 class="title is-1" align="left">Gaming with kids.</h1>
 </div>-->
</template>

<script>
export default {
  name: 'MyHeader',
  props: ['navState']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
h1 {
  margin-left: 25px;
  color: #181E26;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: var(--links-color);
}
/* Style the header */
.header {
  padding: 10px 16px;
  background: var(--accent-color);
}

/* Page content */
.content {
  padding: 16px;
}
/* The sticky class is added to the header with JS when it reaches its scroll position */
.sticky {
  position: fixed;
  background: var(--accent-color);
  top: 0;
  z-index: 1000;
  width: 100%
}

/* Add some top padding to the page content to prevent sudden quick movement (as the header gets a new position at the top of the page (position:fixed and top:0) */
.sticky + .content {
  padding-top: 102px;
}
.logo {
  padding:20px;

}
.isClicked {
  color: #3966bfff;
}
.notClicked {
  color: #b7b7b7ff;
}
</style>
