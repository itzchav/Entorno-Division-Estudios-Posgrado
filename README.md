# Entorno-Division-Estudios-Posgrado
Workspace para la simulación del edificio de la División de Estudios de Posgrado.

<p align="center">
    <img width=70% src="https://github.com/itzchav/Entorno-Division-Estudios-Posgrado/blob/main/plano.png">
</p>

## Ejecución del Plano

### Sin Obstáculos
Para ejecutar el plano sin obstáculos, utiliza el siguiente comando:

```shell
 cd ~/catkin_ws
 source ./devel/setup.bash
 export TURTLEBOT3_MODEL=burger
 roslaunch turtlebot3_gazebo plano_completo.launch 
```

### Con Obstáculos
Para ejecutar el plano con obstáculos, utiliza el siguiente comando:

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_obstaculos.launch 
```

### Sin Obtaculos y Visualizar en RVIZ

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_rviz.launch 
```
### Con Obtaculos y Visualizar en RVIZ

```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_gazebo plano_completo_obstaculos_rviz.launch 
```

### Sin Obstáculos con Gmapping
Para ejecutar el plano sin obstáculos utilizando Gmapping:
```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_gmapping_noetic.launch 
```

### Con Obstáculos y Gmapping
Para ejecutar el plano con obstáculos utilizando Gmapping:
```shell
cd ~/catkin_ws
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo plano_completo_obstaculos_noetic.launch 
```

### Cambios necesarios en las pruebas 

Las coordenadas del plano para cada prueba son los siguientes:
|       | Prueba 1     | Prueba 2      | Prueba 3     | Prueba 4 |
|-------|--------------|---------------|--------------|----------|
| x     |    32.700508 |    24.666824  |    32.700508 |23.642405 |
| y     |    -8.362269 |    -18.216396 |    -8.362269 |2.257198  |

Para modificar la ubicación del plano en el entorno, se deben ajustar los parámetros en el código launch como se muestra a continuación:
```shell
<arg name="x2" default="23.642405"/>
<arg name="y2" default="2.257198"/>
<arg name="x2" default="32.700508"/>
<arg name="y2" default="-8.362269"
```

