from counter import Counter


class CounterLibrary:
    def __init__(self):
        self._counter = Counter()

    def increase_counter(self):
        self._counter.increase()

    def increment_counter_by(self, amount):
        int_amount = int(amount)
        self._counter.increment(int_amount)

    def counter_value_should_be(self, expected):
        int_expected = int(expected)
        if self._counter.value != int_expected:
            raise AssertionError(f"{self._counter.value} != {int_expected}")
        
    def reset_counter(self):
        self.counter.reset()
    def counter_reset_after_one_increment(self):
        self.counter.increase()
        self.counter.reset()
    def counter_reset_after_several_increments(self, amount):
        self.counter.increment(int(amount))
        self.counter.reset()
        
        