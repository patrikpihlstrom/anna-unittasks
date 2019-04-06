from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class Wait(AbstractTask):
	def execute(self):
		events.click(self.driver, {'target': '#test-wait'})
		events.wait(self.driver, {'target': '#test-wait-get'})

	def after_execute(self):
		assertions.element_exists(self.driver, {'target': '#test-wait-get'})
