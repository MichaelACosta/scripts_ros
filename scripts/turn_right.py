#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

leftValue = 0

def stopTurnRight():
    global leftValue
    return leftValue >= 953

def turnRight():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)
    while not stopTurnRight():
        None
    stopMoviment()

def callbackLeft(data):
    global leftValue
    leftValue = int(data.data)

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_x', Int16, queue_size=1)
    stop.publish(135)

def listener():
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    turnRight()
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()
