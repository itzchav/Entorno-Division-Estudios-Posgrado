# Entorno-Division-Estudios-Posgrado
Workspace para la simulación del edificio de la División de Estudios de Posgrado.

<p align="center">
    <img width=70% src="https://github.com/itzchav/Entorno-Division-Estudios-Posgrado/blob/main/plano.png">
</p>

### Para ejecutar el plano sin obtaculos 
Las coordenadas del plano para cada prueba son los siguientes 
|       | Prueba 1     | Prueba 2      | Prueba 3     | Prueba 4 |
|-------|--------------|---------------|--------------|----------|
| x     |    32.700508 |    24.666824  |    32.700508 |23.642405 |
| y     |    -8.362269 |    -18.216396 |    -8.362269 |2.257198  |

Se modifican los parámetros en el código launch, como se muestra a continuación, para cambiar la ubicación del robot en el entorno.
```shell
    <arg name="x2" default="23.642405"/>
  <arg name="y2" default="2.257198"/>
    <arg name="x2" default="32.700508"/>
    <arg name="y2" default="-8.362269"/>
```
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



