# Entorno-Division-Estudios-Posgrado
Workspace para la simulación del edificio de la División de Estudios de Posgrado.



### Para ejecutar el plano sin obtaculos 


```shell
$ cd ~/catkin_ws
$ source ./devel/setup.bash
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo plano_completo.launch 
```







### Para ejecutar el plano con obtaculos 
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo_obstaculos.launch 

### Para ejecutar el plano sin obtaculos y visualizar en RVIZ
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo_rviz.launch 

### Para ejecutar el plano sin obtaculos con gmapping
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo_gmapping_noetic.launch 



### Para ejecutar el plano con obtaculos con gmapping
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo_obstaculos_noetic.launch 
