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

![trello](https://user-images.githubusercontent.com/82821513/121785659-fcc02480-cbb2-11eb-9ec9-7b4f90ea297f.PNG)


## Database

2 small databases, however in reality i am only using 1. This is because once i switch over to the 
second implementation, it will still use the same attributes as the value type did not change. This 
stops issues with database uri needing to be set differently for 2 seperate apps.

![Draft](https://user-images.githubusercontent.com/82821513/121785662-02b60580-cbb3-11eb-9cd4-731e7e8120f1.png)


- ID: unique identifier for the draft (INT)
- position: String value that holds the position value e.g. QB, LF
- pick: Integer value that stores the overall pick value of the drafted player

## Risk Assessment

A risk assessment was completed at the start of the project and later revised towards the
end of the project.

![risk](https://user-images.githubusercontent.com/82821513/121785715-51fc3600-cbb3-11eb-9b8a-479afe754570.PNG)


This revision is shown at the end of the table "Response(end)" signalling my protective measures.
Using the risk matrix and colours, i have identified how big each risk is. Red signals that 
fixing this issue is of high priority

## Test Plans

These were designed to show that the functionality of the app is at 100%. These tests have been reflected in the unit tests that i have created
![Test plan](https://user-images.githubusercontent.com/82821513/121785632-bd91d380-cbb2-11eb-80df-da7d559f263a.PNG)


# Continuous Deployemnt and Integration

Jenkins was used as an automated process of the Contiuous Deployment and Integration devops mindset.

Below is the completed Jenkins pipeline for the project. 

![jenkins](https://user-images.githubusercontent.com/82821513/121785678-12cde500-cbb3-11eb-9f5d-9cd92b0bf54e.PNG)


There are 6 Stages:
1. Setup: This is where all the setup downloads will be implemented into the virtual environment (also set here)
2. Testing: Performs the unit tests for the project
3. Build: This builds the services into seperate images onto the local jenkins machine
4. Push: this uploads the images from the previous stage onto my personal dockerhub account storing the images
5. Ansible: This runs my ansible commands. This means that jenkins will set up the roles for each node connected to it, allowing for sepertion of code from other node e.g. nginx roles do not perform the same actions as manager/worker node. This process create the basis of the docker swarm
6. Deploy: Using a deploy script, jenkins is able to ssh into the manager node, copy over the ansible playbook (due to set up form the previous build) and allows the swarm to be fully created and made availble to the public. Using a stack also paired with nginx means that there is no downtime for the user from when the devs push the code to git hub to when the stack is deployed.

A diagram below describes the full process of the CI pipeline

![PPP flowchart](https://user-images.githubusercontent.com/82821513/121785679-18c3c600-cbb3-11eb-9512-667bfae001a8.png)



# Components in Detail

## Docker

Docker allows for programs to be run in a isolated container. it does this by building the app and putting it into an image. This is sort of like a executable which entails everything that the app needs to run such as the code, dependencies, libraries, directories needed, ports etc. These are defined inside Dockerfile(s)

### Docker Compose

Docker compose is a tool that needs to be installed alongside docker. This tool practically automates the docker build process. Previously, a devops engineer would have to enter in each docker build process into the command line. Docker-Compose allows devops engineers to input all of these into one file. The text is easier to read and debug as most statements are one word commands. Services created and defined inside this file will be in the same network allowing for each service to talk to one another.

### Docker Swarm

A docker swarm is an orchestration tool that allows for applications to be more robust and protected from overloading. Swarms are clusters of machines/VMs that are running shared containers (in most cases), and thus benefit from increased scalabitly and error handing as more machines leads to less points of failure. Docker swarm uses the same docker-compose file used to build the images but with one slight difference. Docker swarm cannot build images which is why it is used in the deployment stage. Swarm needs to pull the images from elsewhere, this has been supplied by running 'docker-compose up -d' in a previous step to build the images. Then the images are pushed to dockerhub which is then pulled down for the swarm.

In this project, a stack is used which i have made use of to carry out rolling updates to the applicaiton. I do not want the user to face any downtime at any point while the applicaiton is updating. Disregarding replicas, having a swarm means that one machine can run an old version of the app while one is updating. Then when it updates, the new one will pick up the slack for the old version while it updates (Ingress load balancing). This is made better with Nginx

## Ansible

Ansible is a piece of software that allows for the automatic configuration of multiple different nodes. In my program, Ansible is reponsible for creating roles. In these roles, the manager and worker need to have docker installed on them; ansible uses a main.yaml inside a docker role to install it to these nodes. This makes it easier to configure multiple different vms at once. Docker needed to be installed in order to run the Docker Swarm Stacks on different nodes

Ansible performs these commands by having jenkins ssh into these machines and taking the liberty to install it itself.

## Nginx

In this project, Nginx was used as an external load balancer. It would listen to the Manager and Worker VMs on port 5000 and load balance. The app will be available on the Nginx IP due to it also mworking as a reverse proxy. Due to this, it is published on port 80 which is the basic HTTP port. This leads to the user not having to enter a port at the end of the ip unlike with the other VMs.

Nginx also, when load balancing, will tend to take the user onto the node which has taken the least load. This way nodes are not overwhelmed with activity

![swarm](https://user-images.githubusercontent.com/82821513/121785692-2c6f2c80-cbb3-11eb-98ed-26429662c4d7.png)

# Services

The project uses 4 services to run the application.

![containers](https://user-images.githubusercontent.com/82821513/121785724-5f192500-cbb3-11eb-9873-435720034544.png)

Services:

1. Front-End, shows the user which player has been drafted. acts as a base for the API calls
2. Generates a random position picked from a pre-existing set
3. Generates a random number
4. Using a post request, the random number and position are inputted to the service. Draft round and position drafted in the round are then calculated

Steps:
- User navigates to the website
- User clicks button
- Service 1 performs a get request on service 2 and 3 (retrieving random position and draft pick)
- The get requests are then passed into a post request for service 4
- Service 4 then calculates the draft round and draft round position
- Service 4 gives this info to Service 1
- Service 1 puts position info and draft pick number into a database
- Service 1 then outputs the current pick to the front-end as well as the last 5 picks

This service changes between the NFL draft and the MLB draft. Service 2 generates different positions. Service 3 changes the random number range, Service 4 changes the length of the draft positional pick. This is because NFL has 32 teams and MLB only has 30 leading to a different calculation needing to be made. Service 1 changes by having a different backround colour. The title and header also change between "NFL Draft" and "MLB Draft"

# Testing

To test this app, i ran automated testing through the jenkins app. Requests_mock was also used to mock the unit test of service 1. This is because the tests run in an environment away from the containers. I needed a way to perform the test without having to create containers. Normally referencing "http://service-1" would not work, but requests_mock allows for a proxy to be created so th etest can run. This allowed me to run the test as if the system was live. Everytime the code is pushed, the program is tested, if it fails, the code is not fully built.

![Imgur](https://i.imgur.com/w0hUdsJ.png)

![Test 3-4 updated](https://user-images.githubusercontent.com/82821513/121815617-4b32f900-cc6f-11eb-9a2c-ac8614aaa3f6.PNG)


As shown above, great test coverage has been achived. This was particularly simple due to the application being very small in nature

# Front End

The front end consists of 2 very simple versions of the same page. The initial empty screen, and then an updated screen once a player has been drafted.

In this example, a base ball position is dislpayed next to the overall pick number e.g. FS (Free Safety) is drafted at pick number 162. A full template is only visible when a player is picked

![frontend empty](https://user-images.githubusercontent.com/82821513/121815588-28084980-cc6f-11eb-9f85-cc7a4906c69e.PNG)

![FE after post](https://user-images.githubusercontent.com/82821513/121815593-2b9bd080-cc6f-11eb-8b3c-bb36e6a41766.PNG)


# Improvements

- Implement CSS
- I probably could have made it so that the round pick and round number was implemented into the database, making it visible to the user
- Streamline the docker-compose build process a little better so it does not take as long
- More intricate testing plan





