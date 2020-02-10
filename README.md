# Learn With Board Games
An insight data-project that helps parents choose board games that teach new concepts to children, and highlights what to focus on when playing games with your kids, web app is availabe [here](https://pcrumley.github.io).

## Problem Statement

Most of the growth in the board game industry is driven by complex games that adults play with other adults. However, it is hard for parents to find interesting games to play with their children because many popular games are too difficult. I built a web-app that scrapes a hobbyist gaming website, finding the best game to play with children by adjusting for biases in the data, as well as using natural language processing on user comments to find skills that the game is good at teaching.

## Implementation

The code used to scrape [BoardGameGeek](https://www.boardgamegeek.com/) is `bbg_scraper.py` it downloads the top ~7000 games and 200 most recent comments for each game. Each game is stored its own  JSON file in the `bbg_json/` directory. The Schema for each JSON is as follows e.g.,
```
{
  name: Number Chase
  yearpublished: 2006 
  description: "In Number Chase ... whoever first collects three cards wins!" 
  img_url: "https://.../pic456666.jpg"
  user_suggested_age: 5.0 
  user_suggested_players: [
    {
      player_num: 1
      Best: 0 
      Recommended: 0, 
      Not Recommended: 0
    } 
    ...
    { ... }
  ] 
  minplayers: 2 
  maxplayers: 5
  playingtime: 15
  minplaytime: 15 
  maxplaytime: 15 
  age: 6, 
  stats: {
    usersrated: 54.0
    average: 5.94259 
    bayesaverage: 5.51699 
    stddev: 1.19359 
    median: 0.0 
    owned: 155.0
    trading: 6.0
    wanting: 4.0
    wishing: 8.0 
    numcomments: 37.0
    numweights: 7.0
    averageweight: 1.2857
  } 
  comments": [
    {
      rating: N/A 
      username: AnnC
      comment: "05-10, 2-5 players, best with 2, 15 mins. Given to OT."
    }
    ...
    { ... }
  ]
}
```
Once all of the games are scraped, you have to scrape all of the thumb_nail images using `thumb_grabber.py`

Finally, the linear regression and sentiment analysis scores are calculated for each game using `gen_scores.py`. This returns a JSON file called data.json. data.json then should be copied and pasted into the `src/json` folder of the `vue-web-app`. The front-end then sorts and displays the games.
