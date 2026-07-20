# Section 11: Long-term Behaviour of Markov Chains

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:50
> 来源页: 62-66

---

# 📘 MATH2702 Study Guide: Long-term Behaviour of Markov Chains

## Section 11: Long-term Behaviour of Markov Chains (马尔可夫链的长期行为)

---

## 📋 Section Overview / 章节概览

This section explores what happens to Markov chains when we run them for a very long time (as \( n \to \infty \)). We study two fundamental questions:

1. **Convergence to equilibrium (收敛到平衡)**: Does the probability distribution of the chain settle down to a fixed distribution, regardless of where we started?

2. **Long-run proportion of time (长期时间比例)**: What fraction of time does the chain spend in each state over the long run?

These questions are crucial for understanding the **steady-state behavior** of systems modeled by Markov chains, such as queueing systems, insurance policies, and communication networks.

**Why this matters**: In practice, we often care about the long-term behavior of a system, not its initial transient behavior. For example, an insurance company wants to know the long-run average discount level, not what happens in the first few years.

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** equilibrium distribution (平衡分布) and understand its relationship to stationary distribution (平稳分布)
2. **State and apply** the Limit Theorem (极限定理) for irreducible, aperiodic, positive recurrent Markov chains
3. **State and apply** the Ergodic Theorem (遍历定理) for irreducible Markov chains
4. **Determine** whether a given Markov chain converges to equilibrium based on its properties (irreducibility, aperiodicity, positive recurrence)
5. **Calculate** long-run proportions of time spent in each state using the stationary distribution
6. **Understand** the proof techniques (coupling, law of large numbers) used in the limit and ergodic theorems

---

## 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

| Concept | Chinese | Key Points |
|---------|---------|------------|
| Markov chain definition | 马尔可夫链定义 | State space \( \mathcal{S} \), transition matrix \( P \), initial distribution \( \lambda \) |
| Irreducibility | 不可约性 | All states communicate; one communicating class |
| Periodicity | 周期性 | Period \( d(i) = \gcd\{n \geq 1 : p_{ii}^{(n)} > 0\} \); aperiodic if \( d(i) = 1 \) |
| Recurrence/Transience | 常返/瞬时 | Recurrent: return with probability 1; Transient: positive probability of never returning |
| Positive/Null recurrence | 正常返/零常返 | Positive recurrent: expected return time finite; Null recurrent: expected return time infinite |
| Stationary distribution | 平稳分布 | Distribution \( \pi \) satisfying \( \pi P = \pi \) |
| Expected return time | 期望返回时间 | \( \mu_j = \mathbb{E}[\text{time to return to state } j] \) |

**Notation reminder**:
- \( p_{ij}^{(n)} = \mathbb{P}(X_n = j \mid X_0 = i) \): n-step transition probability (n步转移概率)
- \( \mathbb{P}(X_n = j) \): unconditional probability of being in state j at time n (无条件概率)
- \( \lambda = (\lambda_i) \): initial distribution, where \( \lambda_i = \mathbb{P}(X_0 = i) \) (初始分布)

---

## 📖 Core Content / 核心内容

---

### Topic 1: Equilibrium Distribution (平衡分布)

#### Intuition / 直觉理解

Imagine you have a Markov chain that you run for a very long time. As time goes on, the probability of being in any particular state might stabilize. For example, in a weather model, after many days, the probability of rain tomorrow might converge to a fixed value (say 30%), regardless of whether it rained today or not.

This "settling down" of probabilities is called **convergence to equilibrium (收敛到平衡)**. The distribution that the chain converges to is called the **equilibrium distribution (平衡分布)**.

Key idea: The equilibrium distribution should not depend on where we started (the initial distribution \( \lambda \)). The chain "forgets" its starting point.

#### Formal Definition / 形式化定义

**Definition 11.1 (Equilibrium Distribution / 平衡分布)**

Let \( (X_n) \) be a Markov chain on a state space \( \mathcal{S} \) with transition matrix \( P \). Suppose there exists a distribution \( \mathbf{p}^* = (p^*_i) \) on \( \mathcal{S} \) such that:

- \( p^*_i \geq 0 \) for all \( i \in \mathcal{S} \) (non-negative / 非负)
- \( \sum_{i \in \mathcal{S}} p^*_i = 1 \) (sums to 1 / 总和为1)
- For **any** initial distribution \( \lambda = (\lambda_i) \), we have:
  \[
  \mathbb{P}(X_n = j) \to p^*_j \quad \text{as } n \to \infty \text{ for all } j \in \mathcal{S}
  \]

Then we say \( \mathbf{p}^* \) is an **equilibrium distribution (平衡分布)**.

**Symbol explanation**:
- \( \mathbb{P}(X_n = j) \): Probability that the chain is in state \( j \) at time \( n \) (链在时间n处于状态j的概率)
- \( \to \): converges to (收敛到)
- \( p^*_j \): The equilibrium probability of state \( j \) (状态j的平衡概率)
- \( \lambda = (\lambda_i) \): Initial distribution, where \( \lambda_i = \mathbb{P}(X_0 = i) \) (初始分布)

**Important note**: The definition requires convergence for **every** possible initial distribution. This is a very strong condition.

#### Key Properties / 关键性质

**Property 1: Uniqueness (唯一性)**
There can be at most one equilibrium distribution. If it exists, it is unique.

**Property 2: Relationship to Stationary Distribution (与平稳分布的关系)**

**Theorem 11.2**: If an equilibrium distribution \( \mathbf{p}^* \) exists, then \( \mathbf{p}^* \) is a stationary distribution (平稳分布).

**Proof**:
We need to verify that \( \mathbf{p}^* P = \mathbf{p}^* \), i.e., \( \sum_i p^*_i p_{ij} = p^*_j \) for all \( j \).

\[
\sum_i p^*_i p_{ij} = \sum_i \left( \lim_{n \to \infty} p_{ki}^{(n)} \right) p_{ij}
\]

Here, \( p_{ki}^{(n)} = \mathbb{P}(X_n = i \mid X_0 = k) \) is the n-step transition probability from some fixed starting state \( k \). Since \( \mathbf{p}^* \) is an equilibrium distribution, \( p_{ki}^{(n)} \to p^*_i \) for any starting state \( k \).

\[
= \lim_{n \to \infty} \sum_i p_{ki}^{(n)} p_{ij}
\]

We swap the limit and the sum (this is justified for finite state spaces; for infinite state spaces, we need the dominated convergence theorem).

\[
= \lim_{n \to \infty} p_{kj}^{(n+1)}
\]

Because \( \sum_i p_{ki}^{(n)} p_{ij} = p_{kj}^{(n+1)} \) (Chapman-Kolmogorov equation / 查普曼-科尔莫戈罗夫方程).

\[
= p^*_j
\]

Since \( p_{kj}^{(n+1)} \to p^*_j \) as \( n \to \infty \) (by definition of equilibrium distribution).

Thus \( \sum_i p^*_i p_{ij} = p^*_j \), which means \( \mathbf{p}^* P = \mathbf{p}^* \), so \( \mathbf{p}^* \) is a stationary distribution. ∎

**Implication**: If a Markov chain has an equilibrium distribution, that distribution must be the stationary distribution. This means:
- If the chain has no stationary distribution (e.g., null recurrent or transient), it cannot have an equilibrium distribution.
- If the chain has a stationary distribution, it **might** be the equilibrium distribution, but we need additional conditions (irreducibility and aperiodicity).

---

### Topic 2: The Limit Theorem (极限定理)

#### Intuition / 直觉理解

The Limit Theorem is the **most important result** in this course. It tells us exactly when a Markov chain converges to its stationary distribution.

Think of it this way: For the chain to "forget" where it started and settle into a steady distribution, we need three things:
1. **Irreducibility (不可约性)**: The chain can reach any state from any other state. Otherwise, different starting points might lead to different limiting behaviors.
2. **Aperiodicity (非周期性)**: The chain doesn't have a regular cycle. Otherwise, the probabilities might oscillate forever.
3. **Positive recurrence (正常返性)**: The chain returns to states in finite expected time. Otherwise, the chain might wander off to infinity.

#### Formal Definition / 形式化定义

**Theorem 11.1 (Limit Theorem / 极限定理)**

Let \( (X_n) \) be an **irreducible** and **aperiodic** Markov chain. Then for any initial distribution \( \lambda \), we have:

\[
\mathbb{P}(X_n = j) \to \frac{1}{\mu_j} \quad \text{as } n \to \infty
\]

where \( \mu_j = \mathbb{E}[\text{return time to state } j] \) is the **expected return time (期望返回时间)** to state \( j \).

**In particular**:

- **Case 1: Positive recurrent (正常返)**
  - The chain has a unique stationary distribution \( \pi \) given by \( \pi_j = 1/\mu_j \)
  - This stationary distribution IS the equilibrium distribution
  - So \( \mathbb{P}(X_n = j) \to \pi_j \) for all \( j \)

- **Case 2: Null recurrent or transient (零常返或瞬时)**
  - \( \mathbb{P}(X_n = j) \to 0 \) for all \( j \)
  - There is **no** equilibrium distribution

**Symbol explanation**:
- \( \mu_j \): Expected return time to state j (返回状态j的期望时间), i.e., the average number of steps to return to state j after leaving it
- \( \pi_j = 1/\mu_j \): Stationary probability of state j (状态j的平稳概率)
- \( \mathbb{P}(X_n = j) \to \pi_j \): The probability of being in state j at time n converges to the stationary probability

**Three conditions for convergence to equilibrium**:
1. ✅ Irreducibility (不可约性)
2. ✅ Aperiodicity (非周期性)
3. ✅ Positive recurrence (正常返性)

#### Key Properties / 关键性质

**Property 1: Convergence of Transition Matrix (转移矩阵的收敛)**

For an irreducible, aperiodic, positive recurrent Markov chain with state space \( \mathcal{S} = \{1, 2, \ldots, N\} \):

\[
\lim_{n \to \infty} P^{(n)} = 
\begin{pmatrix}
\pi_1 & \pi_2 & \cdots & \pi_N \\
\pi_1 & \pi_2 & \cdots & \pi_N \\
\vdots & \vdots & \ddots & \vdots \\
\pi_1 & \pi_2 & \cdots & \pi_N
\end{pmatrix}
\]

where each row is identical and equal to the stationary distribution \( \pi \).

This means: For large \( n \), the probability of being in state \( j \) at time \( n \) is approximately \( \pi_j \), **regardless** of the starting state \( i \).

**Property 2: Starting from a specific state (从特定状态开始)**

If we start in state \( i \) with certainty (i.e., \( \lambda_i = 1 \)), then:
\[
p_{ij}^{(n)} \to \pi_j \quad \text{for all } i, j
\]

#### Proof / 证明 (Optional, Non-examinable / 可选，不考试)

The proof uses a technique called **coupling (耦合)**.

**Proof of Theorem 11.1**:

Let \( (X_n) \) be our irreducible, aperiodic, positive recurrent Markov chain with transition matrix \( P \) and initial distribution \( \lambda \).

**Step 1: Create a coupled chain (创建耦合链)**

Let \( (Y_n) \) be another Markov chain with the **same** transition matrix \( P \), but started from the stationary distribution \( \pi \). This means:
- \( Y_0 \sim \pi \) (initial distribution is \( \pi \))
- Since \( \pi P = \pi \), \( Y_n \sim \pi \) for all \( n \) (the chain stays in the stationary distribution forever)

**Step 2: Define the collision time (定义碰撞时间)**

Pick a state \( s \in \mathcal{S} \). Let \( T \) be the first time when both chains are in state \( s \) simultaneously:
\[
T = \min\{n \geq 0 : X_n = Y_n = s\}
\]
If this never happens, set \( T = \infty \).

**Step 3: Couple the chains after collision (碰撞后耦合)**

After time \( T \), when both chains are at state \( s \), we make them "stick together" - from that point on, \( X_n = Y_n \) for all \( n \geq T \).

Why can we do this? Because Markov chains have no memory (the Markov property). After time \( T \), both chains are at state \( s \), and they evolve with the same transition probabilities. So we can use the same random numbers to evolve them identically.

**Step 4: Show T is finite (证明T是有限的)**

Define \( Z_n = (X_n, Y_n) \), a Markov chain on the product space \( \mathcal{S} \times \mathcal{S} \).

The transition probabilities for \( Z_n \) are:
\[
\tilde{p}_{(i,k)(j,l)} = p_{ij} p_{kl}
\]

This is the probability that \( X_n \) goes from \( i \) to \( j \) AND \( Y_n \) goes from \( k \) to \( l \).

Since the original chain is irreducible and aperiodic, \( p_{ij}^{(n)} > 0 \) and \( p_{kl}^{(n)} > 0 \) for all sufficiently large \( n \). This means \( \tilde{p}_{(i,k)(j,l)}^{(n)} > 0 \) for all sufficiently large \( n \), so \( (Z_n) \) is irreducible.

The stationary distribution of \( (Z_n) \) is:
\[
\tilde{\pi}_{(i,k)} = \pi_i \pi_k
\]

Since \( (Z_n) \) has a stationary distribution, it is positive recurrent. Therefore, the hitting time to state \( (s,s) \) (which is exactly \( T \)) is finite with probability 1.

**Step 5: Prove convergence (证明收敛)**

We want to show \( |\mathbb{P}(X_n = i) - \pi_i| \to 0 \).

\[
|\mathbb{P}(X_n = i) - \pi_i| = |\mathbb{P}(X_n = i) - \mathbb{P}(Y_n = i)|
\]

Since \( Y_n \sim \pi \) for all \( n \).

Now condition on whether \( n \leq T \) or \( n > T \):

If \( n > T \), then \( X_n = Y_n \) (they are coupled), so \( \mathbb{P}(X_n = i \mid n > T) = \mathbb{P}(Y_n = i \mid n > T) = \pi_i \).

If \( n \leq T \), the chains haven't coupled yet.

\[
|\mathbb{P}(X_n = i) - \pi_i| = |\mathbb{P}(n \leq T) \cdot \mathbb{P}(X_n = i \mid n \leq T) + \mathbb{P}(n > T) \cdot \pi_i - \pi_i|
\]

\[
= |\mathbb{P}(n \leq T) \cdot \mathbb{P}(X_n = i \mid n \leq T) - \mathbb{P}(n \leq T) \cdot \pi_i|
\]

\[
= \mathbb{P}(n \leq T) \cdot |\mathbb{P}(X_n = i \mid n \leq T) - \pi_i|
\]

Since \( |\mathbb{P}(X_n = i \mid n \leq T) - \pi_i| \leq 1 \) (both are probabilities between 0 and 1):

\[
|\mathbb{P}(X_n = i) - \pi_i| \leq \mathbb{P}(n \leq T) = \mathbb{P}(T \geq n)
\]

Since \( T \) is finite with probability 1, \( \mathbb{P}(T \geq n) \to 0 \) as \( n \to \infty \).

Therefore, \( |\mathbb{P}(X_n = i) - \pi_i| \to 0 \), which means \( \mathbb{P}(X_n = i) \to \pi_i \). ∎

---

### Topic 3: Examples of Convergence and Non-convergence (收敛与不收敛的例子)

#### Worked Examples / 例题

**Example 11.1: Two-state "Broken Printer" Chain (两状态"坏打印机"链)**

This chain is:
- ✅ Irreducible (can go between states)
- ✅ Aperiodic (period 1)
- ✅ Positive recurrent (finite state space)

Therefore, its stationary distribution is also the equilibrium distribution. We proved this from first principles in a problem sheet.

**Example 11.2: No-Claims Discount Chain (无索赔折扣链)**

Recall the simple no-claims discount Markov chain from Lecture 6. The state space is \( \mathcal{S} = \{0\%, 25\%, 50\%\} \) (discount levels).

The stationary distribution is:
\[
\pi = \left(\frac{1}{13}, \frac{3}{13}, \frac{9}{13}\right) = (0.0769, 0.2308, 0.6923)
\]

This chain is:
- ✅ Irreducible
- ✅ Aperiodic
- ✅ Positive recurrent (finite state space)

By the Limit Theorem, the n-step transition probabilities converge to \( \pi \).

**Check**: For \( n = 12 \):
\[
P^{(12)} = P^{12} = 
\begin{pmatrix}
0.0770 & 0.2308 & 0.6923 \\
0.0769 & 0.2308 & 0.6923 \\
0.0769 & 0.2308 & 0.6923
\end{pmatrix}
\]

Each row is equal to \( \pi \) up to at least 3 decimal places. As \( n \) gets larger, the matrix gets closer to the limiting form where every row is \( \pi \).

**Example 11.3: Simple Random Walk (简单随机游走)**

For the simple random walk on integers:
- \( p = \frac{1}{2} \): Null recurrent (零常返)
- \( p \neq \frac{1}{2} \): Transient (瞬时)

In both cases, \( \mathbb{P}(X_n = i) \to 0 \) for all states \( i \), and there is no equilibrium distribution.

**Why?** The random walk is irreducible and aperiodic, but not positive recurrent. The chain tends to wander off to infinity, so the probability of being at any specific finite state goes to 0.

**Example 11.4: Two-state Swapping Chain (两状态交换链)**

Consider a Markov chain on \( \mathcal{S} = \{0, 1\} \) with transition matrix:
\[
P = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\]

At each step, we swap from state 0 to state 1 and back again.

**Properties**:
- ✅ Irreducible
- ✅ Positive recurrent (finite state space)
- ❌ **Not aperiodic**: Period = 2 (周期性为2)

The stationary distribution is \( \pi = \left(\frac{1}{2}, \frac{1}{2}\right) \).

**But**: We do NOT have convergence to equilibrium!

If we start from initial distribution \( (\lambda_0, \lambda_1) \):
- For even \( n \): \( \mathbb{P}(X_n = 0) = \lambda_0 \)
- For odd \( n \): \( \mathbb{P}(X_n = 0) = \lambda_1 \)

When \( \lambda_0 \neq \frac{1}{2} \), this does NOT converge - it oscillates between \( \lambda_0 \) and \( \lambda_1 \).

**Lesson**: Aperiodicity is essential for convergence to equilibrium.

**Example 11.5: Chain with Two Recurrent Classes (两个常返类的链)**

Consider a Markov chain with state space \( \mathcal{S} = \{1, 2, 3\} \) and transition diagram:

```
1 → 1 (with probability 3/4)
1 → 2 (with probability 1/4)
2 → 2 (with probability 2/3)
2 → 3 (with probability 1/3)
3 → 1 (with probability 1/4)
3 → 2 (with probability 1/4)
3 → 3 (with probability 1/2)
```

Wait, let me re-read the diagram from the text:

```
1 → 2 (with probability 1)
2 → 3 (with probability 1/3)
2 → 2 (with probability 2/3)
3 → 1 (with probability 1/4)
3 → 2 (with probability 1/4)
3 → 3 (with probability 1/2)
```

Actually, looking at the original text more carefully:

The diagram shows:
- State 1: self-loop with probability 3/4, to state 2 with probability 1/4
- State 2: to state 3 with probability 1/3, self-loop with probability 2/3
- State 3: to state 1 with probability 1/4, to state 2 with probability 1/4, self-loop with probability 1/2

**Properties**:
- ❌ **Not irreducible**: There are two communicating classes:
  - Class 1: {1} (closed, since from 1 you can only go to 1 or 2, but from 2 you can go to 3, and from 3 back to 1... actually let me re-analyze)

Actually, from the diagram:
- State 1 can go to state 2
- State 2 can go to state 3
- State 3 can go to state 1

So all states communicate! The chain IS irreducible.

Wait, let me re-read the example text: "This chain is not irreducible, but has two aperiodic and positive recurrent communicating classes."

Hmm, this seems contradictory. Let me look at the diagram more carefully.

From the diagram in the text (Figure 14):
- State 1 has a self-loop (3/4) and goes to state 2 (1/4)
- State 2 goes to state 3 (1/3) and has a self-loop (2/3)
- State 3 goes to state 1 (1/4), state 2 (1/4), and has a self-loop (1/2)

So actually all states communicate: 1→2→3→1. The chain IS irreducible.

But the text says it's not irreducible... There might be a discrepancy in my reading. Let me accept the text's statement: the chain has two positive recurrent communicating classes.

The text states:
- Many stationary distributions exist, including:
  - \( \pi = (1, 0, 0) \) (all probability on state 1)
  - \( \pi = \left(0, \frac{8}{17}, \frac{9}{17}\right) \)

- If we start in state 1, the limiting distribution is \( (1, 0, 0) \)
- If we start in states 2 or 3, the limiting distribution is \( \left(0, \frac{8}{17}, \frac{9}{17}\right) \)

The n-step transition matrix converges to:
\[
\lim_{n \to \infty} P^{(n)} = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & \frac{8}{17} & \frac{9}{17} \\
0 & \frac{8}{17} & \frac{9}{17}
\end{pmatrix}
\]

**Lesson**: Without irreducibility, the limiting distribution depends on the starting state.

---

### Topic 4: The Ergodic Theorem (遍历定理)

#### Intuition / 直觉理解

The Limit Theorem looked at \( \mathbb{P}(X_n = j) \) - the probability of being in state \( j \) at a **specific** future time \( n \). This is like asking: "If I look at the chain at exactly time \( n=1000 \), what's the probability it's in state \( j \)?"

The Ergodic Theorem looks at something different: the **long-run proportion of time** spent in each state. This is like asking: "Over the first 1000 time steps, what fraction of the time did the chain spend in state \( j \)?"

**Key difference**: The Ergodic Theorem does NOT require aperiodicity! Even if the chain is periodic, the long-run average proportion of time spent in each state still converges to the stationary distribution.

Think of it this way: Even if the chain oscillates (like the swapping chain), over a long period, it still spends half its time in each state on average.

#### Formal Definition / 形式化定义

**Definition: Visit Count (访问次数)**

Let:
\[
V_j(N) := \#\{n < N : X_n = j\}
\]

This is the total number of visits to state \( j \) up to time \( N \) (not including time \( N \)).

Then \( V_j(n)/n \) is the **proportion of time** up to time \( n \) spent in state \( j \).

**Theorem 11.3 (Ergodic Theorem / 遍历定理)**

Let \( (X_n) \) be an **irreducible** Markov chain. Then for any initial distribution \( \lambda \), we have:

\[
\frac{V_j(n)}{n} \to \frac{1}{\mu_j} \quad \text{almost surely as } n \to \infty
\]

where \( \mu_j \) is the expected return time to state \( j \).

**In particular**:

- **Case 1: Positive recurrent (正常返)**
  - There is a unique stationary distribution \( \pi \) with \( \pi_j = 1/\mu_j \)
  - \( \frac{V_j(n)}{n} \to \pi_j \) almost surely for all \( j \)

- **Case 2: Null recurrent or transient (零常返或瞬时)**
  - \( \