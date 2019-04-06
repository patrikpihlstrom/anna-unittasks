from anna_lib.selenium import assertions, events
from anna_lib.abstract_task import AbstractTask


class Click(AbstractTask):
	def execute(self):
		events.scroll_to(self.driver, {'target': '#iframe-test-click'})
		events.click(self.driver, {'target': '#iframe-test-click'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.iframe-clicked'}))
		super().after_execute()
