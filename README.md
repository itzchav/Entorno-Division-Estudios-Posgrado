# Entorno-Division-Estudios-Posgrado
Workspace para la simulación del edificio de la División de Estudios de Posgrado.



### Para ejecutar el plano sin obtaculos 
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo.launch 

### Para ejecutar el plano con obtaculos 
cd ~/catkin_ws

source ./devel/setup.bash

export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo plano_completo_obstaculos.launch 
