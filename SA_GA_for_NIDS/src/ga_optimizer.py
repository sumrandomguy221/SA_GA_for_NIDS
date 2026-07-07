import numpy as np

def genetic_algorithm(fitness_fn, pop_size, threshold_range,
                      n_generations, crossover_rate, mutation_rate, seed):
    rng = np.random.default_rng(seed)
    
    # Initialize population (each individual is a single scalar threshold value)
    population = rng.uniform(*threshold_range, pop_size)
    history = []
    
    for gen in range(n_generations):
        print("-"*40)
        print(f"Current Generation: {gen}")
        
        fitness_vals = np.array([fitness_fn(thresh) for thresh in population])
        
        # Elitism: keep top 10% (at least 2 individuals)
        n_elite = max(2, int(pop_size * 0.1))
        elite_idx = np.argsort(fitness_vals)[-n_elite:]
        new_population = list(population[elite_idx].copy())
        
        while len(new_population) < pop_size:
            # Select two parents randomly by index
            idx1, idx2 = rng.choice(len(population), size=2, replace=False)
            parent1, parent2 = population[idx1], population[idx2]
            
            # Arithmetic crossover (blending two scalar thresholds)
            if rng.random() < crossover_rate:
                alpha = rng.random()
                child = alpha * parent1 + (1 - alpha) * parent2
            else:
                child = parent1.copy()
                
            # Mutation: small Gaussian perturbation for continuous parameters
            if rng.random() < mutation_rate:
                child += rng.normal(0, 0.02)
                
            new_population.append(np.clip(child, *threshold_range))
            
        population = np.array(new_population)
        
        best_idx = np.argmax(fitness_vals)  # Track where the best individual lives
        history.append({
            'gen': gen, 
            'threshold': float(population[best_idx]),  
            'fitness': float(fitness_vals.max()), 
            'mean_fitness': float(fitness_vals.mean())         
        })
        
    best_idx = np.argmax(fitness_vals)
    return {'best_threshold': float(population[best_idx]), 'best_fitness': float(fitness_vals[best_idx]), 
            'history': history}