import hassapi as hass
import datetime
from datetime import timedelta
import math

from const import HOME_STATES

class house_state(hass.Hass):

    # _state = None

    def initialize(self):
        self.state_input = self.args.get('state_input', None)
        self.state_home_input = self.args.get('state_home_input', None)
        self.door_lock = self.args.get('door_lock', None)
        self.garage_gate = self.args.get('garage_gate', None)
        self.scenes = self.args.get('scenes', None)
        # self.leave_home = self.args.get('leave_home', None)
        # self.come_home = self.args.get('come_home', None)
        # self.day = self.args.get('day', None)
        # self.night = self.args.get('night', None)
        self.vacation = self.args.get('vacation', None)

        self.listen_state(self.state_input_change, self.state_input)
        self.listen_state(self.door_lock_change, self.door_lock)
        self.listen_state(self.garage_gate_change, self.garage_gate)
        self.listen_state(self.state_home_input_change, self.state_home_input)

        self.log(f"self.scenes: {self.scenes}")


    def state_input_change(self, entity, attribute, old, new, kwargs):
        self.log(f"input_change: {new}") 
        if new == 'Hjemme':
            self.log(f"Hjemme") 
            self.turn_on(self.scenes['come_home'])
        elif new == 'Borte':
            self.log(f"Borte")
            self.turn_on(self.scenes['leave_home'])
        elif new == 'Ferie':
            self.log(f"Ferie")
            self.turn_on(self.scenes['vacation'])
        else:
            self.log(f"New state same as old")
 

    def door_lock_change(self, entity, attribute, old, new, kwargs):
        self.log(f"door_lock_change: {new}") 
        if new == 'unlocked':
            self.conditional_change_to_home()


    def garage_gate_change(self, entity, attribute, old, new, kwargs):
        self.log(f"garage_gate_change: {new}") 
        if new != 'closed' and old == 'closed':
            self.conditional_change_to_home()


    def conditional_change_to_home(self):
        current_state=self.get_state(self.state_input)
        self.log(f"current_state: {current_state}")
        if current_state in ['Borte','Ferie']:
            self.log(f"changing input select to: Hjemme")
            self.select_option(entity_id=self.state_input, option='Hjemme')


    def state_home_input_change(self, entity, attribute, old, new, kwargs):
        self.log(f"state_home_input_change: {new}")
        if self.get_state(self.state_input) == 'Hjemme':
            if new == 'Dag':
                self.turn_on(self.scenes['day'])
            elif new == 'Natt':
                self.turn_on(self.scenes['night'])

