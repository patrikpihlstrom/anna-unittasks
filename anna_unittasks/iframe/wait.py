from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class Wait(AbstractTask):
	def execute(self):
		events.scroll_to(self.driver, {'target': '#iframe-test-wait'})
		events.click(self.driver, {'target': '#iframe-test-wait'})
		events.wait(self.driver, {'target': '#iframe-test-wait-get'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '#iframe-test-wait-get'}))
		super().after_execute()
