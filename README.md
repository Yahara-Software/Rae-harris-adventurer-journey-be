# Adventurer Journey - Back End

Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

_Please use whatever languages, references and tooling you would like to complete the story._

## Story Instructions

You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**

- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.

**Running the Program**

- Enter _python3 AdventureJourney.py_ into the terminal to print out the Euclidean distance to the destination
- To test different directions, update the [./Adventurer Path.md](./Adventurer%20Path.md) file or manually call the distance calculating function with a test direction string by entering _python3 -c 'import AdventureJourney; print(AdventureJourney.calc\_euclidean\_dist(\<direction_string\>))'_ into the terminal. Replace \<direction_string\> with your directions (such as '15L4B')
