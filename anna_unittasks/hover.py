from anna_lib.selenium import assertions, events
from anna_lib.abstract_task import AbstractTask


class Hover(AbstractTask):
	def before_execute(self):
		pass

	def execute(self):
		events.hover(self.driver, {'target': '#test-hover'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.hovered'}))
