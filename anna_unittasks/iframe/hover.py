from anna_lib.selenium import assertions, events
from anna_lib.abstract_task import AbstractTask


class Hover(AbstractTask):
	def execute(self):
		events.scroll_to(self.driver, {'target': '#iframe-test-hover'})
		events.hover(self.driver, {'target': '#iframe-test-hover'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.iframe-hovered'}))
		super().after_execute()
