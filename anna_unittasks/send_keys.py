from anna_lib.selenium import events, assertions
from anna_lib.abstract_task import AbstractTask


class SendKeys(AbstractTask):
	def execute(self):
		events.send_keys(self.driver, {'target': '#test-send-keys', 'value': 'test_send_keys'})

	def after_execute(self):
		self.result.append(assertions.element_exists(self.driver, {'target': '.test_send_keys'}))
		super().after_execute()
