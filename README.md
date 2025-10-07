# Farkle in Python

## Description
This is a small application that I made for fun on an aircraft to play farkle. Since I enjoyed it I used this project as a practice to learn coding best practices such as continuous integration, automated builds, pip-installable formatting, unit testing and more.

## Installation
Steps to install and set up the project.

TODO - Fill out the below.
```sh
# Clone the repository
git clone https://github.com/your-username/your-repo.git

# Navigate to the project directory
cd your-repo

# Install dependencies
npm install  # or pip install -r requirements.txt


## Notes

To expand this what can I do - I would like to train an AI to play farkle. There are some challenges here

The idea I had was to train a new model for each amount of dice on the board.

So there would be 6 separate models and I could use pytrees behavior trees to handle the different behavior
between the different scenarios.

The thing I would like to learn the most though is how to manage risk - thats the hardest part of farkle. And just having 6x AI's acting independently does not give you any capacity to assess and manage risk.

So there would need to be some overarching model that is responsible for producing like a risk tolerance number and it would work in accordance with the sub-models to commit to a decision at any given point.

the overarching model could be responsible for decision making and would consider things like:
- How many dice left / How much score this turn / Score / Opponents Score /