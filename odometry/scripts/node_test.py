#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import String

leftValue = 0
rightValue = 0

def turnLeft():
    global rightValue
    try:
        startMovimentTurnLeft()
    except rospy.ROSInterruptException:
        pass
    while not rightValue >= 953:
        rospy.spin()
    try:
        stopMoviment()
    except rospy.ROSInterruptException:
        pass

def stopGoAhead(value):
    return (value/1200.0)*3.14*0.34 >= 1.0

def goAhead():
    global leftValue
    global rightValue
    try:
        startMovimentAhead()
    except rospy.ROSInterruptException:
        pass
    while not (stopGoAhead(rightValue) or stopGoAhead(leftValue)):
        rospy.spin()
    try:
        stopMoviment()
    except rospy.ROSInterruptException:
        pass

def callbackLeft(data):
    global leftValue
    leftValue = int(data.data)

def callbackRight(data):
    global rightValue
    rightValue = int(data.data)

def callbackWalk(data):
    if (data.data == 'goAhead'):
        goAhead()
    if (data.data == 'turnLeft'):
        turnLeft()

def startMovimentTurnLeft():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_x', Int16, queue_size=1)
    stop.publish(175)

def startMovimentAhead():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_y', Int16, queue_size=1)
    stop.publish(175)

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_y', Int16, queue_size=1)
    stop.publish(135)

def listener():
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    rospy.Subscriber("walk", String, callbackWalk)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()
