class ProfilingTask:
    cache = {}

    def climb_stairs(self, n: int) -> int:
        """Наивное решение задачи о ступеньках"""
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

    def climb_stairs_cache(self, n: int) -> int:
        """Решение через динамическое программирование"""
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in self.cache.keys():
            self.cache[n] = self.climb_stairs_cache(n - 1) + self.climb_stairs_cache(n - 2)
        return self.cache[n]