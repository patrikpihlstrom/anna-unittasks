from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class Submit(AbstractTask):
	def execute(self):
		events.submit(self.driver, {'target': '#test-submit'})

	def after_execute(self):
		assertions.element_exists(self.driver, {'target': '.submitted'})
