import numpy as np
from time import time
from sklearn.neighbors import KNeighborsClassifier
from loguru import logger

def execute_experiment(params):
    m = params['m']
    n = params['n']
    algorithm = params['algorithm']
    iters = params['iters']
    
    rng = np.random.RandomState(42)
    X = rng.uniform(0, 1, (n, m))
    y = rng.randint(0, 2, n)  
    
    fit_perfs = []
    inf_perfs = []
    
    for _ in range(iters):
        model = KNeighborsClassifier(algorithm=algorithm, n_jobs=-1)
        
        fit_perf_start = time()
        model.fit(X, y)
        fit_perf_end = time()
        fit_perfs.append((fit_perf_end - fit_perf_start) * 1e3)  # Convert to milliseconds
        
        inf_perf_start = time()
        model.predict(X)
        inf_perf_end = time()
        inf_perfs.append((inf_perf_end - inf_perf_start) * 1e3)  # Convert to milliseconds

    mean_fit = np.mean(fit_perfs)
    std_fit = np.std(fit_perfs)
    mean_inf = np.mean(inf_perfs)
    std_inf = np.std(inf_perfs)

    print("\n===== Experiment Parameters =====")
    print(f"{'Number of samples':<25}: {m}")
    print(f"{'Number of features':<25}: {n}")
    print(f"{'Number of iterations':<25}: {iters}")
    print(f"{'Algorithm':<25}: {algorithm}")

    print("\n===== Performance Statistics =====")
    print(f"{'Fit Time (Mean)':<25}: {mean_fit:7.3f} ms")
    print(f"{'Fit Time (Std Dev)':<25}: {std_fit:7.3f} ms")
    print(f"{'Inference Time (Mean)':<25}: {mean_inf:7.3f} ms")
    print(f"{'Inference Time (Std Dev)':<25}: {std_inf:7.3f} ms")

if __name__ == "__main__":
    params = {
        "m": 20000,
        "n": 50,
        "algorithm": "brute",
        "iters": 500
    }
    
    execute_experiment(params)
