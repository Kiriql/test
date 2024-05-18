import unreal as ue
from unreal import Actor

# in case the connection is there but the editor is somehow not running
if not ue.is_editor():
    ue.log("Editor not Running\nStart the editor to execute the script")
    quit()


# Funcions for map(func,iter) to make a list easily
def Get_Class_Name(actor:Actor)->str:
    return actor.get_class().get_name()
    

def Get_Actor_Label(actor:Actor)->str:
    return actor.get_actor_label().lower()
    # .lower() is used to make it easier to find with generic text

# ------------------------------------------------



# Get the editor actor subsystem
actor_subsys = ue.get_editor_subsystem(ue.EditorActorSubsystem)

# Get array of actors in the loaded level
ActorList = actor_subsys.get_all_level_actors()

# make a list of the Actor Class names
ActorClassList = list(map(Get_Class_Name,ActorList))
# print(*ActorClassList,sep="\n")

# print("     ")
# print("\n--------------(Start)--------------\nLooking for Module_Sequencer_C ...")
ue.log("--------------(Start)--------------")
ue.log("Looking for Module_Sequencer_C ...")

if 'Module_Sequencer_C' not in ActorClassList:
    # print("\n\n----\nModule Sequencer Actor Not found in Level actors\n----\n")
    ue.log("----")
    ue.log("Module Sequencer Actor Not found in Level actors")
    ue.log("----")
    # Get a class for spawning
    my_class = ue.EditorAssetLibrary.load_blueprint_class('/Game/Level_Modules/Module_Sequencer.Module_Sequencer')

    # Actually spawn the actor at x0 y0 z600
    spawn_location = ue.Vector(0, 0, 600)
    inst = actor_subsys.spawn_actor_from_class(my_class, spawn_location)
    # print(inst,"\n----\nSpawned Module Sequencer\n----")
    ue.log(inst)
    ue.log("----")
    ue.log("Spawned Module Sequencer")
    ue.log("----")

    # Add new instance of actor to current selection
    selection = actor_subsys.get_selected_level_actors()
    selection.append(inst) # add new instance to selected actors
    actor_subsys.set_selected_level_actors(selection)
    # print("added new instance to selected actors\n-------------(Finish)--------------")
    ue.log("added new instance to selected actors")
    ue.log("-------------(Finish)--------------")

else:
    # print("\n\n----\nModule Sequencer Actor already in Level actors\n-------------(Finish)--------------\n")
    ue.log("----")
    ue.log("Module Sequencer Actor already in Level actors")
    ue.log("-------------(Finish)--------------")
    
