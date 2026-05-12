(define (problem sokoban-level)
  (:domain sokoban)
(:objects
     pos0_0
 pos0_1
 pos0_2
 pos0_3
 pos0_4
 pos0_5
 pos0_6
 pos0_7
 pos1_0
 pos1_1
 pos1_2
 pos1_3
 pos1_4
 pos1_5
 pos1_6
 pos1_7
 pos2_0
 pos2_1
 pos2_2
 pos2_3
 pos2_4
 pos2_5
 pos2_6
 pos2_7
 pos3_0
 pos3_1
 pos3_2
 pos3_3
 pos3_4
 pos3_5
 pos3_7
 pos4_0
 pos4_1
 pos4_2
 pos4_3
 pos4_4
 pos4_5
 pos4_6
 pos4_7
 pos5_0
 pos5_1
 pos5_2
 pos5_3
 pos5_4
 pos5_5
 pos5_6
 pos5_7
 pos6_0
 pos6_1
 pos6_2
 pos6_3
 pos6_4
 pos6_5
 pos6_6
 pos6_7
 pos7_0
 pos7_1
 pos7_2
 pos7_3
 pos7_4
 pos7_5
 pos7_6
 pos7_7
 - position
     player_1
 - player
     box_1
 box_2
 - box)
(:init
    (inline pos0_0 pos0_1 pos0_2
)(inline pos0_2 pos0_1 pos0_0
)(inline pos0_1 pos0_2 pos0_3
)(inline pos0_3 pos0_2 pos0_1
)(inline pos0_2 pos0_3 pos0_4
)(inline pos0_4 pos0_3 pos0_2
)(inline pos0_3 pos0_4 pos0_5
)(inline pos0_5 pos0_4 pos0_3
)(inline pos0_4 pos0_5 pos0_6
)(inline pos0_6 pos0_5 pos0_4
)(inline pos0_5 pos0_6 pos0_7
)(inline pos0_7 pos0_6 pos0_5
)(inline pos0_0 pos1_0 pos2_0
)(inline pos2_0 pos1_0 pos0_0
)(inline pos0_1 pos1_1 pos2_1
)(inline pos2_1 pos1_1 pos0_1
)(inline pos1_0 pos1_1 pos1_2
)(inline pos1_2 pos1_1 pos1_0
)(inline pos0_2 pos1_2 pos2_2
)(inline pos2_2 pos1_2 pos0_2
)(inline pos1_1 pos1_2 pos1_3
)(inline pos1_3 pos1_2 pos1_1
)(inline pos0_3 pos1_3 pos2_3
)(inline pos2_3 pos1_3 pos0_3
)(inline pos1_2 pos1_3 pos1_4
)(inline pos1_4 pos1_3 pos1_2
)(inline pos0_4 pos1_4 pos2_4
)(inline pos2_4 pos1_4 pos0_4
)(inline pos1_3 pos1_4 pos1_5
)(inline pos1_5 pos1_4 pos1_3
)(inline pos0_5 pos1_5 pos2_5
)(inline pos2_5 pos1_5 pos0_5
)(inline pos1_4 pos1_5 pos1_6
)(inline pos1_6 pos1_5 pos1_4
)(inline pos0_6 pos1_6 pos2_6
)(inline pos2_6 pos1_6 pos0_6
)(inline pos1_5 pos1_6 pos1_7
)(inline pos1_7 pos1_6 pos1_5
)(inline pos0_7 pos1_7 pos2_7
)(inline pos2_7 pos1_7 pos0_7
)(inline pos1_0 pos2_0 pos3_0
)(inline pos3_0 pos2_0 pos1_0
)(inline pos1_1 pos2_1 pos3_1
)(inline pos3_1 pos2_1 pos1_1
)(inline pos2_0 pos2_1 pos2_2
)(inline pos2_2 pos2_1 pos2_0
)(inline pos1_2 pos2_2 pos3_2
)(inline pos3_2 pos2_2 pos1_2
)(inline pos2_1 pos2_2 pos2_3
)(inline pos2_3 pos2_2 pos2_1
)(inline pos1_3 pos2_3 pos3_3
)(inline pos3_3 pos2_3 pos1_3
)(inline pos2_2 pos2_3 pos2_4
)(inline pos2_4 pos2_3 pos2_2
)(inline pos1_4 pos2_4 pos3_4
)(inline pos3_4 pos2_4 pos1_4
)(inline pos2_3 pos2_4 pos2_5
)(inline pos2_5 pos2_4 pos2_3
)(inline pos1_5 pos2_5 pos3_5
)(inline pos3_5 pos2_5 pos1_5
)(inline pos2_4 pos2_5 pos2_6
)(inline pos2_6 pos2_5 pos2_4
)(inline pos2_5 pos2_6 pos2_7
)(inline pos2_7 pos2_6 pos2_5
)(inline pos1_7 pos2_7 pos3_7
)(inline pos3_7 pos2_7 pos1_7
)(inline pos2_0 pos3_0 pos4_0
)(inline pos4_0 pos3_0 pos2_0
)(inline pos2_1 pos3_1 pos4_1
)(inline pos4_1 pos3_1 pos2_1
)(inline pos3_0 pos3_1 pos3_2
)(inline pos3_2 pos3_1 pos3_0
)(inline pos2_2 pos3_2 pos4_2
)(inline pos4_2 pos3_2 pos2_2
)(inline pos3_1 pos3_2 pos3_3
)(inline pos3_3 pos3_2 pos3_1
)(inline pos2_3 pos3_3 pos4_3
)(inline pos4_3 pos3_3 pos2_3
)(inline pos3_2 pos3_3 pos3_4
)(inline pos3_4 pos3_3 pos3_2
)(inline pos2_4 pos3_4 pos4_4
)(inline pos4_4 pos3_4 pos2_4
)(inline pos3_3 pos3_4 pos3_5
)(inline pos3_5 pos3_4 pos3_3
)(inline pos2_5 pos3_5 pos4_5
)(inline pos4_5 pos3_5 pos2_5
)(inline pos2_7 pos3_7 pos4_7
)(inline pos4_7 pos3_7 pos2_7
)(inline pos3_0 pos4_0 pos5_0
)(inline pos5_0 pos4_0 pos3_0
)(inline pos3_1 pos4_1 pos5_1
)(inline pos5_1 pos4_1 pos3_1
)(inline pos4_0 pos4_1 pos4_2
)(inline pos4_2 pos4_1 pos4_0
)(inline pos3_2 pos4_2 pos5_2
)(inline pos5_2 pos4_2 pos3_2
)(inline pos4_1 pos4_2 pos4_3
)(inline pos4_3 pos4_2 pos4_1
)(inline pos3_3 pos4_3 pos5_3
)(inline pos5_3 pos4_3 pos3_3
)(inline pos4_2 pos4_3 pos4_4
)(inline pos4_4 pos4_3 pos4_2
)(inline pos3_4 pos4_4 pos5_4
)(inline pos5_4 pos4_4 pos3_4
)(inline pos4_3 pos4_4 pos4_5
)(inline pos4_5 pos4_4 pos4_3
)(inline pos3_5 pos4_5 pos5_5
)(inline pos5_5 pos4_5 pos3_5
)(inline pos4_4 pos4_5 pos4_6
)(inline pos4_6 pos4_5 pos4_4
)(inline pos4_5 pos4_6 pos4_7
)(inline pos4_7 pos4_6 pos4_5
)(inline pos3_7 pos4_7 pos5_7
)(inline pos5_7 pos4_7 pos3_7
)(inline pos4_0 pos5_0 pos6_0
)(inline pos6_0 pos5_0 pos4_0
)(inline pos4_1 pos5_1 pos6_1
)(inline pos6_1 pos5_1 pos4_1
)(inline pos5_0 pos5_1 pos5_2
)(inline pos5_2 pos5_1 pos5_0
)(inline pos4_2 pos5_2 pos6_2
)(inline pos6_2 pos5_2 pos4_2
)(inline pos5_1 pos5_2 pos5_3
)(inline pos5_3 pos5_2 pos5_1
)(inline pos4_3 pos5_3 pos6_3
)(inline pos6_3 pos5_3 pos4_3
)(inline pos5_2 pos5_3 pos5_4
)(inline pos5_4 pos5_3 pos5_2
)(inline pos4_4 pos5_4 pos6_4
)(inline pos6_4 pos5_4 pos4_4
)(inline pos5_3 pos5_4 pos5_5
)(inline pos5_5 pos5_4 pos5_3
)(inline pos4_5 pos5_5 pos6_5
)(inline pos6_5 pos5_5 pos4_5
)(inline pos5_4 pos5_5 pos5_6
)(inline pos5_6 pos5_5 pos5_4
)(inline pos4_6 pos5_6 pos6_6
)(inline pos6_6 pos5_6 pos4_6
)(inline pos5_5 pos5_6 pos5_7
)(inline pos5_7 pos5_6 pos5_5
)(inline pos4_7 pos5_7 pos6_7
)(inline pos6_7 pos5_7 pos4_7
)(inline pos5_0 pos6_0 pos7_0
)(inline pos7_0 pos6_0 pos5_0
)(inline pos5_1 pos6_1 pos7_1
)(inline pos7_1 pos6_1 pos5_1
)(inline pos6_0 pos6_1 pos6_2
)(inline pos6_2 pos6_1 pos6_0
)(inline pos5_2 pos6_2 pos7_2
)(inline pos7_2 pos6_2 pos5_2
)(inline pos6_1 pos6_2 pos6_3
)(inline pos6_3 pos6_2 pos6_1
)(inline pos5_3 pos6_3 pos7_3
)(inline pos7_3 pos6_3 pos5_3
)(inline pos6_2 pos6_3 pos6_4
)(inline pos6_4 pos6_3 pos6_2
)(inline pos5_4 pos6_4 pos7_4
)(inline pos7_4 pos6_4 pos5_4
)(inline pos6_3 pos6_4 pos6_5
)(inline pos6_5 pos6_4 pos6_3
)(inline pos5_5 pos6_5 pos7_5
)(inline pos7_5 pos6_5 pos5_5
)(inline pos6_4 pos6_5 pos6_6
)(inline pos6_6 pos6_5 pos6_4
)(inline pos5_6 pos6_6 pos7_6
)(inline pos7_6 pos6_6 pos5_6
)(inline pos6_5 pos6_6 pos6_7
)(inline pos6_7 pos6_6 pos6_5
)(inline pos5_7 pos6_7 pos7_7
)(inline pos7_7 pos6_7 pos5_7
)(inline pos7_0 pos7_1 pos7_2
)(inline pos7_2 pos7_1 pos7_0
)(inline pos7_1 pos7_2 pos7_3
)(inline pos7_3 pos7_2 pos7_1
)(inline pos7_2 pos7_3 pos7_4
)(inline pos7_4 pos7_3 pos7_2
)(inline pos7_3 pos7_4 pos7_5
)(inline pos7_5 pos7_4 pos7_3
)(inline pos7_4 pos7_5 pos7_6
)(inline pos7_6 pos7_5 pos7_4
)(inline pos7_5 pos7_6 pos7_7
)(inline pos7_7 pos7_6 pos7_5
)(connected pos0_0 pos0_1)
(connected pos0_0 pos1_0)
(connected pos0_1 pos0_2)
(connected pos0_1 pos1_1)
(connected pos0_1 pos0_0)
(connected pos0_2 pos0_3)
(connected pos0_2 pos1_2)
(connected pos0_2 pos0_1)
(connected pos0_3 pos0_4)
(connected pos0_3 pos1_3)
(connected pos0_3 pos0_2)
(connected pos0_4 pos0_5)
(connected pos0_4 pos1_4)
(connected pos0_4 pos0_3)
(connected pos0_5 pos0_6)
(connected pos0_5 pos1_5)
(connected pos0_5 pos0_4)
(connected pos0_6 pos0_7)
(connected pos0_6 pos1_6)
(connected pos0_6 pos0_5)
(connected pos0_7 pos1_7)
(connected pos0_7 pos0_6)
(connected pos1_0 pos1_1)
(connected pos1_0 pos2_0)
(connected pos1_0 pos0_0)
(connected pos1_1 pos1_2)
(connected pos1_1 pos2_1)
(connected pos1_1 pos0_1)
(connected pos1_1 pos1_0)
(connected pos1_2 pos1_3)
(connected pos1_2 pos2_2)
(connected pos1_2 pos0_2)
(connected pos1_2 pos1_1)
(connected pos1_3 pos1_4)
(connected pos1_3 pos2_3)
(connected pos1_3 pos0_3)
(connected pos1_3 pos1_2)
(connected pos1_4 pos1_5)
(connected pos1_4 pos2_4)
(connected pos1_4 pos0_4)
(connected pos1_4 pos1_3)
(connected pos1_5 pos1_6)
(connected pos1_5 pos2_5)
(connected pos1_5 pos0_5)
(connected pos1_5 pos1_4)
(connected pos1_6 pos1_7)
(connected pos1_6 pos2_6)
(connected pos1_6 pos0_6)
(connected pos1_6 pos1_5)
(connected pos1_7 pos2_7)
(connected pos1_7 pos0_7)
(connected pos1_7 pos1_6)
(connected pos2_0 pos2_1)
(connected pos2_0 pos3_0)
(connected pos2_0 pos1_0)
(connected pos2_1 pos2_2)
(connected pos2_1 pos3_1)
(connected pos2_1 pos1_1)
(connected pos2_1 pos2_0)
(connected pos2_2 pos2_3)
(connected pos2_2 pos3_2)
(connected pos2_2 pos1_2)
(connected pos2_2 pos2_1)
(connected pos2_3 pos2_4)
(connected pos2_3 pos3_3)
(connected pos2_3 pos1_3)
(connected pos2_3 pos2_2)
(connected pos2_4 pos2_5)
(connected pos2_4 pos3_4)
(connected pos2_4 pos1_4)
(connected pos2_4 pos2_3)
(connected pos2_5 pos2_6)
(connected pos2_5 pos3_5)
(connected pos2_5 pos1_5)
(connected pos2_5 pos2_4)
(connected pos2_6 pos2_7)
(connected pos2_6 pos1_6)
(connected pos2_6 pos2_5)
(connected pos2_7 pos3_7)
(connected pos2_7 pos1_7)
(connected pos2_7 pos2_6)
(connected pos3_0 pos3_1)
(connected pos3_0 pos4_0)
(connected pos3_0 pos2_0)
(connected pos3_1 pos3_2)
(connected pos3_1 pos4_1)
(connected pos3_1 pos2_1)
(connected pos3_1 pos3_0)
(connected pos3_2 pos3_3)
(connected pos3_2 pos4_2)
(connected pos3_2 pos2_2)
(connected pos3_2 pos3_1)
(connected pos3_3 pos3_4)
(connected pos3_3 pos4_3)
(connected pos3_3 pos2_3)
(connected pos3_3 pos3_2)
(connected pos3_4 pos3_5)
(connected pos3_4 pos4_4)
(connected pos3_4 pos2_4)
(connected pos3_4 pos3_3)
(connected pos3_5 pos4_5)
(connected pos3_5 pos2_5)
(connected pos3_5 pos3_4)
(connected pos3_7 pos4_7)
(connected pos3_7 pos2_7)
(connected pos4_0 pos4_1)
(connected pos4_0 pos5_0)
(connected pos4_0 pos3_0)
(connected pos4_1 pos4_2)
(connected pos4_1 pos5_1)
(connected pos4_1 pos3_1)
(connected pos4_1 pos4_0)
(connected pos4_2 pos4_3)
(connected pos4_2 pos5_2)
(connected pos4_2 pos3_2)
(connected pos4_2 pos4_1)
(connected pos4_3 pos4_4)
(connected pos4_3 pos5_3)
(connected pos4_3 pos3_3)
(connected pos4_3 pos4_2)
(connected pos4_4 pos4_5)
(connected pos4_4 pos5_4)
(connected pos4_4 pos3_4)
(connected pos4_4 pos4_3)
(connected pos4_5 pos4_6)
(connected pos4_5 pos5_5)
(connected pos4_5 pos3_5)
(connected pos4_5 pos4_4)
(connected pos4_6 pos4_7)
(connected pos4_6 pos5_6)
(connected pos4_6 pos4_5)
(connected pos4_7 pos5_7)
(connected pos4_7 pos3_7)
(connected pos4_7 pos4_6)
(connected pos5_0 pos5_1)
(connected pos5_0 pos6_0)
(connected pos5_0 pos4_0)
(connected pos5_1 pos5_2)
(connected pos5_1 pos6_1)
(connected pos5_1 pos4_1)
(connected pos5_1 pos5_0)
(connected pos5_2 pos5_3)
(connected pos5_2 pos6_2)
(connected pos5_2 pos4_2)
(connected pos5_2 pos5_1)
(connected pos5_3 pos5_4)
(connected pos5_3 pos6_3)
(connected pos5_3 pos4_3)
(connected pos5_3 pos5_2)
(connected pos5_4 pos5_5)
(connected pos5_4 pos6_4)
(connected pos5_4 pos4_4)
(connected pos5_4 pos5_3)
(connected pos5_5 pos5_6)
(connected pos5_5 pos6_5)
(connected pos5_5 pos4_5)
(connected pos5_5 pos5_4)
(connected pos5_6 pos5_7)
(connected pos5_6 pos6_6)
(connected pos5_6 pos4_6)
(connected pos5_6 pos5_5)
(connected pos5_7 pos6_7)
(connected pos5_7 pos4_7)
(connected pos5_7 pos5_6)
(connected pos6_0 pos6_1)
(connected pos6_0 pos7_0)
(connected pos6_0 pos5_0)
(connected pos6_1 pos6_2)
(connected pos6_1 pos7_1)
(connected pos6_1 pos5_1)
(connected pos6_1 pos6_0)
(connected pos6_2 pos6_3)
(connected pos6_2 pos7_2)
(connected pos6_2 pos5_2)
(connected pos6_2 pos6_1)
(connected pos6_3 pos6_4)
(connected pos6_3 pos7_3)
(connected pos6_3 pos5_3)
(connected pos6_3 pos6_2)
(connected pos6_4 pos6_5)
(connected pos6_4 pos7_4)
(connected pos6_4 pos5_4)
(connected pos6_4 pos6_3)
(connected pos6_5 pos6_6)
(connected pos6_5 pos7_5)
(connected pos6_5 pos5_5)
(connected pos6_5 pos6_4)
(connected pos6_6 pos6_7)
(connected pos6_6 pos7_6)
(connected pos6_6 pos5_6)
(connected pos6_6 pos6_5)
(connected pos6_7 pos7_7)
(connected pos6_7 pos5_7)
(connected pos6_7 pos6_6)
(connected pos7_0 pos7_1)
(connected pos7_0 pos6_0)
(connected pos7_1 pos7_2)
(connected pos7_1 pos6_1)
(connected pos7_1 pos7_0)
(connected pos7_2 pos7_3)
(connected pos7_2 pos6_2)
(connected pos7_2 pos7_1)
(connected pos7_3 pos7_4)
(connected pos7_3 pos6_3)
(connected pos7_3 pos7_2)
(connected pos7_4 pos7_5)
(connected pos7_4 pos6_4)
(connected pos7_4 pos7_3)
(connected pos7_5 pos7_6)
(connected pos7_5 pos6_5)
(connected pos7_5 pos7_4)
(connected pos7_6 pos7_7)
(connected pos7_6 pos6_6)
(connected pos7_6 pos7_5)
(connected pos7_7 pos6_7)
(connected pos7_7 pos7_6)
(clear pos0_0)
(clear pos0_1)
(clear pos0_2)
(clear pos0_3)
(clear pos0_4)
(clear pos0_5)
(clear pos0_6)
(clear pos0_7)
(clear pos1_0)
(clear pos1_1)
(clear pos1_2)
(clear pos1_3)
(clear pos1_4)
(clear pos1_5)
(clear pos1_6)
(clear pos1_7)
(clear pos2_0)
(clear pos2_1)
(clear pos2_2)
(clear pos2_3)
(clear pos2_4)
(clear pos2_5)
(clear pos2_6)
(clear pos2_7)
(clear pos3_0)
(clear pos3_1)
(clear pos3_3)
(clear pos3_4)
(clear pos3_5)
(clear pos3_7)
(clear pos4_0)
(clear pos4_1)
(clear pos4_3)
(clear pos4_4)
(clear pos4_5)
(clear pos4_6)
(clear pos4_7)
(clear pos5_0)
(clear pos5_1)
(clear pos5_2)
(clear pos5_3)
(clear pos5_4)
(clear pos5_5)
(clear pos5_6)
(clear pos5_7)
(clear pos6_0)
(clear pos6_1)
(clear pos6_2)
(clear pos6_3)
(clear pos6_5)
(clear pos6_6)
(clear pos6_7)
(clear pos7_0)
(clear pos7_1)
(clear pos7_2)
(clear pos7_3)
(clear pos7_4)
(clear pos7_5)
(clear pos7_6)
(clear pos7_7)
(at box_1 pos3_2)
(at box_2 pos4_2)
(at player_1 pos6_4)
)
(:goal (and
    (or (at box_1 pos4_5)
 (at box_1 pos5_5)
 )(or (at box_2 pos4_5)
 (at box_2 pos5_5)
 )))
)