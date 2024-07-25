# BigKoala

## Project Description:
BigKoala is a project developed by Cynthia Serrano Najera (https://github.com/cnajera), Jonathan Ceasar Medina (https://github.com/JonathanCMedina), and Randy Angel Jr. (https://github.com/Juztop) for their Bootcamp Capstone Project.

BigKoala was created to simulate an Incident Alert application through the retrieval of data from outside sources, filtering data based on relevance, and displaying it on the Grafana dashboard for use. 

For now, BigKoala retrieves information from our MySQL Database that is being fed 119,999 entries from the incident_event_log.csv from Kaggle (https://www.kaggle.com/datasets/vipulshinde/incident-response-log?resource=download).


Depending on the machine this application is being ran on, processing all 120k lines with 0.1s delay could take approximately 2 hours (from the developers' general estimations). 


This application will have a supplementary Google slides presentation linked here: https://docs.google.com/presentation/d/1fjEAkLGpvn0yyQCQHhJfBsh9KREzoEapN1qVRCmE-RA/edit?usp=sharing 

---

BigKoala uses Docker for containerization, MySQL for database management, Grafana for visualization, as well as Zookeeper and Kafka for managing data streams through the use of producers and consumers. 

## Applications to download prior to running the application:
Google Chrome (or your Browser of choice)
  https://www.google.com/chrome/

VSCode (or your Code Editor of choice) 
  https://code.visualstudio.com/download

Docker Desktop
  https://www.docker.com/products/docker-desktop/
  
MongoDB Compass GUI 
  https://www.mongodb.com/try/download/compass

## How to fork BigKoala:
In your machine's terminal (Zshell, Powershell, Bash, etc.) type 
`git fork https://github.com/JonathanCMedina/BigKoala.git`

## How to run the application: 
1. Turn on Docker Desktop (login not required)
2. Open you terminal of choice then cd into BigKoala/docker-config
3. Type `docker-compose up --build` in your Code Editor's terminal.
   It may take a minute to build all containers, with the last three being built to be kafka-1, producer-1, and consumer-1. Please be patient.
4. Once all containers are running, check your Code Editor's terminal to see if the data from the incident_event_log.csv is being read and added in (there should be a lot going on in your terminal, this is normal!)

## Grafana 
### MySQL Connection
1. In your browser, go to localhost:3000
2. Login with the username of *admin* and password of *admin* . Skip the password update for now
3. On the upper left side of the Grafana homepage, click the hamburger dropdown menu. Look at **Connections**, press **Add new connection**
4. Search *MySQL*
5. On the top right, press **Add new data source**
6. Name the MySQL database connection *incident_event*
7. Under the Connection header, type *mysql:3036* under Host URL and type *incident_event* for the database name
8. Under the Authentication header, type *root* for Username and *password* for Password
9. At the bottom of the page, click **Save & test**

### Troubleshooting MySQL Connection:
1. If it is giving an error in Grafana when creating the connection and is directing you to check the Docker logs, go to:
2. VSCode terminal that's running the docker > press ctrl + c to stop the docker containers.
3. Then in a new terminal (make sure you're in the docker-config directory), do `docker-compose down` to clear the containers.
4. Finally rebuild with `docker-compose up --build`
5. You should be able to remake the connections.
6. If existing connections in the Grafana Data Source tab still exist, delete them then retry after rebooting Docker.

### If your dashboard's grid is showing that there is No data, follow the steps below:
1. Hover over the top right corner of one of the grids (for example, *Incident Assignment Analysis*)
2. Click the **vertical ellipses** (three dots stacked vertically) menu button
3. Click **Edit**
4. Below you'll see that there are SQL queries starting with `SELECT`. Click into those code spaces
5. Do the following for each query row (Incident Assignment Analysis will have Queries A, B, and C, so you'll have to do this thrice):
  6. Select All (ctrl + a)
  7. Cut (ctrl + x)
  8. Paste (ctrl + v)
  9. Press **Run query**
10. In the top right corner, press **Apply**. This will return you to the Grafana dashboard grid view.
11. (OPTIONAL) In the *Incident Assignment Analysis* grid, click the **total_incidents** dropdown then select **assignment_group, incident_count** to get a table of assignment_group and incident_count
12. Repeat steps 1-10 to refresh the remaining dashboards in Grafana. Step 11 is to customize different SQL queries and views of that specific dataset

### Additional customization of Grafana: 
1. To further customize the size of the Grids on the Grafana dashboard, **drag and drop** the bottom right corner of each grid. 
2. To move the grids, **drag and drop** the top of the grid.
3. To change the visual representation of data go Click **Edit** on the top right corner of the grid
4. Click the dropdown on the top right corner then select the visualization that works best for your data. New SQL queries will be needed for certain data

## MongoDB Compass GUI 
1. Open MongoDB Compass
2. It should direct you to make a new connection. Ensure that the text in the textbox for URI is mongodb://localhost:27017/
3. Click the green Connect button
4. To the left you can see the incident_event database. Click it
5. Click incidents. This will show all of the data that is in this database. Your VSCode terminal should still be producing and consuming data from the CSV (unless all of it has been processed).
6. Click the refresh button below the Reset and Find buttons, this will show the current quantity of incidents in the database. 


