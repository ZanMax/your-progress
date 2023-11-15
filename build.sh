#!/bin/bash

# Variables
DOCKER_HUB="10.0.0.200:5000"

# Functions
build_app() {
    read -rp "Enter app name: " APP_NAME
    read -rp "Enter app version: " APP_VERSION

    echo "Select the architecture:"
    echo "1) AMD 64"
    echo "2) ARM 64"
    echo "3) Current"
    read -rp "Enter your choice (1/2/3): " ARCH_CHOICE

    case $ARCH_CHOICE in
        1)
            ARCHITECTURE="amd64"
            docker buildx build --platform linux/amd64 --push -t "${DOCKER_HUB}/${APP_NAME}:${APP_VERSION}-${ARCHITECTURE}" .
            ;;
        2)
            ARCHITECTURE="arm64"
            docker buildx build --platform linux/arm64 --push -t "${DOCKER_HUB}/${APP_NAME}:${APP_VERSION}-${ARCHITECTURE}" .
            ;;
        3)
            docker build -t "${DOCKER_HUB}/${APP_NAME}:${APP_VERSION}" .
            docker push "${DOCKER_HUB}/${APP_NAME}:${APP_VERSION}"
            ;;
        *)
            echo "Invalid architecture option"
            exit 1
            ;;
    esac
}

deploy_app() {
    if [[ $(basename "$PWD") != "k8s" ]]; then
        cd k8s || exit
    fi
    kubectl -n dev apply -f .
}

delete_app() {
    if [[ $(basename "$PWD") != "k8s" ]]; then
        cd k8s || exit
    fi
    kubectl -n dev delete -f .
}

# Main script
echo "Select the operation:"
echo "1) Build"
echo "2) Deploy"
echo "3) Delete"
read -rp "Enter your choice (1/2/3): " OPERATION

case $OPERATION in
    1)
        build_app
        ;;
    2)
        deploy_app
        ;;
    3)
        delete_app
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac
