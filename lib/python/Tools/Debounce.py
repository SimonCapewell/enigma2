from enigma import eTimer

def debounce(delayMs):
	def decorator(func):
		def debounced(*args, **kwargs):
			if kwargs.get("immediate", None):
				kwargs.pop("immediate")
				func(*args, **kwargs)
				return
			def callIt():
				func(*args, **kwargs)
			if not hasattr(debounced, "timer"):
				debounced.timer = eTimer()
				debounced.timer.callback.append(callIt)
			debounced.timer.start(delayMs, True)

		return debounced
	return decorator
