import numpy as np

def simulated_annealing(threshold_range, fitness_fn, n_iterations, seed, 
                        initial_temp, cooling_rate):
    rng = np.random.default_rng(seed)
    current_threshold = rng.uniform(*threshold_range)
    current_fitness = fitness_fn(current_threshold)
    
    best_threshold, best_fitness = current_threshold, current_fitness
    history = []
    
    temp = initial_temp
    for i in range(n_iterations):
        print("-"*40)
        print(f"Current Iteration: {i}")
        
        # Neighborhood: perturb threshold slightly
        proposed_threshold = np.clip(
            current_threshold + rng.normal(scale=0.05), 
            *threshold_range
        )
        
        proposed_fitness = fitness_fn(proposed_threshold)
        delta = proposed_fitness - current_fitness
        
        # Acceptance probability
        if delta > 0 or np.exp(delta / temp) > rng.random():
            current_threshold, current_fitness = proposed_threshold, proposed_fitness
            accepted = True
        else:
            accepted = False
            
        if current_fitness > best_fitness:
            best_threshold, best_fitness = current_threshold, current_fitness
            
        history.append({'iter': i, 'threshold': current_threshold, 
                        'fitness': current_fitness, 'accepted': accepted})
        
        temp *= cooling_rate
        
    return {'best_threshold': best_threshold, 'best_fitness': best_fitness, 'history': history}