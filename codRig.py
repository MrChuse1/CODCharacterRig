import maya.cmds as cmds

# Call of Duty Rigging Tool
# By MrChuse
# Version 1.0.1.1

# Added Spine IK

debug = False
debugScene = ''
if debugScene == 'BO4':
    
    # Open the test scene
    cmds.file(r"D:\OneDrive\Scripts\MrChuse\CODRig\BO3Test\BO4Test.ma", o=True, f=True)
elif debugScene == 'IW9':
    
    # Open the test scene
    cmds.file(r"D:\OneDrive\Scripts\MrChuse\CODRig\IW9Test\IW9Test.ma", o=True, f=True)
    
Joints = {
            'j_neck': {'name': 'Neck', 'color': (0.8,0,1), 'tOffset': (0,0,4), 'rotate': (0,30,0), 'scale': (12,12,12), 'parent': 'Spine_4', 'thickness': 2},
            'j_neck2': {'name': 'Upper_Neck', 'color': (0.8,0,1), 'tOffset': (1,0,0), 'rotate': (0,20,0), 'scale': (8,8,8), 'parent': 'Neck', 'thickness': 2},
            'j_head': {'name': 'Head', 'color': (0.8,0,1), 'tOffset': (4,0,0), 'rotate': (0,0,0), 'scale': (10,10,10), 'parent': 'Upper_Neck', 'thickness': 5},
}
SpineJoints = {
    'j_mainroot': {'name': 'Main_Root', 'color': (0,1,0), 'tOffset': (0,0,0), 'rotate': (0,0,0), 'scale': (19,24,10), 'parent': 'Origin', 'thickness': 3,},
    'j_spinelower': {'name': 'Spine_Lower', 'color': (0,1,0), 'tOffset': (1,0,0), 'rotate': (0,0,0), 'scale': (13,22,10), 'parent': 'Main_Root', 'thickness': 1,},
    'j_spineupper': {'name': 'Spine_Upper', 'color': (0,1,0), 'tOffset': (2,0,0), 'rotate': (0,0,0), 'scale': (13,22,10), 'parent': 'Spine_Lower', 'thickness': 1,},
    'j_spine4': {'name': 'Spine_4', 'color': (0,1,0), 'tOffset': (2,0,0), 'rotate': (0,0,0), 'scale': (17,22,10), 'parent': 'Spine_Upper', 'thickness': 2,},
    
}
IKs = {
    'Left_Arm': {'joint': 'j_shoulder_le', 'effector': 'j_wrist_le', 'solver': 'j_elbow_le', 'name': 'Left_Arm', 'rotate': (-144.176,62.738,-125.098), 'tOffset': (0,0,0), 'scale': (6,6,6), 'color': (0,0,1)},
    'Right_Arm': {'joint': 'j_shoulder_ri', 'effector': 'j_wrist_ri', 'solver': 'j_elbow_ri', 'name': 'Right_Arm', 'rotate': (-144.176,62.738,-159), 'tOffset': (0,0,0), 'scale': (6,6,6), 'color': (1,0,0)},
    'Left_Leg': {'joint': 'j_hip_le', 'effector': 'j_ankle_le', 'solver': 'j_knee_le', 'name': 'Left_Leg', 'rotate': (0,0,0), 'tOffset': (3,0,0), 'scale': (8,8,8), 'color': (0,0,1)},
    'Right_Leg': {'joint': 'j_hip_ri', 'effector': 'j_ankle_ri', 'solver': 'j_knee_ri', 'name': 'Right_Leg', 'rotate': (0,0,0), 'tOffset': (3,0,0), 'scale': (8,8,8), 'color': (1,0,0)}  
}

FKs = {
    'Left_Shoulder': {'joint': 'j_shoulder_le_FK', 'rotate': (90,34,70), 'tOffset': (0,0,0), 'parent': 'Spine_4', 'color': (0.2,0,1)},
    'Left_Elbow': {'joint': 'j_elbow_le_FK', 'rotate': (0,0,45), 'tOffset': (0,0,0), 'parent': 'Left_Shoulder', 'color': (0.2,0,1)},
    'Left_Wrist': {'joint': 'j_wrist_le_FK', 'rotate': (55,-28,-58), 'tOffset': (0,0,0), 'parent': 'Left_Elbow', 'color': (0.2,0,1)},
    'Right_Shoulder': {'joint': 'j_shoulder_ri_FK', 'rotate': (90,34,-70), 'tOffset': (0,0,0), 'parent': 'Spine_4', 'color': (1,0.2,0)},
    'Right_Elbow': {'joint': 'j_elbow_ri_FK', 'rotate': (0,0,-135), 'tOffset': (0,0,0), 'parent': 'Right_Shoulder', 'color': (1,0.2,0)},
    'Right_Wrist': {'joint': 'j_wrist_ri_FK', 'rotate': (55,37,-140), 'tOffset': (0,0,0), 'parent': 'Right_Elbow', 'color': (1,0.2,0)},
    
    'Left_Leg': {'joint': 'j_hip_le_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Main_Root', 'color': (0.2,0,1)},
    'Left_Knee': {'joint': 'j_knee_le_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Left_Leg', 'color': (0.2,0,1)},
    'Left_Ankle': {'joint': 'j_ankle_le_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Left_Knee', 'color': (0.2,0,1)},
    'Right_Leg': {'joint': 'j_hip_ri_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Main_Root', 'color': (1,0.2,0)},
    'Right_Knee': {'joint': 'j_knee_ri_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Right_Leg', 'color': (1,0.2,0)},
    'Right_Ankle': {'joint': 'j_ankle_ri_FK', 'rotate': (0,0,-90), 'tOffset': (0,5,0), 'parent': 'Right_Knee', 'color': (1,0.2,0)},
}

Fingers = {
    'Left_Index': {'joint': 'j_index_le', 'parent': 'j_wrist_le', 'color': (0,0.2,1)},
    'Left_Middle': {'joint': 'j_mid_le', 'parent': 'j_wrist_le', 'color': (0,0.2,1)},
    'Left_Ring': {'joint': 'j_ring_le', 'parent': 'j_wrist_le', 'color': (0,0.2,1)},
    'Left_Pinky': {'joint': 'j_pinky_le', 'parent': 'j_wrist_le', 'color': (0,0.2,1)},
    'Left Thumb': {'joint': 'j_thumb_le', 'parent': 'j_wrist_le', 'color': (0,0.2,1)},

    'Right_Index': {'joint': 'j_index_ri', 'parent': 'j_wrist_ri', 'color': (1,0.2,0)},
    'Right_Middle': {'joint': 'j_mid_ri', 'parent': 'j_wrist_ri', 'color': (1,0.2,0)},
    'Right_Ring': {'joint': 'j_ring_ri', 'parent': 'j_wrist_ri', 'color': (1,0.2,0)},
    'Right_Pinky': {'joint': 'j_pinky_ri', 'parent': 'j_wrist_ri', 'color': (1,0.2,0)},
    'Right Thumb': {'joint': 'j_thumb_ri', 'parent': 'j_wrist_ri', 'color': (1,0.2,0)},
}
Controls = ['Origin']

Shapes = {
    "Arrow": [
                (0.0, 0.0, -2.001501540839854),
                (0.8006006163359417, 0.0, -1.2009009245039126),
                (0.40030030816797085, 0.0, -1.2009009245039126),
                (0.40030030816797085, 0.0, -0.40030030816797085),
                (1.2009009245039126, 0.0, -0.40030030816797085),
                (1.2009009245039126, 0.0, -0.8006006163359417),
                (2.001501540839854, 0.0, 0.0),
                (1.2009009245039126, 0.0, 0.8006006163359417),
                (1.2009009245039126, 0.0, 0.40030030816797085),
                (0.40030030816797085, 0.0, 0.40030030816797085),
                (0.40030030816797085, 0.0, 1.2009009245039126),
                (0.8006006163359417, 0.0, 1.2009009245039126),
                (0.0, 0.0, 2.001501540839854),
                (-0.8006006163359417, 0.0, 1.2009009245039126),
                (-0.40030030816797085, 0.0, 1.2009009245039126),
                (-0.40030030816797085, 0.0, 0.40030030816797085),
                (-1.2009009245039126, 0.0, 0.40030030816797085),
                (-1.2009009245039126, 0.0, 0.8006006163359417),
                (-2.001501540839854, 0.0, 0.0),
                (-1.2009009245039126, 0.0, -0.8006006163359417),
                (-1.2009009245039126, 0.0, -0.40030030816797085),
                (-0.40030030816797085, 0.0, -0.40030030816797085),
                (-0.40030030816797085, 0.0, -1.2009009245039126),
                (-0.8006006163359417, 0.0, -1.2009009245039126),
                (0.0, 0.0, -2.001501540839854)
            ],
    "Sphere": [
            (0.0, 2.001501540839854, 0.0),
            (-9.331221744602883e-09, 1.9768597796103284, 0.3131038753308959),
            (-1.843267699523828e-08, 1.903541130260558, 0.6184980664640812),
            (-2.708025942441291e-08, 1.7833509413547823, 0.9086628426976106),
            (-3.5061033711582e-08, 1.619248777234614, 1.1764531908237743),
            (-4.217849039619503e-08, 1.4152752878617791, 1.4152754071605675),
            (-4.82573740850274e-08, 1.176453071524986, 1.619249015832191),
            (-5.314799968465514e-08, 0.9086627233988221, 1.7833511799523587),
            (-5.672994644226307e-08, 0.6184979471652929, 1.9035413688581349),
            (-5.891501246721531e-08, 0.3131036367333192, 1.9768600182079052),
            (-5.964939417957824e-08, 0.0, 2.001501779437431),
            (-5.891501246721531e-08, -0.3131036367333192, 1.9768600182079052),
            (-5.672994644226307e-08, -0.6184979471652929, 1.9035413688581349),
            (-5.314799968465514e-08, -0.9086627233988221, 1.7833511799523587),
            (-4.82573740850274e-08, -1.176453071524986, 1.619249015832191),
            (-4.217849039619503e-08, -1.4152752878617791, 1.4152754071605675),
            (-3.5061033711582e-08, -1.619248777234614, 1.1764531908237743),
            (-2.708025942441291e-08, -1.7833509413547823, 0.9086628426976106),
            (-1.843267699523828e-08, -1.903541130260558, 0.6184980664640812),
            (-9.331221744602883e-09, -1.9768597796103284, 0.3131038753308959),
            (0.0, -2.001501540839854, 0.0),
            (0.0, -1.9768597796103284, -0.31310399462968425),
            (0.0, -1.903541130260558, -0.6184983050616579),
            (0.0, -1.7833509413547823, -0.9086631409445814),
            (0.0, -1.619248777234614, -1.1764536680189277),
            (0.0, -1.4152752878617791, -1.4152760036545093),
            (0.0, -1.176453071524986, -1.6192494930273444),
            (0.0, -0.9086627233988221, -1.7833517764463007),
            (0.0, -0.6184979471652929, -1.903542084650865),
            (0.0, -0.3131036367333192, -1.9768607340006352),
            (0.0, 0.0, -2.001502495230161),
            (0.0, 0.3131036367333192, -1.9768607340006352),
            (0.0, 0.6184979471652929, -1.903542084650865),
            (0.0, 0.9086627233988221, -1.7833517764463007),
            (0.0, 1.176453071524986, -1.6192494930273444),
            (0.0, 1.4152752878617791, -1.4152760036545093),
            (0.0, 1.619248777234614, -1.1764536680189277),
            (0.0, 1.7833509413547823, -0.9086631409445814),
            (0.0, 1.903541130260558, -0.6184983050616579),
            (0.0, 1.9768597796103284, -0.31310399462968425),
            (0.0, 2.001501540839854, 0.0),
            (-0.31310393498029004, 1.9768597796103284, 0.0),
            (-0.6184981261134754, 1.903541130260558, 0.0),
            (-0.908662961996399, 1.7833509413547823, 0.0),
            (-1.1764533101225625, 1.619248777234614, 0.0),
            (-1.4152756457581444, 1.4152752878617791, 0.0),
            (-1.6192491351309795, 1.176453071524986, 0.0),
            (-1.7833514185499355, 0.9086627233988221, 0.0),
            (-1.9035416074557117, 0.6184979471652929, 0.0),
            (-1.976860256805482, 0.3131036367333192, 0.0),
            (-2.0015020180350076, 0.0, 0.0),
            (-1.976860256805482, -0.3131036367333192, 0.0),
            (-1.9035416074557117, -0.6184979471652929, 0.0),
            (-1.7833514185499355, -0.9086627233988221, 0.0),
            (-1.6192491351309795, -1.176453071524986, 0.0),
            (-1.4152756457581444, -1.4152752878617791, 0.0),
            (-1.1764533101225625, -1.619248777234614, 0.0),
            (-0.908662961996399, -1.7833509413547823, 0.0),
            (-0.6184981261134754, -1.903541130260558, 0.0),
            (-0.31310393498029004, -1.9768597796103284, 0.0),
            (0.0, -2.001501540839854, 0.0),
            (0.3131038455061988, -1.9768597796103284, 0.0),
            (0.6184980068146871, -1.903541130260558, 0.0),
            (0.9086627233988221, -1.7833509413547823, 0.0),
            (1.176453071524986, -1.619248777234614, 0.0),
            (1.4152752878617791, -1.4152752878617791, 0.0),
            (1.619248777234614, -1.176453071524986, 0.0),
            (1.7833509413547823, -0.9086627233988221, 0.0),
            (1.903541130260558, -0.6184979471652929, 0.0),
            (1.9768597796103284, -0.3131036367333192, 0.0),
            (2.001501540839854, 0.0, 0.0),
            (1.9768597796103284, 0.3131036367333192, 0.0),
            (1.903541130260558, 0.6184979471652929, 0.0),
            (1.7833509413547823, 0.9086627233988221, 0.0),
            (1.619248777234614, 1.176453071524986, 0.0),
            (1.4152752878617791, 1.4152752878617791, 0.0),
            (1.176453071524986, 1.619248777234614, 0.0),
            (0.9086627233988221, 1.7833509413547823, 0.0),
            (0.6184980068146871, 1.903541130260558, 0.0),
            (0.3131038455061988, 1.9768597796103284, 0.0),
            (0.0, 2.001501540839854, 0.0),
            (0.0, 1.9768597796103284, -0.31310399462968425),
            (0.0, 1.903541130260558, -0.6184983050616579),
            (0.0, 1.7833509413547823, -0.9086631409445814),
            (0.0, 1.619248777234614, -1.1764536680189277),
            (0.0, 1.4152752878617791, -1.4152760036545093),
            (0.0, 1.176453071524986, -1.6192494930273444),
            (0.0, 0.9086627233988221, -1.7833517764463007),
            (0.0, 0.6184979471652929, -1.903542084650865),
            (0.0, 0.3131036367333192, -1.9768607340006352),
            (0.0, 0.0, -2.001502495230161),
            (0.6184983050616579, 0.0, -1.903542084650865),
            (1.176453787317716, 0.0, -1.619249731624921),
            (1.6192498509237094, 0.0, -1.176453787317716),
            (1.9035423232484419, 0.0, -0.6184983647110521),
            (2.001501540839854, 0.0, 0.0),
            (1.903541130260558, 0.0, 0.6184980068146871),
            (1.619248777234614, 0.0, 1.1764531908237743),
            (1.176453071524986, 0.0, 1.6192488965334026),
            (0.6184979471652929, 0.0, 1.9035412495593464),
            (-5.964939417957824e-08, 0.0, 2.001501779437431),
            (-0.6184981261134754, 0.0, 1.9035413688581349),
            (-1.1764533101225625, 0.0, 1.619249015832191),
            (-1.6192491351309795, 0.0, 1.1764533101225625),
            (-1.9035416074557117, 0.0, 0.6184981261134754),
            (-2.0015020180350076, 0.0, 0.0),
            (-1.9035416074557117, 0.0, -0.6184981261134754),
            (-1.6192492544297676, 0.0, -1.176453429421351),
            (-1.1764535487201393, 0.0, -1.619249373728556),
            (-0.6184983050616579, 0.0, -1.9035419653520766),
            (0.0, 0.0, -2.001502495230161)
        ],
    "Gear": [
            (-0.1831451367158871, 0.0, -1.9688981435835975),
            (-0.08016223035760504, 0.0, -1.424910142313325),
            (0.2913626899858565, 0.0, -1.397105097768184),
            (0.6430317256821292, 0.0, -1.2740896471493144),
            (0.954867881657974, 0.0, -1.7315681158569183),
            (1.3166068046861326, 0.0, -1.4735764149704769),
            (1.6135439258005473, 0.0, -1.1430580934022687),
            (1.1939272305203956, 0.0, -0.781877785172391),
            (1.355609846159615, 0.0, -0.4462249772153243),
            (1.4249099319855256, 0.0, -0.08016261435117376),
            (1.9770167544414288, 0.0, -0.038844183867340044),
            (1.9344591432773475, 0.0, 0.40342536276371044),
            (1.7966906553990056, 0.0, 0.825839198145925),
            (1.2740908453616502, 0.0, 0.6430325043934684),
            (1.064247138807185, 0.0, 0.9508803230361444),
            (0.7818781368370868, 0.0, 1.1939274851034107),
            (1.0221485601850735, 0.0, 1.6927255501307752),
            (0.6178520249074239, 0.0, 1.8770034010800105),
            (0.18314513671588942, 0.0, 1.968898382002176),
            (0.08016221299102935, 0.0, 1.4249104640058996),
            (-0.29136272471900787, 0.0, 1.397105502734753),
            (-0.6430317777818587, 0.0, 1.274090135389879),
            (-0.9548679511242792, 0.0, 1.7315686873714762),
            (-1.316606804686128, 0.0, 1.4735766533890562),
            (-1.6135439258005448, 0.0, 1.1430583318208474),
            (-1.1939272478869714, 0.0, 0.7818781068649654),
            (-1.355609828793037, 0.0, 0.44622513235990835),
            (-1.4249098972523697, 0.0, 0.08016268622176266),
            (-1.9770167023416967, 0.0, 0.03884417246393463),
            (-1.9344588458747152, 0.0, -0.40342655041229425),
            (-1.7966888454342211, 0.0, -0.8258409718969756),
            (-1.2740894521947093, 0.0, -0.6430322795686422),
            (-1.0642471040740267, 0.0, -0.9508802511655553),
            (-0.7818781194705111, 0.0, -1.1939273299588267),
            (-1.0221485254519176, 0.0, -1.692725478260187),
            (-0.6178520249074192, 0.0, -1.8770031626614314),
            (-0.1831451367158871, 0.0, -1.9688981435835975)
        ],
    "Sphere Pin": [
        (0.0, 0.0, 0.0),
        (0.0, 3.602702773511737, 0.0),
        (0.18786230730371928, 3.6174878302494524, 0.0),
        (0.3710988040888123, 3.661479019859315, 0.0),
        (0.5451976340392933, 3.733593133202781, 0.0),
        (0.7058718429149915, 3.8320544316748815, 0.0),
        (0.8491651727170676, 3.9544385252985825, 0.0),
        (0.9715492663407685, 4.097731855100658, 0.0),
        (1.0700105648128693, 4.258406063976356, 0.0),
        (1.1421246781563348, 4.432504929716473, 0.0),
        (1.1861158677661972, 4.615741515975658, 0.0),
        (1.2009009245039124, 4.80360369801565, 0.0),
        (1.1861158677661972, 4.991465880055642, 0.0),
        (1.1421246781563348, 5.174702466314826, 0.0),
        (1.0700105648128693, 5.3488013320549435, 0.0),
        (0.9715492663407685, 5.509475540930642, 0.0),
        (0.8491651727170676, 5.652768870732717, 0.0),
        (0.7058718429149915, 5.775152964356418, 0.0),
        (0.5451976340392933, 5.873614262828519, 0.0),
        (0.3710988040888123, 5.945728376171985, 0.0),
        (0.18786230730371928, 5.989719565781847, 0.0),
        (0.0, 6.004504622519563, 0.0),
        (-0.18786236098817405, 5.989719565781847, 0.0),
        (-0.3710988756680853, 5.945728376171985, 0.0),
        (-0.5451977771978394, 5.873614262828519, 0.0),
        (-0.7058719860735376, 5.775152964356418, 0.0),
        (-0.8491653874548866, 5.652768870732717, 0.0),
        (-0.9715494810785876, 5.509475540930642, 0.0),
        (-1.070010851129961, 5.3488013320549435, 0.0),
        (-1.142124964473427, 5.174702466314826, 0.0),
        (-1.1861161540832894, 4.991465880055642, 0.0),
        (-1.2009012108210046, 4.80360369801565, 0.0),
        (-1.1861161540832894, 4.615741515975658, 0.0),
        (-1.142124964473427, 4.432504929716473, 0.0),
        (-1.070010851129961, 4.258406063976356, 0.0),
        (-0.9715494810785876, 4.097731855100658, 0.0),
        (-0.8491653874548866, 3.9544385252985825, 0.0),
        (-0.7058719860735376, 3.8320544316748815, 0.0),
        (-0.5451977771978394, 3.733593133202781, 0.0),
        (-0.3710988756680853, 3.661479019859315, 0.0),
        (-0.18786236098817405, 3.6174878302494524, 0.0),
        (0.0, 3.602702773511737, 0.0),
        (0.0, 3.6174878302494524, -0.18786239677781055),
        (0.0, 3.661479019859315, -0.3710989830369948),
        (0.0, 3.733593133202781, -0.5451978845667489),
        (0.0, 3.8320544316748815, -0.7058722008113566),
        (0.0, 3.9544385252985825, -0.8491656021927054),
        (0.0, 4.097731855100658, -0.9715496958164066),
        (0.0, 4.258406063976356, -1.0700110658677802),
        (0.0, 4.432504929716473, -1.142125250790519),
        (0.0, 4.615741515975658, -1.1861164404003812),
        (0.0, 4.80360369801565, -1.2009014971380967),
        (0.0, 4.991465880055642, -1.1861164404003812),
        (0.0, 5.174702466314826, -1.142125250790519),
        (0.0, 5.3488013320549435, -1.0700110658677802),
        (0.0, 5.509475540930642, -0.9715496958164066),
        (0.0, 5.652768870732717, -0.8491656021927054),
        (0.0, 5.775152964356418, -0.7058722008113566),
        (0.0, 5.873614262828519, -0.5451978845667489),
        (0.0, 5.945728376171985, -0.3710989830369948),
        (0.0, 5.989719565781847, -0.18786239677781055),
        (0.0, 6.004504622519563, 0.0),
        (-5.59873304676173e-09, 5.989719565781847, 0.18786232519853754),
        (-1.1059606197142967e-08, 5.945728376171985, 0.37109883987844877),
        (-1.6248155654647748e-08, 5.873614262828519, 0.5451977056185664),
        (-2.10366202269492e-08, 5.775152964356418, 0.7058719144942645),
        (-2.530709423771702e-08, 5.652768870732717, 0.8491652442963404),
        (-2.8954424451016442e-08, 5.509475540930642, 0.9715494094993145),
        (-3.188879981079308e-08, 5.3488013320549435, 1.0700107079714152),
        (-3.403796786535784e-08, 5.174702466314826, 1.142124821314881),
        (-3.534900748032919e-08, 4.991465880055642, 1.186116010924743),
        (-3.5789636507746947e-08, 4.80360369801565, 1.2009010676624585),
        (-3.534900748032919e-08, 4.615741515975658, 1.186116010924743),
        (-3.403796786535784e-08, 4.432504929716473, 1.142124821314881),
        (-3.188879981079308e-08, 4.258406063976356, 1.0700107079714152),
        (-2.8954424451016442e-08, 4.097731855100658, 0.9715494094993145),
        (-2.530709423771702e-08, 3.9544385252985825, 0.8491652442963404),
        (-2.10366202269492e-08, 3.8320544316748815, 0.7058719144942645),
        (-1.6248155654647748e-08, 3.733593133202781, 0.5451977056185664),
        (-1.1059606197142967e-08, 3.661479019859315, 0.37109883987844877),
        (-5.59873304676173e-09, 3.6174878302494524, 0.18786232519853754),
        (0.0, 3.602702773511737, 0.0),
        (0.18786230730371928, 3.6174878302494524, 0.0),
        (0.3710988040888123, 3.661479019859315, 0.0),
        (0.5451976340392933, 3.733593133202781, 0.0),
        (0.7058718429149915, 3.8320544316748815, 0.0),
        (0.8491651727170676, 3.9544385252985825, 0.0),
        (0.9715492663407685, 4.097731855100658, 0.0),
        (1.0700105648128693, 4.258406063976356, 0.0),
        (1.1421246781563348, 4.432504929716473, 0.0),
        (1.1861158677661972, 4.615741515975658, 0.0),
        (1.2009009245039124, 4.80360369801565, 0.0),
        (1.1421246781563348, 4.80360369801565, 0.3710988040888123),
        (0.9715492663407685, 4.80360369801565, 0.7058719144942645),
        (0.7058718429149915, 4.80360369801565, 0.9715493379200414),
        (0.37109876829917576, 4.80360369801565, 1.142124749735608),
        (-3.5789636507746947e-08, 4.80360369801565, 1.2009010676624585),
        (-0.3710988756680853, 4.80360369801565, 1.142124821314881),
        (-0.7058719860735376, 4.80360369801565, 0.9715494094993145),
        (-0.9715494810785876, 4.80360369801565, 0.7058719860735376),
        (-1.142124964473427, 4.80360369801565, 0.3710988756680853),
        (-1.2009012108210046, 4.80360369801565, 0.0),
        (-1.142124964473427, 4.80360369801565, -0.3710988756680853),
        (-0.9715495526578605, 4.80360369801565, -0.7058720576528106),
        (-0.7058721292320835, 4.80360369801565, -0.9715496242371335),
        (-0.3710989830369948, 4.80360369801565, -1.142125179211246),
        (0.0, 4.80360369801565, -1.2009014971380967),
        (0.3710989830369948, 4.80360369801565, -1.142125250790519),
        (0.7058722723906297, 4.80360369801565, -0.9715498389749526),
        (0.9715499105542255, 4.80360369801565, -0.7058722723906297),
        (1.142125393949065, 4.80360369801565, -0.3710990188266313),
        (1.2009009245039124, 4.80360369801565, 0.0)]
        }

def CreateCurve(name='curve', shape=None, color=(0,1,0), translate=(0,0,0), tOffset=(0,0,0), tLock=False, rotate=(0,0,0), rLock=False, scale=(1,1,1), sLock=True, thickness=2, freeze=True, **args):
    
    # Create the curve
    if shape == None:
        crv = cmds.circle(n=name)[0]
    else:
        crv = cmds.curve(d=1, p=Shapes[shape], n=name)

        
    print((rotate[0]), (rotate[1]), (rotate[2]))
    
    # Position the curve correctly
    # if debug: print("translate: " + str(translate))
    cmds.move(translate[0] + tOffset[0], translate[1] + tOffset[1], translate[2] + tOffset[2], crv)
    cmds.rotate((rotate[0]), (rotate[1]), (rotate[2]), crv)
    cmds.scale(scale[0], scale[1], scale[2], crv)
    
    # Set the color of the curve
    cmds.setAttr(crv + '.overrideEnabled', 1)
    cmds.setAttr(crv + '.overrideRGBColors', 1)
    cmds.setAttr(crv + '.overrideColorRGB', color[0], color[1], color[2])
    
    # Put the pivot back to the joint
    
    if tOffset != (0,0,0):
        cmds.setAttr(crv + '.rotatePivotX', tOffset[0] * -1)
        cmds.setAttr(crv + '.rotatePivotY', tOffset[1] * -1)
        cmds.setAttr(crv + '.rotatePivotZ', tOffset[2] * -1)
    
    # Set the thickness of the curve
    cmds.setAttr(crv + '.lineWidth', thickness)
    
    # freeze the transforms
    if freeze:
        cmds.makeIdentity(crv, apply=True, t=1, r=1, s=1, n=0)
    
    # Lock the transforms
    if tLock:
        cmds.setAttr(crv + '.translate', lock=True)
    if rLock:
        cmds.setAttr(crv + '.rotate', lock=True)
    if sLock:   
        cmds.setAttr(crv + '.scale', lock=True)
    
    return crv

def CreateControl2(joint=None, name='curve', shape=None, color=(0,1,0), translate=None, tOffset=(0,0,0), tLock=False, rotate=(0,0,0), rLock=False, scale=(1,1,1), parent='Origin', thickness=2, freeze=True, **args):
    
    # if debug: print("translate not given, setting translate to joint position")
    if translate == None: 
        # Get world coordinates for the joint
        translate = cmds.xform(joint, q=True, ws=True, t=True)
        if debug: print("position of " + joint + " is " + str(translate))
    
    Curve = CreateCurve(name=name, shape=shape, color=color, translate=translate, tOffset=tOffset, tLock=tLock, rotate=rotate, rLock=rLock, scale=scale, parent=parent, thickness=2, freeze=True, **args)
    
    cmds.parentConstraint(Curve, joint, mo=True)
    
    if parent != 'skip':
        if cmds.objExists(parent):
            # Parent the curve to the parent control
            cmds.parent(Curve, parent, absolute=True)
        else:
            cmds.parent(Curve, Controls[-1], absolute=True)
    
    # print("Constrained " + Curve + " to " + joint)
    
    return Curve

def CreateIkFkJoints(name, joint, effector, solver, group='Joints'):
    
    IKJoints = []
    IKConstraints = []
    FKJoints = []
    FKConstraints = []
    
    # Create the IK joints
    
    IKMaster = cmds.duplicate(joint, n=name + '_IK_FK_Master', po=True)[0]
    for j in [joint, solver, effector]:
        
        # Note: Constarins may not work if they are a parent, not orient, constraint
        # Note: When making the IK handle, make the .stickiness 1
        
        IKJoint = cmds.duplicate(j, n=j + '_IK', po=True)[0]
        cmds.setAttr(IKJoint + '.visibility', 0)
        try:
            cmds.parent(IKJoint, IKJoints[-1], absolute=True)
        except IndexError:
            cmds.parent(IKJoint, 'Origin', absolute=True)
            cmds.parentConstraint(IKMaster, IKJoint)
            
        IKConstraints.append(cmds.parentConstraint(IKJoint, j, mo=True)[0])
        IKJoints.append(IKJoint)
        
        FKJoint = cmds.duplicate(j, n=j + '_FK', po=True)[0]
        cmds.setAttr(FKJoint + '.visibility', 0)
        try:
            cmds.parent(FKJoint, FKJoints[-1], absolute=True)
        except IndexError:
            cmds.parent(FKJoint, 'Origin', absolute=True)
        
        FKConstraints.append(cmds.parentConstraint(FKJoint, j, mo=True)[0])
        
        FKJoints.append(FKJoint)
    
    FKGroup = cmds.group(FKJoints[0], n=name + '_FK_Master', a=True)
     
    cmds.parent(IKJoints[0], group, absolute=True)
    cmds.parent(FKGroup, group, absolute=True)

    return IKJoints, IKConstraints, FKJoints
    
def CreateIkHandle(joint, effector, solver, name:str, rotate=(0,0,0), tOffset=(0,0,0), scale=(1,1,1), color=(0,1,0), thickness=6):
    
    solverLoc = cmds.xform(solver, q=True, ws=True, t=True)
    
    if name == 'Left_Arm' or name == 'Right_Arm':
        PVtOffset = (-15,0,0)
    elif name == 'Left_Leg' or name == 'Right_Leg':
        PVtOffset = (25,0,0)
    else:
        PVtOffset = (0,0,0)

    solverLoc = (solverLoc[0] + PVtOffset[0], solverLoc[1] + PVtOffset[1], solverLoc[2] + PVtOffset[2])
    
    # Create the pole vector
    pv = CreateCurve(name=name + '_PV', shape='Sphere', color=(color[0], color[1] + 0.3, color[2]), translate=solverLoc, tOffset=PVtOffset, parent='Origin', thickness=1)
    
    # Create the ik handle
    ik = cmds.ikHandle(sj=joint, ee=effector, n=name + '_IKHandle')[0]
    
    # Create the pole vector constraint
    cmds.poleVectorConstraint(pv, ik)

    # Create a curve for the ik
    ikControl = CreateCurve(name=name + '_IK', color=color, translate=(cmds.xform(ik, q=True, ws=True, t=True)), tOffset=tOffset, scale=scale, rotate=rotate, thickness=thickness)
    
    # Parent the ik handle to the control
    cmds.parent(ik, ikControl, absolute=True)
    
    # Parent the pole vector to the origin
    cmds.parent(pv, 'Origin', absolute=True)
    
    # Parent the curve to the origin
    cmds.parent(ikControl, 'Origin', absolute=True)
    
    # Constrain the rotations to the ik
    cmds.orientConstraint(ikControl, effector, mo=True)


def CreateFingerControls(fingerName, finger):
    
        fControls = ['Spine_4']
        
        # Loop through each part of the finger
        for i in range(1,4):
            
            # Check if the game uses IW finger joints
            if cmds.objExists((finger['joint']).replace('j_', 'j_meta') + '_1'):
                if debug: print("MW finger found")
                rOffset = (180,0,0)
            
            # Use Treyarch finger joints
            else:
                if debug: print((finger['joint']).replace('j_', 'j_meta') + '_1' + " finger not found")
                
                # Check what hand it is
                if finger['joint'].endswith('_ri'): # Right hand
                    if debug: print("RI finger found")
                    rOffset = (0,0,0)
                else: # Left hand
                    if debug: print(finger['joint'] + " finger not found")
                    rOffset = (180,0,0)
                    
            # Get the rotation of the joint
            rotation = cmds.xform(finger['joint'] + '_' + str(i), q=True, ws=True, ro=True)
            rotation = (rotation[0] + rOffset[0], rotation[1] + rOffset[1], rotation[2] + rOffset[2])
            
            # Create the control
            control = CreateControl2(joint=(finger['joint'] + '_' + str(i)), name=fingerName + '_' + str(i), shape='Sphere Pin', color=finger['color'],
                                     tlock=False, rotate=rotation, rLock=False, scale=(0.6,0.6,0.6), parent=fControls[-1], thickness=2)
            
            fControls.append(control)

        return fControls[1]
        
        










if __name__ == "__main__":
    # Create the origin curve
    CreateControl2('tag_origin', name='Origin', shape='Arrow', rotate=(90,0,0), scale=(20,20,20), parent='Joints')

    ## Create the IK joints
    
    # Create a group for the IK/FK joints
    IK_FK_Group = cmds.group(n='IK_FK_Joints', em=True)
    IK_FK_Group = cmds.parent(IK_FK_Group, 'Origin', absolute=True)
    
    # Loop for each IK
    for kinematic in IKs:
        # Create the IK/FK switch
        switchLoc = (0,0,0)
        jointLoc = cmds.xform(IKs[kinematic]['joint'], q=True, ws=True, t=True)
        effectorLoc = cmds.xform(IKs[kinematic]['effector'], q=True, ws=True, t=True)
        
        if kinematic == 'Left_Arm' or kinematic == 'Right_Arm':
            switchLoc = (0, (jointLoc[1] + effectorLoc[1]) / 1.5, jointLoc[2])
        elif kinematic == 'Left_Leg' or kinematic == 'Right_Leg':
            switchLoc = (0, (jointLoc[1] * 3), jointLoc[2])
        
        # Create the IK/FK switch
        switch = CreateCurve(name='IK_FK_Switch', shape='Gear', color=IKs[kinematic]['color'], translate=switchLoc, tLock=False, rotate=(0,0,90), rLock=False, scale=(2,2,2), parent='Origin', thickness=2, freeze=False)
        
        # Create the IK/FK switch attribute
        cmds.addAttr(switch, ln='IK_FK_Switch', min=0, max=1, dv=0, k=True, at="float")
        
        # Create the reverse node for the FK
        inverse = cmds.createNode('reverse', n=IKs[kinematic]['name'] + '_Inverse')
        
        # Connect the IK/FK switch to the reverse node
        cmds.connectAttr(switch + '.IK_FK_Switch', inverse + '.inputX')
        
        IK_Joints, IK_Constraints, FK_Joints = CreateIkFkJoints(str(kinematic), IKs[kinematic]['joint'], IKs[kinematic]['effector'], IKs[kinematic]['solver'], group=IK_FK_Group)
        
        for i,constraint in enumerate(IK_Constraints):
            # Connect the IK/FK switch (inverted) to the IK constraints
            cmds.connectAttr(inverse + '.outputX', constraint + '.' + IK_Joints[i] + 'W0')
            
            # Connect the IK/FK switch to the FK constraints
            cmds.connectAttr(switch + '.IK_FK_Switch', constraint + '.' + FK_Joints[i] + 'W1')
            
        # Parent the IK/FK switch to the origin
        cmds.parent(switch, 'Origin', absolute=True)
        
        # Create the IK handle
        CreateIkHandle(IK_Joints[0], IK_Joints[2], IKs[kinematic]['solver'], kinematic, IKs[kinematic]['rotate'], tOffset=IKs[kinematic]['tOffset'], scale=IKs[kinematic]['scale'], color=IKs[kinematic]['color'])


    
    # Create the FK controls
    for i,fk in enumerate(FKs):
        if cmds.objExists(FKs[fk]['joint']):
            CreateControl2(joint=FKs[fk]['joint'], name=fk, shape='Sphere Pin', color=FKs[fk]['color'], tOffset=FKs[fk]['tOffset'], tlock=False, rotate=FKs[fk]['rotate'], rLock=False, scale=(1.5,1.5,1.5), parent=FKs[fk]['parent'], thickness=2)



    ## Create the finger controls
    
    # Loop for each finger
    for i,finger in enumerate(Fingers):
        
        # Create the finger controls for each part of the finger
        fControl = CreateFingerControls(finger, Fingers[finger])
        
        # Creete a group for the finger controls
        fGroup = cmds.group(fControl, n=finger + '_Controls', a=True)
        
        # Parent the finger controls to the wrist
        cmds.parentConstraint([Fingers[finger]['parent']], fGroup, mo=True)
        

    splineJoints= ['j_mainroot', 'j_spinelower', 'j_spineupper', 'j_spine4']
    splineLocs = []
    
    for joint in splineJoints:
        splineLocs.append(cmds.xform(joint, q=True, ws=True, t=True))
     
    
    # splineLocPos2 = [ (splineLocs[0][0] + ((splineLocs[1][0] - splineLocs[0][0]) // 4)),  (splineLocs[0][1] + ((splineLocs[1][1] - splineLocs[0][1]) // 4)),     (splineLocs[0][2] + ((splineLocs[1][2] - splineLocs[0][2]) // 4)) ]
    # splineLocPos6 = [  (splineLocs[3][0] + ((splineLocs[3][0] - splineLocs[2][0]) // 4)), (splineLocs[3][1] + ((splineLocs[2][1] - splineLocs[2][1]) // 4)),     (splineLocs[3][2] + ((splineLocs[3][2] - splineLocs[2][2]) // 4)) ]
    # print("point2: ", splineLocPos2, type(splineLocPos2))
    # splineLocs.insert(1, splineLocPos2)
    # splineLocs.insert(4, splineLocPos6)
    Spline = cmds.curve(d=3, p=splineLocs, n='Spine')

    # Lock the curves transforms
    cmds.setAttr(Spline + '.translate', lock=True)
    cmds.setAttr(Spline + '.rotate', lock=True)
    cmds.setAttr(Spline + '.scale', lock=True)
    
    # Hide the curve
    cmds.setAttr(Spline + '.visibility', 0)
    cmds.setAttr(Spline + '.hiddenInOutliner', 1)
    
    print(splineLocs)   
    print("Spline: " + Spline)
    
    Clusters = ['Origin']
    Controls = ['Origin']
    
    vertexes = cmds.ls(Spline + '.cv[*]', fl=True)

    # Create a cluster for each vertex
    for i,vertex in enumerate(vertexes):
        clusterHandle = (cmds.cluster(vertexes[i], n=splineJoints[i] + '_Cluster')[1])

        print(clusterHandle)
        cmds.makeIdentity(clusterHandle, apply=True, t=1, r=1, s=1, n=0)
        # cmds.parent(clusterHandle, Clusters[-1])
        Clusters.append(clusterHandle)
        
        
    # Create the controls for the spline
    for joint in splineJoints:  
        control = CreateControl2(joint + '_ClusterHandle', name=SpineJoints[joint]['name'], color=SpineJoints[joint]['color'], tOffset=SpineJoints[joint]['tOffset'], 
                            rotate=SpineJoints[joint]['rotate'], scale=SpineJoints[joint]['scale'], translate=(cmds.xform(joint, q=True, ws=True, t=True)), parent='skip', thickness=SpineJoints[joint]['thickness'])
        # if Controls[-1] != 'Origin':
        cmds.parent(control, Controls[-1])
        
        Controls.append(control)
    
    # Create the IK Spline Handle
    cmds.ikHandle(sj=splineJoints[0], ee=splineJoints[-1], sol='ikSplineSolver', n='Spine_IKHandle', ccv=False, c=Spline)
    
    # Parent the IK Spline Handle to the origin
    cmds.parent('Spine_IKHandle', 'Origin', absolute=True)
    
    # unparent the curve to the origin
    cmds.parent(Spline, world=True)
    
    for i,cluster in enumerate(Clusters):
        if i != 0:
            cmds.parent(cluster, Controls[i], absolute=True)
            
    ## Create the rest of the curves
    for i,joint in enumerate(Joints):
        if cmds.objExists(joint):
            CreateControl2(joint, name=Joints[joint]['name'], color=Joints[joint]['color'], tOffset=Joints[joint]['tOffset'], sLock=True, 
                        rotate=Joints[joint]['rotate'], scale=Joints[joint]['scale'], parent=Joints[joint]['parent'], thickness=Joints[joint]['thickness'])
        else:
            print(joint + ' does not exist')
