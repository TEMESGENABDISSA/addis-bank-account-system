import heapq


class PaymentQueue:
    def __init__(self):
        self.queue = []

    def add_payment(self, priority, payment):
        heapq.heappush(
            self.queue,
            (priority, payment)
        )

    def process_payment(self):
        if not self.queue:
            return None

        return heapq.heappop(self.queue)