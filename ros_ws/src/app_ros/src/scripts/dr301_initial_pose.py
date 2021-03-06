#!/usr/bin/env python3

import rospy, sys
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from time import sleep

def talker_main(x, y, theta):
    
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)
    rospy.init_node('dr301_initialpose')
    rate = rospy.Rate(10)

    msg = PoseWithCovarianceStamped()
    msg.header.frame_id = 'map'
    msg.pose.pose.position.x = x
    msg.pose.pose.position.y = y
    quat = quaternion_from_euler(0, 0, theta)
    msg.pose.pose.orientation.x = quat[0]
    msg.pose.pose.orientation.y = quat[1]
    msg.pose.pose.orientation.z = quat[2]
    msg.pose.pose.orientation.w = quat[3]
    
    if not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        rospy.loginfo(msg) #A posição inicial só é aceita após a segunda publicação (?)
        pub.publish(msg)    
          
if __name__ == '__main__':
        
    # initial_x = eval(input("Digite a posicao inicial no eixo X com formato 0.0: "))
    # initial_y = eval(input("Digite a posicao inicial no eixo Y com formato 0.0: "))
    # initial_theta = eval(input("Digite a rotação inicial em radianos no eixo Z: "))

    initial_x = float(sys.argv[1])   
    initial_y = float(sys.argv[2]) 
    initial_theta = float(sys.argv[3]) 
    
    talker_main(initial_x, initial_y, initial_theta)
    
    
    

    
    
    

        
        
        
    