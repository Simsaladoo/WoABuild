// Copy Anims from Epic setup:


// For copying Epic Rig anims, first manually position the pose to frame 1
// then for hips, parent constrain to the pelvis
// for thighs, aim constraint to the shins
// for shins, aim constraint to the foot
// 
// for clavicle_R, aim constrain to upper_arm_R
// for upper_arm_R, aim constrain to forearm_R
// for forearm_R, aim constrain to hand_R
// for hand_R, parent constrain to hand_R





print("Attaching copy rig to Epic's root skeleton");
select -r pelvis ;
selectKey -clear ;
select -add aMasterSkel_M:hips ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","0" };
parentConstraint -mo -weight 1;

// spine
select -r spine_01 ;
selectKey -clear ;
select -add aMasterSkel_M:spine ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","0" };
parentConstraint -mo -weight 1;

select -r spine_02 ;
selectKey -clear ;
select -add aMasterSkel_M:chest_1 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","0" };
parentConstraint -mo -weight 1;



// thighs
select -r thigh_r ;
selectKey -clear ;
select -add aMasterSkel_M:shin_R ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

select -r thigh_l ;
selectKey -clear ;
select -add aMasterSkel_M:shin_L ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

// shins
select -r calf_r ;
selectKey -clear ;
select -add aMasterSkel_M:foot_R ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

select -r calf_l ;
selectKey -clear ;
select -add aMasterSkel_M:foot_L ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;


// knees



// feet




// clavicles
select -r clavicle_r ;
selectKey -clear ;
select -add aMasterSkel_M:deltoid_R ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

select -r clavicle_l ;
selectKey -clear ;
select -add aMasterSkel_M:deltoid_L ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

//upper arms to elbows
select -r upperarm_r ;
selectKey -clear ;
select -add aMasterSkel_M:forearm_R ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

select -r upperarm_l ;
selectKey -clear ;
select -add aMasterSkel_M:forearm_L ;
doCreateAimConstraintArgList 1 { "1","0","0","0","1","0","0","0","1","0","0","1","0","1","vector","","0","0","0","","1" };
aimConstraint -mo -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;

// elbows to hands

select -r hand_r ;
selectKey -clear ;
select -add aMasterSkel_M:hand_R ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","0" };
parentConstraint -mo -weight 1;

select -r hand_l ;
selectKey -clear ;
select -add aMasterSkel_M:hand_L ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","0" };
parentConstraint -mo -weight 1;











