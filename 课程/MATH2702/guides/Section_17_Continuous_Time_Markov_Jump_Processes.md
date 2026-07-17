# Section 17: Continuous Time Markov Jump Processes

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:55
> 来源页: 83-90

---

# MATH2702: Continuous Time Markov Jump Processes
## 连续时间马尔可夫跳跃过程

---

# 📋 Section Overview / 章节概览

This section covers **Continuous Time Markov Jump Processes (连续时间马尔可夫跳跃过程)**, which are stochastic processes that evolve in continuous time over a discrete state space. Unlike discrete-time Markov chains where transitions occur at fixed time steps, these processes wait random amounts of time in each state before "jumping" to another state.

**Why this matters (为什么重要)**:
- Real-world systems often evolve continuously in time (e.g., queue lengths, chemical reactions, population dynamics)
- The Poisson process (泊松过程) is a special case
- These models are fundamental in operations research, biology, physics, and finance

The section covers:
1. **Jump chain and holding times** - the two-component structure
2. **Generator matrix** - the continuous-time analogue of the transition matrix
3. **Forward and backward equations** - differential equations for transition probabilities
4. **Matrix exponential** - the solution method
5. **Explosion** - a technical issue with infinite state spaces

---

# 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** a continuous-time Markov jump process in terms of its jump chain and holding times
2. **Construct** the generator matrix Q from a transition rate diagram
3. **Derive** the jump chain transition matrix R from Q
4. **Calculate** probabilities and expected times using the jump chain and holding times
5. **Formulate** the Kolmogorov forward and backward equations
6. **Compute** transition probabilities using the matrix exponential

---

# 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

| Concept | Details |
|---------|---------|
| **Discrete-time Markov chains (离散时间马尔可夫链)** | Transition matrices, n-step probabilities |
| **Exponential distribution (指数分布)** | PDF: f(t) = λe^{-λt}, memoryless property |
| **Matrix multiplication (矩阵乘法)** | How to multiply matrices |
| **Basic differential equations (基本微分方程)** | First-order ODEs, separation of variables |
| **Taylor series (泰勒级数)** | e^x = 1 + x + x²/2! + ... |
| **Probability theory (概率论)** | Conditional probability, expectation |

---

# 📖 Core Content / 核心内容

---

## Topic 1: Jump Chain and Holding Times / 跳跃链与停留时间

### Intuition / 直觉理解

Imagine you're at a bus station (state i). Several bus routes serve this station:
- Route to state j arrives after an **exponential** time with rate q_{ij}
- Route to state k arrives after an exponential time with rate q_{ik}
- etc.

**Key insight (关键洞察)**: The bus that arrives FIRST determines where you go next. Because exponential distributions are **memoryless (无记忆性)**, the waiting time until ANY bus arrives is also exponential, with rate equal to the SUM of all individual rates.

This gives us a two-step process:
1. **Wait** for an exponential time (holding time)
2. **Jump** to a state chosen according to probabilities proportional to the rates

### Formal Definition / 形式化定义

#### The Generator Matrix Q (生成矩阵 Q)

**Definition**: For a Markov jump process (X(t)) on state space 𝒮, the **transition rates (转移率)** q_{ij} for i ≠ j represent the rate at which the process jumps from state i to state j.

The **generator matrix (生成矩阵)** Q = (q_{ij} : i, j ∈ 𝒮) is defined as:

- **Off-diagonal entries (非对角元)**: q_{ij} ≥ 0 for i ≠ j
  - q_{ij} = 0 means we never jump from i to j
- **Diagonal entries (对角元)**: q_{ii} = -q_i = -∑_{j≠i} q_{ij}
  - These are NEGATIVE (or zero)
  - Each row sums to 0: ∑_j q_{ij} = 0

**Symbol explanation (符号说明)**:
- q_{ij}: transition rate from state i to state j (i→j的转移率)
- q_i = -q_{ii} = ∑_{j≠i} q_{ij}: total rate of leaving state i (离开状态i的总率)
- If q_i = 0 for all j ≠ i, then i is an **absorbing state (吸收态)**

#### The Jump Chain R (跳跃链 R)

**Definition**: The **jump chain (跳跃链)** (Y_n) is a discrete-time Markov chain that records the sequence of states visited, ignoring the timing.

Its transition matrix R = (r_{ij} : i, j ∈ 𝒮) is:

- For states with q_i ≠ 0:
  - r_{ij} = q_{ij}/q_i for j ≠ i (probability of jumping to j)
  - r_{ii} = 0 (cannot stay in same state)
- For absorbing states with q_i = 0:
  - r_{ii} = 1
  - r_{ij} = 0 for j ≠ i

**Symbol explanation (符号说明)**:
- r_{ij}: probability that the jump chain moves from i to j (跳跃链从i到j的概率)
- Note: r_{ij} = q_{ij}/q_i = q_{ij} / ∑_{j≠i} q_{ij}

#### Holding Times (停留时间)

**Definition**: The **holding times (停留时间)** T_1, T_2, ... are the times spent in each state before jumping.

- T_n ∼ Exp(q_{Y_{n-1}})
  - If we are in state i, the holding time is Exp(q_i)
- The holding times are **conditionally independent** given the jump chain (Y_n)

#### The Full Process Definition

**Definition 17.1 (Formal Definition)**:

1. Let 𝒮 be a set (state space), and λ a distribution on 𝒮 (initial distribution)
2. Let Q = (q_{ij}) be a matrix with q_{ij} ≥ 0 for i ≠ j and ∑_j q_{ij} = 0 for all i
   - Write q_i = -q_{ii} = ∑_{j≠i} q_{ij}
3. Define R = (r_{ij}) as:
   - If q_i ≠ 0: r_{ij} = q_{ij}/q_i for j ≠ i, r_{ii} = 0
   - If q_i = 0: r_{ii} = 1, r_{ij} = 0 for j ≠ i
4. The **jump chain** (Y_n) is a DTMC with initial distribution λ and transition matrix R
5. The **holding times** T_n ∼ Exp(q_{Y_{n-1}}), conditionally independent given (Y_n)
6. The **jump times** J_n = T_1 + T_2 + ... + T_n
7. The Markov jump process (X(t)) is:
   - X(t) = Y_0 for t < J_1
   - X(t) = Y_n for J_n ≤ t < J_{n+1}

### Key Properties / 关键性质

**Property 1: Memoryless Property (无记忆性)**
The exponential distribution is the ONLY continuous distribution with the memoryless property:
P(T > s + t | T > s) = P(T > t)

This is essential for the Markov property to hold.

**Property 2: Minimum of Exponentials (指数分布的最小值)**
From Theorem 14.2: If we have independent Exp(q_{ij}) random variables for each j ≠ i, then:
- The minimum has distribution Exp(q_i) where q_i = ∑_{j≠i} q_{ij}
- The probability that the minimum corresponds to state j is r_{ij} = q_{ij}/q_i

**Property 3: Row Sum Zero (行和为零)**
Each row of the generator matrix Q sums to 0:
∑_j q_{ij} = q_{ii} + ∑_{j≠i} q_{ij} = -q_i + q_i = 0

### Worked Examples / 例题

#### Example 17.1: Three-State Process

**Problem**: Consider a Markov jump process on 𝒮 = {1,2,3} with transition rates:
- From 1 to 2: rate 2
- From 2 to 1: rate 1, from 2 to 3: rate 2
- From 3 to 2: rate 1

**Step 1: Write the generator matrix Q**

Q = 
⎛⎜
⎝-2   2   0
 1  -3   2
 0   1  -1⎞⎟
⎠

**Explanation**:
- Row 1: q_{11} = -2 (since q_{12} = 2, no other transitions), q_{12} = 2, q_{13} = 0
- Row 2: q_{21} = 1, q_{22} = -3 (since q_{21} + q_{23} = 1 + 2 = 3), q_{23} = 2
- Row 3: q_{31} = 0, q_{32} = 1, q_{33} = -1 (since q_{32} = 1)

Check: Each row sums to 0 ✓

**Step 2: Find the jump chain transition matrix R**

First, compute q_i = -q_{ii}:
- q_1 = 2, q_2 = 3, q_3 = 1

Then r_{ij} = q_{ij}/q_i:
- Row 1: r_{12} = 2/2 = 1, r_{13} = 0/2 = 0, r_{11} = 0
- Row 2: r_{21} = 1/3, r_{23} = 2/3, r_{22} = 0
- Row 3: r_{32} = 1/1 = 1, r_{31} = 0, r_{33} = 0

R = 
⎛⎜
⎝0   1     0
 1/3  0   2/3
 0   1     0⎞⎟
⎠

**Step 3: Interpret the process**

Starting from state 2:
- Wait T_1 ∼ Exp(q_2) = Exp(3)
- Jump to state 1 with probability 1/3, or state 3 with probability 2/3
- If we jump to state 1: wait Exp(2), then jump to state 2 with certainty
- If we jump to state 3: wait Exp(1), then jump to state 2 with certainty

#### Example 17.2: Process with Absorbing State

**Problem**: States 𝒮 = {A, B, C} with transition rates as shown in Figure 16.

**Step 1: Generator matrix**

Q = 
⎛⎜
⎝-q_A   q_{AB}   q_{AC}
 q_{BA}  -q_B    q_{BC}
   0      0       0   ⎞⎟
⎠

where q_A = q_{AB} + q_{AC} and q_B = q_{BA} + q_{BC}

**Explanation**: State C is absorbing because row 3 has all zeros (q_{Cj} = 0 for all j).

**Step 2: Jump chain**

R = 
⎛⎜
⎝0     q_{AB}/q_A   q_{AC}/q_A
 q_{BA}/q_B    0     q_{BC}/q_B
   0        0         1      ⎞⎟
⎠

**Interpretation**: Once we reach state C, we stay there forever (r_{CC} = 1).

#### Example 17.3: Poisson Process

**Problem**: The Poisson process with rate λ has state space 𝒮 = ℤ_+ = {0,1,2,...}.

**Generator matrix**:
Q = 
⎛⎜⎜⎜
⎝-λ   λ   0   0  ...
 0  -λ   λ   0  ...
 0   0  -λ   λ  ...
 ⋮   ⋮   ⋮   ⋱  ⎞⎟⎟⎟
⎠

**Explanation**: 
- From state i, the only possible transition is to i+1 with rate λ
- q_{i,i+1} = λ, all other q_{ij} = 0
- q_i = λ, so holding time in state i is Exp(λ)

**Jump chain**: The jump chain is deterministic:
- Y_0 = 0, Y_1 = 1, Y_2 = 2, Y_3 = 3, ...
- r_{i,i+1} = 1 for all i

---

## Topic 2: Explosion / 爆炸

### Intuition / 直觉理解

**Explosion (爆炸)** occurs when a process can make infinitely many jumps in finite time. This is only possible with infinite state spaces.

Think of a population that grows faster and faster:
- If birth rates increase with population size, births happen more frequently
- If rates grow fast enough (e.g., λ_j = λj²), the expected time to reach infinite population is finite

### Formal Definition / 形式化定义

**Definition**: A Markov jump process **explodes** if there exists a finite time T such that the process makes infinitely many jumps before time T.

**Condition for explosion**: For a birth process with birth rates λ_j, explosion occurs if:
∑_{j=1}^{∞} 1/λ_j < ∞

**Example**: For λ_j = λj²:
∑_{j=1}^{n} 1/(λj²) = (1/λ)∑_{j=1}^{n} 1/j² → (1/λ)(π²/6) as n → ∞

This is finite, so explosion occurs.

### Key Properties / 关键性质

1. **Finite state spaces never explode** - there are only finitely many states to visit
2. **Explosion is a technical issue** - we can often avoid it by choosing models where explosion probability is 0
3. **Technical fixes exist** - e.g., adding an "infinity" state or restarting the process

---

## Topic 3: Transitions in Infinitesimal Time / 无穷小时间内的转移

### Intuition / 直觉理解

What happens in a very short time τ? Because of the memoryless property, the process "forgets" how long it has been waiting. So:

- **Probability of staying**: P(no jump in time τ) = e^{-q_iτ} ≈ 1 - q_iτ
- **Probability of jumping to j**: P(jump to j in time τ) ≈ q_{ij}τ
- **Probability of multiple jumps**: Negligible (o(τ))

### Formal Definition / 形式化定义

For a very small time τ:

P(X(t+τ) = j | X(t) = i) = 
⎧
⎨
⎩
1 - q_iτ + o(τ)  for i = j
q_{ij}τ + o(τ)   for i ≠ j
⎫
⎬
⎭

**Symbol explanation**:
- o(τ) means "little-o of τ" - terms that go to 0 faster than τ
- Formally: lim_{τ→0} o(τ)/τ = 0

This is an **equivalent definition** of the Markov jump process.

---

## Topic 4: Transition Semigroup and Forward/Backward Equations / 转移半群与向前/向后方程

### Intuition / 直觉理解

In discrete time, we had P^{(n)} = P^n (matrix power). In continuous time, we need P(t) for any real t ≥ 0.

The **transition semigroup (转移半群)** P(t) = (p_{ij}(t)) where:
p_{ij}(t) = P(X(t) = j | X(0) = i)

**Key question**: Given Q (generator matrix), how do we find P(t)?

The answer comes from differential equations:
- **Forward equation**: P'(t) = P(t)Q (looks at changes forward in time)
- **Backward equation**: P'(t) = QP(t) (looks at changes backward in time)

### Formal Definition / 形式化定义

#### Chapman-Kolmogorov Equations (查普曼-科尔莫戈罗夫方程)

For any s, t ≥ 0:

p_{ij}(s+t) = ∑_{k∈𝒮} p_{ik}(s) p_{kj}(t)

In matrix form: P(s+t) = P(s)P(t)

This is the **semigroup property (半群性质)**.

#### Kolmogorov Forward Equation (科尔莫戈罗夫向前方程)

P'(t) = P(t)Q, P(0) = I

In component form:
p'_{ij}(t) = ∑_k p_{ik}(t) q_{kj}

**Derivation**:
1. Start with Chapman-Kolmogorov: p_{ij}(t+τ) = ∑_k p_{ik}(t) p_{kj}(τ)
2. Use infinitesimal approximation:
   p_{kj}(τ) = 
   ⎧
   ⎨
   ⎩
   1 - q_jτ + o(τ)  for k = j
   q_{kj}τ + o(τ)   for k ≠ j
   ⎫
   ⎬
   ⎭
3. Separate the k = j term:
   p_{ij}(t+τ) = p_{ij}(t)(1 - q_jτ) + ∑_{k≠j} p_{ik}(t) q_{kj}τ + o(τ)
4. Rearrange:
   p_{ij}(t+τ) = p_{ij}(t) + ∑_k p_{ik}(t) q_{kj}τ + o(τ)
5. Subtract p_{ij}(t), divide by τ:
   [p_{ij}(t+τ) - p_{ij}(t)]/τ = ∑_k p_{ik}(t) q_{kj} + o(τ)/τ
6. Take limit τ → 0:
   p'_{ij}(t) = ∑_k p_{ik}(t) q_{kj}

#### Kolmogorov Backward Equation (科尔莫戈罗夫向后方程)

P'(t) = QP(t), P(0) = I

**Derivation**: Same as forward equation but start with:
p_{ij}(t+τ) = ∑_k p_{ik}(τ) p_{kj}(t)

### Key Properties / 关键性质

1. **Both equations are equivalent** - they give the same solution
2. **Initial condition**: P(0) = I (identity matrix)
3. **For finite state spaces**: The solution is unique
4. **Minimal nonnegative solution**: For infinite state spaces, there may be multiple solutions; we take the minimal nonnegative one

---

## Topic 5: Matrix Exponential / 矩阵指数

### Intuition / 直觉理解

Just as e^{at} solves the ODE x'(t) = ax(t), the **matrix exponential (矩阵指数)** e^{tQ} solves P'(t) = P(t)Q.

**Analogy (类比)**:
- Discrete time: P^{(n)} = P^n (matrix power)
- Continuous time: P(t) = e^{tQ} (matrix exponential)

### Formal Definition / 形式化定义

For any square matrix A, the **matrix exponential (矩阵指数)** is defined by the Taylor series:

e^A = exp(A) = ∑_{n=0}^{∞} A^n/n! = I + A + A²/2! + A³/3! + ...

where A⁰ = I (identity matrix).

For the generator matrix Q:
P(t) = e^{tQ} = ∑_{n=0}^{∞} (tQ)^n/n! = I + tQ + t²Q²/2! + t³Q³/6! + ...

### Key Properties / 关键性质

**Property 1: Derivative**
d/dt e^{tA} = Ae^{tA} = e^{tA}A

This follows from term-by-term differentiation of the series.

**Property 2: Commutation**
Ae^A = e^A A (A commutes with its own exponential)

**Property 3: Semigroup Property**
e^{(s+t)Q} = e^{sQ} e^{tQ} = P(s)P(t)

**Property 4: Initial Condition**
e^{0·Q} = I = P(0)

**Theorem 18.1**: For a finite state space, the unique solution to both forward and backward equations is:
P(t) = e^{tQ}

### Worked Examples / 例题

#### Example from Problem Sheet, Question 4

**Problem**: For a two-state process with generator matrix:
Q = ⎛⎜⎝-α   α⎞⎟⎠
    ⎝ β  -β⎠

where α, β > 0.

**Part (a)**: Show Q² = -(α+β)Q

**Solution**:
Q² = ⎛⎜⎝-α   α⎞⎟⎠ × ⎛⎜⎝-α   α⎞⎟⎠
     ⎝ β  -β⎠     ⎝ β  -β⎠

= ⎛⎜⎝(-α)(-α) + α·β   (-α)α + α(-β)⎞⎟⎠
  ⎝ β(-α) + (-β)β     β·α + (-β)(-β)⎠

= ⎛⎜⎝α² + αβ   -α² - αβ⎞⎟⎠
  ⎝-αβ - β²   αβ + β² ⎠

= ⎛⎜⎝α(α+β)   -α(α+β)⎞⎟⎠
  ⎝-β(α+β)   β(α+β) ⎠

= -(α+β) ⎛⎜⎝-α   α⎞⎟⎠ = -(α+β)Q ✓
          ⎝ β  -β⎠

**Part (b)**: Write Q^n for n ≥ 1 in terms of Q.

**Solution**: From part (a), Q² = -(α+β)Q.
Then Q³ = Q·Q² = Q·(-(α+β)Q) = -(α+β)Q² = -(α+β)·(-(α+β)Q) = (α+β)²Q

By induction: Q^n = (-(α+β))^{n-1} Q for n ≥ 1

**Part (c)**: Show P(t) = e^{tQ} = I + Q/(α+β)(1 - e^{-(α+β)t})

**Solution**:
e^{tQ} = ∑_{n=0}^{∞} (tQ)^n/n!
= I + ∑_{n=1}^{∞} t^n Q^n/n!
= I + ∑_{n=1}^{∞} t^n (-(α+β))^{n-1} Q/n!
= I + Q ∑_{n=1}^{∞} t^n (-(α+β))^{n-1}/n!
= I + Q/(α+β) ∑_{n=1}^{∞} (-(α+β)t)^n/n!
= I + Q/(α+β) (e^{-(α+β)t} - 1)
= I + Q/(α+β)(1 - e^{-(α+β)t}) ✓

**Part (d)**: Find p_{11}(t).

**Solution**: From part (c), the (1,1) entry of P(t) is:
p_{11}(t) = 1 + q_{11}/(α+β)(1 - e^{-(α+β)t})
= 1 + (-α)/(α+β)(1 - e^{-(α+β)t})
= 1 - α/(α+β) + α/(α+β)e^{-(α+β)t}
= β/(α+β) + α/(α+β)e^{-(α+β)t}

---

## 🔗 Connections / 知识关联

### Connections to Previous Topics (与前面内容的联系)

1. **Discrete-time Markov chains (离散时间马尔可夫链)**: The jump chain is a DTMC; the generator matrix Q plays the role of P - I in discrete time
2. **Exponential distribution (指数分布)**: Essential for holding times; its memoryless property ensures the Markov property
3. **Poisson process (泊松过程)**: A special case of a Markov jump process with only forward jumps

### Connections to Future Topics (与后面内容的联系)

1. **Communicating classes (通信类)**: Will be studied next, analogous to DTMC theory
2. **Hitting times and recurrence (击中时间与常返性)**: Continuous-time analogues of DTMC concepts
3. **Birth-death processes (生灭过程)**: Important applications in queueing theory
4. **Stationary distributions (平稳分布)**: Will be studied later

---

## ⚠️ Common Mistakes / 常见误区

### Mistake 1: Confusing Q and R
**错误**: Thinking the jump chain transition matrix R is the same as the generator matrix Q.

**Correct**: R is a PROBABILITY matrix (rows sum to 1), Q is a RATE matrix (rows sum to 0). They are related by r_{ij} = q_{ij}/q_i for i ≠ j.

### Mistake 2: Forgetting the diagonal of Q
**错误**: Writing Q with all positive entries.

**Correct**: The diagonal entries of Q are NEGATIVE (or zero). q_{ii} = -∑_{j≠i} q_{ij}.

### Mistake 3: Confusing forward and backward equations
**错误**: Writing P'(t) = QP(t) as the forward equation.

**Correct**: 
- Forward: P'(t) = P(t)Q (Q on the right)
- Backward: P'(t) = QP(t) (Q on the left)

### Mistake 4: Assuming explosion is always a problem
**错误**: Thinking all infinite state space processes explode.

**Correct**: Explosion only occurs when ∑ 1/λ_j < ∞. Many processes (like the Poisson process) never explode.

### Mistake 5: Forgetting the initial condition
**错误**: Solving the forward/backward equations without P(0) = I.

**Correct**: Always check P(0) = I (identity matrix).

---

## ✍️ Practice / 练习

### Question 1: Generator Matrix Construction

Consider a Markov jump process on 𝒮 = {1,2,3} with transition rates:
- From 1 to 2: rate 3, from 1 to 3: rate 1
- From 2 to 1: rate 2, from 2 to 3: rate 4
