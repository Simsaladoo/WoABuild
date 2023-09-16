// Copy Anims from Horse setup:


// For copying Horse Rig anims, first manually position the skeleton under a group to frame 1
// then for hips, parent constrain TPs BR_Root to the Hips
// for thighs, aim constraint to the shins
// for shins, aim constraint to the foot
// 
// for clavicle_R, aim constrain to upper_arm_R
// for upper_arm_R, aim constrain to forearm_R
// for forearm_R, aim constrain to hand_R
// for hand_R, parent constrain to hand_R





print("Attaching copy rig to Horse's root skeleton");
// first is hips and torso
select -r Idle_Horse:BR_Root ;
select -tgl -sym aMasterHorseREF:torso_5 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:Spine_5 ;
select -tgl -sym aMasterHorseREF:torso_1 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

// copy leg controls
select -r -sym Idle_Horse:F_L_Leg_4 ;
select -tgl -sym aMasterHorseREF:FrontLegControls2 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:F_L_Leg_5 ;
select -tgl -sym aMasterHorseREF:FrontLegControls1 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:F_R_Leg_4 ;
select -tgl -sym aMasterHorseREF:FrontLegControls3 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:F_R_Leg_5 ;
select -tgl -sym aMasterHorseREF:FrontLegControls4 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:B_L_Leg_3 ;
select -tgl -sym aMasterHorseREF:RearLegControls2 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:B_L_Leg_4 ;
select -tgl -sym aMasterHorseREF:RearLegControls1 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:B_R_Leg_3 ;
select -tgl -sym aMasterHorseREF:RearLegControls3 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;

select -r -sym Idle_Horse:B_R_Leg_4 ;
select -tgl -sym aMasterHorseREF:RearLegControls4 ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

select -cl -sym  ;



//Neck control

select -r -sym Idle_Horse:Neck_1 ;
select -tgl -sym aMasterHorseREF:neck_1 ;
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;