#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

rightValue = 0

def turn_left():
    global rightValue

    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(175)

    if (rightValue >= 953):
        try:
            stopMoviment()
        except rospy.ROSInterruptException:
            pass

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
    turn_left()
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()



