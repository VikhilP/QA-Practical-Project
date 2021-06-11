# QA-Practical-Project

For training purposes, i have been tasked with a individual project in which i must use CD/CI tools in
order to trigger a rolling update. The pipeline consists of 4 services split into different responsibilies.

- Service 1: Front-end of the program, makes use of api calls to display the program by calling
the other 3 services
- Service 2/3: Generates random entities
- Service 4: called by a POST request in service 1

The app itself is very basic, the complexity increases when we get to the CD/CI tools needs.
- Docker and Docker-Compose used to containerise the images and builds
- Docker Swarm will spread the program across worker nodes/managers, using multiple replicas
- Nginx will load balance the project so the server is not overloaded
- Testing provided by the jenkins environment, ideally through github webhooks

# Sports Draft

The app i have chosen to create is a program that gives the user a chance to draft a player. a database 
will store a players position and overall draft position, service 4 will calculate the round they were
picked and the pick they were taken in that round.

# Software design

## Trello

before i created my app, i created a trello board for items needed to be created. i made 5 seperate
sections:

- User Stories: What i belive are requirements users should meet
- Plans: Elements that need to be learnt for the project
- To Do: Planned features
- Doing: Ongoing programmed features
- Done: Completed features

## Database

2 small databases, however in reality i am only using 1. This is because once i switch over to the 
second implementation, it will still use the same attributes as the value type did not change. This 
stops issues with database uri needing to be set differently for 2 seperate apps.

- ID: unique identifier for the draft (INT)
- position: String value that holds the position value e.g. QB, LF
- pick: Integer value that stores the overall pick value of the drafted player

## Risk Assessment

A risk assessment was completed at the start of the project and later revised towards the
end of the project.
This revision is shown at the end of the table "Response(end)" signalling my protective measures.
Using the risk matrix and colours, i have identified how big each risk is. Red signals that 
fixing this issue is of high priority







