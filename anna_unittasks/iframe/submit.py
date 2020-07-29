from anna_lib.task.abstract_task import AbstractTask


class Submit(AbstractTask):
	def __execute__(self):
		self.scroll_to('#iframe-test-submit')
		self.submit('#iframe-test-submit')

	def after_execute(self):
		self._assert('element_exists', '.iframe-submitted')
