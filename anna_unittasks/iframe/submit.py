from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class Submit(AbstractTask):
	def execute(self):
		events.scroll_to(self.driver, {'target': '#iframe-test-submit'})
		events.submit(self.driver, {'target': '#iframe-test-submit'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.iframe-submitted'}))
		super().after_execute()
