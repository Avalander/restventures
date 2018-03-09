class ActionHandler:
	def __init__(self):
		self._handlers = {}

	def handler(self, name=None):
		def inner(fun):
			self._handlers[name or fun.__name__] = fun
			return fun
		return inner

	def __call__(self, name, options):
		return self._handlers[name](**options)

	def concat(self, other):
		new = ActionHandler()
		new._handlers.update(self._handlers)
		new._handlers.update(other._handlers)
		return new
