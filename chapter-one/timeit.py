import timeit
import cProfile


def main():
    timeit.timeit("x = 2 + 2")
    timeit.timeit("x = sum(range(10))")


if __name__ == "__main__":
    main()
    cProfile.run('main()')