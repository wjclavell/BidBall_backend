# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Work-plan / Priority Matrix / Timeline `backend`| Complete
|Day 1| Create app and configure JWT auth | Complete
|Day 2| Set up models | Incomplete
|Day 3| Set up views| Incomplete
|Day 3| Set up routes | Incomplete
|Day 4| Test the endpoints/routes/CRUD | Incomplete


## Project Description

This project will be a sports "betting" app (not real currency), in a similar style to DraftKings or FanDuel. Users
 will be able to signup/login and view all current sports games for the day. Users can make their picks on what team(s)
 they think will win and place a bet. Users will gain or lose virtual currency based on correct/incorrect picks
 . Users can view their current balance, favorite team/sport, and their stats. Games will be updated each day using a
  third-party api to retrieve game data.

## Models

**User**    
*name, email, username, password, balance, correct, incorrect, favorite*    
*Has many Bids*

**Game**    
*team1, team2, sport, score1, score2*  
*Has many bids*

**Bid**     
*owner\*, game\*, amount, team*

>\* references to parent models

## Time/Priority Matrix 

Full list of features that have been prioritized based on the [Time and Priority Matrix](https://res.cloudinary.com/wjclavell/image/upload/v1600025693/P4/P4-backend-TPM.png)

### MVP/PostMVP

The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.  

#### MVP

- Authentication
- User model (name, email, username, password, balance, correct, incorrect, favorite)
- Game model (teams, sport, scores, )
- Bid model (user, game, amount, team)
- Views
- Routes
- Allow user to choose favorite sport/team
- 100 coins on sign up

#### PostMVP 

- filter by sports
- betting history
- team description route/page
- plus 50 coins each new login day

## Functional Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional
 components.

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Authentication | H | 1hr | 1hr | -hr|
| User model | H | 1hr | 1hr | -hr|
| Game model | H | 1hr | 1.5hr | -hr|
| Bet model | H | 2hr| 1.5hr | -hr |
| Account model| M | 2hr | -hr | -hr|
| Views| H | 5hr | -hr | -hr|
| Routes | H | 2hrs| -hr | -hr |
| Sign up coins | M | 1hr | .5hr | -hr|
| Favorites | M | 2hr | -hr | -hr|
| Total | - | 17hrs| 5.5hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Filter | H | 2hr | -hr | -hr|
| Betting history | M | 4hr | -hr | -hr|
| Team description | M | 2hr | -hr | -hr|
| coins on login | M | 2hr | -hr | -hr|
| Total | - | 10hrs| -hrs | -hrs |

## Additional Libraries
- Flask
- Restframework
- JWT

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

## Previous Project Worksheet
 - [Readme's](https://github.com/jkeohan/fewd-class-repo/tree/master/final-project-worksheet/project-worksheet-examples)
 - [Best of class readme](https://github.com/jkeohan/fewd-class-repo/blob/master/final-project-worksheet/project-worksheet-examples/portfolio-gracie.md)