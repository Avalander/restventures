import unittest

from actions import ActionHandler

class TestActionHandler(unittest.TestCase):
	def test_handler_should_register_handler(self):
		handler = ActionHandler()
		@handler.handler('some_handler')
		def some_handler():
			pass

		self.assertIs(some_handler, handler._handlers['some_handler'])

	def test_should_call_handler(self):
		handler = ActionHandler()
		@handler.handler('some_handler')
		def some_handler():
			return 1

		actual = handler('some_handler')
		self.assertEqual(1, actual)

	def test_should_pass_options_to_handler(self):
		handler = ActionHandler()
		@handler.handler('some_handler')
		def some_handler(test):
			return test

		actual = handler('some_handler', {'test': 1})
		self.assertEqual(1, actual)

	def test_should_raise_error_when_no_handler_found(self):
		handler = ActionHandler()

		self.assertRaises(KeyError, lambda: handler('some_handler'))

	def test_concat_should_merge_handlers(self):
		handler_1 = ActionHandler()
		@handler_1.handler('one')
		def one():
			pass
		handler_2 = ActionHandler()
		@handler_2.handler('two')
		def two():
			pass

		actual = handler_1.concat(handler_2)
		self.assertIs(one, actual._handlers['one'])
		self.assertIs(two, actual._handlers['two'])
