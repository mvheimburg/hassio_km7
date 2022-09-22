import hassapi as hass
import datetime
from datetime import timedelta
import math

class systemair_cotwo(hass.Hass):
    def initialize(self):
        self.sensor = self.args.get('sensor', None)
        self.systemair = self.args.get('systemair', None)
        # self.sensor.listen_state(self.state_change)
        self.listen_state(self.state_change, self.sensor)


    def state_change(self, entity, attribute, old, new, kwargs):
        self.log(f"new co2 ppm: {new}") 
        self.call_service("systemair/set_cotwo_meas", entity_id=self.systemair, value=int(new))
