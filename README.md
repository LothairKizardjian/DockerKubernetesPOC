# DockerKubernetesPOC
Little project to deploy a simple app through docker containers and manage them via kubernetes / minikube

# Requirements
The following are required in order to run this project:
    - Docker (via Docker desktop for example)
    - minikube
    - kubectl

# Instructions
Build the image of this project and push it to your registry (dockerhub for example) with the following commands :
````bash
Docker build -t your-registry/python-app:1.0.0
Docker push your-registry/python-app:1.0.0
````

Launch minikube :
````bash
minikube start
````

You can now create a deployment with kubectl :
```bash
kubectl create deployment python-app --image=your-registry/python-app:1.0.0
```