from anna_lib.selenium import events
from anna_lib.abstract_task import AbstractTask


class SwitchTo(AbstractTask):
	def execute(self):
		events.switch_to(self.driver, {'target': '#test-switch-to'})
