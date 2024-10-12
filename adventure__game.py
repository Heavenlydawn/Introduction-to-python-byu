# For Creativity I wrapped each level in a defined function and called the function where I would like to use it

def start_adventure():
    print("ANCIENT PYRAMID")
    print()
    print("You stand before the entrance of an ancient, crumbling pyramid. Legends say it’s filled with traps, treasure, and dark secrets.")
    print("In front of you, there are three entrances into the pyramid: a WIDE OPEN archway, a NARROW passage covered in vines, and a STONE door with strange markings.")
    users_choice = input("Do you enter through the 'ARCHWAY', 'PASSAGE', or 'DOOR'?: ").lower()

    if users_choice == "archway":
        level_2_archway()
    elif users_choice == "passage":
        level_2_passage()
    elif users_choice == "door":
        level_2_door()
    else:
        print("Invalid choice. Please type 'archway', 'passage', or 'door'.")
        start_adventure()

def level_2_archway():
    print("\nYou step through the wide open archway, and it leads into a grand chamber filled with sand. In the center, you see a GOLDEN STATUE of a pharaoh, ")
    print("and to the left, a TORCH flickers dimly on the wall. You also notice a HIDDEN STAIRWAY leading downward.")
    choice = input("Do you investigate the 'STATUE', grab the 'TORCH', or go down the 'STAIRWAY'?: ").lower()

    if choice == "statue":
        level_3_statue()
    elif choice == "torch":
        level_3_torch()
    elif choice == "stairway":
        level_3_stairway()
    else:
        print("Invalid choice. Please type 'statue', 'torch', or 'stairway'.")
        level_2_archway()

def level_2_passage():
    print("\nYou squeeze through the narrow passage, feeling the cool vines brush against your skin. As you go further, you find a **STONE TABLET** with strange engravings,")
    print("a **BOWL** filled with shimmering liquid, and an **ANCIENT SARCOPHAGUS** lying in the corner.")
    choice = input("Do you examine the 'TABLET', drink from the 'BOWL', or open the 'SARCOPHAGUS'?: ").lower()

    if choice == "tablet":
        level_3_tablet()
    elif choice == "bowl":
        level_3_bowl()
    elif choice == "sarcophagus":
        level_3_sarcophagus()
    else:
        print("Invalid choice. Please type 'tablet', 'bowl', or 'sarcophagus'.")
        level_2_passage()

def level_2_door():
    print("\nYou push open the heavy stone door with a loud groan. Inside, you find a room filled with treasure, but in the center lies a **JEWELED DAGGER**.")
    print("There is also a MYSTERIOUS PEDESTAL and a TRAPDOOR hidden behind a pile of gold.")
    choice = input("Do you take the 'DAGGER', investigate the 'PEDESTAL', or open the 'TRAPDOOR'?: ").lower()

    if choice == "dagger":
        level_3_dagger()
    elif choice == "pedestal":
        level_3_pedestal()
    elif choice == "trapdoor":
        level_3_trapdoor()
    else:
        print("Invalid choice. Please type 'dagger', 'pedestal', or 'trapdoor'.")
        level_2_door()

# Archway Path Continuations
def level_3_statue():
    print("\nYou approach the golden statue, admiring its craftsmanship. But as soon as you touch it, the floor beneath you collapses,")
    print("and you find yourself sliding down a chute into a dark pit. Inside, a horde of scarabs swarms towards you!")
    choice = input("Do you 'RUN', 'FIGHT' the scarabs, or 'CLIMB' the walls to escape?: ").lower()

    if choice == "run":
        print("\nYou run as fast as you can, but the scarabs are too quick. They overwhelm you. The adventure ends.")
    elif choice == "fight":
        print("\nYou swing your hands wildly, crushing as many scarabs as you can, but there are too many. The adventure ends.")
    elif choice == "climb":
        print("\nYou manage to grab hold of the walls and climb out of the pit, narrowly escaping the scarabs. Congratulations! You survive.")
    else:
        print("Invalid choice. Please type 'run', 'fight', or 'climb'.")
        level_3_statue()

def level_3_torch():
    print("\nYou grab the torch from the wall, but as soon as you do, you hear a rumbling noise. The walls start closing in on you!")
    choice = input("Do you 'DROP' the torch, 'RUN' forward, or try to 'STOP' the walls from moving?: ").lower()

    if choice == "drop":
        print("\nYou drop the torch, and the walls stop closing in. It seems the torch was a trigger for the trap. Congratulations! You survive.")
    elif choice == "run":
        print("\nYou sprint forward into the next room just before the walls close behind you. You narrowly escape!")
    elif choice == "stop":
        print("\nYou try to stop the walls from moving, but they’re too strong. The adventure ends.")
    else:
        print("Invalid choice. Please type 'drop', 'run', or 'stop'.")
        level_3_torch()

def level_3_stairway():
    print("\nYou descend the hidden stairway into a chamber filled with glittering jewels and golden relics. However, there is a **SCEPTER** in the center of the room,")
    print("and strange markings on the floor hint at a trap.")
    choice = input("Do you 'TAKE' the scepter, 'SEARCH' the room for traps, or 'LEAVE' immediately?: ").lower()

    if choice == "take":
        print("\nThe moment you take the scepter, the floor collapses beneath you, and you fall into a pit. The adventure ends.")
    elif choice == "search":
        print("\nYou search the room carefully and find hidden pressure plates. You safely avoid the traps and take the treasure. Congratulations!")
    elif choice == "leave":
        print("\nYou decide it’s not worth the risk and leave the treasure behind. Sometimes safety is the greatest treasure. You survive!")
    else:
        print("Invalid choice. Please type 'take', 'search', or 'leave'.")
        level_3_stairway()

# Passage Path Continuations
def level_3_tablet():
    print("\nYou examine the stone tablet and realize it's written in an ancient language. You find a lever nearby.")
    choice = input("Do you 'PULL' the lever, 'LEAVE' it alone, or try to 'TRANSLATE' the tablet?: ").lower()

    if choice == "pull":
        print("\nYou pull the lever, and a hidden door opens, revealing a secret room filled with treasure. Congratulations!")
    elif choice == "leave":
        print("\nYou leave the lever alone and back away. Perhaps it was best not to risk it. You survive, but you wonder what you left behind.")
    elif choice == "translate":
        print("\nAs you try to translate the tablet, a trap is triggered, and spikes shoot up from the floor. The adventure ends.")
    else:
        print("Invalid choice. Please type 'pull', 'leave', or 'translate'.")
        level_3_tablet()

def level_3_bowl():
    print("\nYou drink from the shimmering liquid, and suddenly, you feel a surge of energy course through your body.")
    choice = input("Do you 'EXPLORE' further into the pyramid, 'LEAVE' the pyramid immediately, or 'WAIT' to see what happens?: ").lower()

    if choice == "explore":
        print("\nYou explore deeper into the pyramid with newfound strength. You discover ancient treasures hidden within. Congratulations!")
    elif choice == "leave":
        print("\nYou leave the pyramid while you still feel strong, escaping before any dangers arise. You survive!")
    elif choice == "wait":
        print("\nYou wait too long, and the effects of the liquid wear off. You feel weaker and weaker until you collapse. The adventure ends.")
    else:
        print("Invalid choice. Please type 'explore', 'leave', or 'wait'.")
        level_3_bowl()

def level_3_sarcophagus():
    print("\nYou open the ancient sarcophagus, and inside, you find a mummified pharaoh. Suddenly, the eyes of the mummy glow red.")
    choice = input("Do you 'RUN', 'FIGHT' the mummy, or 'BOW' in respect?: ").lower()

    if choice == "run":
        print("\nYou run as fast as you can, but the mummy chases after you. The adventure ends.")
    elif choice == "fight":
        print("\nYou try to fight the mummy, but it’s too powerful. The adventure ends.")
    elif choice == "bow":
        print("\nYou bow respectfully, and the mummy nods before crumbling into dust. You’ve passed the test of the ancients. Congratulations!")
    else:
        print("Invalid choice. Please type 'run', 'fight', or 'bow'.")
        level_3_sarcophagus()

# Door Path Continuations
def level_3_dagger():
    print("\nYou take the jeweled dagger, but as soon as you do, a series of spears shoot out from the walls!")
    choice = input("Do you 'DODGE', 'DROP' the dagger, or try to 'DEFLECT' the spears with it?: ").lower()

    if choice == "dodge":
        print("\nYou roll to the side and narrowly avoid the spears. You survive, but the dagger is lost.")
    elif choice == "drop":
        print("\nYou drop the dagger, and the spears stop. It seems the treasure was cursed. You survive!")
    elif choice == "deflect":
        print("\nYou try to deflect the spears, but they’re too fast. The adventure ends.")
    else:
        print("Invalid choice. Please type 'dodge', 'drop', or 'deflect'.")
        level_3_dagger()

def level_3_pedestal():
    print("\nYou examine the mysterious pedestal and find a glowing orb on top of it.")
    choice = input("Do you 'TOUCH' the orb, 'LEAVE' the room, or 'DESTROY' the pedestal?: ").lower()

    if choice == "touch":
        print("\nYou touch the orb, and the room fills with light. You feel yourself being transported to another realm. The adventure continues in ways you can’t yet imagine.")
    elif choice == "leave":
        print("\nYou decide not to risk it and leave the room. Sometimes, it’s best not to meddle with the unknown. You survive!")
    elif choice == "destroy":
        print("\nYou try to destroy the pedestal, but it triggers a trap. The room collapses, and the adventure ends.")
    else:
        print("Invalid choice. Please type 'touch', 'leave', or 'destroy'.")
        level_3_pedestal()

def level_3_trapdoor():
    print("\nYou open the trapdoor and find a ladder leading down to a hidden chamber.")
    choice = input("Do you 'CLIMB' down the ladder, 'CLOSE' the trapdoor, or 'THROW' a rock down first to check for traps?: ").lower()

    if choice == "climb":
        print("\nYou climb down the ladder and discover a hidden treasure room. Congratulations!")
    elif choice == "close":
        print("\nYou close the trapdoor and decide to explore elsewhere. You survive, but you wonder what was down there.")
    elif choice == "throw":
        print("\nYou throw a rock down, and a trap is triggered. Spikes shoot up, saving you from a deadly fall. You survive!")
    else:
        print("Invalid choice. Please type 'climb', 'close', or 'throw'.")
        level_3_trapdoor()

# Start the adventure game
start_adventure()