#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist


class OdomInitializer:
    def __init__(self):
        # Inicializa el nodo
        rospy.init_node('odometry_initializer', anonymous=True)

        # Suscriptor al tópico de odometría del robot
        self.subscriber = rospy.Subscriber('/robot/odom', Odometry, self.odom_callback)
        
        # Publicador para el tópico '/punto_h'
        self.ph_pub = rospy.Publisher('/punto_h', Odometry, queue_size=10)

        # Variable para almacenar la odometría inicial
        self.initial_odom = None
        
        # Define la tasa de publicación
        self.rate = rospy.Rate(10)  # 10 Hz

    def odom_callback(self, msg):
        if self.initial_odom is None:
            self.initial_odom = msg
            rospy.loginfo("Inicializando con la odometría actual")
            self.publish_initial_odom()

    def publish_initial_odom(self):
        if self.initial_odom:
            # Publica el mensaje con los datos de la odometría inicial
            self.ph_pub.publish(self.initial_odom)

    def run(self):
        while not rospy.is_shutdown():
            # Mantiene el nodo activo y publica la odometría inicial
            self.rate.sleep()

if __name__ == '__main__':
    try:
        initializer = OdomInitializer()
        initializer.run()
    except rospy.ROSInterruptException:
        pass



