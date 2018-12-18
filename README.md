Project: Temperature Logger

Our project takes into acount the field need to be able to plot data from field results.  
The Temperature Logger as indicated by the name focuses on temperature data receive by a sensor.
The Sensor is hooked up to a rasberry pie, which is also where our local Apache server is running.  
Through the rasberry pie the data is logged in sqlite3.
The sqlite3 data is converted and applied to a google charts api which displays the data in graph format.  
The javascript for the graph and the rest of the web app is created through a python script.   
The sql data stacks on top of itself.  The web app gives you the ability to view the data in 6, 12, or 24 hour time frames.
 
