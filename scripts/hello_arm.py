#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import *
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import joint_goals

class Manipulator:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        self.group = moveit_commander.MoveGroupCommander("manipulator")
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("manipulator")
        self.display_trajectory_publisher = rospy.Publisher(
                                        '/move_group/display_planned_path',
                                        moveit_msgs.msg.DisplayTrajectory, queue_size = 10)
        
        #create a virtual table to prevent collisions
        self.table = PoseStamped()
        self.table.header.frame_id = "base_link"
        self.table.pose.position.x = 0
        self.table.pose.position.y = 0
        self.table.pose.position.z = -0.14
        self.table.pose.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, 0.0))
        self.scene.add_box("table", self.table, size=(2, 2, 0.01))

    def get_current_joints(self):
        return self.group.get_current_joint_values()

    def move_joints(self, joints):
        target_joint = self.group.get_current_joint_values()
        target_joint[0] = joints[0]
        target_joint[1] = joints[1]
        target_joint[2] = joints[2]
        target_joint[3] = joints[3]
        target_joint[4] = joints[4]
        target_joint[5] = joints[5]

        self.group.go(target_joint, wait=True)
        self.group.stop()

class Barista(Manipulator):
    def __init__(self):
        Manipulator.__init__(self)
        rospy.Subscriber("brewing", String, self.order_callback, queue_size = 10)
        #rostopic pub -1 /brewing std_msgs/String "test"
        self.order = None

    def order_callback(self, coffee):
        rospy.loginfo("Order Received %s", coffee.data)
        self.order = coffee.data

def main():
        rospy.init_node('manipulator_test', anonymous=True)
        barista = Barista()
        while not rospy.is_shutdown():
            if barista.order == "test":
                #grab the cup
                barista.move_joints(joint_goals.cup_dock())
                barista.move_joints(joint_goals.cup())
                rospy.sleep(2)
                barista.move_joints(joint_goals.cup_dock())

                #move to first machine
                barista.move_joints(joint_goals.machine_a_dock())
                barista.move_joints(joint_goals.machine_a())
                rospy.sleep(5)
                barista.move_joints(joint_goals.machine_a_dock())

                #move to second machine
                barista.move_joints(joint_goals.machine_b_dock())
                barista.move_joints(joint_goals.machine_b())
                rospy.sleep(5)
                barista.move_joints(joint_goals.machine_b_dock())

                #move to third machine
                barista.move_joints(joint_goals.machine_c_dock())
                barista.move_joints(joint_goals.machine_c())
                rospy.sleep(5)
                barista.move_joints(joint_goals.machine_c_dock())

                #deliver coffee to customer
                barista.move_joints(joint_goals.cup_dock())
                barista.move_joints(joint_goals.cup())

                barista.order = None
            
if __name__ == '__main__':
    main()