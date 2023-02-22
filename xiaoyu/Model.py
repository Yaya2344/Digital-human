#Construct human behavior components, behavior models, etc. based on the requirements of the input specific behavior, and provide the simulation group to realize the human behavior
# simulation
class HumanBehaviorModel(object):
    def __init__(self, human_behavior, human_behavior_name, human_behavior_type, human_behavior_model):
        self.human_behavior = human_behavior
        self.human_behavior_name = human_behavior_name
        self.human_behavior_type = human_behavior_type
        self.human_behavior_model = human_behavior_model

    def get_human_behavior(self):
        return self.human_behavior

    def get_human_behavior_name(self):
        return self.human_behavior_name

    def get_human_behavior_type(self):
        return self.human_behavior_type

    def get_human_behavior_model(self):
        return self.human_behavior_model

    def set_human_behavior(self, human_behavior):
        self.human_behavior = human_behavior

    def set_human_behavior_name(self, human_behavior_name):
        self.human_behavior_name = human_behavior_name

    def set_human_behavior_type(self, human_behavior_type):
        self.human_behavior_type = human_behavior_type

    def set_human_behavior_model(self, human_behavior_model):
        self.human_behavior_model = human_behavior_model


