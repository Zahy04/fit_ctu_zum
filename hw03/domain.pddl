(define (domain sokoban)
  (:requirements :typing :disjunctive-preconditions)
  (:types position player box)
  
  (:predicates
    (at ?obj - object ?loc - position)
    (clear ?loc - position)
    (connected ?from ?to - position)
    (inline ?loc1 ?loc2 ?loc3 - position) 
  )

  (:action move
    :parameters (?p - player ?from ?to - position)
    :precondition (and
      (at ?p ?from)
      (connected ?from ?to)
      (clear ?to)
    )
    :effect (and
      (not (at ?p ?from))
      (at ?p ?to)
      (clear ?from)
      (not (clear ?to))
    )
  )

  (:action push
    :parameters (?p - player ?b - box ?player_loc ?box_loc ?dest_loc - position)
    :precondition (and
      (at ?p ?player_loc)
      (at ?b ?box_loc)
      (connected ?player_loc ?box_loc)
      (connected ?box_loc ?dest_loc)
      (clear ?dest_loc)
      (inline ?player_loc ?box_loc ?dest_loc) 
    )
    :effect (and
      (not (at ?p ?player_loc))
      (at ?p ?box_loc)
      (not (at ?b ?box_loc))
      (at ?b ?dest_loc)
      (clear ?player_loc)
      (not (clear ?dest_loc))
    )
  )
)