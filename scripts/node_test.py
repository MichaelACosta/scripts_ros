#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import String

leftValue = 0
rightValue = 0
state = 'stop'

def turnRight():
    try:
        startMovimentTurnRight()
    except rospy.ROSInnterruptException:
        pass

def turnLeft():
    try:
        startMovimentTurnLeft()
    except rospy.ROSInnterruptException:
        pass

def goAhead():
    try:
        startMovimentAhead()
    except rospy.ROSInnterruptException:
        pass

def followMe():
    try:
        None
    except rospy.ROSInnterruptException:
        pass

def stopMoviment():
    try:
        stop()
    except rospy.ROSInnterruptException:
        pass

def callbackLeft(data):
    global leftValue
    leftValue = int(data.data)
    evaluateStop()

def callbackRight(data):
    global rightValue
    rightValue = int(data.data)
    evaluateStop()

def callbackWalk(data):
    global state
    if data.data == 'go ahead':
        state = 'goAhead'
        goAhead()
    elif data.data == 'turn left':
        state = 'turnLeft'
        turnLeft()
    elif data.data == 'turn right':
        state = 'turnRight'
        turnRight()
    elif data.data == 'follow me':
        state = 'followMe'
        followMe()
    elif data.data == 'stop':
        state = 'stop'
        stopMoviment()

def stopGoAhead(value, distance):
    return (value/1200.0)*3.14*0.34 >= distance

def evaluateStop():
    global state
    global leftValue
    global rightValue
    if state == 'stop':
        stopMoviment()
    elif state == 'turnRight' and leftValue >= 400:
        stopMoviment()
    elif state == 'turnLeft' and rightValue >= 400:
        stopMoviment()
    elif state == 'goAhead' and (stopGoAhead(rightValue, 1.0) or stopGoAhead(leftValue, 1.0)):
        stopMoviment()
    elif state == 'followMe':
        None

def startMovimentTurnRight():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)

def startMovimentTurnLeft():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(160)

def startMovimentAhead():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(175)

def stop():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stopy = rospy.Publisher('channel_y', Int16, queue_size=1)
    stopy.publish(135)
    stopx = rospy.Publisher('channel_x', Int16, queue_size=1)
    stopx.publish(135)

def listener():
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    rospy.Subscriber("walk", String, callbackWalk)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()