# Shortest_Path_Graph_Dijkstra
finding the shortest path for a graph using dijkstra algorithm

## How to run the code ?
First you need to clone the repo into you machine. Use the following command:
```
$ git clone https://github.com/SupervisionT/Shortest_Path_Graph_Dijkstra.git
```
Make sure you have python 2.7. You may check using this command ``` python --version ```

Navigate to the directory that contain the project.

You can run the solution using bash shell. Type in your terminal
```
$ ./run.sh < path to graph > < from osm-id > < to-osm-id>
```
Working example:
```
$ ./run.sh mapping-coding--graph.dat 287740912 287740913
```
If you have problem making the script executable please try the following command
```
$ chmod a+x main.py
```

To run the test script, type in the terminal:
```
$ python test.py
```
