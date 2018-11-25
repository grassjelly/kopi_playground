#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import *
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion

# rabbitmq
import pika
import sys

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

    def move(self, target): 
        self.group.set_pose_target(target)

        plan1 = self.group.plan()
        self.display_trajectory = moveit_msgs.msg.DisplayTrajectory()

        self.display_trajectory.trajectory_start = self.robot.get_current_state()
        self.display_trajectory.trajectory.append(plan1)
        self.display_trajectory_publisher.publish(self.display_trajectory)

        rospy.sleep(5)
        self.group.go(wait=True)


class Barista(Manipulator):
    """
    RabbitMQ consumer worker
    """
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )   # todo: change localhost to static IP
        self.channel = self.connection.channel()

    def start_order_queue(self):
        # RabbitMQ exchange
        self.channel.exchange_declare(exchange='coffee',
                                      exchange_type='topic')

        # RabbitMQ queue configuration
        # todo: change to load from config file
        # todo: routing key is currently read all - to be changed
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange='coffee',
                                queue=queue_name,
                                routing_key='#')
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.order_callback,
                                   queue=queue_name,
                                   no_ack=True)
        rospy.info('Ready to take order ..')
        return True

    def wait_for_order(self):
        if self.start_order_queue:
            self.channel.start_consuming()
        else:
            rospy.logerr('ERROR: Rabbitmq configuration failed')    

    # todo: validate coffee type
    def order_callback(ch, method, properties, body):
        rospy.loginfo('Order received! YAY!')
        """
        I supposed editing here will work?
        - brew method with find_object as argument
        """


def find_object():
    # this is a place holder function for object detection
    #returns the pose of the pseudo object
    target_object = geometry_msgs.msg.Pose()
    target_object.position.x = 0.367
    target_object.position.y = 0.114
    target_object.position.z = 0.906
    target_object.orientation = Quaternion(*quaternion_from_euler(-3.138, -0.000, 1.570))

    return target_object

def milk_pose():
    target_object = geometry_msgs.msg.Pose()
    target_object.position.x = -0.215
    target_object.position.y = 0.617
    target_object.position.z =  0.401
    target_object.orientation = Quaternion(*quaternion_from_euler(-3.138, 0.000, 1.572))

    return target_object
        
def main():
        rospy.init_node('manipulator_test', anonymous=True)
        barista = Barista()
        barista.start_order_queue()  # config rabbitmq consumer

        while not rospy.is_shutdown():
            barista.wait_for_order()

if __name__ == '__main__':
    main()
