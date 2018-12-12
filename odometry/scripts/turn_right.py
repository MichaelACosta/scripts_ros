#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

leftValue = 0

def turn_right():
    global leftValue

    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)

    if (leftValue >= 953):
        try:
            stopMoviment()
        except rospy.ROSInterruptException:
            pass

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
    turn_right()
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()
