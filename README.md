# DockerKubernetesPOC
Little project to deploy a simple app through docker containers and manage them via kubernetes / minikube

## Requirements
The following are required in order to run this project:
    - Docker (via Docker desktop for example)
    - minikube
    - kubectl

## Instructions
Build the image of each app by first going in the corresponding directory and push it to your registry (dockerhub for example) with the following commands :
```bash
cd src/app-(1 or 2)
Docker build -t your-registry/python-app-(1 or 2):x # with x being the version of the app (e.g. 1.0.0). Don't forget to update the deployment.yaml version of the image aswell.
Docker push your-registry/python-app:x
```

Create a single node cluster :
```bash
minikube start
```

Add a new node to the cluster that will serve as a worker node on which the pods will be created to execute the containers :
```bash
minikube node add
```

Add a label for each created node:
```bash
kubectl label node minikube-m02 role=worker
```

You can now create a deployment with kubectl using the **deployment.yaml** file:
```bash
kubectl apply -f deployment.yaml
```

## Description
-- This section is evolving as the code is being improved --

Currently this project will start a kubernetes deployment. The deployment is configured to launch two containers in one pod. The first container will execute the app-1/app.py code and the second container will execute the app-2/app.y code.

Each app will try to write in the **/python-app/test-file.text** the message ```App (1 or 2): Hello World !```. This file is stored in a persistent volume described in the **deployment.yaml** configuration file. This persistent volume is of type **hostPath** meaning it is a volume stored in the host of the pods which is the control-pane node. Each pod will be able to access this same file. They obviously need to be coordinated as they could access this file concurrently and overwrite each others' modifications, hence a file lock on this file is used to manage this behaviour.

After applying the deployment, two pods should be running and each executing a app.py application, one corresponding to app-1 and the other to app-2. To see the results one can log in to one of the pods with following command :
```bash
kubectl exec -it python-app-deployment-(pod-id) --container python-app-(1 or 2) -- bash
```

It is then possible to see the result with:

```bash
tail -f /python-app/test-file.txt
```

The result should look like this:

```bash
App 1 : Hello World !
App 2 : Hello World !
... # above is repeated infinitely as it is a while true
```
