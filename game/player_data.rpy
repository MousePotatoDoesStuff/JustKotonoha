init -10 python:
    import random
    class Category:
        def __init__(self):
            return # TODO create category class
    class PlayerData:
        def __init__(self,pref_choices=dict()):
            self.pref_choices=pref_choices # A dictionary for player preference choices.
            return
        def set_pref_choice(self,topic,option,value=0): # Set preference choice, e.g. player.set_pref_choice('games','VNs',0)
            if topic not in self.pref_choices:
                X=dict()
                self.pref_choices[topic]=X
            else:
                X=self.pref_choices[topic] # X is equal to self.pref_choices['games']
            X[option]=value
            return
        def remove_pref_choice(self,topic,option): # Remove preference choice, e.g. player.remove_pref_choice('games','VNs',0)
            if topic not in self.pref_choices:
                X=dict()
                self.pref_choices[topic]=X
            else:
                X=self.pref_choices[topic] # X is equal to self.pref_choices['games']
            if option in X:
                X.pop(option)
            return
        def add_pref_choice(self,topic,option,value=1): # Record a preference choice by the player, e.g. player.add_pref_choice('games','VNs')
            if topic not in self.pref_choices:
                X=dict()
                self.pref_choices[topic]=X
            else:
                X=self.pref_choices[topic] # X is equal to self.pref_choices['games']
            if option not in X:
                X[option]=0
            X[option]+=value # Increment choice counter.
            return
        def get_odds(self,topic,def_val=[]):
            if topic not in self.pref_choices:
                return def_val
            return list(self.pref_choices[topic].items())
        def choose(self,topic,nullvalue=None,random_key=lambda x:x+1):
            X=self.get_odds(topic,None)
            if X is None:
                return None
            selection=random.choices(X,weights=[random_key(e[1]) for e in X], k=1)[0]
            return selection[0]