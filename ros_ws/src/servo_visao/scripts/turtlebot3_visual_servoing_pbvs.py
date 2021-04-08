#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################
#                                           #
# Node to control the Turtlebot3 simulator. #
# This node receives image poit and sends   #
# control signal to the cmd_vel topic.      #
# Atualizado por:                           #
# Author: Alexander Silva                   #
# Autonomous Vehicle - Infnet	            #
# Version: 1.0                              #
# Date: 29-03-2021                          #
#                                           #
#############################################

# importing libraries
import rospy, time, sys, math, control_lib, tf
import numpy as np
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Bool, Int32
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CameraInfo
import image_geometry

############ WORK FUNCTIONS ##################

def callback_camera_info(msg):

    global model
    global camera_matrix
    
    model.fromCameraInfo(msg)
    
    K = np.array(msg.K).reshape([3, 3])
    f = K[0][0]
    u0 = K[0][2]
    v0 = K[1][2]

    camera_matrix[0] = f
    camera_matrix[1] = u0
    camera_matrix[2] = v0
    
def callback_img_point(msg):
    """
    This function receives the goal and saves it 
    in a globa variable goal
    """

    global camera_height
    global image_point
    global mask_is_true

    # recovering point
    u = msg.x
    v = msg.y
    base_point = [u, v]
    mask_is_true = msg.theta
    distance = 0   

    try:
        # finding distance to the point 
        pixel_rectified = model.rectifyPoint(base_point)
        line = model.projectPixelTo3dRay(pixel_rectified)
        th = math.atan2(line[2],line[1])
        distance = math.tan(th) * camera_height

        image_point.x = u
        image_point.y = v
        image_point.theta = distance

        rospy.loginfo(rospy.get_caller_id() + " Distancia do objejto = %s m", '{:.2f}'.format(image_point.theta))
        rospy.loginfo(rospy.get_caller_id() + " Ponto base u = %s pixel", '{:.2f}'.format(image_point.x))
        rospy.loginfo(rospy.get_caller_id() + " Ponto base v = %s pixel", '{:.2f}'.format(image_point.y))                

    except:
        pass


def callback_odom(msg):
   
    global robot_pose
    
    robot_pose.x = round(msg.pose.pose.position.x, 3)
    robot_pose.y = round(msg.pose.pose.position.y, 3)
    
    q = [msg.pose.pose.orientation.x, 
        msg.pose.pose.orientation.y, 
        msg.pose.pose.orientation.z, 
        msg.pose.pose.orientation.w]

    euler = tf.transformations.euler_from_quaternion(q)
    
    theta = round(euler[2],3)
    
    robot_pose.theta = theta


def callback_control_type(msg):
    """
    This function receives the type of controller:
    0: Cartesian control
    1: Polar control
    """
    global ctrl_type 
    ctrl_type = msg.data


def control_robot():
    """
    This function is called from the main conde and calls 
    all work methods of fucntions into the codde.
    """

    # Global variables    
    global image_point
    global robot_pose
    global gains_cart
    global ctrl_type
    global max_lin
    global max_ang    
    global camera_matrix
    global mask_is_true
    global vel_lim
    
    # Initializing ros node
    rospy.init_node('turtlebot3_control', anonymous=True)    # node name
    
    # Subscribers
    rospy.Subscriber('img_point',Pose2D, callback_img_point)   # receives the goal coordinates
    rospy.Subscriber('odom', Odometry, callback_odom)    # receives thr robot odometry
    rospy.Subscriber('control_type',Int32,callback_control_type) #receives c.t.
    rospy.Subscriber('camera_info',CameraInfo, callback_camera_info)   # receives the goal coordinates

    # Publishers
    cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)  # send control signals

    # control rate
    rate = rospy.Rate(30)   # run the node at 15H

    # main loop
    while not rospy.is_shutdown():

        # Computing the control signal
        control_signal = Twist()       

        # calling PBVS
        try:
            if ctrl_type == 0:                
                
                control_signal = control_lib.pbvs(image_point, camera_matrix, robot_pose, gains_cart, vel_lim, threshold)                
                #rospy.loginfo(control_signal)
    
            else:
                control_signal = Twist()
                control_signal.linear.x = 0.0
                control_signal.angular.z = 0.5
        except:
            pass

        #print control_signal
        cmd_vel.publish(control_signal)       
        
        rate.sleep()

############ MAIN CODE #######################
# initializing Global variables
# Readin from launch
K_eu = float(sys.argv[1])   # Control gain for linear velocity
K_ev = float(sys.argv[2])   # Control gain for angular velocity
threshold = float(sys.argv[3])
max_lin = float(sys.argv[4])
max_ang = float(sys.argv[5])
ctrl_type = int(sys.argv[6])
camera_height = float(sys.argv[7])

# Inner values
robot_pose = Pose2D()
image_point = Pose2D()
gains_cart = [K_eu, K_ev]
camera_matrix = np.zeros((3,1))
vel_lim = [max_lin, max_ang]
mask_is_true = 0

# creating a camera model
model = image_geometry.PinholeCameraModel()

if __name__ == '__main__':
    control_robot()
    '''
    try:
        control_robot()
    except:
        print('Node ended.')
    '''
