<template>
  <div class="box">
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-12">
        <div class="tile">
          <div class="tile is-parent is-2 is-vertical">
            <article class="tile is-child">
              <figure class="image">
                <img v-bind:src="game.img">
              </figure>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child has-text-left">
              <p class="title is-4">  <a :href="bgg_url" target="_blank">{{game.name}}</a> ({{game.yearpublished}})</p>
                Players: {{game.minplayers}} - {{game.maxplayers}} people
                <br>
                Playtime: {{game.playingtime}} minutes
                <br>
                User suggested age: {{game.user_suggested_age.toFixed(1)}} years

            </article>
          </div>
        </div>

      </div>
    </div>
    <div v-if="!isActive" class="box mybutton noselect"  @click="isActive = !isActive">
      Read more
    </div>
<!--
  <div class="tile is-ancestor">
<div class="tile is-3">
  <div class ="box">
    <img v-bind:src="game.img">
  </div>
</div>
<div class="tile">
  <div class = "box">
  <div class="title is-5">
  <p><a :href="bgg_url" target="_blank">{{game.name}}</a></p>
</div>
</div>
  </div>
</div>
-->

<article class="message"
  v-if="isActive">
  <div class="message-header">
       Game Description:
      <button class="delete" @click="isActive = !isActive"></button>
    </div>
  <div class="message-body">
    <div class="content has-text-left">
      <span  v-html="game.description"></span>
    </div>
<div class="content has-text-left">
      <p class="subtitle"> Top Comments: </p>

<ul>
  <li
    v-for="(comment, index) in comments"
    :key="index">
    <div class="box has-text-left">
    <span  v-html="comment"></span>
    </div>
  </li>
</ul>
</div>
</div>
</article>
    <!--
    <article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img v-bind:src="game.img">
    </p>
  </figure>
  <div class="media-content ">
    <div class="content">
      <p>
        <strong><a :href="bgg_url" target="_blank">{{game.name}}</a></strong>
        <br>

          <span  v-html="game.description"></span>
        </p>

    </div>


  </div>


  <div class="media-right">
    <strong>{{ game.overall_score.toFixed(2) }}</strong>/10
  </div>

</article>
-->
</div>
</template>

<script>
export default {
  name: 'GameListItem',
  props: ['game', 'comments'],
  data () {
    return {
      isActive: false
    }
  },
  computed: {
    bgg_url: function () {
      return `https://boardgamegeek.com/boardgame/${this.game.game_id}/`
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  /*list-style-type: none;*/
  margin-left: 0em
}
li {
  display: inline-block;
  padding:.2em;

}
a {
  color: var(--links-color);
}
.mybutton {
  background:  var(--accent-color);
}
</style>
