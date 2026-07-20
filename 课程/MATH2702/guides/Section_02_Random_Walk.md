# Section 2: Random Walk

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:44
> 来源页: 14-18

---

# 📘 MATH2702: Random Walks Study Guide

## 📋 Section Overview / 章节概览

This section introduces **random walks (随机游走)**—a fundamental stochastic process used to model phenomena that evolve randomly over time. We begin with the **simple random walk (简单随机游走)** on the integers, where at each step we move up or down by one unit. We then generalize to **general random walks (一般随机游走)** with arbitrary increment distributions, and derive formulas for their **expectation (期望)** and **variance (方差)**. Finally, we derive the **exact binomial distribution (精确二项分布)** of the simple random walk's position at any time.

**Why this matters**: Random walks appear everywhere—from stock price movements and population dynamics to physics (gas particle motion) and biology (animal foraging). Understanding them builds intuition for more complex stochastic processes like Brownian motion and diffusion.

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** the simple random walk as a discrete-time Markov chain on ℤ, and write its transition probabilities.
2. **Calculate** probabilities of specific positions after a given number of steps using combinatorial reasoning.
3. **Derive** the expectation 𝔼𝑋ₙ and variance Var(𝑋ₙ) for any random walk, and apply these formulas to the simple random walk.
4. **State** the exact binomial distribution formula for ℙ(𝑋ₙ = i) for the simple random walk.
5. **Apply** the normal approximation (central limit theorem) to approximate the distribution of a random walk for large n.
6. **Recognize** the Markov property in the random walk context.

---

## 📚 Prerequisites / 前置知识

Before studying this section, you should be comfortable with:

- **Probability basics (概率基础)**: Random variables, probability distributions, expectation, variance
- **Binomial distribution (二项分布)**: ℙ(Y = k) = C(n,k) p^k (1-p)^{n-k}
- **Combinatorics (组合数学)**: Binomial coefficients C(n,k) = n!/(k!(n-k)!)
- **Independence (独立性)**: Independent and identically distributed (IID) random variables
- **Properties of expectation and variance (期望与方差的性质)**: Linearity of expectation, variance of sums of independent variables
- **Central limit theorem (中心极限定理)**: Sum of IID variables approximates normal distribution

---

## 📖 Core Content / 核心内容

---

### Topic 1: Simple Random Walk / 简单随机游走

#### Intuition / 直觉理解

Imagine a drunk person trying to walk home. At each step, they either stumble forward (+1) or backward (-1). Their position after n steps is the net displacement. This is the **"drunkard's walk" (醉汉行走)**.

The simple random walk models many real processes:
- **Stock prices (股票价格)**: Each day the price might go up or down
- **Population sizes (种群规模)**: Birth (+1) or death (-1) events
- **Gas particles (气体粒子)**: Random collisions change position

The **simple symmetric random walk (简单对称随机游走)** occurs when up and down are equally likely (p = q = 1/2).

#### Formal Definition / 形式化定义

**Definition 1: Simple Random Walk (简单随机游走)**

Let (Xₙ) be a stochastic process with:
- **Discrete time (离散时间)**: n ∈ {0, 1, 2, ...} = ℤ⁺
- **Discrete state space (离散状态空间)**: 𝒮 = ℤ (all integers)
- **Initial condition (初始条件)**: X₀ = 0 (we start at 0)
- **Transition rule (转移规则)**: For n ≥ 0,
  ```
  X_{n+1} = { X_n + 1  with probability p
            { X_n - 1  with probability q = 1 - p
  ```

**Symbol explanation (符号说明)**:
- Xₙ: position at time n (n时刻的位置)
- p: probability of moving up one step (向上移动一步的概率)
- q = 1 - p: probability of moving down one step (向下移动一步的概率)
- ℤ: set of all integers (所有整数集合)
- ℤ⁺: non-negative integers (非负整数)

**Markov Property (马尔可夫性质)**: The future X_{n+1} depends only on the present Xₙ, not on the past X_{n-1}, ..., X₁, X₀. Thus the simple random walk is a **discrete-time Markov chain (离散时间马尔可夫链)**.

#### Key Properties / 关键性质

**Property 1: Markov Property**
ℙ(X_{n+1} = j | Xₙ = i, X_{n-1} = i_{n-1}, ..., X₀ = i₀) = ℙ(X_{n+1} = j | Xₙ = i)

**Property 2: Increment Representation**
The simple random walk can be written as:
```
Xₙ = X₀ + Σ_{i=1}^{n} Zᵢ
```
where:
- Z₁, Z₂, ... are **independent and identically distributed (IID) (独立同分布)** random variables
- ℙ(Zᵢ = 1) = p and ℙ(Zᵢ = -1) = q
- This means X_{n+1} = Xₙ + Z_{n+1}

#### Worked Examples / 例题

**Example 2.1 (from course material)**: What is the probability that after two steps a simple random walk has reached X₂ = 2?

**Solution**:
To reach X₂ = 2, we must go up in both steps:
- Step 1: up (+1) with probability p
- Step 2: up (+1) with probability p

Since steps are independent:
ℙ(X₂ = 2) = p × p = p²

**Example 2.2 (from course material)**: What is the probability that after three steps a simple random walk has reached X₃ = -1?

**Solution**:
To reach X₃ = -1, we need net displacement of -1 after 3 steps. This means 1 up and 2 downs. The possible sequences are:
1. Up, Down, Down (UDD): probability p × q × q = pq²
2. Down, Up, Down (DUD): probability q × p × q = pq²
3. Down, Down, Up (DDU): probability q × q × p = pq²

Since these are mutually exclusive:
ℙ(X₃ = -1) = pq² + pq² + pq² = 3pq²

---

### Topic 2: General Random Walks / 一般随机游走

#### Intuition / 直觉理解

The simple random walk is a special case where increments are only ±1. A **general random walk (一般随机游走)** allows the increments Zᵢ to have any distribution—they could be normal, Poisson, or any other distribution. The key idea remains: the position is the sum of IID increments.

#### Formal Definition / 形式化定义

**Definition 2: General Random Walk (一般随机游走)**

Any stochastic process of the form:
```
Xₙ = X₀ + Σ_{i=1}^{n} Zᵢ
```
where:
- X₀ is the starting position (初始位置)
- Z₁, Z₂, ... are IID random variables (独立同分布随机变量)
- The distribution of Zᵢ can be any distribution (not just ±1)

**Examples of state spaces (状态空间示例)**:
- ℤ (integers): Simple random walk, or steps of size ±2, etc.
- ℤ² (2D integer lattice): Step up, down, left, or right each with probability 1/4
- ℝ (real numbers): Zᵢ ~ N(μ, σ²) (normal distribution)

#### Key Properties / 关键性质

**Property 3: Expectation of a General Random Walk**

For any random walk (Xₙ):
```
𝔼[Xₙ] = 𝔼[X₀ + Σ_{i=1}^{n} Zᵢ]
       = 𝔼[X₀] + Σ_{i=1}^{n} 𝔼[Zᵢ]   (by linearity of expectation)
       = 𝔼[X₀] + n 𝔼[Z₁]             (since Zᵢ are identically distributed)
```

**For the simple random walk**:
- 𝔼[X₀] = 0 (we start at 0 with certainty)
- 𝔼[Z₁] = 1 × p + (-1) × q = p - q
- Therefore: 𝔼[Xₙ] = n(p - q)

**Interpretation (解释)**:
- If p > 1/2 (p > q): 𝔼[Xₙ] grows positive over time (upward drift)
- If p < 1/2 (p < q): 𝔼[Xₙ] grows negative over time (downward drift)
- If p = 1/2 = q (symmetric): 𝔼[Xₙ] = 0 for all time (no drift)

**Property 4: Variance of a General Random Walk**

For any random walk (Xₙ):
```
Var(Xₙ) = Var(X₀ + Σ_{i=1}^{n} Zᵢ)
        = Var(X₀) + Σ_{i=1}^{n} Var(Zᵢ)   (since X₀ and all Zᵢ are independent)
        = Var(X₀) + n Var(Z₁)              (since Zᵢ are identically distributed)
```

**For the simple random walk**:
- Var(X₀) = 0 (we start at 0 with certainty)
- Var(Z₁) = 𝔼[(Z₁ - 𝔼[Z₁])²]

Let's calculate Var(Z₁) step by step:

**Step 1**: 𝔼[Z₁] = p - q

**Step 2**: Z₁ - 𝔼[Z₁] takes two values:
- When Z₁ = 1: 1 - (p - q) = 1 - p + q = (1 - p) + q = q + q = 2q (since 1 - p = q)
- When Z₁ = -1: -1 - (p - q) = -1 - p + q = -(1 + p) + q = -(1 + p) + (1 - p) = -2p

**Step 3**: Compute expectation of squared deviation:
```
Var(Z₁) = p × (2q)² + q × (-2p)²
        = p × 4q² + q × 4p²
        = 4pq² + 4p²q
        = 4pq(q + p)
        = 4pq × 1          (since p + q = 1)
        = 4pq
```

**Therefore**: Var(Xₙ) = 4pqn

**For the simple symmetric random walk (p = q = 1/2)**:
Var(Xₙ) = 4 × (1/2) × (1/2) × n = n

**Interpretation**: Unless p = 0 or p = 1, the variance grows linearly with time, making prediction increasingly difficult.

#### Proof / 证明

**Proof of Variance Calculation (方差计算证明)**

We need to verify the algebra carefully:

Given: 𝔼[Z₁] = p - q

Compute (Z₁ - 𝔼[Z₁])² for each possible value:

Case 1: Z₁ = 1 (probability p)
```
Z₁ - 𝔼[Z₁] = 1 - (p - q) = 1 - p + q = q + q = 2q
```
Since 1 - p = q, we have 1 - p + q = q + q = 2q ✓

Case 2: Z₁ = -1 (probability q)
```
Z₁ - 𝔼[Z₁] = -1 - (p - q) = -1 - p + q = -(1 + p) + q
```
Now q = 1 - p, so:
```
-(1 + p) + (1 - p) = -1 - p + 1 - p = -2p
```
Thus Z₁ - 𝔼[Z₁] = -2p ✓

Now compute the expectation:
```
Var(Z₁) = p × (2q)² + q × (-2p)²
        = p × 4q² + q × 4p²
        = 4pq² + 4p²q
        = 4pq(q + p)
        = 4pq × 1
        = 4pq
```

**Property 5: Normal Approximation (正态近似)**

For large n, if the increments (Zₙ) have mean μ and variance σ², and X₀ = 0:
- 𝔼[Xₙ] = μn
- Var(Xₙ) = σ²n

The **Central Limit Theorem (中心极限定理)** gives:
```
(Xₙ - nμ) / (σ√n) → N(0, 1)  as n → ∞
```

This means for large n, Xₙ is approximately normally distributed:
```
Xₙ ≈ N(μn, σ²n)
```

**Important note**: The Xₙ are NOT independent, but the approximation still holds for the marginal distribution.

---

### Topic 3: Exact Distribution of the Simple Random Walk / 简单随机游走的精确分布

#### Intuition / 直觉理解

Since each step is independent with probability p of going up, the number of upward steps in n steps follows a binomial distribution. The position is determined by the difference between upward and downward steps.

#### Formal Definition / 形式化定义

**Definition 3: Exact Distribution of Simple Random Walk**

Let Yₙ = number of upward steps in the first n time periods.

Then Yₙ ~ Bin(n, p), meaning:
```
ℙ(Yₙ = k) = C(n, k) p^k q^{n-k}   for k = 0, 1, ..., n
```
where C(n, k) = n!/(k!(n-k)!) is the binomial coefficient "n choose k" (二项式系数).

If Yₙ = k, then:
- Number of upward steps = k
- Number of downward steps = n - k
- Position = k - (n - k) = 2k - n

Therefore:
```
ℙ(Xₙ = 2k - n) = ℙ(Yₙ = k) = C(n, k) p^k q^{n-k}    (Equation 2)
```

**Parity observation (奇偶性观察)**:
- If n is odd: Xₙ is always at an odd-numbered state (since 2k - odd = odd)
- If n is even: Xₙ is always at an even-numbered state (since 2k - even = even)

**Alternative form**: Let i = 2k - n, then k = (n + i)/2 and n - k = (n - i)/2.

```
ℙ(Xₙ = i) = C(n, (n+i)/2) p^{(n+i)/2} q^{(n-i)/2}
```
when n and i have the same parity (奇偶性相同) and -n ≤ i ≤ n, and 0 otherwise.

**For the simple symmetric random walk (p = q = 1/2)**:
```
ℙ(Xₙ = i) = C(n, (n+i)/2) × (1/2)^{(n+i)/2} × (1/2)^{(n-i)/2}
           = C(n, (n+i)/2) × 2^{-n}
```

#### Key Properties / 关键性质

**Property 6: Support of the Distribution (分布的支持集)**
- Xₙ can only take values i such that:
  - i has the same parity as n (both even or both odd)
  - -n ≤ i ≤ n
- Otherwise, ℙ(Xₙ = i) = 0

**Property 7: Binomial Structure**
The distribution is derived from the binomial distribution of the number of upward steps.

#### Worked Examples / 例题

**Example**: For a simple random walk with p = 0.6, find ℙ(X₅ = 3).

**Solution**:
- n = 5, i = 3
- Check parity: n = 5 (odd), i = 3 (odd) ✓ same parity
- Check bounds: -5 ≤ 3 ≤ 5 ✓
- k = (n + i)/2 = (5 + 3)/2 = 4
- n - k = 5 - 4 = 1

ℙ(X₅ = 3) = C(5, 4) × (0.6)⁴ × (0.4)¹
           = 5 × 0.1296 × 0.4
           = 5 × 0.05184
           = 0.2592

---

## 🔗 Connections / 知识关联

### Connection to Previous Topics (与前面知识的联系)

1. **Binomial distribution (二项分布)**: The exact distribution of the simple random walk is directly derived from the binomial distribution—a key concept from introductory probability.

2. **Expectation and variance (期望与方差)**: We used linearity of expectation and properties of variance of independent sums, which are fundamental probability tools.

3. **Central limit theorem (中心极限定理)**: The normal approximation for random walks is a direct application of the CLT.

### Connection to Future Topics (与后面知识的联系)

1. **Discrete-time Markov chains (离散时间马尔可夫链)**: The next section generalizes the Markov property we observed in random walks to arbitrary state spaces and transition probabilities.

2. **Continuous-time processes (连续时间过程)**: Random walks are the discrete-time precursors to Brownian motion and diffusion processes.

3. **Stochastic calculus (随机微积分)**: The normal approximation leads to the Wiener process, which is fundamental in financial mathematics.

---

## ⚠️ Common Mistakes / 常见误区

1. **Confusing Xₙ with Yₙ (混淆Xₙ和Yₙ)**
   - Yₙ counts upward steps (0 to n)
   - Xₙ = 2Yₙ - n gives the position
   - Remember: Xₙ is NOT the number of upward steps!

2. **Forgetting parity condition (忘记奇偶性条件)**
   - After an odd number of steps, you can only be at odd positions
   - After an even number of steps, you can only be at even positions
   - Example: ℙ(X₃ = 2) = 0 because 3 is odd but 2 is even

3. **Misapplying variance formula (错误应用方差公式)**
   - Var(Xₙ) = Var(X₀) + n Var(Z₁) ONLY if X₀ and all Zᵢ are independent
   - This holds for random walks but not for all stochastic processes

4. **Confusing expectation and variance growth (混淆期望和方差的增长)**
   - For symmetric random walk: 𝔼[Xₙ] = 0 but Var(Xₙ) = n (grows!)
   - The walk is not "staying near 0"—it's spreading out

5. **Forgetting that Xₙ are dependent (忘记Xₙ之间的依赖性)**
   - Even though increments are independent, Xₙ and X_{n+1} are correlated
   - The normal approximation applies to the marginal distribution, not joint distribution

---

## ✍️ Practice / 练习

**Question 1**: For a simple random walk with p = 0.3, calculate ℙ(X₄ = 0).

**Hint**: First check parity: n = 4 (even), i = 0 (even) ✓. Then find k = (n + i)/2.

**Question 2**: For a simple symmetric random walk (p = 1/2), find ℙ(X₆ = 2).

**Hint**: Use the simplified formula with 2^{-n}.

**Question 3**: A simple random walk has 𝔼[X₁₀] = 2. What is p?

**Hint**: Use 𝔼[Xₙ] = n(p - q) and q = 1 - p.

**Question 4**: For a general random walk with Zᵢ ~ N(0.5, 2) and X₀ = 10, find 𝔼[X₂₀] and Var(X₂₀).

**Hint**: Use the formulas for general random walks.

**Question 5**: Show that for a simple random walk, ℙ(Xₙ = n) = pⁿ.

**Hint**: What does it mean to reach position n after n steps? How many upward steps are needed?

---

## 📌 Key Takeaways / 要点总结

1. **Simple random walk (简单随机游走)**: X₀ = 0, each step up (+1) with prob p or down (-1) with prob q = 1-p. It satisfies the Markov property.

2. **General random walk (一般随机游走)**: Xₙ = X₀ + Σᵢ₌₁ⁿ Zᵢ, where Zᵢ are IID with any distribution.

3. **Expectation (期望)**: 𝔼[Xₙ] = 𝔼[X₀] + n𝔼[Z₁]. For simple random walk: 𝔼[Xₙ] = n(p - q).

4. **Variance (方差)**: Var(Xₙ) = Var(X₀) + n Var(Z₁). For simple random walk: Var(Xₙ) = 4pqn. For symmetric case: Var(Xₙ) = n.

5. **Exact distribution (精确分布)**: ℙ(Xₙ = i) = C(n, (n+i)/2) p^{(n+i)/2} q^{(n-i)/2}, valid when n and i have same parity and -n ≤ i ≤ n.

6. **Normal approximation (正态近似)**: For large n, Xₙ ≈ N(μn, σ²n) where μ = 𝔼[Z₁] and σ² = Var(Z₁).

7. **Key insight (关键洞察)**: The variance grows linearly with time, meaning the walk becomes harder to predict as time increases—even when the expectation is zero.

---

*End of Section 2 Study Guide*