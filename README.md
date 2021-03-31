# Run the project locally
```bash
docker-compose up --build
```

# Deploy the project to a kubernetes cluster

* connect to cluster

## configmaps
### create fastapi configmap
```bash
kubectl create configmap fastapi-config --from-env-file=k8s/fastapi/fastapi.env
```

## deployments
```bash
kubectl apply -f k8s/db/postgres-deployment.yml
kubectl apply -f k8s/fastapi/fastapi-deployment.yml
```

## services
```bash
kubectl apply -f k8s/db/postgres-clip.yml
kubectl apply -f k8s/fastapi/fastapi-clip.yml

```
## secrets
* pg secret

```bash
kubectl create secret generic pg-user \
--from-literal=PGUSER=<put user name here> \
--from-literal=PGPASSWORD=<put password here>
```


# docker registry
## Github Packages
* enable improved container support
* create personal access token
* tag an image
```bash
docker build -t ghcr.io/tsadimas/myfastapi:latest -f fastapi.Dockerfile .
```
* login to deokcer registry
```bash
cat ~/github-image-repo.txt | docker login ghcr.io -u tsadimas --password-stdin
```
* push image
```bash
docker push ghcr.io/tsadimas/myfastapi:latest
```

## create docker login secret
* create <AUTH> from the command
```bash
echo <USER>:<TOKEN> | base64
```
* create kubernetes secret
```bash
echo '{"auths":{"ghcr.io":{"auth":"<AUTH>"}}}' | kubectl create secret generic dockerconfigjson-github-com --type=kubernetes.io/dockerconfigjson --from-file=.dockerconfigjson=/dev/stdin
```



# Links
* [Control startup and shutdown order in Compose](https://docs.docker.com/compose/startup-order/)

* [Github: create a personla access token for packages](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

* [Configure docker to use with github packages](https://docs.github.com/en/packages/guides/configuring-docker-for-use-with-github-packages)

* [create kubernetes secret to access github packages](https://stackoverflow.com/questions/61912589/how-can-i-use-github-packages-docker-registry-in-kubernetes-dockerconfigjson)