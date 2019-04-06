from anna_lib.selenium import assertions, events
from anna_lib.abstract_task import AbstractTask


class CurrentUrl(AbstractTask):
	def before_execute(self):
		super().before_execute()

	def execute(self):
		events.click(self.driver, {'target': '#test-current-url'})

	def after_execute(self):
		self.result.append(assertions.current_url(self.driver, {'in': 'test/switchto'}))
		self.result.append(assertions.current_url(self.driver, {'is': 'http://annahub.se:8000/test/switchto'}))
		super().after_execute()
