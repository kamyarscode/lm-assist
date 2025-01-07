#!/bin/bash

verbose=0
repo_pull=0
update_model_engine=0
install_path="$PWD"

LOG="Language Model Assist Tool Installation"


while getopts ":e:b:mhvp" o; do
    case "${o}" in
        h|--help)
            functionhere
            ;;
        e|--env)
            someenvfunction
            ;;
        v|--verbose)
            verbose=1
            ;;
        m|--update-model)
            update_model_engine=1
            ;;
        p|--update)
            repo_pull=1
            ;;
        b|--branch)
            repo_pull=1
            tag=$
            ;;
        *)
            functionhere
            ;;
    esac
done

shift $((OPTIND-1))

if [[ $update_model_engine == 1]]; then
    echo "$LOG Updating Model Engine"

    if [[verbose == 1]]; then
        echo "$LOG Installing with logs."
        docker compose -f $install_path/docker-compose-model.yml up --build --force-recreate
    else
    echo "$LOG Running in background."
    docker compose -f $install_path/docker-compose-model.yml up -d --build --force-recreate
    fi

else
    echo "$LOG Installing only Language Model Assist API."
    if [[verbose == 1]]; then
        echo "$LOG Installing with logs."
        docker compose -f $install_path/docker-compose.yml up --build --force-recreate
    else
        echo "$LOG Running in background."
        docker compose -f $install_path/docker-compose.yml up -d --build --force-recreate
    fi
fi


# Perform cleanup
echo "$LOG Cleaning up images"
docker rmi $(docker images -f "dangling=true" -q)
