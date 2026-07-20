# Section 9: Stationary Distributions

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:49
> 来源页: 51-56

---

# 📘 MATH2702: Markov Chains - Section 9 Study Guide
## Stationary Distributions (平稳分布)

---

## 📋 Section Overview / 章节概览

This section introduces the concept of **stationary distributions (平稳分布)** for Markov chains - probability distributions that remain unchanged as the chain evolves over time. Understanding stationary distributions is crucial because they describe the long-term behavior of Markov chains and answer questions like: "If I run this chain for a very long time, what proportion of time will I spend in each state?"

**Why this matters (为什么重要)**:
- Stationary distributions are the Markov chain equivalent of equilibrium in physics
- They allow us to compute long-run average behavior without simulating the chain
- They are essential for applications in queueing theory, population genetics, and Google's PageRank algorithm

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** a stationary distribution and explain its meaning in both mathematical and intuitive terms
2. **Find** stationary distributions for finite-state Markov chains using the system of equations π = πP
3. **Apply** the three-step method for solving stationary distribution problems
4. **State** Theorem 9.1 on existence and uniqueness conditions
5. **Determine** whether a stationary distribution exists based on chain classification (irreducible, positive recurrent, null recurrent, transient)
6. **Analyze** chains with multiple communicating classes and describe the resulting stationary distributions

---

## 📚 Prerequisites / 前置知识

Before studying this section, you should be comfortable with:

| Concept | Details |
|---------|---------|
| **Markov chains basics** | States, transition probabilities, transition matrix P |
| **Matrix-vector multiplication** | Row vector × matrix multiplication |
| **Irreducibility (不可约性)** | All states communicate with each other |
| **Recurrence and transience (常返性与瞬时性)** | From Section 7 |
| **Positive recurrence (正常返)** | Expected return time is finite |
| **Expected return time μᵢ** | Average time to return to state i |
| **Solving linear equations** | Basic algebra, substitution method |

---

## 📖 Core Content / 核心内容

---

### Topic 1: Definition of Stationary Distribution (平稳分布的定义)

#### Intuition / 直觉理解

Imagine you have a large population of independent Markov chains, all running simultaneously. You start them according to some initial distribution - for example, 30% start in state 0, 70% start in state 1. After one step, you check what proportion of chains are in each state. If those proportions are exactly the same as when you started, then you have found a **stationary distribution**.

**Analogy (类比)**: Think of a well-shuffled deck of cards. No matter how many times you shuffle, the probability of drawing any specific card remains 1/52. The uniform distribution is "stationary" under shuffling.

The key insight: **The chain itself keeps moving** - individual chains jump between states - but the **overall distribution** of where chains are located stays constant.

#### Formal Definition / 形式化定义

**Definition 9.1 (Stationary Distribution)**:
Let $(X_n)$ be a Markov chain on a state space $\mathcal{S}$ with transition matrix $\mathbf{P}$. Let $\pi = (\pi_i)$ be a distribution on $\mathcal{S}$, meaning:
- $\pi_i \geq 0$ for all $i \in \mathcal{S}$ (non-negative probabilities)
- $\sum_{i \in \mathcal{S}} \pi_i = 1$ (total probability equals 1)

We call $\pi$ a **stationary distribution (平稳分布)** if:

$$\pi_j = \sum_{i \in \mathcal{S}} \pi_i p_{ij} \quad \text{for all } j \in \mathcal{S}$$

Or equivalently, in matrix notation:

$$\pi = \pi \mathbf{P}$$

where $\pi$ is a **row vector (行向量)**.

**Symbol Explanation (符号说明)**:
- $\pi_j$: probability of being in state $j$ under the stationary distribution
- $\pi_i$: probability of being in state $i$ under the stationary distribution
- $p_{ij}$: transition probability from state $i$ to state $j$
- $\sum_{i \in \mathcal{S}}$: sum over all states $i$ in the state space
- $\pi = \pi \mathbf{P}$: row vector $\pi$ multiplied by matrix $\mathbf{P}$ equals $\pi$ itself

**Important Note**: The condition $\pi = \pi \mathbf{P}$ means $\pi$ is a **left eigenvector (左特征向量)** of $\mathbf{P}$ with eigenvalue 1.

#### Motivating Example: Two-State Broken Printer (双态故障打印机)

Consider the two-state Markov chain from Lecture 4 with transition diagram:

```
        α
    0 ←----→ 1
    ↑       ↑
    |       |
    1-α    1-β
    |       |
    +-------+
```

**Transition Matrix**:
$$\mathbf{P} = \begin{pmatrix} 1-\alpha & \alpha \\ \beta & 1-\beta \end{pmatrix}$$

**Initial Distribution** (from Problem Sheet 3, Question 3):
$$\lambda_0 = \mathbb{P}(X_0 = 0) = \frac{\beta}{\alpha + \beta}, \quad \lambda_1 = \mathbb{P}(X_0 = 1) = \frac{\alpha}{\alpha + \beta}$$

**Check after one step**:
By conditioning on the initial state:
$$\mathbb{P}(X_1 = 0) = \lambda_0 p_{00} + \lambda_1 p_{10} = \frac{\beta}{\alpha+\beta}(1-\alpha) + \frac{\alpha}{\alpha+\beta}\beta = \frac{\beta}{\alpha+\beta}$$

$$\mathbb{P}(X_1 = 1) = \lambda_0 p_{01} + \lambda_1 p_{11} = \frac{\beta}{\alpha+\beta}\alpha + \frac{\alpha}{\alpha+\beta}(1-\beta) = \frac{\alpha}{\alpha+\beta}$$

**Result**: The distribution after step 1 is exactly the same as the initial distribution! By repeating the calculation, it stays the same after step 2, step 3, and forever.

**Interpretation**: If we start 1000 chains with $\frac{\beta}{\alpha+\beta} \times 1000$ in state 0 and $\frac{\alpha}{\alpha+\beta} \times 1000$ in state 1, then at any future time, approximately $\frac{\beta}{\alpha+\beta} \times 1000$ chains will be in state 0 and $\frac{\alpha}{\alpha+\beta} \times 1000$ in state 1 - but **not necessarily the same individual chains** each time.

---

### Topic 2: Finding a Stationary Distribution (寻找平稳分布)

#### Intuition / 直觉理解

Finding a stationary distribution means solving the system of equations $\pi = \pi \mathbf{P}$. This is a system of linear equations where the unknowns are the $\pi_i$ values. However, because $\pi$ must sum to 1, we have one extra equation (the normalizing condition) that helps us determine the exact values.

**Key Observation**: The equation $\pi = \pi \mathbf{P}$ always gives one **redundant equation (冗余方程)** - meaning there are only $|\mathcal{S}| - 1$ independent equations from the matrix equation, plus the normalizing condition gives the $|\mathcal{S}|$-th equation.

#### The Three-Step Method (三步法)

**Step 1**: Write out $\pi = \pi \mathbf{P}$ coordinate by coordinate. Discard one of the equations.

**Step 2**: Select one of the $\pi_i$ as a **working variable (工作变量)** and treat it as a parameter. Solve the remaining equations in terms of this working variable.

**Step 3**: Substitute the solution into the normalizing condition $\sum_i \pi_i = 1$ to find the working variable, and hence the full solution.

**Optional Check**: Use the discarded equation to verify your answer.

#### Worked Example 1: No-Claims Discount Chain (无索赔折扣链)

Consider the no-claims discount Markov chain from Lecture 5 with state space $\mathcal{S} = \{1, 2, 3\}$ and transition matrix:

$$\mathbf{P} = \begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}$$

**Step 1**: Write $\pi = \pi \mathbf{P}$ coordinate-wise:

$$\pi_1 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2$$
$$\pi_2 = \frac{3}{4}\pi_1 + \frac{1}{4}\pi_3$$
$$\pi_3 = \frac{3}{4}\pi_2 + \frac{3}{4}\pi_3$$

We also have the normalizing condition:
$$\pi_1 + \pi_2 + \pi_3 = 1$$

**Step 2**: Choose $\pi_2$ as our working variable. Discard the second equation (we can discard any one).

From the first equation:
$$\pi_1 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2$$
$$\pi_1 - \frac{1}{4}\pi_1 = \frac{1}{4}\pi_2$$
$$\frac{3}{4}\pi_1 = \frac{1}{4}\pi_2$$
$$\pi_1 = \frac{1}{3}\pi_2$$

From the third equation:
$$\pi_3 = \frac{3}{4}\pi_2 + \frac{3}{4}\pi_3$$
$$\pi_3 - \frac{3}{4}\pi_3 = \frac{3}{4}\pi_2$$
$$\frac{1}{4}\pi_3 = \frac{3}{4}\pi_2$$
$$\pi_3 = 3\pi_2$$

So we have:
$$\pi_1 = \frac{1}{3}\pi_2, \quad \pi_3 = 3\pi_2$$

**Step 3**: Substitute into the normalizing condition:
$$\pi_1 + \pi_2 + \pi_3 = \frac{1}{3}\pi_2 + \pi_2 + 3\pi_2 = \frac{13}{3}\pi_2 = 1$$

Therefore:
$$\pi_2 = \frac{3}{13}$$

Substituting back:
$$\pi_1 = \frac{1}{3} \times \frac{3}{13} = \frac{1}{13}$$
$$\pi_3 = 3 \times \frac{3}{13} = \frac{9}{13}$$

**Solution**:
$$\pi = \left(\frac{1}{13}, \frac{3}{13}, \frac{9}{13}\right)$$

**Check using discarded second equation**:
$$\pi_2 = \frac{3}{4}\pi_1 + \frac{1}{4}\pi_3 = \frac{3}{4} \times \frac{1}{13} + \frac{1}{4} \times \frac{9}{13} = \frac{3}{52} + \frac{9}{52} = \frac{12}{52} = \frac{3}{13}$$
✓ Correct!

#### Worked Example 2 (Example 9.1 from text)

Consider a Markov chain on state space $\mathcal{S} = \{1, 2, 3\}$ with transition matrix:

$$\mathbf{P} = \begin{pmatrix}
\frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\
\frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}$$

**Step 1**: Write $\pi = \pi \mathbf{P}$ coordinate-wise:

$$\pi_1 = \frac{1}{2}\pi_1 + \frac{1}{4}\pi_2$$
$$\pi_2 = \frac{1}{4}\pi_1 + \frac{1}{2}\pi_2 + \frac{1}{4}\pi_3$$
$$\pi_3 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 + \frac{3}{4}\pi_3$$

We choose to discard the third equation.

**Step 2**: Choose $\pi_1$ as our working variable.

From the first equation:
$$\pi_1 = \frac{1}{2}\pi_1 + \frac{1}{4}\pi_2$$
$$\pi_1 - \frac{1}{2}\pi_1 = \frac{1}{4}\pi_2$$
$$\frac{1}{2}\pi_1 = \frac{1}{4}\pi_2$$
$$\pi_2 = 2\pi_1$$

From the second equation:
$$\pi_2 = \frac{1}{4}\pi_1 + \frac{1}{2}\pi_2 + \frac{1}{4}\pi_3$$
Substitute $\pi_2 = 2\pi_1$:
$$2\pi_1 = \frac{1}{4}\pi_1 + \frac{1}{2}(2\pi_1) + \frac{1}{4}\pi_3$$
$$2\pi_1 = \frac{1}{4}\pi_1 + \pi_1 + \frac{1}{4}\pi_3$$
$$2\pi_1 = \frac{5}{4}\pi_1 + \frac{1}{4}\pi_3$$
$$2\pi_1 - \frac{5}{4}\pi_1 = \frac{1}{4}\pi_3$$
$$\frac{3}{4}\pi_1 = \frac{1}{4}\pi_3$$
$$\pi_3 = 3\pi_1$$

So we have:
$$\pi_2 = 2\pi_1, \quad \pi_3 = 3\pi_1$$

**Step 3**: Normalizing condition:
$$\pi_1 + \pi_2 + \pi_3 = \pi_1 + 2\pi_1 + 3\pi_1 = 6\pi_1 = 1$$

Therefore:
$$\pi_1 = \frac{1}{6}$$

Substituting back:
$$\pi_2 = 2 \times \frac{1}{6} = \frac{1}{3}$$
$$\pi_3 = 3 \times \frac{1}{6} = \frac{1}{2}$$

**Solution**:
$$\pi = \left(\frac{1}{6}, \frac{1}{3}, \frac{1}{2}\right)$$

**Check using discarded third equation**:
$$\pi_3 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 + \frac{3}{4}\pi_3 = \frac{1}{4} \times \frac{1}{6} + \frac{1}{4} \times \frac{1}{3} + \frac{3}{4} \times \frac{1}{2}$$
$$= \frac{1}{24} + \frac{2}{24} + \frac{9}{24} = \frac{12}{24} = \frac{1}{2}$$
✓ Correct!

---

### Topic 3: Existence and Uniqueness (存在性与唯一性)

#### Intuition / 直觉理解

Not every Markov chain has a stationary distribution, and some have many. The key factors are:

1. **Irreducibility (不可约性)**: Can we reach any state from any other state?
2. **Positive recurrence (正常返性)**: Is the expected return time to each state finite?

**Analogy**: Think of a stationary distribution as the "equilibrium" of a physical system. Some systems reach a unique equilibrium (irreducible, positive recurrent), some never settle down (transient/null recurrent), and some have multiple possible equilibria depending on initial conditions (multiple closed classes).

#### Theorem 9.1: Existence and Uniqueness Theorem

**Theorem 9.1**: Consider an **irreducible (不可约)** Markov chain.

- **If the Markov chain is positive recurrent (正常返)**: Then a stationary distribution $\pi$ exists, is **unique**, and is given by:
  $$\pi_i = \frac{1}{\mu_i}$$
  where $\mu_i$ is the **expected return time (期望返回时间)** to state $i$.

- **If the Markov chain is null recurrent (零常返) or transient (瞬时)**: Then **no stationary distribution** exists.

**Symbol Explanation**:
- $\pi_i$: stationary probability of state $i$
- $\mu_i = \mathbb{E}[\text{return time to state } i \mid X_0 = i]$: expected number of steps to return to state $i$

#### Application to No-Claims Discount Example

The no-claims discount chain is:
- **Irreducible**: All states communicate (you can go from any discount level to any other)
- **Finite state space**: All finite irreducible chains are positive recurrent

Therefore, the stationary distribution $\pi = (\frac{1}{13}, \frac{3}{13}, \frac{9}{13})$ is **unique**.

From $\pi_i = 1/\mu_i$, we get the expected return times:
- $\mu_1 = 1/\pi_1 = 13$ steps
- $\mu_2 = 1/\pi_2 = 13/3 \approx 4.33$ steps
- $\mu_3 = 1/\pi_3 = 13/9 \approx 1.44$ steps

#### What If the Chain Is Not Irreducible?

If the Markov chain has **more than one communicating class (通信类)**:

| Scenario | Result |
|----------|--------|
| **No positive recurrent classes** | No stationary distribution exists |
| **Exactly one positive recurrent class** | Unique stationary distribution, supported only on that closed class |
| **Multiple positive recurrent classes** | Infinitely many stationary distributions exist |

#### Example 9.2: Simple Random Walk (简单随机游走)

Consider the simple random walk with $p \neq 0, 1$:
- This chain is **irreducible**
- For $p = \frac{1}{2}$: **null recurrent** (expected return time is infinite)
- For $p \neq \frac{1}{2}$: **transient** (probability of return is less than 1)

**Conclusion**: No stationary distribution exists for any $p \neq 0, 1$.

#### Example 9.3: Chain with Two Closed Classes

Consider the Markov chain with transition matrix:

$$\mathbf{P} = \begin{pmatrix}
\frac{1}{2} & \frac{1}{2} & 0 & 0 \\
\frac{1}{2} & \frac{1}{2} & 0 & 0 \\
0 & 0 & \frac{1}{4} & \frac{3}{4} \\
0 & 0 & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}$$

This chain has **two closed positive recurrent classes**: $\{1, 2\}$ and $\{3, 4\}$.

**Solving $\pi = \pi \mathbf{P}$**:

For states 1 and 2:
$$\pi_1 = \frac{1}{2}\pi_1 + \frac{1}{2}\pi_2 \Rightarrow \pi_1 = \pi_2$$
$$\pi_2 = \frac{1}{2}\pi_1 + \frac{1}{2}\pi_2 \Rightarrow \pi_1 = \pi_2$$

For states 3 and 4:
$$\pi_3 = \frac{1}{4}\pi_3 + \frac{1}{2}\pi_4 \Rightarrow 3\pi_3 = 2\pi_4$$
$$\pi_4 = \frac{3}{4}\pi_3 + \frac{1}{2}\pi_4 \Rightarrow 3\pi_3 = 2\pi_4$$

Normalizing condition:
$$\pi_1 + \pi_2 + \pi_3 + \pi_4 = 1$$

Let $\pi_1 + \pi_2 = \alpha$ and $\pi_3 + \pi_4 = 1 - \alpha$, where $0 \leq \alpha \leq 1$.

From $\pi_1 = \pi_2$: $\pi_1 = \pi_2 = \frac{\alpha}{2}$
From $3\pi_3 = 2\pi_4$ and $\pi_3 + \pi_4 = 1 - \alpha$:
$$\pi_3 = \frac{2}{5}(1-\alpha), \quad \pi_4 = \frac{3}{5}(1-\alpha)$$

**General solution**:
$$\pi = \left(\frac{\alpha}{2}, \frac{\alpha}{2}, \frac{2}{5}(1-\alpha), \frac{3}{5}(1-\alpha)\right)$$

for **any** $0 \leq \alpha \leq 1$.

**Conclusion**: There are **infinitely many stationary distributions**, parameterized by $\alpha$.

---

### Topic 4: Proof of Existence and Uniqueness (Optional, Non-Examinable)

#### Intuition / 直觉理解

This proof shows why positive recurrent irreducible Markov chains have a unique stationary distribution. The key idea is to construct a **stationary vector** by counting expected visits to states before returning to a fixed starting state, then normalize by the expected return time.

#### Existence Proof: Every Positive Recurrent Markov Chain Has a Stationary Distribution

**Definition**: A **stationary vector (平稳向量)** $\nu$ satisfies $\nu \mathbf{P} = \nu$ but may not sum to 1.

**Proof**:

**Step 1**: Construct a stationary vector.

Fix an initial state $k$. Let $\nu_i$ be the **expected number of visits to state $i$ before returning to state $k$**:

$$\nu_i = \mathbb{E}\left[\sum_{n=1}^{M_k} \mathbb{1}_{\{X_n = i\}} \mid X_0 = k\right]$$

where $M_k$ is the return time to state $k$ (from Section 7).

This can be written as:
$$\nu_i = \sum_{n=1}^{\infty} \mathbb{P}(X_n = i \text{ and } n \leq M_k \mid X_0 = k)$$

**Note**: $\nu_k = 1$ because the only visit to $k$ is the return itself.

**Step 2**: Show $\nu$ is a stationary vector.

We need to show $\sum_i \nu_i p_{ij} = \nu_j$:

$$\sum_{i \in \mathcal{S}} \nu_i p_{ij} = \sum_{i \in \mathcal{S}} \sum_{n=1}^{\infty} \mathbb{P}(X_n = i \text{ and } n \leq M_k \mid X_0 = k) p_{ij}$$

$$= \sum_{n=1}^{\infty} \sum_{i \in \mathcal{S}} \mathbb{P}(X_n = i \text{ and } X_{n+1} = j \text{ and } n \leq M_k \mid X_0 = k)$$

$$= \sum_{n=1}^{\infty} \mathbb{P}(X_{n+1} = j \text{ and } n \leq M_k \mid X_0 = k)$$

(The exchange of sums is valid because recurrence means $M_k$ is finite with probability 1.)

**Step 3**: Shift the time index.

Instead of counting visits from time 1 to $M_k$, count from time 0 to $M_k - 1$:

$$= \sum_{n=0}^{\infty} \mathbb{P}(X_{n+1} = j \text{ and } n \leq M_k - 1 \mid X_0 = k)$$

$$= \sum_{n+1=1}^{\infty} \mathbb{P}(X_{n+1} = j \text{ and } n+1 \leq M_k \mid X_0 = k)$$

$$= \sum_{n=1}^{\infty} \mathbb{P}(X_n = j \text{ and } n \leq M_k \mid X_0 = k) = \nu_j$$

Therefore, $\nu$ is a stationary vector.

**Step 4**: Normalize to get a stationary distribution.

We need $\sum_i \nu_i$ to be finite. But $\sum_i \nu_i$ is the expected total number of visits to all states before return to $k$, which is exactly the expected return time $\mu_k$.

Since the chain is **positive recurrent**, $\mu_k$ is finite. Therefore:

$$\pi = \frac{1}{\mu_k} \nu$$

is a stationary distribution (it sums to 1).

#### Uniqueness Proof: For Irreducible, Positive Recurrent Chains, $\pi_i = 1/\mu_i$

**Proof** (from Stirzaker, *Elementary Probability*, Section 9.5):

**Step 1**: Recall equations from Section 7.

For expected return time:
$$\mu_k = 1 + \sum_j p_{kj} \eta_{jk} \quad \text{(Equation 6)}$$

For expected hitting times (for $i \neq k$):
$$\eta_{ik} = 1 + \sum_j p_{ij} \eta_{jk} \quad \text{(Equation 7)}$$

where $\eta_{ik}$ is the expected time to hit state $k$ starting from state $i$.

**Step 2**: Multiply Equation 7 by $\pi_i$ and sum over all $i \neq k$:

$$\sum_{i \neq k} \pi_i \eta_{ik} = \sum_{i \neq k} \pi_i + \sum_j \sum_{i \neq k} \pi_i p_{ij} \eta_{jk}$$

Note: $\eta_{kk} = 0$, so the left sum can be over all $i$.

**Step 3**: Multiply Equation 6 by $\pi_k$:

$$\pi_k \mu_k = \pi_k + \sum_j \pi_k p_{kj} \eta_{jk}$$

**Step 4**: Add the two equations:

$$\sum_i \pi_i \eta_{ik} + \pi_k \mu_k = \sum_i \pi_i + \sum_j \sum_i \pi_i p_{ij} \eta_{jk}$$

**Step 5**: Use $\sum_i \pi_i p_{ij} = \pi_j$ (stationarity) and $\sum_i \pi_i = 1$:

$$\sum_i \pi_i \eta_{ik} + \pi_k \mu_k = 1 + \sum_j \pi_j \eta_{jk}$$

**Step 6**: The first term on the left and the last term on the right are equal:
$$\sum_i \pi_i \eta_{ik} = \sum_j \pi_j \eta_{jk}$$

Since the chain is irreducible and positive recurrent, these sums are finite (from