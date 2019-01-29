#!/usr/bin/env python

#rostopic echo /joint_states
# joints[0] = shoulder_pan_joint
# joints[1] = shoulder_lift_joint
# joints[2] = elbow_joint
# joints[3] = wrist_1_joint
# joints[4] = wrist_2_joint
# joints[5] = wrist_3_joint

def cup_dock():
    joints = [0,0,0,0,0,0]
    joints[0] = 0.013821992074441347
    joints[1] = -0.39267338040411826
    joints[2] =  0.6244952353813273
    joints[3] = -0.23190523584773626
    joints[4] = 1.644195960617691 
    joints[5] = -0.0003506978661116378

    return joints

def cup():
    joints = [0,0,0,0,0,0]
    joints[0] = 0.01050379385586453
    joints[1] = -0.15672710500094045
    joints[2] =  0.14094231764867438
    joints[3] = 0.015494696097811733
    joints[4] = 1.6405839817724042
    joints[5] = -0.00039735378972771684

    return joints

def machine_a_dock():
    joints = [0,0,0,0,0,0]
    joints[0] = 0.3214675163223246
    joints[1] = -0.653290831663977
    joints[2] =  1.3216962732038837
    joints[3] = -0.6684121441922848
    joints[4] = 0.3215160801323691
    joints[5] = 0.00

    return joints

def machine_a():
    joints = [0,0,0,0,0,0]
    joints[0] = 0.4561069565716158
    joints[1] =  -0.546428612848544
    joints[2] =  1.098097327623587
    joints[3] = -0.5518819168246605
    joints[4] = 0.4561121763400191
    joints[5] = 0.00

    return joints

def machine_b_dock():
    joints = [0,0,0,0,0,0]
    joints[0] = -0.6495586821105643
    joints[1] = -0.5006920596081912
    joints[2] = 1.1870893078397433
    joints[3] = -0.6867958590584493
    joints[4] = 2.4666957479385836
    joints[5] = -0.000305910421836586

    return joints

def machine_b():
    joints = [0,0,0,0,0,0]
    joints[0] = -0.7201078117333779
    joints[1] =  -0.42833236273487785
    joints[2] =  1.02718660867302
    joints[3] = -0.5992296356121729
    joints[4] =  2.396151157853806
    joints[5] = -6.389561469877236e-05

    return joints

def machine_c_dock():
    joints = [0,0,0,0,0,0]
    joints[0] =  -1.6267635711384951
    joints[1] = -0.9291061464135097
    joints[2] =  2.3070844545983746
    joints[3] = -1.378411137085033
    joints[4] = 1.4895799451368212
    joints[5] = 0.00

    return joints

def machine_c():
    joints = [0,0,0,0,0,0]
    joints[0] = -1.6035316224070186
    joints[1] =  -0.8111147292690539
    joints[2] =  1.9288023102381437
    joints[3] = -1.117966336848184
    joints[4] = 1.5127154646715102
    joints[5] = 0.0001122606731307485

    return joints