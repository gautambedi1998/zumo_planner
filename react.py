#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

rospy.init_node('scared_robot', anonymous=True)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)


def callback(frontdata):
 rospy.loginfo(rospy.get_caller_id() + 'I heard %d', frontdata.data)
 
 if frontdata.data > 15:
  vel_msg = Twist()
  vel_msg.linear.x = 2
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = 0
  pub.publish(vel_msg)

def callback0(frontdata):
 rospy.loginfo(rospy.get_caller_id() + 'I heard %d', frontdata.data)

 if frontdata.data < 15:
  vel_msg = Twist()
  vel_msg.linear.x = -2
#Since we are moving just in x-axis

  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = 0
  pub.publish(vel_msg)

def callback1(leftdata):
 rospy.loginfo(rospy.get_caller_id() + 'I heard %d', leftdata.data)

 if leftdata.data < 15:
  vel_msg = Twist()
  vel_msg.linear.x = -2
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0                                            
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = -2
  pub.publish(vel_msg)

def callback2(rightdata):
 rospy.loginfo(rospy.get_caller_id() + 'I heard %d', rightdata.data)

 if rightdata.data < 15:
  vel_msg = Twist()
  vel_msg.linear.x = -2
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0                                            
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = -2
  pub.publish(vel_msg)



def listener():
 rospy.Subscriber('/zumo/front', Int16, callback)
 rospy.Subscriber('/zumo/front', Int16, callback0)
 rospy.Subscriber('/zumo/left', Int16, callback1)
 rospy.Subscriber('/zumo/right', Int16, callback2)
 #rospy.Subscriber('speed', Int16, callback3)


# spin() simply keeps python from exiting until this node is stopped
 rospy.spin()
if __name__ == '__main__' :
 listener()
