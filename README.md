# Entorno-Division-Estudios-Posgrado
Workspace para la simulación del edificio de la División de Estudios de Posgrado.

<p align="center">
    <img width=40% src="https://github.com/itzchav/Navegacion-con-Aprendizaje-por-Refuerzo/blob/main/turtle_rviz.png">
</p>

### Para ejecutar el plano sin obtaculos 


```shell
 cd ~/catkin_ws
 source ./devel/setup.bash
 export TURTLEBOT3_MODEL=burger
 roslaunch turtlebot3_gazebo plano_completo.launch 
```







### Para ejecutar el plano con obtaculos 
```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_obstaculos.launch 
```

### Para ejecutar el plano sin obtaculos y visualizar en RVIZ

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_rviz.launch 
```
### Para ejecutar el plano sin obtaculos con gmapping

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_gmapping_noetic.launch 
```

### Para ejecutar el plano con obtaculos con gmapping

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_obstaculos_noetic.launch 
```
