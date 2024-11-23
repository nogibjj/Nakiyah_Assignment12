# Nakiyah_Assignment12

[![Build and Push Docker Image](https://github.com/nogibjj/Nakiyah_Assignment12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_Assignment12/actions/workflows/cicd.yml)

## File Structure
```
Nakiyah_Assignment12/
│
├── .github/                
│   ├── worklows/                  
│   │   └── cicd.yml         
├── templates/                
│   └── index.html            
├── .gitignore
├── app.py                    
├── Makefile
├── Dockerfile                    
├── requirements.txt              
└── README.md                 
```


## Project Overview
This repository demonstrates a simple Python application built on flask that is containerized using Docker. The application is built, run, and managed using Docker commands and a CI/CD workflow to automate the build and push process to Docker Hub.

### Docker Image: 
[Docker Image](https://hub.docker.com/r/nakiyah24/nd191_assignment12)

## Features
- Python Flask Web Application: A web application that shows the time for different time zones; serving as a foundation for containerization.
- Dockerized Deployment: A Docker image for consistent deployment across environments.
- Makefile Automation: Simplifies Docker commands for building and running the container.


### CI/CD Integration
This project uses a CI/CD pipeline to automate Docker image builds and deployments:

Build: The Docker image is automatically built.
Push: The image is pushed to Docker Hub.

## Deployment to Docker Hub
### Manually
1. Authenticate with Docker Hub
`docker login`

2. Tag the Docker Image
`docker tag assignment12:latest nakiyah24/assignment12:latest`

3. Push the Image to Docker Hub
`docker push nakiyah24/assignment12:latest`


### Using 
`make push`

Docker pull command
`docker pull nakiyah24/nd191_assignment12`