#!/usr/bin/env python3

import rospy, sys
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from time import sleep

def talker_main(x, y, theta):
    
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.init_node('dr301_pose_goal')
    rate = rospy.Rate(10)

    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.pose.position.x = x
    pose.pose.position.y = y
    quat = quaternion_from_euler(0, 0, theta)
    pose.pose.orientation.x = quat[0]
    pose.pose.orientation.y = quat[1]
    pose.pose.orientation.z = quat[2]
    pose.pose.orientation.w = quat[3]
    
    if not rospy.is_shutdown():
        rospy.loginfo(pose)
        pub.publish(pose)
        rate.sleep()
        rospy.loginfo(pose) #O destino só é aceito após a segunda publicação (?)
        pub.publish(pose)
    
    
          
if __name__ == '__main__':
        
    # goal_x = eval(input("Digite a posicao desejada no eixo X com formato 0.0: "))
    # goal_y = eval(input("Digite a posicao desejada no eixo Y com formato 0.0: "))
    # goal_theta = eval(input("Digite a rotação desejada em radianos no eixo Z: "))

    goal_x = float(sys.argv[1])   
    goal_y = float(sys.argv[2]) 
    goal_theta = float(sys.argv[3]) 
    
    talker_main(goal_x, goal_y, goal_theta)
    
    

    
    
    

        
        
        
    