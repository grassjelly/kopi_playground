### Running the demo :coffee:

Open three new terminals and run the following:

Manipulator's gazebo world:
``` 
roslaunch ur_gazebo ur5.launch
```

MoveIt!:
```
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
```

Sample application:
```
rosrun kopi_playground hello_arm.py
```

Rviz(optional):
```
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```

Now choose a sample order from the web app.
