import unreal as ue
from unreal import Actor


ue.log("WoW Testing Log")
ue.log_warning("WoW Testing Log Warning")
ue.log_error("WoW Testing Log Error")


# Funcions for map(func,iter) to make a list easily
def Get_Class_Name(actor:Actor)->str:
    return actor.get_class().get_name()
    

def Get_Actor_Label(actor:Actor)->str:
    return actor.get_actor_label()
# ------------------------------------------------



# Get the editor actor subsystem
actor_subsys = ue.get_editor_subsystem(ue.EditorActorSubsystem)

# Get array of actors in the loaded level
ActorList = actor_subsys.get_all_level_actors()

# make a list of the Actor Class names
ActorClassList = list(map(Get_Class_Name,ActorList))
ActorLabelList = list(map(Get_Actor_Label,ActorList))
# print(*ActorClassList,sep="\n")

ue.log("List of actor Classes in loaded level:")
ue.log("-------------------------------------")

for i in range(0,len(ActorClassList)):
    ue.log("Class: " + ActorClassList[i] + "\t\tLabel: "  + ActorLabelList[i])