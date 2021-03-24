Run the project locally
```bash
docker-compose up --build
```

* pg secret

```bash
kubectl create secret generic pg-user \
--from-literal=PGUSER=<put user name here> \
--from-literal=PGPASSWORD=<put password here>
```
# Links
* [Control startup and shutdown order in Compose
](https://docs.docker.com/compose/startup-order/)
