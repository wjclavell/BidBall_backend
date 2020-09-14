# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Incomplete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches and Present | Incomplete

## Project Description

This project will be a sports "betting" app (not real currency), in a similar style to DraftKings or FanDuel. Users
 will be able to signup/login and view all current sports games for the day. Users can make their picks on what team(s)
 they think will win and place a bet. Users will gain or lose virtual currency based on correct/incorrect picks
 . Users can view their current balance, favorite team/sport, and their stats. Games will be updated each day using a
  third-party api to retrieve game data.

## Wireframes

Upload images of wireframe to cloudinary and add the link here with a description of the specific wireframe. Do not include the actual image and have it render on the page.  

- [Mobile](https://res.cloudinary.com/wjclavell/image/upload/v1600036460/P4/SportsBettingMobile_iff43t.png)
- [Desktop](https://res.cloudinary.com/wjclavell/image/upload/v1600053553/P4/p4-desktop_mgscsk.png)

## Time/Priority Matrix 

Full list of features that have been prioritized based on the [Time and Priority Matrix](https://res.cloudinary.com/wjclavell/image/upload/v1600025693/P4/P4-backend-TPM.png)

### MVP/PostMVP

The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.  

#### MVP

- Authentication
- User model (name, email, username, password)
- Game model (teams, sport, scores, )
- Bet model (amount, team)
- Account model (currency, favorites, stats)
- Routes
- Allow user to choose favorite sport/team
- 100 coins on sign up

#### PostMVP 

- filter by sports
- betting history
- team description route/page
- plus 50 coins each new login day

## Functional Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional components, and by that we mean functions.  Try and capture what logic would need to be defined if the game was broken down into the following categories.

Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Authentication | H | 1hr | 1.5hr | -hr|
| User model | H | 1hr | -hr | -hr|
| Game model | H | 1hr | 2hr | -hr|
| Bet model | H | 2hr| -hr | -hr |
| Account model| M | 2hr | 2hr | -hr|
| Routes | H | 5hrs| 2hr | -hr |
| Sign up coins | M | 1hr | -hr | -hr|
| Favorites | M | 2hr | -hr | -hr|
| Total | - | 15hrs| -hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Filter | H | 2hr | -hr | -hr|
| Betting history | M | 4hr | -hr | -hr|
| Team description | M | 2hr | -hr | -hr|
| coins on login | M | 2hr | -hr | -hr|
| Total | - | 10hrs| -hrs | -hrs |

## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project. 

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