from anna_lib.selenium import assertions, events
from anna_lib.abstract_task import AbstractTask


class Click(AbstractTask):
	def before_execute(self):
		pass

	def execute(self):
		events.click(self.driver, {'target': '#test-click'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.clicked'}))
