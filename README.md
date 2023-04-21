# Livejournal CS3200 Database Design Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
4. In a terminal or command prompt, navigate to `LiveJournalCS3200Project/`, the folder with the `docker-compose.yml` file.  
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`.

## Running Thunder Client Tests
**Important** - you need the vscode Thunder Client extension and the containers must be running

1. Navigate to the Thunder Client extension
2. Open the collections tab
3. If no collections are visible make sure the `Thunder-client: Save to Workspace` extension setting is on
4. Right click on either the `SalesTests` or `InfluencerTests` and click `Run All`
5. Click the blue `Run` button in the pop up

Note: Tests should be run on startup before the data is manipulated via the web app

## Accessing the Appsmith appplication
1. With the containers running go [here](http://localhost:8080/app/appsmith3200projectfrontend/post-creation-643f382a67dcf9058096ce3e?branch=master)
2. For more info on the frontend see [this repo](https://github.com/psullivan235/Appsmith3200ProjectFrontend)
