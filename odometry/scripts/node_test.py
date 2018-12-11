#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

leftValue = 0
rightValue = 0

def stopGoAhead(value):
    return (value/1200.0)*3.14*0.34 >= 1.0

def goAhead():
    global leftValue
    global rightValue

    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)

    if ((stopGoAhead(rightValue)) or (stopGoAhead(leftValue)):
        try:
            stopMoviment()
        except rospy.ROSInterruptException:
            pass

def callbackLeft(data):
    global leftValue
    leftValue = int(data.data)
    goAhead()

def callbackRight(data):
    global rightValue
    rightValue = int(data.data)
    goAhead()

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_y', Int16, queue_size=1)
    stop.publish(135)

def listenerLeft():
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listenerLeft()
