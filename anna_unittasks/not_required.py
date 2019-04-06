from anna_lib.selenium import events
from anna_lib.abstract_task import AbstractTask


class NotRequired(AbstractTask):
	def before_execute(self):
		self.required = False

	def execute(self):
		events.click(self.driver, {'target': '.some-element-that-isn\'t-clickable'})

	def after_execute(self):
		super().after_execute()
