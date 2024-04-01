from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 15
))
missile25 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 25
))
missile40 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 40
))
missile60 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 60
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 3 >= 6
))
super12 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 3 >= 12
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 3 >= 30
))
powerBomb6 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb9 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb12 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Missile in loadout) or
        (Super in loadout)
        )
))
purpleDoor = LogicShortcut(lambda loadout: (
    (super6 in loadout) or
    (missile25 in loadout) or
    (
        (Super in loadout) and
        (missile10 in loadout)
    )
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canDBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Bombs in loadout) or
        (HiJump in loadout)
        )
))
canJumpHigh = LogicShortcut(lambda loadout: (
    (HiJump in loadout) or
    (SpaceJump in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (HiJump in loadout) and
    (Morph in loadout)
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canCF = LogicShortcut(lambda loadout: (
    (missile10 in loadout) and
    (super12 in loadout) and
    (powerBomb12 in loadout)
))
eastCrateria = LogicShortcut(lambda loadout: (
    (pinkDoor in loadout) and
    (
        (canFly in loadout) or
        (SpeedBooster in loadout) or
        (
            (canUseBombs in loadout) and
            (canDBJ in loadout)
            )
        )
))
bombTorizo = LogicShortcut(lambda loadout: (
    (eastCrateria in loadout) and
    (Bombs in loadout)
))
kraid = LogicShortcut(lambda loadout: (
    (Super in loadout) and
    (pinkDoor in loadout) and
    (
        (canUseBombs in loadout) or
        (
            (canUsePB in loadout) and
            (canIBJ in loadout)
            )
        )
))
canHellrun = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
canBreakWestNorfairTube = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (pinkDoor in loadout) and
    (Super in loadout)
))
crateriaDepths = LogicShortcut(lambda loadout: (
    (eastCrateria in loadout) and
    (Super in loadout) and
    (GravitySuit in loadout) and
    (
        (canFly in loadout) or
        (canJumpHigh in loadout)
        ) and
    (
        (canFly in loadout) or
        (SpeedBooster in loadout) or
        (purpleDoor in loadout)
        ) and
    (
        (SpeedBooster in loadout) or
        (
            (Grapple in loadout) and
            (purpleDoor in loadout)
            )
        )
))
norfair = LogicShortcut(lambda loadout: (
    (kraid in loadout) and
    (
        (Varia in loadout) or
        (energy400 in loadout)
    )
))
varia = LogicShortcut(lambda loadout: (
    (Super in loadout) and
    (canUseBombs in loadout) and
    (
        (canFly in loadout) or
        (Ice in loadout)
    )
))
norfairElevator = LogicShortcut(lambda loadout: (
    (Super in loadout) and
    (pinkDoor in loadout) and
    (canUseBombs in loadout)
))
enterWestNorfairTube = LogicShortcut(lambda loadout: (
    (canBreakWestNorfairTube in loadout) and
    (
        (Grapple in loadout) or
        (SpaceJump in loadout) or
        (Varia in loadout)
    )
))
leaveWestNorfairTube = LogicShortcut(lambda loadout: (
    (
        (canFly in loadout) or
        (canJumpHigh in loadout)
    ) and
    (pinkDoor in loadout) and
    (
        (Grapple in loadout) or
        (SpaceJump in loadout) or
        (
            (GravitySuit in loadout) and
            (canIBJ in loadout) and
            (Varia in loadout)
        )
    ) and
    (
        (Varia in loadout) or
        (energy400 in loadout)
    )
))
clipWestNorfairTube = LogicShortcut(lambda loadout: (
    (leaveWestNorfairTube in loadout) and
    (GravitySuit in loadout) and
    (HiJump in loadout)
))
westNorfair = LogicShortcut(lambda loadout: (
    (Varia in loadout) and
    (clipWestNorfairTube in loadout)
))
eastNorfair = LogicShortcut(lambda loadout: (
    (kraid in loadout) and
    (Varia in loadout) and
    (canUsePB in loadout) and
    (canDBJ in loadout) and
    (
        (Grapple in loadout) or
        (canFly in loadout)
    ) and
    (
        (GravitySuit in loadout) or
        (
            (purpleDoor in loadout) and
            (
                (Grapple in loadout) or
                (SpaceJump in loadout)
            )
        )
    )
))
escapeGrappleGauntlet = LogicShortcut(lambda loadout: (
    (eastNorfair in loadout) and
    (
        (HiJump in loadout) or
        (
            (canIBJ in loadout) and
            (GravitySuit in loadout)
        ) or
        (SpaceJump in loadout) or
        (Grapple in loadout)
    )
))
writg = LogicShortcut(lambda loadout: (
    (SpaceJump in loadout) or
    (HiJump in loadout) or
    (Ice in loadout)
))
lowerNorfair = LogicShortcut(lambda loadout: (
    (eastNorfair in loadout) and
    (canFly in loadout) and
    (
        (
            (GravitySuit in loadout) and
            (purpleDoor in loadout) and
            (writg in loadout)
            ) or
        (HiJump in loadout)
        )
))
ridley = LogicShortcut(lambda loadout: (
    (lowerNorfair in loadout) and
    (Charge in loadout) and
    (energy300 in loadout)
))
maridia = LogicShortcut(lambda loadout: (
    (GravitySuit in loadout) and
    (Morph in loadout) and
    (
        (canFly in loadout) or
        (canJumpHigh in loadout)
    ) and
    (Super in loadout) and
    (pinkDoor in loadout) and
    (canUseBombs in loadout)
))
leaveCentralMaridia = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (canUsePB in loadout)
))
eastMaridia = LogicShortcut(lambda loadout: (
    (
        (crateriaDepths in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (
            (canFly in loadout) or
            (kraid in loadout)
        )
     ) or
        (
            (leaveCentralMaridia in loadout) and
            (canFly in loadout) and
            (
                (SpaceJump in loadout) or
                (
                    (HiJump in loadout) and
                    (Screw in loadout)
                )
            )
        )
))
botwoon = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (SpeedBooster in loadout) and
    (purpleDoor in loadout) and
    (
        (leaveCentralMaridia in loadout) or
        (Grapple in loadout)
    )
))
draygon = LogicShortcut(lambda loadout: (
    (leaveCentralMaridia in loadout) and
    (canFly in loadout) and
    (botwoon in loadout) and
    (
        (SpaceJump in loadout) or
        (
            (HiJump in loadout) and
            (Screw in loadout)
            )
        )
))

allItems = LogicShortcut(lambda loadout: (
    (Missile in loadout) and
    (super12 in loadout) and
    (PowerBomb in loadout) and
    (Morph in loadout) and
    (Springball in loadout) and
    (Grapple in loadout) and
    (Bombs in loadout) and
    (HiJump in loadout) and
    (GravitySuit in loadout) and
    (Varia in loadout) and
    (Wave in loadout) and
    (SpeedBooster in loadout) and
    (Spazer in loadout) and
    (Ice in loadout) and
    (Plasma in loadout) and
    (Screw in loadout) and
    (Charge in loadout) and
    (SpaceJump in loadout)
))


area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "*Morph Ball": lambda loadout: (
        True
    ),
    "*Missile (First)": lambda loadout: (
        (Morph in loadout)
    ),
    "*Bombs": lambda loadout: (
        (eastCrateria in loadout) and
        (canIBJ in loadout) and #maybe
        (
            (
                (canDBJ in loadout) and
                (
                    (canUseBombs in loadout) or
                    (Wave in loadout)
                )
            ) or
            (SpeedBooster in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "*Super Missile (Spore Spawn)": lambda loadout: (
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
    ),
    "*Missile (Landing Site)": lambda loadout: (
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Power Bomb (Parlor)": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Brinstar small sidehopper alley)": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "*Wall-Jump Boots": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "*Super Missile (West Crateria chain)": lambda loadout: (
        (Super in loadout) and
        (SpeedBooster in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Crateria west of landing site)": lambda loadout: (
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
    ),
    "*Energy Tank (Parlor)": lambda loadout: (
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
    ),
    "*Missile (Crateria west courtyard)": lambda loadout: (
        (eastCrateria in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "*Missile (East Crateria green doors)": lambda loadout: (
        (eastCrateria in loadout) and
        (canUseBombs in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Bomb Torizo)": lambda loadout: (
        (eastCrateria in loadout) and
        (
            (canBreakBlocks in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "*Super Missile (Brinstar spikes)": lambda loadout: (
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
    ),
    "*Energy Tank (Brinstar bat cave)": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "*Power Bomb (Crateria east courtyard)": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "*Super Missile (Crateria west courtyard)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        ) and
        (canUseBombs in loadout) and
        (purpleDoor in loadout)
    ),
    "*Missile (Purple Crateria lower depths access)": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        )
    ),
    "*Missile (Maridia-Brinstar tube)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (canUsePB in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        )
    ),
    "*Energy Tank (Red Brinstar zebbos)": lambda loadout: (
        (kraid in loadout)
    ),
    "*Missile (Red Brinstar Samus eaters)": lambda loadout: (
        (kraid in loadout) and
        (canDBJ in loadout)
    ),
    "*Missile (Red Brinstar underwater)": lambda loadout: (
        (kraid in loadout)
    ),
    "*Varia Suit": lambda loadout: (
        (varia in loadout)
    ),
    "*Missile (Warehouse entrance)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Super Missile (Warehouse entrance)": lambda loadout: (
        (pinkDoor in loadout) and
        (
            (kraid in loadout) or
            (
                (Super in loadout) and
                (canUsePB in loadout)
            )
        )
    ),
    "*Missile (Brinstar junction)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (
            (canUseBombs in loadout) or
            (
                (SpaceJump in loadout) and
                (Screw in loadout)
            )
        )
    ),
    "*Missile (Hi-Jump)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Charge Beam": lambda loadout: (
        (pinkDoor in loadout) and
        (Super in loadout)
    ),
    "*Reserve Tank (Brinstar)": lambda loadout: (
        (kraid in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Draygon sandfall)": lambda loadout: (
        (leaveCentralMaridia in loadout) and
        (SpaceJump in loadout)
    ),
    "*Missile (East Maridia NEStroid item room)": lambda loadout: (
        (eastMaridia in loadout) or
        (
            (leaveCentralMaridia in loadout) and
            (canIBJ in loadout)
        )
    ),
    "*Missile (Draygon sandfall access)": lambda loadout: (
        (eastMaridia in loadout)
    ),
    "*Missile (East Maridia top)": lambda loadout: (
        (eastMaridia in loadout) and
        (canFly in loadout)
    ),
    "*Missile (East Maridia shaft ceiling)": lambda loadout: (
        (eastMaridia in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        )
    ),
    "*Super Missile (East Maridia shinespark)": lambda loadout: (
        (eastMaridia in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Super Missile (Maridia speedball)": lambda loadout: (
        (leaveCentralMaridia in loadout) and
        (canFly in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Super Missile (Parlor)": lambda loadout: (
        (canUsePB in loadout) and
        (canJumpHigh in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Parlor blue gate)": lambda loadout: (
        (Wave in loadout) and
        (pinkDoor in loadout)
    ),
    "*Power Bomb (Purple Crateria one-shot spark)": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        )
    ),
    "*Missile (East Crateria wall)": lambda loadout: (
        (eastCrateria in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Energy Tank (East Crateria Chain)": lambda loadout: (
        (eastCrateria in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Power Bomb (East Crateria maze)": lambda loadout: (
        (eastCrateria in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout) and
        (canUseBombs in loadout) and
        (canSBJ in loadout)
    ),
    "*Power Bomb (Crateria west of landing site)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (canIBJ in loadout) and
        (
            (
                (SpeedBooster in loadout) and
                (HiJump in loadout)
            ) or
            (SpaceJump in loadout) or
            (Ice in loadout)
        )
    ),
    "*Missile (West Brinstar Guardian right)": lambda loadout: (
        (canUsePB in loadout) and
        (kraid in loadout) and
        (pinkDoor in loadout) and
        (Super in loadout)
    ),
    "*Missile (West Brinstar Guardian left)": lambda loadout: (
        (canUsePB in loadout) and
        (kraid in loadout) and
        (pinkDoor in loadout) and
        (Super in loadout)
    ),
    "*Hi-Jump Boots": lambda loadout: (
        (purpleDoor in loadout) and
        (canUseBombs in loadout) and
        (
            (Grapple in loadout) or
            (
                (GravitySuit in loadout) and
                (canFly in loadout)
            )
        )
    ),
    "*Energy Tank (Brinstar fish tank)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (canBreakBlocks in loadout) and
        (
            (Ice in loadout) or
            (
                (canFly in loadout) and
                (GravitySuit in loadout)
            )
        )
    ),
    "*Missile (Brinstar-Norfair tube)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (
                (varia in loadout) and
                (
                    (
                        (Varia in loadout) and
                        (
                            (Grapple in loadout) or
                            (SpaceJump in loadout) or
                            (energy400 in loadout)
                        )
                    ) or
                    (
                        (energy400 in loadout) and
                        (
                            (Grapple in loadout) or
                            (SpaceJump in loadout)
                        )
                    )
                )
            )
        )
    ),
    "*Power Bomb (Maridia-Brinstar tube)": lambda loadout: (
        (leaveCentralMaridia in loadout)
    ),
    "*Missile (Botwoon sandfall)": lambda loadout: (
        (maridia in loadout) and
        (SpaceJump in loadout)
    ),
    "*Power Bomb (West Maridia sandpit)": lambda loadout: (
        (maridia in loadout)
    ),
    "*Missile (West Maridia sandpit left)": lambda loadout: (
        (maridia in loadout)
    ),
    "*Missile (West Maridia sandpit right)": lambda loadout: (
        (maridia in loadout)
    ),
    "*Missile (West Maridia ramps)": lambda loadout: (
        (maridia in loadout) and
        (canDBJ in loadout)
    ),
    "*Missile (West Maridia chain)": lambda loadout: (
        (maridia in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (West Maridia red gates)": lambda loadout: (
        (eastNorfair in loadout)
    ),
    "*Energy Tank (Botwoon)": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout)
    ),
    "*Space Jump": lambda loadout: (
        (botwoon in loadout)
    ),
    "*Missile (West Maridia sandfall)": lambda loadout: (
        (maridia in loadout) and
        (
            (canUsePB in loadout) or
            (Grapple in loadout) or
            (SpaceJump in loadout)
        ) and
        (
            (HiJump in loadout) or
            (Screw in loadout)
        )
    ),
    "*Missile (Maridia sandcanyon)": lambda loadout: (
        (maridia in loadout) and
        (
            (leaveCentralMaridia in loadout) or
            (Grapple in loadout)
        )
    ),
    "*Super Missile (East Maridia chain)": lambda loadout: (
        (SpeedBooster in loadout) and
        (canFly in loadout) and
        (canDBJ in loadout) and
        (
            (leaveCentralMaridia in loadout) or
            (eastMaridia in loadout)
        )
    ),
    "*Missile (Maridia uterus room)": lambda loadout: (
        (maridia in loadout)
    ),
    "*Power Bomb (West Maridia gate hall)": lambda loadout: (
        (draygon in loadout) and
        (canIBJ in loadout)
    ),
    "*Super Missile (Crateria Depths super ceiling)": lambda loadout: (
        (crateriaDepths in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "*Super Missile (Brinstar-Crateria elevator)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Reserve Tank (Maridia)": lambda loadout: (
        (leaveCentralMaridia in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Reserve Tank (Crateria)": lambda loadout: (
        (crateriaDepths in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Parlor tsundere)": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Lost Caverns)": lambda loadout: (
        (crateriaDepths in loadout)
    ),
    "*Super Missile (Lost Caverns)": lambda loadout: (
        (crateriaDepths in loadout)
    ),
    "*Power Bomb (East Crateria Guardian)": lambda loadout: (
        (crateriaDepths in loadout) and
        (SpeedBooster in loadout) and
        (Wave in loadout)
    ),
    "*Gravity Suit": lambda loadout: (
        (crateriaDepths in loadout)
    ),
    "*Energy Tank (Crateria green gates)": lambda loadout: (
        (crateriaDepths in loadout) and
        (
            (canFly in loadout) or
            (
                (HiJump in loadout) and
                (SpeedBooster in loadout)
            )
        )
    ),
    "*Power Bomb (Crateria map)": lambda loadout: (
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Crateria awakening)": lambda loadout: (
        (pinkDoor in loadout) and
        (
            (canUseBombs in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "*Super Missile (Crateria courtyard tunnel)": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        )
    ),
    "*Missile (Crateria Depths entrance)": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (
            (canUseBombs in loadout) and
            (SpeedBooster in loadout) and
            (
                (canFly in loadout) or
                (canJumpHigh in loadout)
            ) or
            (
                (eastCrateria in loadout) and
                (purpleDoor in loadout) and
                (Grapple in loadout) and
                (
                    (GravitySuit in loadout) or
                    (SpaceJump in loadout)
                )
            )
        )
    ),
    "*Super Missile (Purple Crateria bat cave)": lambda loadout: (
        (Super in loadout) and
        (canUseBombs in loadout) and
        (
            (canFly in loadout) or
            (
                (canJumpHigh in loadout) and
                (Ice in loadout)
            )
        )
    ),
    "*Missile (Spazer)": lambda loadout: (
        (canDBJ in loadout) and
        (Super in loadout) and
        (pinkDoor in loadout)
    ),
    "*Spazer": lambda loadout: (
        (Super in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Brinstar-Crateria elevator)": lambda loadout: (
        (canDBJ in loadout) and
        (canUseBombs in loadout) and
        (pinkDoor in loadout)
    ),
    "Missile (Brinstar bat cave)": lambda loadout: (
        (pinkDoor in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Power Bomb (West Brinstar Guardian)": lambda loadout: (
        (canUsePB in loadout) and
        (kraid in loadout) and
        (pinkDoor in loadout) and
        (Super in loadout)
    ),
    "*Super Missile (Brinstar Diagon Alley)": lambda loadout: (
        (canUsePB in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout) and
        (pinkDoor in loadout)
    ),
    "*Missile (Brinstar Dachora access)": lambda loadout: (
        (Super in loadout) and
        (kraid in loadout)
    ),
    "*Power Bomb (Charge)": lambda loadout: (
        (pinkDoor in loadout) and
        (Super in loadout) and
        (canUsePB in loadout)
    ),
    "*Power Bomb (Crateria awakening)": lambda loadout: (
        (canUsePB in loadout) and
        (
            (canIBJ in loadout) or
            (HiJump in loadout)
        )
    ),
    "*Missile (Brinstar Diagon Alley)": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Power Bomb (Crateria first missile)": lambda loadout: (
        (canUsePB in loadout)
    ),
    "*Power Bomb (Warehouse top)": lambda loadout: (
        (kraid in loadout) and
        (canUsePB in loadout)
    ),
    "*X-ray Scope": lambda loadout: (
        (pinkDoor in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Red Brinstar land guardian)": lambda loadout: (
        (kraid in loadout) and
        (canUsePB in loadout) and
        (canDBJ in loadout)
    ),
    "*Power Bomb (Red Brinstar top entrance)": lambda loadout: (
        (kraid in loadout) and
        (canUsePB in loadout) and
        (
            (SpaceJump in loadout) or
            (
                (HiJump in loadout) and
                (SpeedBooster in loadout)
            )
        )
    ),
    "*Power Bomb (Lower Norfair entrance)": lambda loadout: (
        (eastNorfair in loadout) and
        (canFly in loadout) and
        (
            (GravitySuit in loadout) or
            (HiJump in loadout)
        )
    ),
    "*Ice Beam": lambda loadout: (
        (norfair in loadout)
    ),
    "Missile (Ridley gate shaft)": lambda loadout: (
        (lowerNorfair in loadout)
    ),
    "*Speed Booster": lambda loadout: (
        (westNorfair in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout)
    ),
    "Power Bomb (Norfair sine room)": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (purpleDoor in loadout) and
        (GravitySuit in loadout)
    ),
    "*Super Missile (Crocomire)": lambda loadout: (
        (westNorfair in loadout) and
        (canUseBombs in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout) or
            (
                (Ice in loadout) and
                (Charge in loadout)
            )
        )
    ),
    "Power Bomb (Crocomire)": lambda loadout: (
        (westNorfair in loadout) and
        (canDBJ in loadout)
    ),
    "*Missile (Norfair-Brinstar tube lava)": lambda loadout: (
        (westNorfair in loadout) and
        (
            (GravitySuit in loadout) or
            (energy200 in loadout)
        )
    ),
    "*Missile (Lower Norfair top)": lambda loadout: (
        (lowerNorfair in loadout)
    ),
    "*Missile (Lower Norfair shinespark)": lambda loadout: (
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile (Grapple)": lambda loadout: (
        (escapeGrappleGauntlet in loadout)
    ),
    "*Power Bomb (Grapple)": lambda loadout: (
        (escapeGrappleGauntlet in loadout) and
        (
            (GravitySuit in loadout) or
            (energy200 in loadout)
        )
    ),
    "*Energy Tank (Ridley)": lambda loadout: (
        (escapeGrappleGauntlet in loadout) and
        (ridley in loadout)
    ),
    "*Grapple Beam": lambda loadout: (
        (escapeGrappleGauntlet in loadout)
    ),
    "*Power Bomb (West Norfair sanctum)": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "*Missile (West Norfair sanctum hidden)": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout) and
        (
            (Ice in loadout) or
            (GravitySuit in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "*Power Bomb (East Norfair Guardian)": lambda loadout: (
        (escapeGrappleGauntlet in loadout)
    ),
    "*Missile (Bob Jr.)": lambda loadout: (
        (kraid in loadout) and
        (Varia in loadout) and
        (canUsePB in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (kraid in loadout)
            ) or
            (
                (purpleDoor in loadout) and
                (
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                )
            )
        )
    ),
    "*Missile (East Norfair Alcoon hideout)": lambda loadout: (
        (kraid in loadout) and
        (Varia in loadout) and
        (canUsePB in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (kraid in loadout)
            ) or
            (
                (purpleDoor in loadout) and
                (
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                )
            )
        ) and
        (
            (canIBJ in loadout) or
            (
                (Wave in loadout) and
                (canFly in loadout) or
                (
                    (HiJump in loadout) and
                    (SpeedBooster in loadout) and
                    (Ice in loadout)
                )
            )
        )
    ),
    "*Wave Beam": lambda loadout: (
        (westNorfair in loadout) and
        (
            (SpeedBooster in loadout) or
            (canFly in loadout)
        )
    ),
    "Missile (Pantry)": lambda loadout: (
        (kraid in loadout) and
        (Varia in loadout) and
        (canUsePB in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (kraid in loadout)
            ) or
            (
                (purpleDoor in loadout) and
                (
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                ) and
                (
                    (canFly in loadout) or
                    (SpeedBooster in loadout)
                ) and
                (SpaceJump in loadout) or
                (
                    (HiJump in loadout) and
                    (Screw in loadout)
                )
            )
        )

    ),
    "*Missile (Bob Jr. underpass)": lambda loadout: (
        (westNorfair in loadout) and
        (canUsePB in loadout) and
        (canDBJ in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (kraid in loadout)
            ) or
            (
                (purpleDoor in loadout) and
                (
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                )
            )
        )
    ),
    "*Power Bomb (Lower Norfair Violas)": lambda loadout: (
        (lowerNorfair in loadout) and
        (canDBJ in loadout)
    ),
    "*Power Bomb (Golden Torizo)": lambda loadout: (
        (lowerNorfair in loadout) and
        (ridley in loadout)
    ),
    "Missile (Ridley gate room)": lambda loadout: (
        (ridley in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Missile (Lower Norfair puromi hall)": lambda loadout: (
        (lowerNorfair in loadout)
    ),
    "*Plasma Beam": lambda loadout: (
        (ridley in loadout) and
        (GravitySuit in loadout)
    ),
    "*Super Missile (Lower Norfair holtz tease)": lambda loadout: (
        (lowerNorfair in loadout) and
        (
            (canSBJ in loadout) or
            (canIBJ in loadout)
        )
    ),
    "*Screw Attack": lambda loadout: (
        (eastNorfair in loadout) and
        (
            (SpeedBooster in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "Missile (Lower Norfair desgeega boost room)": lambda loadout: (
        (ridley in loadout) and
        (
            (GravitySuit in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "*Missile (East Norfair Indiana Jones)": lambda loadout: (
        (eastNorfair in loadout)
    ),
    "*Super Missile (East Norfair Guardian)": lambda loadout: (
        (eastNorfair in loadout) and
        (canJumpHigh in loadout)
    ),
    "*Power Bomb (Magmoor Tunnel)": lambda loadout: (
        (canUseBombs in loadout) and
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "*Energy Tank (Magmoor Tunnel)": lambda loadout: (
        (norfair in loadout) and
        (canUseBombs in loadout) and
        (canDBJ in loadout)
    ),
    "*Power Bomb (Early PB maze)": lambda loadout: (
        (westNorfair in loadout) and
        (
            (Wave in loadout) or
            (Charge in loadout)
        ) and
        (
            (canIBJ in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "Missile (West Norfair Ridley face)": lambda loadout: (
        (westNorfair in loadout) and
        (canUsePB in loadout)
    ),
    "*Energy Tank (East Norfair cavern storage)": lambda loadout: (
        (eastNorfair in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (
                (Screw in loadout) and
                (HiJump in loadout)
            ) or
            (
                (GravitySuit in loadout) and
                (canIBJ in loadout)
            )
        )
    ),
    "*Missile (East Crateria buried treasure)": lambda loadout: (
        (crateriaDepths in loadout) and
        (Wave in loadout) and
        (canUseBombs in loadout)
    ),
    "*Reserve Tank (Norfair)": lambda loadout: (
        (westNorfair in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout) and
        (GravitySuit in loadout) and
        (canFly in loadout)
    ),
    "*Missile (West Norfair morph lock)": lambda loadout: (
        (westNorfair in loadout) and
        (canSBJ in loadout)
    ),
    "*Energy Tank (Maridia Ridley tube)": lambda loadout: (
        (maridia in loadout) and
        (ridley in loadout)
    ),
    "*Energy Tank (West Maridia chain)": lambda loadout: (
        (maridia in loadout) and
        (SpeedBooster in loadout) and
        (
            (SpaceJump in loadout) or
            (
                (draygon in loadout) and
                (canDBJ in loadout)
            )
        )
    ),
    "Power Bomb (West Maridia chain)": lambda loadout: (
        (maridia in loadout) and
        (SpeedBooster in loadout) and
        (HiJump in loadout)
    ),
    "*Energy Tank (Draygon sandfall)": lambda loadout: (
        (
            (eastMaridia in loadout) and
            (
                (canFly in loadout) or
                (SpeedBooster in loadout)
            ) and
            (canUseBombs in loadout)
        ) or
        (
            (leaveCentralMaridia in loadout) and
            (SpaceJump in loadout)
        )
    ),
    "*Missile (East Maridia mocktroid cave)": lambda loadout: (
        (leaveCentralMaridia in loadout) and
        (
            (canFly in loadout) or
            (
                (canJumpHigh in loadout) or
                (SpeedBooster in loadout)
            )
        )
    ),
    "Missile (East Maridia mocktroid hall)": lambda loadout: (
        (eastMaridia in loadout) and
        (
            (canFly in loadout) or
            (canJumpHigh in loadout)
        ) and
        (SpeedBooster in loadout)
    ),
    "*Super Missile (East Maridia Draygon lock)": lambda loadout: (
        (draygon in loadout)
    ),
    "*Beam Combo": lambda loadout: (
        (leaveCentralMaridia in loadout) and
        (
            (canFly in loadout) or
            (
                (canUseBombs in loadout) and
                (canJumpHigh in loadout)
            )
        ) and
        (
            (draygon in loadout) and
            (canIBJ in loadout)
        ) and
        ( #not sure of this section
            (Charge in loadout) and
            (Wave in loadout) #??
        )
    ),
    "Missile (West Norfair sanctum chozo)??": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (Screw in loadout)
        )
    ),
    "*Missile (Norfair-Brinstar elevator)": lambda loadout: (
        (westNorfair in loadout) and
        (
            (GravitySuit in loadout) or
            (energy400 in loadout)
        )
    ),
    "*Energy Tank (Grapple)": lambda loadout: (
        (escapeGrappleGauntlet in loadout) and
        (GravitySuit in loadout) #simplest logic for now
    ),
    "*Super Missile (West Norfair Sanctum)": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile (West Norfair Sanctum Top)": lambda loadout: (
        (westNorfair in loadout) and
        (SpeedBooster in loadout) and
        (
            (Ice in loadout) or
            (GravitySuit in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "*Power Bomb (East Norfair Purple Maze)": lambda loadout: (
        #copied logic from alcoon hideout
        (kraid in loadout) and
        (Varia in loadout) and
        (canUsePB in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (kraid in loadout)
            ) or
            (
                (purpleDoor in loadout) and
                (
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                )
            )
        ) and
        (
            (canIBJ in loadout) or
            (
                (Wave in loadout) and
                (canFly in loadout) or
                (
                    (HiJump in loadout) and
                    (SpeedBooster in loadout) and
                    (Ice in loadout)
                )
            )
        )
    ),
}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
