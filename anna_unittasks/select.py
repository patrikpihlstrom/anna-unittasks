from anna_lib.selenium import events
from anna_lib.abstract_task import AbstractTask


class Select(AbstractTask):
	def before_execute(self):
		pass

	def execute(self):
		events.click(self.driver, {'target': {'type': 'xpath', 'value': '//select[@name="xpath"]/option[@value="option"]'}})
