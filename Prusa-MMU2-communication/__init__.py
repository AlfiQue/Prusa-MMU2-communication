# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import serial


__plugin_name__ = "Prusa MMU2 communication"
__plugin_version__ = "0.0.1"
__plugin_description__ = "Communication with Prusa MMU2 by USB"

class OctoremotePlugin(octoprint.plugin.SettingsPlugin,
					   octoprint.plugin.AssetPlugin,
					   octoprint.plugin.TemplatePlugin,
					   octoprint.plugin.StartupPlugin,
					   octoprint.plugin.ShutdownPlugin):
	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			comport="COM3",
			baudrate=115200,
			baudrateOpt=[9600, 19200, 115200],
		)

	def get_config_vars(self):
		return dict(
			comport=self._settings.get(["comport"]),
			baudrate=self._settings.get(["baudrate"]),
			baudrateOpt=self._settings.get(["baudrateOpt"]),
		)
		
	# def get_template_configs(self):
		# return [
			dict(type="navbar", custom_bindings=False),
			# dict(type="settings", custom_bindings=False)
		# ]

	def on_settings_save(self, data):
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
			USB = serial.Serial(port=comport, baudrate=baudrate, timeout=1
				if USB.isOpen():
					while False:
						self.interrupt()
						callbackClass.getLogger().error("Prusa MMU2 communication, could not open comport:" + self.portname)

	##~~ Softwareupdate hook
	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			MMU2-communication=dict(
				displayName="Prusa MMU2 communication",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="AlfiQue",
				repo="Prusa-MMU2-communication",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/AlfiQue/Prusa-MMU2-communication/archive/{target_version}.zip"
			)
		)

	def on_after_startup(self):
	USB = serial.Serial(port=comport, baudrate=baudrate, timeout=1
	if USB.isOpen():
		while False:
			self.interrupt()
			callbackClass.getLogger().error("Prusa MMU2 communication, could not open comport:" + self.portname)

	def on_shutdown(self):
	USB.close()
		self._logger.info("on shutdown")

		
def gcodescan(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
			if gcode == T0:
				USB.write("T0")
				#ok\n
				While (ack=="ok"):
				ack=str(USB.readline())
				print(ack)
			elif gcode == T1:
				USB.write("T1")
				#ok\n
				While (ack=="ok"):
				ack=str(USB.readline())
				print(ack)
			elif gcode == T2:
				USB.write("T2")
				#ok\n
				While (ack=="ok"):
				ack=str(USB.readline())
				print(ack)
			elif gcode == T3:
				USB.write("T3")
				#ok\n
				While (ack=="ok"):
				ack=str(USB.readline())
				print(ack)
			elif gcode == T4:
				USB.write("T4")
				#ok\n
				While (ack=="ok"):
				ack=str(USB.readline())
				print(ack)
			
			

__plugin_name__ = "Prusa MMU2 communication"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Prusa-MMU2-communication()
	
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.gcodescan,
    "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
}