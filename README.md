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

### Here is a 

README.md

 file that explains how to deploy and access the `hello-world-app` using Minikube and Kubernetes:

markdown
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
#### 3.1 Check docker image availability 

```sh
docker images
```

#### 3.2 In case you want to run the local environment Dockerfile 

```sh
docker run -p 5000:5000 ivakadock/hello-world-app
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

## PostgreSQL Integration

### Prerequisites
- PostgreSQL 13
- psycopg2-binary
- SQLAlchemy

### Database Setup

1. **Create PostgreSQL Secret**:
```sh
kubectl apply -f postgresql-secret.yml
```

Let's add PostgreSQL connectivity documentation to the README.md.

Plan:
1. Add PostgreSQL prerequisites
2. Document secret creation
3. Add PostgreSQL deployment steps
4. Document connectivity testing
5. Add troubleshooting section

```markdown
## PostgreSQL Integration

### Prerequisites
- PostgreSQL 13
- psycopg2-binary
- SQLAlchemy

### Database Setup

1. **Create PostgreSQL Secret**:
```sh
kubectl apply -f postgresql-secret.yml
```

2. **Deploy PostgreSQL**:
```sh
kubectl apply -f postgresql-deployment.yml
kubectl apply -f postgresql-service.yml
```

3. **Verify PostgreSQL Deployment**:
```sh
kubectl get pods -l app=postgresql
kubectl get services postgresql
```

### Testing Database Connectivity

1. **Check Service Endpoints**:
```sh
kubectl get endpoints postgresql
```

2. **Test Database Connection**:
```sh
# Enter PostgreSQL pod
kubectl exec -it $(kubectl get pod -l app=postgresql -o jsonpath='{.items[0].metadata.name}') -- psql -U postgres

# Inside psql
\l           # List databases
\dt          # List tables
\q           # Quit
```

3. **Verify App Connection**:
```sh
# Check app logs
kubectl logs -l app=hello-world-app

# Test app endpoint
curl http://$(minikube ip):30000
```

### Troubleshooting

1. **Check PostgreSQL Logs**:
```sh
kubectl logs -l app=postgresql
```

2. **Verify Environment Variables**:
```sh
kubectl exec -it $(kubectl get pod -l app=hello-world-app -o jsonpath='{.items[0].metadata.name}') -- env | grep POSTGRES
```

3. **Test DNS Resolution**:
```sh
kubectl run -it --rm --restart=Never dns-test --image=busybox -- nslookup postgresql
```


# Deployment with Helm

## Prerequisites

- Minikube installed
- Helm installed

## Steps

1. **Start Minikube**:
   ```sh
   minikube start
   ```

2. **Delete Existing Kubernetes Deployment**:
   If you have an existing deployment, delete it:
   ```sh
   kubectl delete deployment my-python-app
   kubectl delete service my-python-app-service
   ```

3. **Create a Helm Chart**:
   If you don't already have a Helm chart, create one:
   ```sh
   helm create my-helm-chart
   ```

4. **Update `values.yaml`**:
   Replace the contents of `values.yaml` in your Helm chart with the following configuration:
   ```yaml
   app:
     name: hello-world-app
     image:
       repository: ivakadock/hello-world-app
       tag: latest
       pullPolicy: IfNotPresent
     service:
       type: NodePort
       port: 5000
       nodePort: 30000
     env:
       - name: POSTGRES_HOST
         value: "{{ .Release.Name }}-postgresql"
       - name: POSTGRES_USER
         value: "{{ .Values.postgresql.auth.username }}"
       - name: POSTGRES_PASSWORD
         value: "{{ .Values.postgresql.auth.password }}"
       - name: POSTGRES_DB
         value: "{{ .Values.postgresql.auth.database }}"

   postgresql:
     enabled: true
     image:
       repository: postgres
       tag: "13"
     auth:
       username: postgres
       password: postgres
       database: postgres
     service:
       port: 5432
   ```

5. **Update the Deployment Template**:
   Modify the `deployment.yaml` template in your Helm chart to use the values from `values.yaml`. For example:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: {{ .Values.app.name }}
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: {{ .Values.app.name }}
     template:
       metadata:
         labels:
           app: {{ .Values.app.name }}
       spec:
         containers:
         - name: {{ .Values.app.name }}
           image: "{{ .Values.app.image.repository }}:{{ .Values.app.image.tag }}"
           ports:
           - containerPort: {{ .Values.app.service.port }}
           env:
           {{- range .Values.app.env }}
           - name: {{ .name }}
             value: {{ .value | quote }}
           {{- end }}
   ```

6. **Deploy the Helm Chart**:
   Deploy the Helm chart to your Kubernetes cluster:
   ```sh
   helm install my-release my-helm-chart
   ```

7. **Access the Application**:
   Get the URL to access your application:
   ```sh
   minikube service my-release-hello-world-app --url
   ```

8. **Curl the Application**:
   Use the URL obtained from the previous step to `curl` your application. For example:
   ```sh
   curl $(minikube service my-release-hello-world-app --url)
   ```


## License

This project is licensed under the MIT License.
```

This 

README.md

 file provides a comprehensive guide on how to deploy and access the `hello-world-app` using Minikube and Kubernetes. Adjust the instructions as needed based on your specific setup and requirements.
