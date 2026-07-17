# Section 7: Hitting Times

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:48
> 来源页: 40-43

---

# MATH2702: Markov Chains and Random Processes
## Section 7: Hitting Times / 击中时间

---

### 📋 Section Overview / 章节概览

This section introduces the concept of **hitting times (击中时间)** for Markov chains. We study:
- The **probability** that a Markov chain ever reaches a particular state or set of states
- The **expected time** it takes to reach those states
- **Return times** - the time to come back to a starting state
- Application to the **simple random walk (简单随机游走)**

**Why this matters**: Hitting times are fundamental to understanding:
- Gambler's ruin problems (already introduced in Section 3)
- Absorption probabilities in Markov chains
- Whether states are visited infinitely often or only finitely many times
- Long-run behavior of Markov chains

---

### 🎯 Learning Objectives / 学习目标

By the end of this section, you should be able to:

1. **Define** hitting probability ℎ𝑖𝐴 and expected hitting time 𝜂𝑖𝐴 for a Markov chain
2. **Set up and solve** equations for hitting probabilities by conditioning on the first step
3. **Set up and solve** equations for expected hitting times by conditioning on the first step
4. **Calculate** return probability 𝑚𝑖 and expected return time 𝜇𝑖
5. **Apply** these methods to the simple random walk
6. **Interpret** the results for symmetric vs. asymmetric random walks

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be comfortable with:

| Topic | Details |
|-------|---------|
| **Markov chains basics** | State space, transition matrix, Markov property |
| **Conditional probability** | ℙ(𝐴|𝐵) and the law of total probability |
| **Expectation** | 𝔼(𝑋) and conditional expectation |
| **Gambler's ruin** | From Section 3 - the method of conditioning on first step |
| **Simple random walk** | Definition: 𝑋𝑛 = 𝑋₀ + ∑ᵢ₌₁ⁿ 𝑌ᵢ where ℙ(𝑌ᵢ=1)=𝑝, ℙ(𝑌ᵢ=-1)=𝑞=1-𝑝 |
| **Solving equations** | Linear equations, quadratic equations |

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Hitting Probabilities and Expected Hitting Times / 击中概率和期望击中时间

##### Intuition / 直觉理解

Imagine you are lost in a city (the state space 𝒮). You want to reach a specific destination (the set 𝐴). 

- **Hitting probability (击中概率)** ℎ𝑖𝐴: Starting from your current location 𝑖, what is the probability you will EVER reach your destination?
- **Expected hitting time (期望击中时间)** 𝜂𝑖𝐴: Starting from 𝑖, how long (on average) will it take you to reach your destination?

The key insight: **We can figure this out by considering just ONE step**. After taking one step, we are in a new state, and the problem "starts over" from that new state. This is the **Markov property (马尔可夫性)** - the future depends only on the present, not the past.

##### Formal Definition / 形式化定义

**Definition 7.1 (Hitting Time / 击中时间)**

Let (𝑋ₙ) be a Markov chain on state space 𝒮 (状态空间). Let 𝐻_𝐴 be a random variable (随机变量) representing the **hitting time** to hit the set 𝐴 ⊂ 𝒮, given by:

𝐻_𝐴 = min{𝑛 ∈ {0,1,2,…} : 𝑋ₙ ∈ 𝐴}

Where:
- **𝐻_𝐴** = the first time (smallest n) that the chain enters set A
- **min** = minimum (最小值)
- **𝑛** = time step (时间步)
- **{0,1,2,…}** = non-negative integers (非负整数)
- **𝑋ₙ** = the state of the chain at time n
- **∈** = belongs to (属于)
- **𝐴** = the target set of states (目标状态集合)
- **⊂** = subset of (子集)

**Convention (约定)**: 𝐻_𝐴 = ∞ if 𝑋ₙ ∉ 𝐴 for all 𝑛 (the chain never hits A)

**Most common case**: 𝐴 = {𝑗} is a single state, so:

𝐻ⱼ = min{𝑛 ∈ {0,1,2,…} : 𝑋ₙ = 𝑗}

**Definition (Hitting Probability / 击中概率)**

The **hitting probability** ℎᵢᴬ of the set 𝐴 starting from state 𝑖 is:

ℎᵢᴬ = ℙ(𝑋ₙ ∈ 𝐴 for some 𝑛 ≥ 0 | 𝑋₀ = 𝑖) = ℙ(𝐻_𝐴 < ∞ | 𝑋₀ = 𝑖)

Where:
- **ℎᵢᴬ** = probability of ever hitting set A starting from state i
- **ℙ** = probability (概率)
- **𝑋ₙ ∈ 𝐴 for some 𝑛 ≥ 0** = the chain is in A at some time n (including n=0)
- **|** = given that (给定)
- **𝑋₀ = 𝑖** = the chain starts in state i
- **𝐻_𝐴 < ∞** = the hitting time is finite (we actually hit A)

**Most common case**: ℎᵢⱼ = hitting probability of state j starting from state i

**Definition (Expected Hitting Time / 期望击中时间)**

The **expected hitting time** 𝜂ᵢᴬ of the set 𝐴 starting from state 𝑖 is:

𝜂ᵢᴬ = 𝔼(𝐻_𝐴 | 𝑋₀ = 𝑖)

Where:
- **𝜂ᵢᴬ** = expected (average) time to hit set A starting from state i
- **𝔼** = expectation (期望)
- **𝐻_𝐴** = the hitting time random variable

**Important**: 𝜂ᵢᴬ can only be finite if ℎᵢᴬ = 1 (if we are certain to hit A eventually)

**Summary**:
- **ℎᵢⱼ** = probability we hit state j starting from state i
- **𝜂ᵢⱼ** = expected time until we hit state j starting from state i

##### Key Properties / 关键性质

**General Formula for Hitting Probabilities (by conditioning on first step)**:

ℎᵢᴬ = { ∑ⱼ∈𝒮 𝑝ᵢⱼ ℎⱼᴬ if 𝑖 ∉ 𝐴
       { 1 if 𝑖 ∈ 𝐴

Where:
- **𝑝ᵢⱼ** = transition probability from state i to state j (转移概率)
- **∑ⱼ∈𝒮** = sum over all states j in the state space
- **𝑖 ∉ 𝐴** = i is NOT in the target set
- **𝑖 ∈ 𝐴** = i IS in the target set (we're already there!)

**Important**: If these equations have multiple solutions, the hitting probabilities are the **smallest non-negative solutions (最小非负解)**.

**General Formula for Expected Hitting Times**:

𝜂ᵢᴬ = { 1 + ∑ⱼ∈𝒮 𝑝ᵢⱼ 𝜂ⱼᴬ if 𝑖 ∉ 𝐴
       { 0 if 𝑖 ∈ 𝐴

Where:
- **1** accounts for the time taken by the first step
- **∑ⱼ∈𝒮 𝑝ᵢⱼ 𝜂ⱼᴬ** = expected remaining time after the first step

Again, if multiple solutions exist, take the **smallest non-negative solution**.

##### Worked Examples / 例题

**Example 7.1: Finding Hitting Probability**

Consider a Markov chain with transition matrix:

P = ⎛⎜⎜⎜⎝
1/5  1/5  1/5  2/5
0    1    0    0
0    1/2  0    1/2
0    0    0    1
⎞⎟⎟⎟⎠

**Question**: Calculate the probability that the chain is absorbed at state 2 when started from state 1.

**Solution**:

**Step 1: Identify what we need**
We need ℎ₁₂ = probability of hitting state 2 starting from state 1.

**Step 2: Set up the equation by conditioning on the first step**

ℎ₁₂ = 𝑝₁₁ℎ₁₂ + 𝑝₁₂ℎ₂₂ + 𝑝₁₃ℎ₃₂ + 𝑝₁₄ℎ₄₂

Where:
- **𝑝₁₁** = 1/5 = probability of staying at state 1
- **𝑝₁₂** = 1/5 = probability of moving to state 2
- **𝑝₁₃** = 1/5 = probability of moving to state 3
- **𝑝₁₄** = 2/5 = probability of moving to state 4

So: ℎ₁₂ = (1/5)ℎ₁₂ + (1/5)ℎ₂₂ + (1/5)ℎ₃₂ + (2/5)ℎ₄₂

**Step 3: Find the other hitting probabilities**

- **ℎ₂₂** = 1 (we are already at state 2, so we've hit it!)
- **ℎ₄₂** = 0 (state 4 is absorbing - once we enter it, we never leave, and it's not state 2)

For ℎ₃₂, condition on the first step from state 3:
ℎ₃₂ = 𝑝₃₂ℎ₂₂ + 𝑝₃₄ℎ₄₂
     = (1/2)(1) + (1/2)(0)
     = 1/2

**Step 4: Substitute back**

ℎ₁₂ = (1/5)ℎ₁₂ + (1/5)(1) + (1/5)(1/2) + (2/5)(0)
     = (1/5)ℎ₁₂ + 1/5 + 1/10
     = (1/5)ℎ₁₂ + 3/10

**Step 5: Solve for ℎ₁₂**

ℎ₁₂ - (1/5)ℎ₁₂ = 3/10
(4/5)ℎ₁₂ = 3/10
ℎ₁₂ = (3/10)(5/4) = 15/40 = 3/8

**Answer**: ℎ₁₂ = 3/8

---

**Example 7.2: Finding Expected Hitting Time**

Consider the simple no-claims discount chain with transition matrix:

P = ⎛⎜⎝
1/4  3/4  0
1/4  0    3/4
0    1/4  3/4
⎞⎟⎠

States: 1 = no discount, 2 = 25% discount, 3 = 50% discount

**Question**: Given we start in state 1 (no discount), find the expected amount of time until we reach state 3 (50% discount).

**Solution**:

**Step 1: Identify what we need**
We need 𝜂₁₃ = expected time to hit state 3 starting from state 1.

**Step 2: Set up equations for all 𝜂ᵢ₃**

- **𝜂₃₃** = 0 (we're already at state 3)

For 𝜂₁₃, condition on first step:
𝜂₁₃ = 1 + 𝑝₁₁𝜂₁₃ + 𝑝₁₂𝜂₂₃ + 𝑝₁₃𝜂₃₃
     = 1 + (1/4)𝜂₁₃ + (3/4)𝜂₂₃ + (0)(0)
     = 1 + (1/4)𝜂₁₃ + (3/4)𝜂₂₃

Rearranging: 𝜂₁₃ - (1/4)𝜂₁₃ - (3/4)𝜂₂₃ = 1
(3/4)𝜂₁₃ - (3/4)𝜂₂₃ = 1  ... Equation (1)

For 𝜂₂₃, condition on first step:
𝜂₂₃ = 1 + 𝑝₂₁𝜂₁₃ + 𝑝₂₂𝜂₂₃ + 𝑝₂₃𝜂₃₃
     = 1 + (1/4)𝜂₁₃ + (0)𝜂₂₃ + (3/4)(0)
     = 1 + (1/4)𝜂₁₃

Rearranging: 𝜂₂₃ - (1/4)𝜂₁₃ = 1
-(1/4)𝜂₁₃ + 𝜂₂₃ = 1  ... Equation (2)

**Step 3: Solve the system of equations**

From Equation (2): 𝜂₂₃ = 1 + (1/4)𝜂₁₃

Substitute into Equation (1):
(3/4)𝜂₁₃ - (3/4)[1 + (1/4)𝜂₁₃] = 1
(3/4)𝜂₁₃ - 3/4 - (3/16)𝜂₁₃ = 1
(12/16)𝜂₁₃ - (3/16)𝜂₁₃ = 1 + 3/4
(9/16)𝜂₁₃ = 7/4 = 28/16
𝜂₁₃ = 28/9 ≈ 3.11

**Answer**: 𝜂₁₃ = 28/9 ≈ 3.11 time steps

---

#### Topic 2: Return Times / 返回时间

##### Intuition / 直觉理解

When we talk about hitting a state FROM ITSELF, the definitions above give:
- ℎᵢᵢ = 1 (we're already there!)
- 𝜂ᵢᵢ = 0 (it takes no time)

These are trivial. Instead, we ask: **After leaving state i, when do we come back?**

Think of it like leaving your house in the morning. The "return time" is when you come back home, not counting the moment you left.

##### Formal Definition / 形式化定义

**Definition (Return Time / 返回时间)**

Let 𝑀ᵢ be the **return time** to state i:

𝑀ᵢ = min{𝑛 ∈ {1,2,…} : 𝑋ₙ = 𝑖}

**Important**: This only considers times 𝑛 = 1,2,… (not including 𝑛 = 0). So it's the NEXT time we come back after the starting time.

**Definition (Return Probability / 返回概率)**

The **return probability** 𝑚ᵢ to state i is:

𝑚ᵢ = ℙ(𝑋ₙ = 𝑖 for some 𝑛 ≥ 1 | 𝑋₀ = 𝑖) = ℙ(𝑀ᵢ < ∞ | 𝑋₀ = 𝑖)

Where:
- **𝑚ᵢ** = probability of ever returning to state i after leaving it
- **𝑛 ≥ 1** = at least one step has been taken
- **𝑀ᵢ < ∞** = the return time is finite (we actually return)

**Definition (Expected Return Time / 期望返回时间)**

The **expected return time** 𝜇ᵢ to state i is:

𝜇ᵢ = 𝔼(𝑀ᵢ | 𝑋₀ = 𝑖)

##### Key Properties / 关键性质

**General Formulas for Return Quantities**:

By conditioning on the first step:

𝑚ᵢ = ∑ⱼ∈𝒮 𝑝ᵢⱼ ℎⱼᵢ

𝜇ᵢ = 1 + ∑ⱼ∈𝒮 𝑝ᵢⱼ 𝜂ⱼᵢ

Where:
- **𝑝ᵢⱼ** = probability of moving from i to j in the first step
- **ℎⱼᵢ** = hitting probability of state i starting from state j
- **𝜂ⱼᵢ** = expected hitting time of state i starting from state j
- The **1** accounts for the first step itself

Again, take the **minimal non-negative solution** if multiple solutions exist.

---

#### Topic 3: Hitting and Return Times for the Simple Random Walk / 简单随机游走的击中与返回时间

##### Intuition / 直觉理解

The simple random walk on ℤ (integers) moves:
- Up (+1) with probability 𝑝
- Down (-1) with probability 𝑞 = 1-𝑝

Key questions:
1. Starting from 0, what's the probability we ever reach a specific level i?
2. Starting from 0, what's the probability we ever return to 0?
3. If we do return, how long does it take on average?

The answers depend critically on whether 𝑝 = 1/2 (symmetric) or 𝑝 ≠ 1/2 (asymmetric).

##### Formal Definition / 形式化定义

**Simple Random Walk (简单随机游走)**:
- State space: ℤ = {..., -2, -1, 0, 1, 2, ...}
- Transition probabilities: 𝑝ᵢ,ᵢ₊₁ = 𝑝, 𝑝ᵢ,ᵢ₋₁ = 𝑞 = 1-𝑝
- Starting from 0: 𝑋₀ = 0

##### Theorem 7.1: Hitting Probabilities for Simple Random Walk

**Theorem 7.1**: Consider a random walk with up probability 𝑝 ≠ 0,1. Then:

**For hitting from 0 to i > 0** (hitting a positive level):

ℎ₀ᵢ = { (𝑝/𝑞)ⁱ < 1 if 𝑝 < 1/2
       { 1 if 𝑝 ≥ 1/2

**For hitting from 0 to i < 0** (hitting a negative level):

ℎ₀ᵢ = { (𝑞/𝑝)⁻ⁱ < 1 if 𝑝 > 1/2
       { 1 if 𝑝 ≤ 1/2

Where:
- **ℎ₀ᵢ** = probability of ever hitting state i starting from state 0
- **𝑝** = probability of moving up
- **𝑞** = 1-𝑝 = probability of moving down
- **𝑖** = target state (positive or negative integer)
- **(𝑝/𝑞)ⁱ** = (p/q) raised to the power i

**Interpretation**:
- If the walk is biased TOWARDS the target (𝑝 ≥ 1/2 for positive targets, 𝑝 ≤ 1/2 for negative targets), we hit with probability 1
- If the walk is biased AWAY from the target, the probability is less than 1

##### Proof / 证明

**Proof of Theorem 7.1**:

We prove the case for 𝑖 > 0. The case for 𝑖 < 0 follows by symmetry (swap p and q, consider -i > 0).

**Step 1: Show ℎ₀ᵢ = (ℎ₀₁)ⁱ**

We prove this by induction (归纳法).

**Base case**: ℎ₀₁ = (ℎ₀₁)¹ ✓ (trivially true)

**Inductive step**: Assume ℎ₀ᵢ = (ℎ₀₁)ⁱ. We need to show ℎ₀,ᵢ₊₁ = (ℎ₀₁)ⁱ⁺¹.

Let 𝑇ᵢ = min{𝑛 ≥ 1 : 𝑋ₙ = 𝑖} be the first time the walk hits i.

By the Markov property, conditional on the event {𝑇ᵢ < ∞} (the walk ever hits i):
- The process (𝑋ₙ)ₙ≥ₜᵢ is independent of (𝑋ₙ)ₙ<ₜᵢ
- It has the same distribution as a simple random walk starting from i

Let (𝑌ₙ) be a simple random walk starting from i. Then:

ℙ(∃𝑛 ≥ 𝑇ᵢ : 𝑋ₙ = 𝑖+1 | 𝑇ᵢ < ∞) = ℙ(∃𝑛 ≥ 0 : 𝑌ₙ = 𝑖+1) = ℎ₀₁

This is because from state i, hitting i+1 is the same as hitting 1 starting from 0 (by translation invariance - 平移不变性).

Now expand the conditional probability:

ℎ₀₁ = ℙ(∃𝑛 ≥ 𝑇ᵢ : 𝑋ₙ = 𝑖+1, 𝑇ᵢ < ∞) / ℙ(𝑇ᵢ < ∞)
     = ℙ(𝑇ᵢ₊₁ < ∞) / ℙ(𝑇ᵢ < ∞)
     = ℎ₀,ᵢ₊₁ / ℎ₀ᵢ

Therefore: ℎ₀,ᵢ₊₁ = ℎ₀₁ · ℎ₀ᵢ = ℎ₀₁ · (ℎ₀₁)ⁱ = (ℎ₀₁)ⁱ⁺¹

This completes the induction. ✓

**Step 2: Find ℎ₀₁**

Condition on the first step from state 0:

ℎ₀₁ = ℙ(𝑋₁ = 1) · ℎ₁₁ + ℙ(𝑋₁ = -1) · ℎ₋₁,₁

Where:
- **ℎ₁₁** = probability of hitting 1 starting from 1 = 1 (we're already there!)
- **ℎ₋₁,₁** = probability of hitting 1 starting from -1

From Step 1, ℎ₋₁,₁ = ℎ₀₂ = (ℎ₀₁)² (since from -1 to 1 is the same as from 0 to 2)

So: ℎ₀₁ = 𝑝 · 1 + 𝑞 · (ℎ₀₁)²

This gives us a quadratic equation (二次方程):

𝑞(ℎ₀₁)² - ℎ₀₁ + 𝑝 = 0

**Step 3: Solve the quadratic**

Using the quadratic formula: ℎ₀₁ = [1 ± √(1 - 4𝑝𝑞)] / (2𝑞)

Note that: 1 - 4𝑝𝑞 = 1 - 4𝑝(1-𝑝) = 1 - 4𝑝 + 4𝑝² = (1-2𝑝)² = (𝑝-𝑞)²

So: √(1 - 4𝑝𝑞) = |𝑝 - 𝑞|

Therefore: ℎ₀₁ = [1 ± |𝑝 - 𝑞|] / (2𝑞)

**Two possible solutions**:
- Solution 1: (1 + |𝑝 - 𝑞|) / (2𝑞)
- Solution 2: (1 - |𝑝 - 𝑞|) / (2𝑞)

**Step 4: Choose the correct solution**

Solution 1: (1 + |𝑝 - 𝑞|) / (2𝑞)

If 𝑝 < 1/2: |𝑝 - 𝑞| = 𝑞 - 𝑝, so (1 + 𝑞 - 𝑝) / (2𝑞) = (1 + 𝑞 - 𝑝) / (2𝑞)
Since 1 = 𝑝 + 𝑞, this becomes (𝑝 + 𝑞 + 𝑞 - 𝑝) / (2𝑞) = (2𝑞) / (2𝑞) = 1

If 𝑝 > 1/2: |𝑝 - 𝑞| = 𝑝 - 𝑞, so (1 + 𝑝 - 𝑞) / (2𝑞) = (𝑝 + 𝑞 + 𝑝 - 𝑞) / (2𝑞) = (2𝑝) / (2𝑞) = 𝑝/𝑞 > 1

A probability cannot be > 1, so Solution 1 is invalid when 𝑝 > 1/2.

Solution 2: (1 - |𝑝 - 𝑞|) / (2𝑞)

If 𝑝 < 1/2: |𝑝 - 𝑞| = 𝑞 - 𝑝, so (1 - (𝑞-𝑝)) / (2𝑞) = (1 - 𝑞 + 𝑝) / (2𝑞) = (𝑝 + 𝑝) / (2𝑞) = (2𝑝) / (2𝑞) = 𝑝/𝑞 < 1 ✓

If 𝑝 > 1/2: |𝑝 - 𝑞| = 𝑝 - 𝑞, so (1 - (𝑝-𝑞)) / (2𝑞) = (1 - 𝑝 + 𝑞) / (2𝑞) = (𝑞 + 𝑞) / (2𝑞) = (2𝑞) / (2𝑞) = 1 ✓

If 𝑝 = 1/2: Both solutions give 1 (since |𝑝-𝑞| = 0)

**Therefore**:
ℎ₀₁ = { 1 if 𝑝 ≥ 1/2
       { 𝑝/𝑞 if 𝑝 < 1/2

**Step 5: Generalize to ℎ₀ᵢ**

From Step 1: ℎ₀ᵢ = (ℎ₀₁)ⁱ

So for 𝑖 > 0:
ℎ₀ᵢ = { (𝑝/𝑞)ⁱ if 𝑝 < 1/2
       { 1 if 𝑝 ≥ 1/2

This completes the proof. ∎

##### Return Probability for Simple Random Walk

**Calculation of return probability 𝑚₀**:

By conditioning on the first step:

𝑚₀ = 𝑝 · ℎ₁₀ + 𝑞 · ℎ₋₁,₀

Where:
- **ℎ₁₀** = probability of hitting 0 starting from 1
- **ℎ₋₁,₀** = probability of hitting 0 starting from -1

By symmetry and Theorem 7.1:
- ℎ₁₀ = ℎ₀,₋₁ (by translation invariance)
- For hitting a negative target from 0: ℎ₀,₋₁ = { 1 if 𝑝 ≤ 1/2, (𝑞/𝑝) if 𝑝 > 1/2 }

So:
- ℎ₁₀ = { 1 if 𝑝 ≤ 1/2, (𝑞/𝑝) if 𝑝 > 1/2 }
- ℎ₋₁,₀ = { 1 if 𝑝 ≥ 1/2, (𝑝/𝑞) if 𝑝 < 1/2 }

**Case 1: 𝑝 = 1/2 (symmetric)**
𝑚₀ = (1/2)(1)