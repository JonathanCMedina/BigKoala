# BigKoala

## Team:

* Cynthia Serrano Najera (https://github.com/cnajera)
* Jonathan Ceasar Medina (https://github.com/JonathanCMedina)
* Randy Angel Jr. (https://github.com/Juztop)


## Project Description:
BigKoala is a project developed by Cynthia Serrano Najera, Jonathan Ceasar Medina, and Randy Angel Jr. for their Bootcamp Capstone Project. The BigKoala project is intended to simulate the functionality of the existing Incident Alert and Management Tool BigPanda. 

BigKoala was created to simulate an Incident Management application through the retrieval of data from outside sources, filtering data, and displaying it on the Grafana dashboard for use. 

BigKoala utilizes Kafka producers and consumers to retrieve and filter information from the incident_event_log.csv file into a MySQL database. The log is from Kaggle (https://www.kaggle.com/datasets/vipulshinde/incident-response-log?resource=download).

Depending on the machine this application is being ran on, processing all 120k lines with 0.1s delay could take approximately 4 hours (from the developers' general estimations). 

This project is a full backend application. The project is primarily written with Python code. 


This application will have a supplementary Google slides presentation linked here: https://docs.google.com/presentation/d/1fjEAkLGpvn0yyQCQHhJfBsh9KREzoEapN1qVRCmE-RA/edit?usp=sharing 

### Technologies used:

BigKoala uses Docker for containerization, MongoDB and MySQL for database management, Grafana for visualization, as well as Zookeeper and Kafka for managing data streams through the use of producers and consumers. MongoDB Compass GUI is used to look into which incidents have been successfully consumed and saved in the database. 

## Applications to download prior to running the application:
Google Chrome (or your Browser of choice)
  https://www.google.com/chrome/

VSCode (or your Code Editor of choice) 
  https://code.visualstudio.com/download

Docker Desktop
  https://www.docker.com/products/docker-desktop/
  
MongoDB Compass GUI 
  https://www.mongodb.com/try/download/compass

### Potentially needed:
Pip
  https://pip.pypa.io/en/stable/installation/

Git
  https://git-scm.com/downloads

## How to fork BigKoala:
In your machine's terminal (Zshell, Powershell, Bash, etc.) type 
`git fork https://github.com/JonathanCMedina/BigKoala.git`

## How to run the application: 
1. Turn on Docker Desktop (login not required)
2. Open you terminal of choice then cd into BigKoala/docker-config
3. Type `docker-compose up --build` in your terminal.
   It may take a minute to build all containers, with the last three being built to be kafka-1, producer-1, and consumer-1. Please be patient.
4. Once all containers are running, check your terminal to see if the data from the incident_event_log.csv is being read and added in (there should be a lot going on in your terminal, this is normal!)

## Grafana 
### MySQL Connection
1. In your browser, go to localhost:3000
2. Login with the username of *admin* and password of *admin*. Skip the password update for now
3. On the upper left side of the Grafana homepage, click the hamburger dropdown menu. Look at **Connections**, press **Add new connection**
4. Search *MySQL*
5. On the top right, press **Add new data source**
6. Name the MySQL database connection *incident_event*
7. Under the Connection header, type *mysql:3036* under Host URL and type *incident_event* for the database name
8. Under the Authentication header, type *root* for Username and *password* for Password
9. At the bottom of the page, click **Save & test**

### Troubleshooting MySQL Connection:
1. If it is giving an error in Grafana when creating the connection and is directing you to check the Docker logs, go to:
2. The original terminal that's running the docker > press ctrl + c to stop the docker containers.
3. Then in the terminal after everything has stopped (make sure you're in the docker-config directory), do `docker-compose down` to clear the containers.
4. Finally rebuild with `docker-compose up --build`
5. You should be able to remake the connections.
6. If existing connections in the Grafana Data Source tab still exist, delete them then retry after rebooting Docker.

### If your dashboard's grid is showing that there is No data, follow the steps below:
1. Hover over the top right corner of one of the grids (for example, *Incident Assignment Analysis*)
2. Click the **vertical ellipses** (three dots stacked vertically) menu button
3. Click **Edit**
4. Below you'll see that there are SQL queries starting with `SELECT`. Click into those code spaces
5. Do the following for each MySQL code query (if there are more than 1 query row applicable):
  6. Select All (ctrl + a)
  7. Cut (ctrl + x)
  8. Paste (ctrl + v)
  9. Press **Run query**
10. In the top right corner, press **Apply**. This will return you to the Grafana dashboard grid view.
11. Repeat steps 1-10 to refresh the remaining dashboards in Grafana. 

### Additional customization of Grafana: 
1. To further customize the size of the Grids on the Grafana dashboard, **drag and drop** the bottom right corner of each grid. 
2. To move the grids, **drag and drop** the top of the grid.
3. To change the visual representation of data go Click **Edit** on the top right corner of the grid
4. Click the **dropdown** on the top right corner then select the **visualization** that works best for your data. New SQL queries will be needed for certain data
5. To change the visualization type, you may need to customize the SQL query to match it. But for example purposes:
    * Go to **Resolution time (in minutes)** grid edit using the **ellipses** in the top right corner
    * Change the SQL query (if needed)
    * In the top right corner where it says Bar Chart, click the **dropdown**
    * Either go into the **Visualizations** Tab or the **Suggestions** tab to select other Visualization options. Going into the Suggestions tab is recommended. These suggestions populate based on the MySQL query already written to see what is compatible. 
    * If you want to modify the SQL query for a specific visualization, change the SQL query then pick the Visualization chart type (or vice versa) until it shows what you want it to show. 

## MongoDB Compass GUI 
1. Open **MongoDB Compass** 
2. It should direct you to make a new connection. Ensure that the text in the textbox for URI is mongodb://localhost:27017/
3. Click the green **Connect** button
4. To the left you can see the **incident_event** database. Click it
5. Click **incidents**. This will show all of the data that is in this database. Your VSCode terminal should still be producing and consuming data from the CSV (unless all of it has been processed).
6. Click the **refresh** button below the Reset and Find buttons, this will show the current quantity of incidents in the database. 


## Diagrams and Screenshots

### BigKoala Logo
Below is the BigKoala logo which takes a very close likeness to the BigPanda logo
![BigKoala Logo in a similar style to the BigPanda logo, the Logo is of a black outlined Koala with big square glasses over its eyes](Images/BigKoalaLogo.png)

### BigKoala Dashboards
Below are the Grafana dashboard grids after all of the data has been processed.

The first dashboard grid shows the Recent Incidents Table filtered by the 10 most recent incidents, their states, opened at date times, resolved at date times, assigned groups, and the priorty
![The Grafana dashboard grid of the Recent Incidents Table which includes 11 rows, 10 rows are the incidents' details. There are 6 columns in the following left-to-right order: incident_number, incident_state, opened_at, resolved_at, assigned_to, and priority](Images/BigKoalaDash1.png)

The second dashboard grid shows a bar graph of the 15 most recent incidents with an incident state of closed. The graphs' heights are indicated by the amount of time in minutes it took to resolve each incident. 
![The Grafana dashboard grid of the Resolution time in minutes shows the 15 most recent incidents on the x-axis with time in minutes on the y-axis. The bars on each incident show the amount of minutes it took to resolve the incident and are color coded from green (shortest time) to red (longest time) spanning shades of yellow-green to yellow to orange as the time taken increases](Images/BigKoalaDash2.png)

The third dashboard picture shows three grids. The first grid shows Incident Count by Priority, showcasing how many out of 119,999 entries have the priority levels of 4 indicating low, 3 indicating moderate, 2 indicating high, and 1 indicating critical. The second grid on the top right shows the Incident Resolution Time (in hours). The third grid at the bottom shows the Incidents by Hour of Day. 
![The Grafana dashboard grid shows Incident Count by Priorty on the top left. The first row shows the priority levels of 4, 3, 2, and 1 with 4 being the lowest and 1 being the highest priority. The second row shows the amount of incidents that fit the priority level. The dashboard grid to the right of the Incident Count grid shows the Incident Resolution time in hours for each priority level. The first row is the priority level and the second row is the average time in minutes. The third dashboard grid spans the width of the two grids above. This grid shows the Incidents by Hour of Day. The x-axis shows the times of day from 00:00 to 23:00. The y-axis shows the total amount of Incidents from our entire dataset with 09:00 being the most active.](Images/BigKoalaDash3.png)

The fourth dashboard picture shows four grids. The top left graph shows a line graph of the Trend Analysis, indicating total incidents per day in our dataset from February 29 to May 13. The top right graph is the Incidents by Day of the Week, indicating which day of the week has the most incidents from our dataset. The bottom left grid is the Incident Count per Assignment Group table that has two columns. The first column is the Incident Group which is the assigned group that resolved the incident, and the second column shows the amount of incidents resolved by the corresponding incident group. The fourth grid on the bottom left is the Incident Count per Mnemonic Group that shows which Mnemonic Category encounters the most incidents. The left column shows the mnemonic category and the right column shows the incident count. 
![The Grafana dashboard grid shows four graphs. The top left is a line graph Trend Analysis spanning February 29 until May 13. The x-axis shows dates on the calendar, the y-axis shows the amount of incidents. The top right grid is a bar graph with the x-axis being days of the week and the y-axis being the amount of incidents. The bottom left table shows two columns, the left column being the assigned incident group, the right column being the amount of incidents resolved by that group. The bottom right grid shows another table of two columns. The first column is the mnemonic group and the second column indicates the amount of incidents that affected that mnemonic category.](Images/BigKoalaDash4.png)
