# Section 10: Reversibility of Markov Chains

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:50
> 来源页: 57-61

---

# 📘 MATH2702: Markov Chains - Section 10: Reversibility of Markov Chains

## 📋 Section Overview / 章节概览

This section explores a fundamental question: **If we observe a Markov chain running forward in time, does it "look" the same as if we ran it backward?** This property, called **reversibility (可逆性)**, is crucial for understanding the symmetry of Markov chains and has practical applications in queueing theory, statistical physics, and MCMC (Markov Chain Monte Carlo) methods.

We will learn:
- How to define and construct the **time-reversed chain (时间逆转链)**
- The **detailed balance equations (细致平衡方程)** and their relationship to stationarity
- A **graph-theoretic condition** for reversibility
- How to check if a Markov chain is reversible

**Why this matters**: Reversibility simplifies analysis—if a chain is reversible, we can often find its stationary distribution by solving the simpler detailed balance equations instead of the full stationary equations.

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** the time-reversed chain and compute its transition probabilities
2. **State** the detailed balance conditions and explain their relationship to stationarity
3. **Determine** whether a given Markov chain is reversible by checking detailed balance
4. **Solve** the detailed balance equations to find a stationary distribution
5. **Apply** the tree condition to quickly decide reversibility
6. **Identify** when a chain is NOT reversible (counterexamples)

---

## 📚 Prerequisites / 前置知识

Before starting, you should be comfortable with:

- **Markov chain basics**: State space, transition matrix, transition diagram (Sections 1-3)
- **Stationary distribution**: Definition, existence for irreducible positive recurrent chains (Section 9)
- **Expected return time**: μᵢ = expected time to return to state i (Section 9)
- **Probability notation**: Conditional probability ℙ(A|B), joint probability ℙ(A,B)
- **Graph theory basics**: Trees, cycles, connected components

---

## 📖 Core Content / 核心内容

---

### Topic 1: Time Reversal of a Markov Chain / 马尔可夫链的时间逆转

#### Intuition / 直觉理解

Imagine you have a video of a Markov chain running. You watch the sequence of states: x₁ → x₂ → x₃ → ... → xₙ. Now someone asks: "Is this video playing forward or backward?" 

If the chain is **reversible**, you **cannot tell**—the probabilistic behavior looks the same in both directions. If it's **not reversible**, you might notice patterns that only make sense in one direction.

**Analogy**: Think of a random walk on a line. If the walk has equal probability of moving left or right (p = 0.5), it looks the same forward and backward. But if it has a drift (p ≠ 0.5), you can tell the direction because the walk tends to move one way.

#### Formal Definition / 形式化定义

**Definition 10.1 (Time-Reversed Chain)**  
Let (Xₙ)ₙ∈ℕ be a Markov chain on state space 𝒮. For a fixed integer N, define the **reversed chain (逆转链)**:

**Yₙ := X_{N-n}** for n = 0, 1, ..., N

This means:
- (Y₀, Y₁, ..., Yₙ) = (X_N, X_{N-1}, ..., X₀)
- The reversed chain runs backward through the original chain's states

**Theorem 10.1 (Transition Probabilities of the Reversed Chain)**  
Suppose (Xₙ)ₙ∈ℕ is an **irreducible positive recurrent** Markov chain on state space 𝒮, started from its **stationary distribution π**. Then the reversed chain (Yₙ)ₙ₌₀^N is also an irreducible positive recurrent Markov chain with transition probabilities:

**p̂(x, y) = π(y) · p(y, x) / π(x)** for all x, y ∈ 𝒮

where:
- p̂(x, y) = ℙ(Y_{n+1} = y | Y_n = x) = probability that the reversed chain goes from x to y
- p(y, x) = ℙ(X_{n+1} = x | X_n = y) = probability that the original chain goes from y to x
- π(x) = stationary probability of state x
- π(y) = stationary probability of state y

The stationary distribution for Yₙ is also π.

#### Proof / 证明

**Step 1**: Set up the conditional probability we need to compute.

For k < N and a possible sequence of states x₀, x₁, ..., x_k, x_{k+1} ∈ 𝒮:

ℙ(Y_{k+1} = x_{k+1} | Y_k = x_k, ..., Y₁ = x₁, Y₀ = x₀)

**Step 2**: Rewrite in terms of the original chain.

Since Yₙ = X_{N-n}, we have:
- Y_{k+1} = X_{N-(k+1)} = X_{N-k-1}
- Y_k = X_{N-k}
- Y₁ = X_{N-1}
- Y₀ = X_N

So the probability becomes:
ℙ(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k, ..., X_{N-1} = x₁, X_N = x₀)

**Step 3**: Use the "backwards Markov property" (from Problem Sheet 4).

The Markov property says that given the present state, the future is independent of the past. For the reversed chain, this means:

ℙ(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k, ..., X_N = x₀) = ℙ(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k)

**Why?** Because X_{N-k-1} is "in the past" relative to X_{N-k}, but the Markov property works forward in time. However, the "backwards Markov property" (proved in Problem Sheet 4) tells us that the conditional probability depends only on the nearest known state.

**Step 4**: Express as a ratio of probabilities.

ℙ(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k) = ℙ(X_{N-k-1} = x_{k+1}, X_{N-k} = x_k) / ℙ(X_{N-k} = x_k)

**Step 5**: Use stationarity.

Since the chain started from its stationary distribution π, for any time n:
- ℙ(X_n = x) = π(x) for all x ∈ 𝒮
- ℙ(X_{n+1} = y, X_n = x) = π(x) · p(x, y)

Therefore:
ℙ(X_{N-k-1} = x_{k+1}, X_{N-k} = x_k) = π(x_{k+1}) · p(x_{k+1}, x_k)
ℙ(X_{N-k} = x_k) = π(x_k)

**Step 6**: Combine to get the transition probability.

ℙ(Y_{k+1} = x_{k+1} | Y_k = x_k) = π(x_{k+1}) · p(x_{k+1}, x_k) / π(x_k)

This is exactly p̂(x_k, x_{k+1}) as claimed.

**Step 7**: Verify irreducibility and stationarity.

- **Irreducibility**: Since Xₙ is irreducible, for any states x, y there is a path from x to y. The reversed chain can follow this path backward, so it is also irreducible.
- **Stationarity**: Since ℙ(X_n = x) = π(x) for all n, we have ℙ(Y_n = x) = ℙ(X_{N-n} = x) = π(x) for all n = 0, 1, ..., N. Thus π is the stationary distribution for Yₙ.

---

### Topic 2: The Detailed Balance Equations / 细致平衡方程

#### Intuition / 直觉理解

The **detailed balance equations** describe a special kind of equilibrium. Imagine a system where particles move between states. Detailed balance means that for every pair of states (x, y), the **flow** from x to y equals the **flow** from y to x:

- Flow from x to y = π(x) · p(x, y) = probability of being in x × probability of moving to y
- Flow from y to x = π(y) · p(y, x) = probability of being in y × probability of moving to x

When these are equal for **every** pair, the system is in a state of **microscopic reversibility**—each individual transition is balanced by its reverse.

**Contrast with stationarity**: Stationarity only requires that the total flow into each state equals the total flow out. Detailed balance is a stronger condition—it requires pairwise balance.

#### Formal Definition / 形式化定义

**Definition 10.2 (Reversibility / Reversible Markov Chain)**  
Let (Xₙ)ₙ∈ℕ be a Markov chain on state space 𝒮 with transition probabilities p_{xy}. If there exists a probability distribution π on 𝒮 such that Xₙ and π satisfy the **detailed balance conditions (细致平衡条件)**:

**π_x · p_{xy} = π_y · p_{yx}** for all x, y ∈ 𝒮

then we say that Xₙ is **reversible (可逆的)**.

**Notation**:
- π_x = stationary probability of state x (also written π(x))
- p_{xy} = ℙ(X_{n+1} = y | X_n = x) = transition probability from x to y
- p_{yx} = ℙ(X_{n+1} = x | X_n = y) = transition probability from y to x

#### Key Properties / 关键性质

**Corollary 10.1 (Detailed Balance ⇒ Stationarity)**  
Any distribution π that satisfies the detailed balance conditions for a Markov chain Xₙ on 𝒮 with transition probabilities p(x, y) is a **stationary distribution** for Xₙ.

**Proof** (left as an exercise, but here's the idea):
- Sum the detailed balance equation over all y:
  ∑_y π_x · p_{xy} = ∑_y π_y · p_{yx}
- The left side is π_x · ∑_y p_{xy} = π_x · 1 = π_x
- The right side is ∑_y π_y · p_{yx} = (πP)_x
- So π_x = (πP)_x for all x, meaning π is stationary.

**Important**: The converse is NOT true. A stationary distribution does NOT necessarily satisfy detailed balance. We'll see a counterexample in Example 10.2.

#### Worked Example / 例题

**Example 10.1: The Discrete-Time Queue (离散时间队列)**

**Problem**: Consider a queue (等待队列) where at each time step:
- A customer arrives with probability p ∈ (0,1) [Bernoulli(p) arrival]
- If there are customers, one is served with probability q ∈ (0,1] [Bernoulli(q) service]

Let Xₙ = length of the queue at time n. Show that (Xₙ) is a reversible Markov chain and find its stationary distribution.

**Step 1**: Find the transition probabilities.

At each time step, the queue length changes by at most 1 (at most one arrival and at most one departure). So p_{ij} = 0 if |i - j| > 1.

For i > 0 (queue not empty):
- **p_{i,i+1}** (one arrival, no service): p · (1 - q)
- **p_{i,i}** (arrival and service, or no arrival and no service): p·q + (1-p)(1-q)
- **p_{i,i-1}** (no arrival, one service): (1-p) · q

For i = 0 (queue empty):
- **p_{0,0}** (no arrival, no service): (1-p)(1-q)
- **p_{0,1}** (one arrival, no service possible since queue empty): p
- **p_{0,-1}** = 0 (can't have negative queue length)

**Step 2**: Set up the detailed balance equations.

We want to find π such that π_i · p_{ij} = π_j · p_{ji} for all i, j.

Since p_{ij} = 0 for |i-j| > 1, the only non-trivial equations are for adjacent states.

**For i > 0, j = i+1**:
π_i · p_{i,i+1} = π_{i+1} · p_{i+1,i}

Substituting:
π_i · p(1-q) = π_{i+1} · (1-p)q

This gives:
π_{i+1} = [p(1-q)] / [(1-p)q] · π_i

**For i = 0, j = 1**:
π₀ · p_{0,1} = π₁ · p_{1,0}

Substituting:
π₀ · p = π₁ · (1-p)q

This gives:
π₁ = [p] / [(1-p)q] · π₀

**Step 3**: Solve the recurrence.

Let r = [p(1-q)] / [(1-p)q] (the ratio for i > 0)

From the i=0 equation: π₁ = [p/((1-p)q)] · π₀

For i = 1: π₂ = r · π₁ = r · [p/((1-p)q)] · π₀

For i = 2: π₃ = r · π₂ = r² · [p/((1-p)q)] · π₀

In general, for i ≥ 0:
π_{i+1} = r^i · [p/((1-p)q)] · π₀

Or equivalently:
π_{i+1} = [p/(1-p)]^{i+1} · [(1-q)/q]^i · (1/q) · π₀

**Step 4**: Check the normalization condition.

We need ∑_{i≥0} π_i = 1.

π₀ + ∑_{i≥0} π_{i+1} = 1

π₀ + π₀ · [p/((1-p)q)] · ∑_{i≥0} r^i = 1

The geometric series ∑_{i≥0} r^i converges if and only if |r| < 1, i.e.:
p(1-q) < (1-p)q
p - pq < q - pq
p < q

So we need **q > p** (service rate > arrival rate) for a stationary distribution to exist. This makes intuitive sense—if customers arrive faster than they can be served, the queue grows without bound.

**Step 5**: Compute π₀.

∑_{i≥0} r^i = 1/(1-r) = 1 / [1 - p(1-q)/((1-p)q)]

Simplifying:
1 - r = [(1-p)q - p(1-q)] / [(1-p)q] = [q - pq - p + pq] / [(1-p)q] = (q-p) / [(1-p)q]

So ∑_{i≥0} r^i = [(1-p)q] / (q-p)

Now:
π₀ + π₀ · [p/((1-p)q)] · [(1-p)q/(q-p)] = π₀ + π₀ · p/(q-p) = 1

π₀ · [1 + p/(q-p)] = π₀ · [(q-p + p)/(q-p)] = π₀ · [q/(q-p)] = 1

Therefore:
**π₀ = (q-p)/q**

**Step 6**: Write the full stationary distribution.

For i ≥ 0:
π_{i+1} = [p/(1-p)]^{i+1} · [(1-q)/q]^i · (1/q) · (q-p)/q

Simplifying:
π_{i+1} = [p/(1-p)]^{i+1} · [(1-q)/q]^i · (q-p)/q²

**Verification**: The chain is reversible because we found π by solving detailed balance equations.

---

### Topic 3: When Detailed Balance is NOT Necessary / 细致平衡并非必要条件

#### Intuition / 直觉理解

Just because a chain has a stationary distribution doesn't mean it's reversible. Think of a **one-way street** system: traffic might flow in a cycle (A→B→C→A) with equal numbers of cars at each intersection, but the flow from A to B is not balanced by flow from B to A.

#### Worked Example / 例题

**Example 10.2: A Non-Reversible 3-State Chain**

**Problem**: Consider a Markov chain with transition matrix:

P = 
| 0   1   0   |
| 3/4 0   1/4 |
| 1   0   0   |

**Step 1**: Draw the transition diagram.

```
    0 → 1 (probability 1)
    1 → 0 (probability 3/4)
    1 → 2 (probability 1/4)
    2 → 0 (probability 1)
```

**Step 2**: Find the stationary distribution.

Solve π = πP:
- π₀ = 0·π₀ + (3/4)·π₁ + 1·π₂ = (3/4)π₁ + π₂
- π₁ = 1·π₀ + 0·π₁ + 0·π₂ = π₀
- π₂ = 0·π₀ + (1/4)·π₁ + 0·π₂ = (1/4)π₁

From π₁ = π₀ and π₂ = (1/4)π₁ = (1/4)π₀:

Normalization: π₀ + π₁ + π₂ = π₀ + π₀ + (1/4)π₀ = (9/4)π₀ = 1

So: π₀ = 4/9, π₁ = 4/9, π₂ = 1/9

Stationary distribution: **π = (4/9, 4/9, 1/9)**

**Step 3**: Check detailed balance.

Check π₀ · p₀₁ = π₁ · p₁₀:
- Left: π₀ · p₀₁ = (4/9) · 1 = 4/9
- Right: π₁ · p₁₀ = (4/9) · (3/4) = 1/3

4/9 ≠ 1/3, so detailed balance fails.

Check π₁ · p₁₂ = π₂ · p₂₁:
- Left: π₁ · p₁₂ = (4/9) · (1/4) = 1/9
- Right: π₂ · p₂₁ = (1/9) · 0 = 0

1/9 ≠ 0, so detailed balance fails again.

**Conclusion**: The chain has a stationary distribution but is **NOT reversible**.

---

### Topic 4: A Condition for Reversibility / 可逆性的一个条件

#### Intuition / 直觉理解

When is it easy to check reversibility? If the **graph** of the Markov chain (ignoring directions) is a **tree** (no cycles), then the chain is automatically reversible. Why? Because on a tree, there's only one path between any two states, so the flow must balance along each edge.

**Analogy**: Think of water flowing through pipes. If the pipe network has no loops (it's a tree), then at each junction, the flow in must equal the flow out for the system to be in equilibrium. This forces pairwise balance.

#### Formal Definition / 形式化定义

**Definition 10.3 (Graph of a Markov Chain)**  
Let (Xₙ)ₙ∈ℕ be a Markov chain on state space 𝒮. The **graph (图)** of Xₙ is obtained by:
1. Taking the transition diagram of Xₙ
2. Forgetting all directions of edges (making them undirected)
3. Removing multiple edges and self-loops

**Tree (树)**: A simple graph (no multiple edges or self-loops) is a **tree** if it has **no cycles** (no closed loops).

#### Key Lemma / 关键引理

**Lemma 10.1 (Tree ⇒ Reversibility)**  
If the graph of a Markov chain (Xₙ)ₙ∈ℕ with stationary distribution π is a **tree**, then the chain is **reversible**.

**Proof** (non-examinable, but included for understanding):

**Step 1**: Set up the problem.
- Let G = (𝒮, E) be the graph of the Markov chain (a tree).
- π is the stationary distribution.
- We want to show π satisfies detailed balance: π_i · p_{ij} = π_j · p_{ji} for all i, j.

**Step 2**: Handle the trivial case.
- If i and j are NOT connected by an edge, then p_{ij} = p_{ji} = 0 (no direct transition), so detailed balance holds trivially (0 = 0).

**Step 3**: Consider connected states.
- Suppose i and j are connected by an edge.
- Since G is a tree, removing this edge splits the graph into two disjoint components:
  - G₁ = (𝒮₁, E₁) containing i
  - G₂ = (𝒮₂, E₂) containing j

**Step 4**: Use stationarity.
- Stationarity says: ∑_{k∈𝒮} π_k · p_{ki} = π_i = π_i · ∑_{k∈𝒮} p_{ik}
- Sum this over all ℓ ∈ 𝒮₁:
  ∑_{ℓ∈𝒮₁} ∑_{k∈𝒮} π_k · p_{kℓ} = ∑_{ℓ∈𝒮₁} ∑_{k∈𝒮} π_ℓ · p_{ℓk}

**Step 5**: Subtract internal flows.
- Subtract ∑_{ℓ,k∈𝒮₁} π_k · p_{kℓ} from the left side and ∑_{ℓ,k∈𝒮₁} π_ℓ · p_{ℓk} from the right side.
- These are equal (just relabeling indices), so they cancel.
- We get:
  ∑_{ℓ∈𝒮₁} ∑_{k∈𝒮₂} π_ℓ · p_{ℓk} = ∑_{ℓ∈𝒮₁} ∑_{k∈𝒮₂} π_k · p_{kℓ}

**Step 6**: Use the tree structure.
- Since the only edge connecting 𝒮₁ and 𝒮₂ is the edge between i and j, the only non-zero terms in these sums are:
  - Left: ℓ = i, k = j → π_i · p_{ij}
  - Right: ℓ = i, k = j → π_j · p_{ji}
- Therefore: π_i · p_{ij} = π_j · p_{ji}

This is exactly the detailed balance condition. ∎

---

## 🔗 Connections / 知识关联

### Previous Sections
- **Section 9 (Stationary Distribution)**: We learned that irreducible positive recurrent chains have a unique stationary distribution. Now we see that this distribution may or may not satisfy detailed balance.
- **Section 3 (Transition Diagrams)**: The graph of a Markov chain is derived from its transition diagram.

### Future Sections
- **Continuous-time queues**: The discrete-time queue in Example 10.1 prepares us for continuous-time queueing theory.
- **MCMC methods**: Reversibility is a key property for Markov Chain Monte Carlo algorithms (e.g., Metropolis-Hastings).

### Real-World Applications
- **Queueing theory**: Modeling customer service systems
- **Statistical physics**: Detailed balance is fundamental in thermodynamics
- **Machine learning**: Reversible Markov chains are used in sampling algorithms

---

## ⚠️ Common Mistakes / 常见误区

1. **Confusing stationarity with reversibility**
   - ❌ "If a chain has a stationary distribution, it must be reversible."
   - ✅ Stationarity is necessary but NOT sufficient for reversibility. Example 10.2 shows a chain with a stationary distribution that is not reversible.

2. **Forgetting to check all pairs in detailed balance**
   - ❌ Only checking a few pairs and assuming the rest work.
   - ✅ You must verify π_x · p_{xy} = π_y · p_{yx} for ALL x, y ∈ 𝒮.

3. **Misinterpreting the tree condition**
   - ❌ "If the chain is reversible, its graph must be a tree."
   - ✅ The tree condition is SUFFICIENT but NOT necessary. A chain can be reversible even if its graph has cycles (e.g., a random walk on a cycle graph with symmetric probabilities).

4. **Incorrectly computing the reversed chain's transition probabilities**
   - ❌ p̂(x, y) = p(y, x) (forgetting the π ratio)
   - ✅ p̂(x, y) = π(y) · p(y, x) / π(x)

5. **Assuming all reversible chains have the same stationary distribution forward and backward**
   - ✅ Actually, Theorem 10.1 shows they DO have the same stationary distribution, but this is a result, not an assumption.

---

## ✍️ Practice / 练习

### Question 1
Consider a Markov chain with transition matrix:
P = 
| 1/3  2/3  0   |
| 1/6  1/3  1/2 |
| 0    1/3  2/3 |

Find a stationary distribution. Is the chain reversible?

**Hint**: Solve π = πP first, then check detailed balance for at least one pair of states.

---

### Question 2
Consider a Markov chain with state space S = {1, 2, 3, 4} and transition matrix:
P = 
| 1/4  1/2  1/4  0   |
| 1/4  1/4  1/2  0   |
| 1/2  1/2  0    0   |
| 1/4  0    1/4  1/2 |

(a) Draw the transition diagram.
(b) Identify communicating classes.
(c) Find a stationary distribution.
(d) Is the chain reversible?

**Hint**: For (d), check if the graph is a tree first. If not, you'll need to check detailed balance directly.

---

### Question 3
Prove Corollary 10.1: If π satisfies detailed balance for a Markov chain Xₙ, then π is a stationary distribution for Xₙ.

**Hint**: Start with the detailed balance equation π_x · p_{xy} = π_y · p_{yx}. Sum over all y and use the fact that ∑_y p_{xy} = 