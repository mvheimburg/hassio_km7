import appdaemon.plugins.hass.hassapi as hass

#
# Hellow World App
#
# Args:
#

class CandleLightWithStrobe(hass.Hass):

  def initialize(self):
    self.log("Hello from AppDaemon")
    self.log("You are now ready to run Apps!")
    try:
      self._light_entity = self.args.get('light_entity', None)
      self._trigger_entity = self.args.get('trigger_entity', None)
      self._strobe_condition_entity = self.args.get('strobe_condition_entity', None)
    except (TypeError, ValueError):
      self.log("Invalid Configuration", level="ERROR")
      return
        
    
    self.listen_state(self.on_halloween_mode, self._trigger_entity , new="on")

  def on_halloween_mode (self, entity, attribute, old, new, kwargs):
    
    a_variabele_with_a_usable_name = self.get_state("device_tracker.some_mobile")
    if  a_variabele_with_a_usable_name == "home":
      self.turn_on("light.some_light")
