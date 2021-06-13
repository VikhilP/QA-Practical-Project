#!/bin/bash

# copy over compose yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@draft-manager:/home/jenkins/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@draft-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    export DOCKER_USERNAME=${DOCKER_USERNAME}
    docker stack deploy --compose-file docker-compose.yaml draft
EOF