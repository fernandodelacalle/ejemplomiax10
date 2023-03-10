# ejemplomiax10
1. Creamos un repo en ECR ---> desde la consola/web de aws.

2. Construir la imagen.
```bash
docker build -t ejemplomiax10 .
```

3. Tag la imagen a aws ecr
```bash
docker tag ejemplomiax10 467432373215.dkr.ecr.eu-west-1.amazonaws.com/ejemplomiax10
```
2-3. Los pasos anteriores en solo uno:
```bash
docker build -t 467432373215.dkr.ecr.eu-west-1.amazonaws.com/ejemplomiax10 .
```

- Solamente 1 vez para comunicar el docker con aws
```bash
aws ecr get-login-password | docker login --username AWS --password-stdin 467432373215.dkr.ecr.eu-west-1.amazonaws.com
```
- Subir la imagen
```bash
docker push 467432373215.dkr.ecr.eu-west-1.amazonaws.com/ejemplomiax10
```

- Crear la lambda en AWS.

- Actualizar la imagen de la función lambda:
```bash
aws lambda update-function-code --region eu-west-1 --function-name ejemplomiax10 --image-uri 467432373215.dkr.ecr.eu-west-1.amazonaws.com/ejemplomiax10:latest
```
