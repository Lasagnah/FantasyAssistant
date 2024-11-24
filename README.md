![Cunningham-Curry-Possibilities](https://github.com/user-attachments/assets/8ca4c94f-4f4e-45a2-952f-5864d5499fb3)
# Fantasy Assistant
## Table of Contents
* Introduction
* Data Collection and Cleaning
* Setting up and Training Models
* Results
## What is this project? 
* Fantasy Assistant is a comprehensive NBA fantasy draft simulation and analysis tool developed as a senior-level software engineering project. The system provides intelligent player drafting, team performance prediction, and statistical analysis. 
* See requirements.md for more information.
## How is this project organized?
* This project is organized in a way such that the src folder contains most of the python files and the docs folder contains the documents and the tests folder contains tests for the python code.
## Prerequisites
* Python 3.9+
* pip package manager
* Git
## Key Features
* NBA player data scraping
* Interactive fantasy draft simulation
* Advanced team performance prediction using Markov Decision Process
## Data Collection
* The project collects player data from Basketball Reference using web scraping techniques. The data is then cleaned and processed to ensure accuracy, removing any incomplete or irrelevant entries. This step is crucial for creating a reliable dataset that informs the drafting and prediction algorithms.
## Training Models
* The project utilizes various algorithms, including value iteration for Markov Decision Processes (MDP) to predict team performance based on player statistics. The models are trained on the cleaned dataset, allowing for dynamic evaluation of player contributions and team strategies during the draft simulation.
## Results
* The Fantasy Assistant provides users with detailed insights into team performance, including scoring potential, playmaking ability, defensive impact, and shooting efficiency. The system also predicts the winning team based on current rosters and player statistics, offering a data-driven approach to fantasy sports drafting.
* <img width="488" alt="image" src="https://github.com/user-attachments/assets/06a39038-b71d-44fb-9925-cd81a14c187c">
* Program starts with asking how many teams are picking, then first team are given the top 5 players avaialble with the option to see all players by typing 's' and a suggested pick.
* <img width="335" alt="image" src="https://github.com/user-attachments/assets/a22a1ddb-de71-4173-985f-e87eb350a00c">

