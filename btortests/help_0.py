from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        line = p.apply_async(f, args=(2,)).get()
        print(line)