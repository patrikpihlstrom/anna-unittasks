from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class SendKeys(AbstractTask):
	def execute(self):
		events.click(self.driver, {'target': '#test-send-keys', 'value': 'test_send_keys'})

	def after_execute(self):
		assertions.element_exists(self.driver, {'target': '.test_send_keys'})
