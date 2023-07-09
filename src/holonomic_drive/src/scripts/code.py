#!/usr/bin/env python3
import rospy
# from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray , Int32MultiArray
from sensor_msgs.msg import Joy
from math import floor

def callback(data):
    # twist = Twist()
    wheel_l_r = 0
    wheel_2_l = 0
    wheel_3_l = 0
    wheel_4_r = 0

    ang_wheel_1 = 0
    ang_wheel_2 = 0
    ang_wheel_3 = 0
    ang_wheel_4 = 0

# Case 1 : onspot rotation

    if(data.axes[3]==1): # digital key

        ang_wheel_1 = -0.78539816339744830961566084581988
        ang_wheel_2 = 0.78539816339744830961566084581988
        ang_wheel_3 = -0.78539816339744830961566084581988
        ang_wheel_4 = 0.78539816339744830961566084581988

        if(data.axes[1]>0): # right command
            wheel_l_r = -floor(15*data.axes[1])
            wheel_2_l = floor(15*data.axes[1])
            wheel_3_l = floor(15*data.axes[1])
            wheel_4_r = -floor(15*data.axes[1])
        
        elif(data.axes[0]>0): # left command
            wheel_l_r = floor(15*data.axes[1])
            wheel_2_l = -floor(15*data.axes[1])
            wheel_3_l = -floor(15*data.axes[1])
            wheel_4_r = floor(15*data.axes[1])
# Case 2 : zigzag motion

    elif(data.axes[2]==1): # digital key

        if(data.axes[1]>0): # right command
            ang_wheel_1 = (3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_2 = (3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_3 = (3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_4 = (3.1415926535897932384626433832795*(data.axes[1]))

            if(data.axes[2]>0): # right and forward
                wheel_l_r = floor(15*data.axes[1])
                wheel_2_l = floor(15*data.axes[1])
                wheel_3_l = floor(15*data.axes[1])
                wheel_4_r = floor(15*data.axes[1])
            
            elif(data.axes[3]>0): # right and backward
                wheel_l_r = -floor(15*data.axes[1])
                wheel_2_l = -floor(15*data.axes[1])
                wheel_3_l = -floor(15*data.axes[1])
                wheel_4_r = -floor(15*data.axes[1])

        elif(data.axes[3]>0): # left command
            ang_wheel_1 = -(3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_2 = -(3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_3 = -(3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_4 = -(3.1415926535897932384626433832795*(data.axes[1]))

            if(data.axes[2]>0): # left and forward
                wheel_l_r = floor(15*data.axes[1])
                wheel_2_l = floor(15*data.axes[1])
                wheel_3_l = floor(15*data.axes[1])
                wheel_4_r = floor(15*data.axes[1])
            
            elif(data.axes[3]>0): # left and backward
                wheel_l_r = -floor(15*data.axes[1])
                wheel_2_l = -floor(15*data.axes[1])
                wheel_3_l = -floor(15*data.axes[1])
                wheel_4_r = -floor(15*data.axes[1])

# Case 3 : curve turn

    elif(data.axes[4]==1): # digital key

        if(data.axes[1]>0): # right command
            ang_wheel_1 = (3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_2 = (3.1415926535897932384626433832795*(data.axes[1]))

            if(data.axes[2]>0): # right and forward
                wheel_l_r = floor(15*data.axes[1])
                wheel_2_l = floor(15*data.axes[1])
                wheel_3_l = floor(15*data.axes[1])
                wheel_4_r = floor(15*data.axes[1])
            
            elif(data.axes[3]>0): # right and backward
                wheel_l_r = -floor(15*data.axes[1])
                wheel_2_l = -floor(15*data.axes[1])
                wheel_3_l = -floor(15*data.axes[1])
                wheel_4_r = -floor(15*data.axes[1])

        elif(data.axes[3]>0): # left command
            ang_wheel_1 = -(3.1415926535897932384626433832795*(data.axes[1]))
            ang_wheel_2 = -(3.1415926535897932384626433832795*(data.axes[1]))

            if(data.axes[2]>0): # left and forward
                wheel_l_r = floor(15*data.axes[1])
                wheel_2_l = floor(15*data.axes[1])
                wheel_3_l = floor(15*data.axes[1])
                wheel_4_r = floor(15*data.axes[1])
            
            elif(data.axes[3]>0): # left and backward
                wheel_l_r = -floor(15*data.axes[1])
                wheel_2_l = -floor(15*data.axes[1])
                wheel_3_l = -floor(15*data.axes[1])
                wheel_4_r = -floor(15*data.axes[1])

# Case 4 : Default Differential 

    else:
        if(data.axes[1]>0): # right command

            wheel_l_r = floor((15*data.axes[1])*(1-data.axes[3]))
            wheel_2_l = floor((15*data.axes[1])*(1+data.axes[3]))
            wheel_3_l = floor((15*data.axes[1])*(1+data.axes[3]))
            wheel_4_r = floor((15*data.axes[1])*(1-data.axes[3]))
        
        elif(data.axes[0]>0): # left command

            wheel_l_r = floor((15*data.axes[1])*(1+data.axes[3]))
            wheel_2_l = floor((15*data.axes[1])*(1-data.axes[3]))
            wheel_3_l = floor((15*data.axes[1])*(1-data.axes[3]))
            wheel_4_r = floor((15*data.axes[1])*(1+data.axes[3]))

    wheel_vels_arr = [wheel_l_r , wheel_2_l , wheel_3_l , wheel_4_r]
    ang_arr = [ang_wheel_1 , ang_wheel_2 , ang_wheel_3 , ang_wheel_4]
    wheel_data_to_send = Int32MultiArray()
    ang_data_to_send = Int32MultiArray()
    wheel_data_to_send.data = wheel_vels_arr
    ang_data_to_send.data = ang_arr
    pub1.publish(wheel_data_to_send)
    pub2.publish(ang_data_to_send)
    print(wheel_data_to_send)
    print(ang_data_to_send)

def main():
    rospy.init_node('joy_to_rover')
    global pub1, pub2
    pub1=rospy.Publisher('/wheel_vels',Int32MultiArray,queue_size = 10)
    pub2=rospy.Publisher('/angles',Int32MultiArray,queue_size = 10)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()
    

if name == 'main':
    main()