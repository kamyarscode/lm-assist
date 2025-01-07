#!/bin/bash

verbose=0
repo_pull=0
update_model_engine=0
install_path="$PWD"

LOG="Language Model Assist Tool Installation"

# Create help function
help_instructions() {

    echo "Installation for Language Model Assist and model engine API"
    echo "$LOG Usage: $0 [-v] [-b <branch>] [-p] [-h] [-m]
    
    Usage:
        -h, --help              Help menu.
        -v, --verbose           Show verbose installation logs.
        -m, --update-model      Update model API/engine.
        -p, --pull              Pull from branch/remote repo.
        -b, --branch            Branch to use for pulling.
    
    "
}

# Pass in and receive args.
while getopts ":e:b:mhvp" o; do
    case "${o}" in
        h|--help)
            help_instructions
            ;;
        # e|--env)
        #     someenvfunction
        #     ;;
        v|--verbose)
            verbose=1
            ;;
        m|--update-model)
            update_model_engine=1
            ;;
        p|--pull)
            repo_pull=1
            ;;
        b|--branch)
            repo_pull=1
            tag=$
            ;;
        *)
            help_instructions
            ;;
    esac
done

shift $((OPTIND-1))

# Switch branches if repo pull is true/1.
if [ [ repo_pull == 1] ]; then
    echo "Get latest version"
    git reset --hard
    git pull
    MSG=$?
    if [$MSG -ne 0]; then
        echo "Failed to pull latest branch version. Exiting."
        exit 1
    fi

    if [ ! -z "$branch" ]; then
        echo "Switching branches."
        git checkout "$branch"
        MSG=$?

        if [ $MSG -ne 0]; then
            echo "Failed to change branches. Exiting."
            exit 1
        fi
    fi
fi

# Update model engine along with language model APIs. Just runs different docker compose file.
if [ [ $update_model_engine == 1] ]; then
    echo "$LOG Updating Model Engine"

    if [[verbose == 1]]; then
        echo "$LOG Installing with logs."
        docker compose -f $install_path/docker-compose-model.yml up --build --force-recreate

    else
        echo "$LOG Running in background."
        docker compose -f $install_path/docker-compose-model.yml up -d --build --force-recreate
    fi

# Install just language model api.
else
    echo "$LOG Installing only Language Model Assist API."
    if [ [verbose == 1] ]; then
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
