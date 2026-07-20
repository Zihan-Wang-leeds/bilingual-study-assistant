# Section 19: Class Structure and Hitting Times (CT)

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:55
> 来源页: 91-93

---

# 📘 MATH2702 Study Guide: Class Structure and Hitting Times

## Section 19: Class Structure and Hitting Times / 类结构与击中时间

---

### 📋 Section Overview / 章节概览

This section extends the discrete-time Markov chain theory to **continuous-time Markov jump processes** (连续时间马尔可夫跳跃过程). We explore:

- **Communicating classes** (通信类) - how states are connected
- **Hitting probabilities** (击中概率) - probability of reaching certain states
- **Expected hitting times** (期望击中时间) - expected time to reach states
- **Recurrence and transience** (常返性与瞬时性) - whether states are visited infinitely often

**Why this matters**: Understanding these concepts is essential for analyzing the long-term behavior of continuous-time stochastic processes, which model real-world phenomena like queueing systems, chemical reactions, population dynamics, and financial markets.

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you will be able to:

1. **Identify** communicating classes from a generator matrix or rate diagram
2. **Calculate** hitting probabilities using the jump chain transition matrix
3. **Compute** expected hitting times accounting for exponential holding times
4. **Define** return times, return probabilities, and expected return times for continuous-time processes
5. **Classify** states as recurrent, transient, positive recurrent, or null recurrent
6. **Distinguish** between discrete-time and continuous-time periodicity

---

### 📚 Prerequisites / 前置知识

Before studying this section, ensure you understand:

- **Discrete-time Markov chains** (离散时间马尔可夫链): transition matrices, communicating classes, hitting probabilities
- **Exponential distribution** (指数分布): memoryless property, rate parameter λ, expected value 1/λ
- **Generator matrix Q** (生成矩阵): off-diagonal entries qᵢⱼ (transition rates), diagonal entries qᵢᵢ = -∑ⱼ≠ᵢ qᵢⱼ
- **Jump chain** (跳跃链): the discrete-time chain embedded in the continuous-time process
- **Conditioning on first step** (对第一步取条件): the fundamental technique for solving hitting probability equations

---

### 📖 Core Content / 核心内容

---

#### Topic 19.1: Communicating Classes / 通信类

##### Intuition / 直觉理解

In a continuous-time Markov jump process, states are connected if we can travel from one to another via a sequence of jumps. Think of it like a transportation network: if you can take a bus (jump) from city A to city B, and another bus from B to C, then C is "accessible" from A.

The key insight: **the communicating classes of a continuous-time process are exactly the same as those of its discrete-time jump chain**. This is because whether we can reach state j from state i depends only on the sequence of jumps, not on the waiting times between jumps.

##### Formal Definition / 形式化定义

**Definition 19.1**: Let (X(t)) be a Markov jump process on a state space 𝒮 with transition semigroup (P(t)). 

- **Accessibility (可达性)**: We say state j ∈ 𝒮 is **accessible** from state i ∈ 𝒮, written i → j, if pᵢⱼ(t) > 0 for some t ≥ 0.

  - pᵢⱼ(t) = ℙ(X(t) = j | X(0) = i) is the transition probability from i to j at time t
  - t ≥ 0 means we consider any non-negative time
  - > 0 means there is a positive probability (not necessarily 1)

- **Communication (互通)**: If i → j and j → i, we say i **communicates** with j, written i ↔ j.

- **Communicating classes (通信类)**: The equivalence relation ↔ partitions 𝒮 into equivalence classes called communicating classes.

- **Irreducible (不可约)**: If all states are in the same class, the jump process is irreducible.

- **Closed class (封闭类)**: A class C is **closed** if i → j for i ∈ C implies j ∈ C also. (You cannot leave the class.)

- **Absorbing state (吸收态)**: If {i} is a closed class by itself, then i is an **absorbing state**.

**Relationship with jump chain**: Let R = (rᵢⱼ) be the transition matrix for the jump chain (Yₙ). Then:
- pᵢⱼ(t) > 0 for some t if and only if rᵢⱼ⁽ⁿ⁾ > 0 for some n
- rᵢⱼ > 0 if and only if qᵢⱼ > 0 (the off-diagonal entries of the generator matrix)

Therefore, we can determine communicating classes directly from the transition rate diagram.

##### Key Properties / 关键性质

1. **Equivalence relation**: ↔ is an equivalence relation (reflexive, symmetric, transitive)
2. **Unique class**: Each state belongs to exactly one communicating class
3. **Class characterization**: A communicating class is the set of all j such that i ↔ j for a given i
4. **Jump chain equivalence**: Communicating classes for the continuous-time process = communicating classes for its jump chain
5. **Rate diagram**: We can read classes directly from the rate diagram (qᵢⱼ > 0 indicates a possible jump)

##### Worked Example / 例题

**Example 19.1**: Write down the communicating classes for the Markov jump process with generator matrix:

Q = ⎛⎜⎝
-2   2   0
 1  -3   2
 0   0   0
⎞⎟⎠

**Solution**:

Step 1: Interpret the generator matrix
- q₁₁ = -2, so q₁ = 2 (rate of leaving state 1)
- q₁₂ = 2, so from state 1, we always go to state 2 (since q₁₂ = q₁)
- q₂₁ = 1, q₂₃ = 2, so from state 2: go to 1 with rate 1, go to 3 with rate 2
- q₃₃ = 0, so state 3 is absorbing (never leaves)

Step 2: Draw the transition rate diagram (Figure 17 in text):
```
1 ←→ 2 → 3
```
- From 1 to 2: rate 2
- From 2 to 1: rate 1
- From 2 to 3: rate 2
- State 3: no outgoing arrows

Step 3: Identify communicating classes
- States 1 and 2 communicate (1→2 and 2→1), so {1,2} is one class
- State 3 only goes to itself, so {3} is another class

Step 4: Determine if classes are closed
- {1,2}: Not closed because we can go from 2 to 3 (leaving the class)
- {3}: Closed because no outgoing arrows; state 3 is absorbing

**Result**: Communicating classes are {1,2} (not closed) and {3} (closed, absorbing). The process is **not irreducible**.

---

#### Topic 19.2: A Brief Note on Periodicity / 关于周期性的简要说明

##### Intuition / 直觉理解

In discrete-time Markov chains, periodicity was a concern because you could only move at integer time steps. For example, a 2-state chain where you always alternate between states has period 2.

In continuous time, you can stay in a state for **any positive real amount of time** (exponentially distributed). This means you can return to a state at any time, not just at multiples of some period. With probability 1, we never see periodic behavior.

**This is one way continuous-time processes are simpler than discrete-time ones!**

##### Formal Definition / 形式化定义

There is no formal definition needed here - the key point is:

**For a continuous-time Markov jump process, periodicity is not a concern.** The holding times are exponentially distributed, allowing returns at any positive real time.

##### Key Properties / 关键性质

1. **No periodicity**: With probability 1, continuous-time jump processes exhibit no periodic behavior
2. **Simpler analysis**: We don't need to check for periodicity when studying long-term behavior
3. **Contrast with discrete time**: In discrete time, periodicity affected convergence to equilibrium; in continuous time, this issue disappears

---

#### Topic 19.3: Hitting Probabilities and Expected Hitting Times / 击中概率与期望击中时间

##### Intuition / 直觉理解

**Hitting probabilities**: The probability that we ever reach a set of states A, starting from state i. Since this only depends on where we jump (not how long we wait), we can use the jump chain exactly as in discrete time.

**Expected hitting times**: The expected time to reach set A. This is more complex because we spend random exponential time in each state before jumping. We must account for:
- The expected holding time in the current state (1/qᵢ)
- The probability of jumping to each next state
- The expected remaining time from each next state

##### Formal Definitions / 形式化定义

**Hitting probability** (击中概率): ℎᵢᴬ = ℙ(reach set A at any future time | start at i)

**Expected hitting time** (期望击中时间): ηᵢᴬ = 𝔼(time to reach set A | start at i)

**Return time** (返回时间): Mᵢ = min{t > T₁ : X(t) = i}
- T₁ ~ Exp(qᵢ) is the first time we leave state i
- Mᵢ is the first return to i AFTER leaving

**Return probability** (返回概率): mᵢ = ℙ(X(t) = i for some t > T₁ | X(0) = i) = ℙ(Mᵢ < ∞ | X(0) = i)

**Expected return time** (期望返回时间): μᵢ = 𝔼(Mᵢ | X(0) = i)

**Important**: If qᵢ = 0 (absorbing state, never leave), return time/probability are not defined.

##### Key Properties / 关键性质

**For hitting probabilities**:
- Use jump chain transition matrix R = (rᵢⱼ)
- Condition on first jump: ℎᵢᴬ = ∑ⱼ rᵢⱼ ℎⱼᴬ
- Same equations as discrete time

**For expected hitting times**:
- Account for expected holding time 1/qᵢ in current state
- Condition on first jump: ηᵢᴬ = 1/qᵢ + ∑ⱼ rᵢⱼ ηⱼᴬ
- The 1/qᵢ term is the expected time spent in state i before jumping

**For return probability**:
- mᵢ = ∑ⱼ rᵢⱼ ℎⱼᵢ = ∑ⱼ≠ᵢ (qᵢⱼ/qᵢ) ℎⱼᵢ
- Same as jump chain return probability

**For expected return time**:
- μᵢ = 1/qᵢ + ∑ⱼ rᵢⱼ ηⱼᵢ = (1/qᵢ)(1 + ∑ⱼ≠ᵢ qᵢⱼ ηⱼᵢ)

##### Worked Examples / 例题

**Example 19.2**: Calculate ℎ₂₁, the probability of hitting state 1 starting from state 2, for the process in Example 19.1.

**Solution**:

Step 1: Find the jump chain transition matrix R
From the generator matrix Q:
- From state 1: q₁₂ = 2, q₁ = 2, so r₁₂ = 2/2 = 1
- From state 2: q₂₁ = 1, q₂₃ = 2, q₂ = 3, so r₂₁ = 1/3, r₂₃ = 2/3
- From state 3: q₃ = 0, so r₃₃ = 1 (absorbing)

R = ⎛⎜⎜⎝
0    1    0
1/3  0    2/3
0    0    1
⎞⎟⎟⎠

Step 2: Set up equations by conditioning on first step
ℎ₂₁ = r₂₁ ℎ₁₁ + r₂₃ ℎ₃₁
     = (1/3)ℎ₁₁ + (2/3)ℎ₃₁

Step 3: Determine boundary conditions
- ℎ₁₁ = 1 (starting in state 1, we've already hit it)
- ℎ₃₁ = 0 (state 3 is absorbing and not state 1, so we never reach state 1)

Step 4: Calculate
ℎ₂₁ = (1/3)(1) + (2/3)(0) = 1/3

**Result**: ℎ₂₁ = 1/3

---

**Example 19.3**: Find the expected hitting time η₁₃ for the same process.

**Solution**:

Step 1: Set up equations by conditioning on first step

From state 1:
- Expected holding time: 1/q₁ = 1/2
- After holding, jump to state 2 with probability 1
- η₁₃ = 1/2 + η₂₃

From state 2:
- Expected holding time: 1/q₂ = 1/3
- After holding: go to state 1 with probability 1/3, go to state 3 with probability 2/3
- η₂₃ = 1/3 + (1/3)η₁₃ + (2/3)η₃₃

From state 3:
- Already at target, so η₃₃ = 0

Step 2: Substitute η₃₃ = 0
η₂₃ = 1/3 + (1/3)η₁₃

Step 3: Substitute into first equation
η₁₃ = 1/2 + [1/3 + (1/3)η₁₃]
    = 1/2 + 1/3 + (1/3)η₁₃
    = 5/6 + (1/3)η₁₃

Step 4: Solve for η₁₃
η₁₃ - (1/3)η₁₃ = 5/6
(2/3)η₁₃ = 5/6
η₁₃ = (5/6)(3/2) = 15/12 = 5/4

**Result**: η₁₃ = 5/4 = 1.25 time units

---

#### Topic 19.4: Recurrence and Transience / 常返性与瞬时性

##### Intuition / 直觉理解

**Recurrence** means we will almost surely return to a state (or never leave it). **Transience** means there's a positive probability we never return.

Think of it like a wandering explorer:
- **Recurrent state**: The explorer keeps coming back to this location, or sets up camp and never leaves
- **Transient state**: The explorer might visit, but eventually leaves and never returns

The classification depends entirely on the **jump chain** (discrete-time part), not on the waiting times. This is because return probability mᵢ depends only on jump probabilities.

##### Formal Definition / 形式化定义

**Definition 19.2**: For a state i ∈ 𝒮:

- **Recurrent (常返)**: If return probability mᵢ = 1, OR if qᵢ = 0 (never leave the state)
- **Transient (瞬时)**: If mᵢ < 1
- **Positive recurrent (正常返)**: If i is recurrent AND expected return time μᵢ < ∞, OR if qᵢ = 0
- **Null recurrent (零常返)**: If i is recurrent AND expected return time μᵢ = ∞

##### Key Properties / 关键性质

1. **Jump chain determines recurrence**: Return probability mᵢ is determined by the jump chain, so recurrence/transience classification is the same as in discrete time

2. **Class property**: In a communicating class, either ALL states are recurrent or ALL states are transient

3. **Finite closed classes**: Finite closed classes are always recurrent

4. **Non-closed classes**: Non-closed classes are always transient

5. **Absorbing states**: An absorbing state (qᵢ = 0) is positive recurrent (never leaves, so trivially returns)

##### Worked Example / 例题

**Example 19.4**: Classify the states in Example 19.1.

**Solution**:

Recall the communicating classes: {1,2} and {3}

Class {1,2}:
- Not closed (can leave to state 3)
- Therefore: **transient**

Class {3}:
- Closed (no outgoing arrows)
- Finite (only one state)
- q₃ = 0 (absorbing)
- Therefore: **positive recurrent**

**Result**: States 1 and 2 are transient; state 3 is positive recurrent.

---

### 🔗 Connections / 知识关联

**Previous connections**:
- This section builds directly on **discrete-time Markov chain theory** (Section 18 or earlier course)
- The **generator matrix Q** and **jump chain** concepts are essential prerequisites
- **Exponential holding times** connect to probability theory

**Future connections**:
- The next section (Section 20) will use these concepts to study:
  - **Stationary distributions** (平稳分布)
  - **Convergence to equilibrium** (收敛到平衡)
  - **Ergodic theorem** (遍历定理)
- Understanding recurrence/transience is crucial for determining whether a stationary distribution exists
- Hitting probabilities are used in queueing theory, reliability analysis, and population models

---

### ⚠️ Common Mistakes / 常见误区

1. **Confusing hitting probability with transition probability**
   - ℎᵢᴬ is the probability of EVER reaching A (over infinite time)
   - pᵢⱼ(t) is the probability of being at j at EXACTLY time t
   - They are different concepts!

2. **Forgetting the holding time in expected hitting time calculations**
   - Always add 1/qᵢ (expected time in current state) before considering the next jump
   - Common error: ηᵢᴬ = ∑ⱼ rᵢⱼ ηⱼᴬ (missing the 1/qᵢ term)

3. **Misinterpreting return time definition**
   - Mᵢ is the first return AFTER leaving (t > T₁)
   - It does NOT include the initial time 0
   - If you start at i, the "return" at time 0 doesn't count

4. **Assuming all closed classes are positive recurrent**
   - Finite closed classes are always positive recurrent
   - Infinite closed classes can be null recurrent (expected return time infinite)
   - Example: symmetric random walk on ℤ is recurrent but null recurrent

5. **Ignoring the qᵢ = 0 special case**
   - Absorbing states have undefined return time/probability
   - But they are classified as positive recurrent by definition

---

### ✍️ Practice / 练习

**Question 1**: Consider a Markov jump process with generator matrix:
Q = ⎛⎜⎝
-3   2   1
 1  -2   1
 0   0   0
⎞⎟⎠

Find the communicating classes and determine whether each is closed.

**Hint**: Draw the rate diagram first. Check which states can reach each other.

---

**Question 2**: For the process in Question 1, calculate ℎ₁₃ (probability of hitting state 3 starting from state 1).

**Hint**: Set up equations for ℎ₁₃, ℎ₂₃, ℎ₃₃. Remember ℎ₃₃ = 1.

---

**Question 3**: For the same process, find η₂₃ (expected time to hit state 3 starting from state 2).

**Hint**: Set up equations with holding times. You'll need η₁₃ and η₃₃ = 0.

---

**Question 4**: Classify each state in Question 1 as recurrent/transient and positive/null recurrent.

**Hint**: Check which classes are closed and finite.

---

**Question 5**: Explain why periodicity is not a concern for continuous-time Markov jump processes, but was important for discrete-time chains.

**Hint**: Think about the distribution of holding times and what times are possible for returns.

---

### 📌 Key Takeaways / 要点总结

1. **Communicating classes** for continuous-time processes are identical to those of the discrete-time jump chain, and can be read from the rate diagram (qᵢⱼ > 0 indicates possible jumps).

2. **Hitting probabilities** use the same equations as discrete time: ℎᵢᴬ = ∑ⱼ rᵢⱼ ℎⱼᴬ, conditioning on the first jump.

3. **Expected hitting times** require adding the expected holding time 1/qᵢ: ηᵢᴬ = 1/qᵢ + ∑ⱼ rᵢⱼ ηⱼᴬ.

4. **Return probability** mᵢ depends only on the jump chain (same as discrete time), but **expected return time** μᵢ includes holding times.

5. **Recurrence/transience** classification is determined by the jump chain: finite closed classes are recurrent, non-closed classes are transient.

6. **Periodicity** is not a concern in continuous time because exponential holding times allow returns at any positive real time.

7. **Absorbing states** (qᵢ = 0) are a special case: they are positive recurrent by definition, but return time/probability are undefined.

8. **Continuous-time processes are often simpler** than discrete-time ones because we don't need to worry about periodicity, and the exponential holding times provide nice mathematical properties.