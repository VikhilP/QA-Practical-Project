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

## Test Plans

These were designed to show that the functionality of the app is at 100%. These tests have been reflected in the unit tests that i have created

# Continuous Deployemnt and Integration

Jenkins was used as an automated process of the Contiuous Deployment and Integration devops mindset.

Below is the completed Jenkins pipeline for the project. 

There are 6 Stages:
1. Setup: This is where all the setup downloads will be implemented into the virtual environment (also set here)
2. Testing: Performs the unit tests for the project
3. Build: This builds the services into seperate images onto the local jenkins machine
4. Push: this uploads the images from the previous stage onto my personal dockerhub account storing the images
5. Ansible: This runs my ansible commands. This means that jenkins will set up the roles for each node connected to it, allowing for sepertion of code from other node e.g. nginx roles do not perform the same actions as manager/worker node. This process create the basis of the docker swarm
6. Deploy: Using a deploy script, jenkins is able to ssh into the manager node, copy over the ansible playbook (due to set up form the previous build) and allows the swarm to be fully created and made availble to the public. Using a stack also paired with nginx means that there is no downtime for the user from when the devs push the code to git hub to when the stack is deployed.

A diagram below describes the full process of the CI pipeline


# Components in Detail

## Docker

Docker allows for programs to be run in a isolated container. it does this by building the app and putting it into an image. This is sort of like a executable which entails everything that the app needs to run such as the code, dependencies, libraries, directories needed, ports etc. These are defined inside Dockerfile(s)

### Docker Compose

Docker compose is a tool that needs to be installed alongside docker. This tool practically automates the docker build process. Previously, a devops engineer would have to enter in each docker build process into the command line. Docker-Compose allows devops engineers to input all of these into one file. The text is easier to read and debug as most statements are one word commands. Services created and defined inside this file will be in the same network allowing for each service to talk to one another.

### Docker Swarm

A docker swarm is an orchestration tool that allows for applications to be more robust and protected from overloading. Swarms are clusters of machines/VMs that are running shared containers (in most cases), and thus benefit from increased scalabitly and error handing as more machines leads to less points of failure. Docker swarm uses the same docker-compose file used to build the images but with one slight difference. Docker swarm cannot build images which is why it is used in the deployment stage. Swarm needs to pull the images from elsewhere, this has been supplied by running 'docker-compose up -d' in a previous step to build the images. Then the images are pushed to dockerhub which is then pulled down for the swarm.

In this project, a stack is used which i have made use of to carry out rolling updates to the applicaiton. I do not want the user to face any downtime at any point while the applicaiton is updating. Disregarding replicas, having a swarm means that one machine can run an old version of the app while one is updating. Then when it updates, the new one will pick up the slack for the old version while it updates. This is made better with Nginx
## Ansible

## Nginx









