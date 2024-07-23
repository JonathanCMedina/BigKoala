# BigKoala

## Project Description:
{Insert a description about the project}

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
3. Type `docker-compose up --build` in your VSCode terminal
     It may take a minute to build all containers, with the last three being built to be kafka-1, producer-1, and consumer-1. Please be patient.
4. Once all containers are running, check your VSCode's terminal to see if the data from the incident_event_log.csv is being read and added in (there should be a lot going on in your terminal, this is normal!)

## Grafana 
### MySQL Connection
1. In your browser, go to localhost:3000
2. Login with the username of *admin* and password of *admin* . Skip the password update for now
3. On the upper left side of the Grafana homepage, click the hamburger dropdown menu. Look at **Connections**, press **Add new connection**
4. Search *MySQL*
5. On the top right, press **Add new data source**
6. Name the MySQL database connection *incident_event_csv*
7. Under the Connection header, type *mysql:3036* under Host URL and type *incident_event* for the database name
8. Under the Authentication header, type *root* for Username and *password* for Password
9. At the bottom of the page, click **Save & test**

## Importing the Dashboard 
1. On the left, click the **Dashboards** menu
2. On the top right, click the **New** dropdown button
3. Click **Import**
4. Click **Update dashboard JSON file**
5. Within the directory BigKoala > docker-config on your local computer, upload the *TheRealDashboard* JSON file.
   Alternatively, you can copy/paste the *TheRealDashboard* JSON file into the textbox under **Import via dashboard JSON model**
6. Rename the dashboard to *incident_event*
7. Click the **Import** button

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
1. To further customize the size of the Grids on the Grafana dashboard, 
