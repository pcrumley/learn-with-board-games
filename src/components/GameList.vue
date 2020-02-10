<template>
  <div>
        <game-list-item
          v-for="item in topGames"
          v-bind:game="gamesData[item]"
          v-bind:comments="topComments[item]"
          v-bind:key="item.id"
        >

        </game-list-item>
        <!--{{gamesData.entries()}}-->
        <!--<ol v-for="game in games"
          v-bind:key="game.id">
          {{ game.text }}
        </ol>
      -->
  </div>
</template>

<script>
import GameListItem from  './GameListItem.vue'
import GAMES_DATA from '../json/data.json'
export default {
  name: 'GameList',
  //gamesData: GAMES_DATA,
  data () {
    return {
      gamesData: GAMES_DATA,
      coop: false
    }
  },
  props: ['navState'],
  computed: {
    topGames: function () {
      var tmpArr = []
      for (var i = 0; i < this.gamesData.best_games.length; i++) {
        if (this.navState == 'co-op') {
          if (i === this.gamesData['co-operative_score_games'].length) { break }
          tmpArr.push(this.gamesData['co-operative_score_games'][i])
        } else if (this.navState == 'overall') {
          tmpArr.push(this.gamesData.best_games[i])
        } else if (this.navState == 'logic') {
          if (i === this.gamesData['logic_score_games'].length) { break }
          tmpArr.push(this.gamesData['logic_score_games'][i])
        } else if (this.navState == 'reasoning') {
          if (i === this.gamesData['deductive_score_games'].length) { break }
          tmpArr.push(this.gamesData['deductive_score_games'][i])
        }  else if (this.navState == 'learn') {
          if (i === this.gamesData['learning_score_games'].length) { break }
          tmpArr.push(this.gamesData['learning_score_games'][i])
        } else if (this.navState == 'dexterity') {
          if (i === this.gamesData['dexterity_score_games'].length) { break }
          tmpArr.push(this.gamesData['dexterity_score_games'][i])
        } else if (this.navState == 'math') {
          if (i === this.gamesData['math_score_games'].length) { break }
          tmpArr.push(this.gamesData['math_score_games'][i])
        } else if (this.navState == 'pattern') {
          if (i === this.gamesData['pattern_score_games'].length) { break }
          tmpArr.push(this.gamesData['pattern_score_games'][i])
        } else if (this.navState == 'memory') {
            if (i === this.gamesData['memorization_score_games'].length) { break }
          tmpArr.push(this.gamesData['memorization_score_games'][i])
        }

      }
      // `this` points to the vm instance
      //let tmpArr = [...this.gamesData.best_games].map( id => this.gamesData[id])
      //return tmpArr.sort().map(g => g.game_id)//.sort()//((a, b)=>{b.overall_score - a.overall_score}).map(g => g.game_id)
      return tmpArr.sort((a,b) => this.gamesData[b].overall_score - this.gamesData[a].overall_score).slice(0, 20)
      //return ['130792', '16142', '247314', '256952', '92644']
    },
    topComments: function () {
      var tmpObj = {}
      for (var i = 0; i < this.topGames.length; i++) {
        if (this.navState == 'co-op') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['co-operative_score_comments']
        } else if (this.navState == 'overall') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]].best_comments
        } else if (this.navState == 'logic') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['logic_score_comments']
        } else if (this.navState == 'reasoning') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['deductive_score_comments']
        }  else if (this.navState == 'learn') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['learning_score_comments']
        } else if (this.navState == 'math') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['math_score_comments']
        } else if (this.navState == 'pattern') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['pattern_score_comments']
        } else if (this.navState == 'memory') {
          tmpObj[this.topGames[i]] = this.gamesData[this.topGames[i]]['memorization_score_comments']
        }
      }
      return tmpObj

      //return ['130792', '16142', '247314', '256952', '92644']
    }
  },
  components: {
    //HelloWorld,
    GameListItem
  }
}
</script>

<style>

</style>
