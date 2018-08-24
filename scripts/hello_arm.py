#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import *
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion

class Manipulator:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        self.group = moveit_commander.MoveGroupCommander("manipulator")
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("manipulator")
        self.display_trajectory_publisher = rospy.Publisher(
                                        '/move_group/display_planned_path',
                                        moveit_msgs.msg.DisplayTrajectory)

    def brew(self, target): 
        self.group.set_pose_target(target)

        plan1 = self.group.plan()
        self.display_trajectory = moveit_msgs.msg.DisplayTrajectory()

        self.display_trajectory.trajectory_start = self.robot.get_current_state()
        self.display_trajectory.trajectory.append(plan1)
        self.display_trajectory_publisher.publish(self.display_trajectory);

        rospy.sleep(5)
        self.group.go(wait=True)

class Barista(Manipulator):
    def __init__(self):
        Manipulator.__init__(self)
        rospy.Subscriber("brewing", String, self.order_callback, queue_size = 10)
        self.order = None

    def order_callback(self, coffee):
        rospy.loginfo("Order Received %s", coffee.data)
        self.order = coffee.data
        

def find_object():
    # this is a place holder function for object detection
    #returns the pose of the pseudo object
    target_object = geometry_msgs.msg.Pose()
    target_object.position.x = 0.367
    target_object.position.y = 0.114
    target_object.position.z = 0.906
    target_object.orientation = Quaternion(*quaternion_from_euler(-3.138, -0.000, 1.570))

    return target_object
        
def main():
        rospy.init_node('manipulator_test', anonymous=True)
        barista = Barista()
        while not rospy.is_shutdown():
            if barista.order == "test":
                barista.brew(find_object())
                barista.order = None
            
if __name__ == '__main__':
    main()