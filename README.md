Run the project locally
```bash
docker-compose up --build
```

## SSL
* create a dns entry in [cloud dns](https://www.cloudns.net/)
* get certificates from [sslforfree.com/](sslforfree.com/)
* put them in nginx/certs directory with names server.key and server.crt
* run the application and access it with https://<YOUR-DOMAIN>
# Links
* [Control startup and shutdown order in Compose
](https://docs.docker.com/compose/startup-order/)
* [sslforfree.com/](sslforfree.com/)
* [cloud dns](https://www.cloudns.net/)