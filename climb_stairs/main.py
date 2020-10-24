import cProfile, pstats, io

from Profiling import ProfilingTask


def output_profiling(pr, filename: str):
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    pr.dump_stats(filename)


if __name__ == '__main__':
    pr = cProfile.Profile()

    var = ProfilingTask()
    pr.enable()
    print(var.climb_stairs(5) == 8)
    pr.disable()
    output_profiling(pr, 'climb_stairs_5.prof')

    pr = cProfile.Profile()
    pr.enable()
    print(var.climb_stairs(45) == 1836311903)
    pr.disable()
    output_profiling(pr, 'climb_stairs_45.prof')

    pr = cProfile.Profile()
    pr.enable()
    print(var.climb_stairs_cache(5) == 8)
    pr.disable()
    output_profiling(pr, 'climb_stairs_cache_5.prof')

    pr = cProfile.Profile()
    pr.enable()
    print(var.climb_stairs_cache(45) == 1836311903)
    pr.disable()
    output_profiling(pr, 'climb_stairs_cache_45.prof')


