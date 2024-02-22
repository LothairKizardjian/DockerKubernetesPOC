# DockerKubernetesPOC
Little project to deploy a simple app through docker containers and manage them via kubernetes / minikube

## Requirements
The following are required in order to run this project:
    - Docker (via Docker desktop for example)
    - minikube
    - kubectl

## Instructions
Build the image of this project and push it to your registry (dockerhub for example) with the following commands :
```bash
Docker build -t your-registry/python-app:x # with x being the version of the app (e.g. 1.0.0). Don't forget to update the deployment.yaml version of the image aswell.
Docker push your-registry/python-app:x
```


Launch minikube :
```bash
minikube start
```

You can now create a deployment with kubectl using the **deployment.yaml** file:
```bash
kubectl create -f deployment.yaml
```