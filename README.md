# Hello World App Deployment

This repository contains the necessary files to deploy a simple Flask application (`hello-world-app`) using Minikube and Kubernetes.

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Docker](https://docs.docker.com/get-docker/)

## Steps to Deploy

### 1. Start Minikube

Start Minikube to create a local Kubernetes cluster:

```sh
minikube start

### Here is a 

README.md

 file that explains how to deploy and access the `hello-world-app` using Minikube and Kubernetes:

```markdown
# Hello World App Deployment

This repository contains the necessary files to deploy a simple Flask application (`hello-world-app`) using Minikube and Kubernetes.

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Docker](https://docs.docker.com/get-docker/)

## Steps to Deploy

### 1. Start Minikube

Start Minikube to create a local Kubernetes cluster:

```sh
minikube start
```

### 2. Use Minikube's Docker Daemon

Configure your shell to use Minikube's Docker daemon:

```sh
eval $(minikube docker-env)
```

### 3. Build Docker Image

Build the Docker image for the Flask application:

```sh
docker build -t ivakadock/hello-world-app:latest .
```

### 4. Apply Deployment Configuration

Apply the Kubernetes deployment configuration:

```sh
kubectl apply -f deployment.yml
```

### 5. Apply Service Configuration

Apply the Kubernetes service configuration to expose the application:

```sh
kubectl apply -f service.yml
```

### 6. Check Deployment and Service Status

Verify that the deployment and service are running:

```sh
kubectl get deployments
kubectl get services
```

### 7. Get Minikube IP

Get the Minikube IP address:

```sh
minikube ip
```

### 8. Access the Application

Open your browser and navigate to the Minikube IP address and NodePort:

```
http://<minikube-ip>:30000
```

Replace `<minikube-ip>` with the IP address obtained from the `minikube ip` command.

## Files

- `app.py`: The Flask application code.
- `Dockerfile`: The Dockerfile to build the Docker image.
- `deployment.yml`: The Kubernetes deployment configuration.
- `service.yml`: The Kubernetes service configuration.

## Troubleshooting

### Check Pod Status

If the pod is not running, check its status:

```sh
kubectl get pods
```

### Describe Pod

Get detailed information about the pod:

```sh
kubectl describe pod <pod-name>
```

### Check Pod Logs

Check the logs of the pod:

```sh
kubectl logs <pod-name>
```

### Restart Pod

To restart a pod, delete it and let the deployment create a new one:

```sh
kubectl delete pod <pod-name>
```

## License

This project is licensed under the MIT License.
```

This 

README.md

 file provides a comprehensive guide on how to deploy and access the `hello-world-app` using Minikube and Kubernetes. Adjust the instructions as needed based on your specific setup and requirements.