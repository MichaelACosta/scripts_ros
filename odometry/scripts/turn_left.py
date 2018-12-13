#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

rightValue = 0

def stopTurnLeft():
    global rightValue
    return rightValue >= 953

def turnLeft():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(175)
    while not stopTurnLeft():
        None
    stopMoviment()

def callbackRight(data):
    global rightValue
    rightValue = int(data.data)

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_x', Int16, queue_size=1)
    stop.publish(135)

def listener():
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    turnLeft()
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()



