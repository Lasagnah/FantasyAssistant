## 1. Team Info and Policies 
### Team Members and Roles 
* Lily Stauffer – Product Owner 
* Yohanse Nurga  - Scrum Master 
* Akhil Jobi – Database Manager 
* Mahir Sadique – Frontend Developer  
* Syed - Backend Developer
### Relevant Artifacts
* [Lasagnah/FantasyAssistant · GitHub](https://github.com/Lasagnah/FantasyAssistant) 
### Communication Channels 
* FantasyAssistant Discord Channel 
## 2. Product Description 
### Description:
* This project plans to create an assistant for fantasy sports drafting. It will include a way to create teams and model the drafting process, while including an LLM to give recommendations to users for players to pick. It will also include an algorithm to predict the outcome of games given two teams. 
### Major Features: 
* Team creation/drafting simulation 
* Outcome prediction 
* LLM to help during drafting 
* Generation of visualizations 
### Stretch Goals: 
* Models to apply to multiple sports 
* Increasing model accuracy 
## 3. Use Cases 
### Use Case: Draft Team in Fantasy Sports 
* Goal In Context: Enable a user to draft an optimal team for their fantasy sports league using AI-assisted recommendations.  
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions 
    * User has access to AI systems.  
    * League settings and scoring rules are configured. 
    * Draft has been initiated.  
* Success End Condition: User has successfully drafted a complete team that adheres to league rules and maximizes potential points based on AI recommendations. 
* Failed End Condition: Draft is incomplete, team violates league rules, or user is unsatisfied with the drafted team. 
* Primary Actor: Fantasy Sports Player 
* Trigger: User initiates the draft process or responds to their turn in an ongoing draft.  
* Main Success Scenario: 
1. System presents current draft state and available players. 
2. System analyzes league scoring rules, remaining players, and team needs. 
3. System generates and presents top recommendations for the next draft pick. 
4. User reviews recommendations and player statistics. 
5. User selects a player to draft. 
6. System confirms the selection and updates the user's team roster. 
7. Steps 1-6 repeat until the user's team is complete. 
Extensions:  
* 2a. Unable to analyze league rules or player data: 
    * System notifies user of the issue. 
    * System provides option to proceed with limited functionality or contact support. 
* 3a. No suitable recommendations available: 
    * System informs user and suggests broadening search criteria. 
* 5a. User disagrees with recommendations: 
    * User requests alternative recommendations. 
    * System generates new recommendations based on adjusted criteria. 
    * Return to step 4. 
* 5b. User's preferred player is already drafted: 
    * System alerts user and suggests alternatives. 
    * Return to step 4. 
* 6a. Selected player violates league rules (e.g., salary cap, roster limits): 
    * System warns user of the violation. 
    * System suggests alternatives that comply with rules. 
    * Return to step 4. 
### Use Case: Trading Players in Fantasy Sports 
* Goal In Context: Enable a user to swap players for another player.  
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions 
    * User has access to AI system 
    * Draft has been initiated or completed.  
* Success End Condition: User has successfully completed a trade of players or swapped a player.  
* Failed End Condition: User is unable to swap a player onto their team for some reason (e.g., other player denies trade offer, player unavailable) 
* Primary Actor: Fantasy Sports Player 
* Trigger: User attempts to initiate a trade.  
* Main Success Scenario:  
1. System presents current draft state and available players. 
2. User attempts to create a trade offer.  
3. User 2 accepts or denies trade offer.  
4. If User 2 accepts the trade offer, swap the desired players.  
5. If User 2 denies the trade offer, close the trade offer.  
* Extensions: 
* 2a. Selected players violate league rules (e.g., salary cap, roster limits): 
    * System warns user of the violation. 
    * System suggests alternatives that comply with rules. 
    * Return to step 1.  
### Use Case: Waiver Wire Analysis 
* Goal In Context: Enables users to pick up the best available players and drop a player from your team 
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions:   
    * The players to be picked up is available in the waiver wire  
    * The user has an available roster spot or a player they are willing to drop 
* Succes End Condition: The user was successfully able to pick up a player from the waiver wire  
* Failed End Conditions: The user wasn't able to pick up the player they put in claim from the waiver wire  
* Primary Actor: Fantasy Sports player  
* Trigger: User puts in a claim for a player in the waiver wire  
* Main Succes Scenario:  
1. System shows the user what players are available in the waiver wire  
2. The user decides what player they want from the waiver wire and what player they want to drop from the roster  
3. The user adds the player or put the claim in the for the player, and click the drop button from roster they want to drop  
4. The system asks for the confirmation for the selections that they choose, and they update the roster  
* Extensions:  
    * The selected player is no longer available in the waiver wire list because it was picked by another team  
    * The users team roster is full and they don't want to drop any players from the roster 
### Use Case: Lineup Optimization 
* Goal In Context: Enables user to put the best lineup each week 
* Scope: Fantasy Basketball Assistant System 
* Level: User Goal 
* Precondition:  
    * Users team and player stats are loaded into the analyzer 
    * League scoring system must be understood by the analyzer 
* Success End Condition: User has updated lineup to the best potential based on projections and Analyzer suggestions 
* Failed End Condition: Analyzer receives outdated, or wrong player data and user does not create the best possible lineup 
* Primary Actor: Fantasy Sports Player 
* Trigger: The user requests lineup optimization to maximize their team’s performance based on current player statuses, matchups, or recent performance. 
* Main Success Scenario: 
1. User provides analyzer with current roster, league scoring rules 
2. Analyzer collects stats and league scoring rules and player performance, matchup and other factor that might impact the player 
3. Apply algorithm to suggest best possible lineup, selecting players who projects the most points 
4. Present lineup to user and provide rationale behind the recommendations 
5. User can review recommendations and make necessary adjustments 
* Extensions: 
    * Analyzer can handle changes to lineup such as injuries, trades or other mid season adjustments 
    * Incorporate user preferences for specific players 
    * Provide new recommendations in response to new information or last-minute injury reports 
### Use Case: Injury Management 
* Goal In Context: Enable players to be substituted when they are injured 
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal  
* Preconditions: 
    * System notifies user that their is an injured player in the starting lineup 
    * User picks and substitutes a player from available bench players 
* Success End Condition: User substituted an injured player successfully  
* Failed End Condition: substituted player might not be the best in statistical stand point, compared to the injured player 
* Primary Actor: Fantasy Sports Player 
* Trigger: Lineup player injury 
* Main Success Scenario: If the substitute has same level of stat with the injured player 
## 4. Non-Functional Requirements 
* Every year/season that goes by, our model and program would have to be updated/trained again. 
* System should be available 24/7 and be able to provide responses quickly 
* UI should be user friendly allowing users to manage and utilize features  
## 5. External Requirements 
* When drafting, a user may attempt to draft a player by inputting their name in the “FirstName, LastName” format.  
* When drafting, a user may attempt to trade a player by inputting “trade Player1 Player2”. 
* If a user’s input does not match any of the previous inputs, then the user will be notified, and they will continue drafting.  
* The product should be a basic Python script with a few extra files/folders attached to make it easily runnable.  
## 6. Team Process Description  
### Tools
* Tools we are going to be using includes Python, Pytorch, LLM packages, and Data Science packages, as well as PostgreSQL for our database. 
    * We will be using Python because it is the easiest programming language for what we are trying to accomplish. 
    * We will be using Pytorch, LLM packages, and Data Science packages to make it easier to implement the things they are associated with, so that we don't have to create the things from scratch. 
    * We will be using PostgreSQL for our database because it's easy and open-source. It's starting to become an industry standard. 
### Team member roles
* Lily's role is the Product Owner, her job is to help define what goes into the product. She also is helping with development where she can. She chose this role because she was the one to pitch this product, so she already had a view for what the product would be. The team needs this role filled to have a solid way forward and a solid list of goals for development. 
* Yohanse's role is the ScrumMaster, his job is to help the developers be able to do what they need to do. He will try to find ways to solve problems that occur during the process of building our project.
* Akhil's role is the Database Manager, his job is to create and manage the database and data systems. He has to make sure the data is up to date and accurate, and the developers can understand how to integrate data and ensure data consistency across systems. He chose this role because it is a crucial part of this project since we will be using a lot of data from various different databases, and he can grow his knowledge about implementing effective database queries. The team needs this role filled because this project revolves around efficiently managing vast amounts of data, and a database manager ensures data consistency and accuracy.
* Mahir's role is the front-end developer, responsible for creating the interface that the user interacts with in the program. His job is to design and implement a simple UI that asks for input, ensuring that the user experience is intuitive and smooth. The team needs this role filled because the success of the project depends on having a user-friendly interface that facilitates interaction with the system.
* Syed's role is the Backend developer, his job is to create the way that our program responds to the input from the user.
### Documentation Plan
* Within the Docs folder, we will create a guide.md file which is a guide for the functionality for the user. 
    * Includes examples of importing drafts, and running drafts
    * Includes examples of interacting with the LLM and game prediction algorithm
### Schedule
* Developer's Schedule
    * Create system infrastructure by October 4th.
    * Create system database by October 4th. 
    * Train system by October 25th.
    * Create LLM by November 29th.
    * Process external feedback December 6th.
### Risks
* The biggest risk has to do with our data. If we don't have a good dataset or way of storing our data, our product just can't really work well or in some cases even at all. 
* Another potential risk has to do with the data being inaccurate or outdated which could lead to bad recommendations. Even if a player is injured or traded and the data isn't updated, it can make our system unreliable. 
* Another risk can be trying to add too many features to our product which can lead us to missed deadline and lose focus on the main idea. With features such as advanced analytics, and custom tools it can be tempting to include all of these, so it's crucial to prioritize key features. 
* If the UI does not properly validate user inputs (like incorrect formats or missing data), this can lead to errors in the backend or incorrect data processing, affecting the overall system reliability.
* Another potential risk would not getting stats of the players
### External Feedback
* We will be processing external feedback the week of December 6th, which is basically after we have most of our product finished. We do this then because at that point, we have everything set up and we are able to easily incorporate feedback that doesn't fundamentally change how our program works. We would incorporate things that would potentially require us to retrain our models, but that would probably be the most significant.
## 7. Software Architecture
### Components
* Database to store player data and to train our ML models off of. 
* ML models to predict game outcomes and an LLM model to assist users when drafting. 
* Python code to draft players, predict game outcomes, use our LLM, and generate insights for the user on players.
### Interface
* Call setup database at the start to ensure the database is up to date.
* Retrieve player data for the draft.
### Data
* Use SQLite database to store NBA player data.
* A table contains a list of players, each with their associated Name, Team, Games played, Points, Rebounds, Assists, Steals, Blocks, Field Goal%, Free Throw%, and Number of 3 pointers made. 
### Assumptions
* Assume the structure of the website (Basketball Reference) where the data is from is consistent.
### Alternative
* Instead of web scraping we can use an API to get the data. Pros are more reliable and stable data source. Cons are it is hard to get and could have usage limits.
* Instead of using SQLite we could use MongoDB as the database system. Pros are it can handle large amounts of data and high traffic load. Cons are uses more memory and storage space and harder to use. 
## 8. Software Design
* We will be using conda and its preinstalled packages, mainly BeautifulSoup4, Pandas, Sqlite3, requests, and numpy. We will also be using Pytorch for our ML models. 
    * We use BeautifulSoup4, Pandas, Sqlite, and requests for database management and creation.
    * We use Pytorch, pandas, and Numpy for our ML models.
## 9. Coding Guideline
We plan to code our assignment following the [PEP 8 Python Style](https://peps.python.org/pep-0008). PEP 8 is the official style guide for Python and is widely used across the Python community. PEP 8 emphasizes code readability, which aligns well with Python's philosophy of creating clear and understandable code.
## 10. Process description
### Risk Assessment
* The likelihood of our dataset not having a good dataset would be medium and the impact will be medium too since it wouldn't be a quality data as we hoped to get. we are carefully collecting the dataset to reduce the likelihood of it happening. We are planning to mitigate the risk by picking and cleaning the dataset.
* The likelihood of our data being outdated will be low since we can get updated data. If it occurs the impact would be high because we are not going to be assisting the fantasy managers with updated data, which might lead them to get low potential fantasy scores due to the quality of the data. We are going to reduce, mitigate, or avoid this by getting updated data.
* The likelihood of adding too many features in order to please our customers(fantasy managers) would be medium because we might be tempted to do it in order to gain more customers. The impact if it occurs would be high as it takes more of our time leading us to not deliver on time. The steps we are taking to reduce the impact are to just make the basics first and then add the additional features later on if we have enough time. Plan to detect the problem is just as easy as tracking our progress and time management. If it occurs mitigation plan is to work overtime to deliver the full product.
* The likelihood of the UI not validating user input would be low but it might happen. As long as we work on it carefully we believe we will succeed on that part. If it occurs as we said it could lead to errors in the backend and data processing leading to our product malfunction. We haven't done any experiments to know if it is going to happen or not. To reduce the impact we are working on being as accurate as possible on the backend and then working on the front end. The mitigation plan is if it occurs try to fix the bug by going back and checking the code.
* The last risk likelihood of occurring is very low as there are a lot of stat datasets that we can get from different databases. If it occurs it will skew the quality of assistance we would give to the fantasy manager as it is important to have a player's stat to assist on a specific player. There are lots of resources the potential of this happening is low. To reduce the impact of this happening we will get as many stats as we could to give detailed assistance.  Plan to detect the problem is to check on the player's stat and what is missing then get the missing stat. The mitigation plan should it occur is just to get more stats from different databases to fulfill the need stat for the players.
### Test-automation
**We will use unittest as our test automation framework for the project.**
#### Justification for unittest
* We chose unittest for the following reasons:
* It's built into Python, requiring no additional installation
* It provides a rich set of assertions for thorough testing
* It supports test discovery, making it easy to run all tests
#### Adding a New Test:
* Create a new Python file in the tests directory, naming it <feature>_test.py
* Import the unittest module and the code to be tested
* Create a class that inherits from unittest.TestCase
* Write test methods within this class, naming them test_<specific_functionality>
* Use unittest assertions to verify expected behavior
### Continuous Integration (CI)
**We will use GitHub Actions as our CI service, directly integrated with our GitHub repository.**
#### Justification for GitHub Actions:
* Seamless integration with our GitHub repository
* Free for public repositories and generous free tier for private ones
* Flexible workflow configuration using YAML
* Extensive marketplace of pre-built actions
#### Two CI services we are considering were GitHub Actions and Travis CI
##### Pros
GitHub Action:
* Native GitHub integration
* Free for public repos
* Large marketplace of actions
Travis CI:
* Simple configuration
* Good documentation
##### Cons
GitHub Action:
* Potentially complex YAML config
* Limited run time on free tier
Travis CI:
* Can be slow for larger projects
* Limited free tier
#### CI Build Execution:
The following tests will be executed in each CI build:
* Unit tests
* Integration tests
* Linting checks (using flake8)
* Type checking (using mypy)
#### CI Build Triggers:
A CI build will be triggered by the following development actions:
* Push to any branch
* Pull request creation or update
* Scheduled daily builds on the main branch
