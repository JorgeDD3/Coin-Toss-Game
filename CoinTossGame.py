import random

def simulate_game(n):
    # a sequence of n coin tosses
    tosses = ''.join(random.choice(['H', 'T']) for _ in range(n))
    alice_point = tosses.count("HH")
    bob_point = tosses.count("HT")
    
    if alice_point > bob_point:
        return "Alice"
    elif bob_point > alice_point:
        return "Bob"
    else:
        return "Tie"

def calc_prob(n, simulations=10000):
    results = {"Alice": 0, "Bob": 0, "Tie": 0}
    
    for _ in range(simulations):
        result = simulate_game(n)
        results[result] += 1
    
    # Calculate probabilities
    prob_alice = results["Alice"] / simulations
    prob_bob = results["Bob"] / simulations
    prob_tie = results["Tie"] / simulations
    
    return prob_alice, prob_bob, prob_tie

# Calculate probabilities for n = 2, 3, 4, and 5
for n in range(2, 6):
    p_alice, p_bob, p_tie = calc_prob(n)
    print(f"n = {n}: P(Alice wins) = {p_alice:.4f}, P(Bob wins) = {p_bob:.4f}, P(Tie) = {p_tie:.4f}")

# Calculate probabilities for n = 1024
n_big = 1024
p_alice_big, p_bob_big, p_tie_big = calc_prob(n_big)
print(f"n = {n_big}: P(Alice wins) = {p_alice_big:.4f}, P(Bob wins) = {p_bob_big:.4f}, P(Tie) = {p_tie_big:.4f}")

