# Section 8: Recurrence and Transience

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:48
> 来源页: 44-50

---

# 📚 MATH2702 Study Guide: Recurrence and Transience / 递归与瞬变性

## 📋 Section Overview / 章节概览

This section introduces the fundamental classification of states in Markov chains into **recurrent (递归)** and **transient (瞬变)** states. Understanding whether a state is recurrent or transient is crucial for analyzing the long-run behavior of Markov chains. We will learn:

- How to classify states as recurrent or transient
- How these properties are shared within communicating classes
- The distinction between positive and null recurrence
- The Strong Markov Property and its applications

This classification helps us predict whether a Markov chain will keep returning to certain states or eventually leave them forever, which is essential for understanding stationary distributions and long-term stability.

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** recurrent and transient states using return probability
2. **Apply** Theorem 8.1 to determine recurrence/transience using ∑p_ii^(n)
3. **Prove** that recurrence/transience is a class property
4. **Classify** communicating classes as open/closed, finite/infinite, and determine their recurrence status
5. **Distinguish** between positive and null recurrence
6. **Understand** the Strong Markov Property and its role in proofs

## 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

- **Markov chains basics**: State space, transition matrix, transition diagram
- **Communicating classes**: Definition, closed/open classes
- **Chapman-Kolmogorov equations**: p_ij^(n+m) = ∑_k p_ik^(n) p_kj^(m)
- **Geometric distribution**: P(X = r) = (1-p)^r p, E[X] = (1-p)/p
- **Conditional probability**: P(A|B) = P(A∩B)/P(B)
- **Stopping times**: Definition from Section 4

## 📖 Core Content / 核心内容

### Topic 1: Recurrent and Transient States / 递归状态与瞬变状态

#### Intuition / 直觉理解

Imagine you are at a party. Some people you keep running into again and again (recurrent states), while others you might meet a few times but eventually never see again (transient states).

**Recurrent states (递归状态)**: If we ever visit state i, we keep returning to i again and again. Starting from i, the expected number of visits to i is infinite, and the number of visits is certain to be infinite.

**Transient states (瞬变状态)**: We might visit state i a few times, but eventually we leave i and never come back. Starting from i, the expected number of visits to i is finite, and the number of visits is certain to be finite.

The key difference is the **return probability** m_i:
- If m_i = 1: recurrent
- If m_i < 1: transient

#### Formal Definition / 形式化定义

**Definition 8.1**: Let (X_n) be a Markov chain on a state space 𝒮. For i ∈ 𝒮, let m_i be the **return probability (返回概率)**:

m_i = ℙ(X_n = i for some n ≥ 1 | X_0 = i)

where:
- X_n = state at time n
- X_0 = initial state
- ℙ = probability measure
- n ≥ 1 means we consider returns at any future time (not counting the starting point)

If m_i = 1, we say state i is **recurrent (递归的)**.
If m_i < 1, we say state i is **transient (瞬变的)**.

#### Key Properties / 关键性质

**Theorem 8.1**: Consider a Markov chain with transition matrix P.

- If state i is **recurrent**, then ∑_{n=1}^∞ p_ii^(n) = ∞, and we return to state i infinitely many times with probability 1.
- If state i is **transient**, then ∑_{n=1}^∞ p_ii^(n) < ∞, and we return to state i infinitely many times with probability 0.

Where:
- p_ii^(n) = ℙ(X_n = i | X_0 = i), the n-step transition probability from i to i
- ∑_{n=1}^∞ p_ii^(n) = expected number of visits to i (starting from i), excluding the initial visit

**Important note**: The expected number of visits to i starting from i is:
𝔼(# visits to i | X_0 = i) = ∑_{n=0}^∞ ℙ(X_n = i | X_0 = i) = 1 + ∑_{n=1}^∞ p_ii^(n)

The "1" accounts for the initial visit at time 0.

#### Proof / 证明

**Proof of Theorem 8.1**:

**Part 1: Recurrent case**

Suppose state i is recurrent, so m_i = 1.

Step 1: Starting from i, the probability we return is m_i = 1.
Step 2: After that return, because of the Markov property, it is as if we restart the chain from i. So the probability we return again is still m_i = 1.
Step 3: Repeating this argument, we keep on returning, so we definitely visit infinitely often (with probability 1).
Step 4: Since the number of visits to i starting from i is always infinite, its expectation is infinite too.
Step 5: This expectation is ∑_{n=1}^∞ p_ii^(n) = ∞.

**Part 2: Transient case**

Suppose state i is transient, so m_i < 1.

Step 1: The probability we return to i exactly r times before never coming back is:
ℙ((number of returns to i) = r) = m_i^r (1 - m_i)

This is because we must return on the first r occasions (probability m_i^r), but then fail to return on the next occasion (probability 1 - m_i).

Step 2: This is a geometric distribution Geom(1 - m_i) with support {0, 1, 2, ...}.

Step 3: The expectation of this type of geometric random variable is (1-p)/p, where p = 1 - m_i.

Step 4: Therefore:
𝔼(number of returns to i) = ∑_{n=1}^∞ p_ii^(n) = (1 - (1 - m_i))/(1 - m_i) = m_i/(1 - m_i)

Step 5: Since m_i < 1, this expectation is finite.

Step 6: Since the expected number of returns is finite, the probability we return infinitely many times must be 0.

**Commentary**: The key insight is that the Markov property allows us to "restart" the chain after each return, making the return events independent with probability m_i each time.

#### Worked Examples / 例题

**Example 8.1: Simple Random Walk (简单随机游走)**

Consider the simple random walk on ℤ where:
- At each step, move right with probability p, left with probability q = 1-p
- p_ii^(n) = probability of being at position i after n steps starting from i

From Section 7, we know:
- For p = 1/2 (symmetric random walk): m_i = 1, so the chain is **recurrent**
- For p ≠ 1/2: m_i < 1, so the chain is **transient**

**Example 8.2: A Markov Chain with Multiple Classes**

Consider the Markov chain from Example 6.7 with states {1, 2, 3, 4, 5, 6, 7}:

[Transition diagram described in text]

**States 5, 6, 7**: These form a triangle where the chain cycles around. The return probability is clearly 1, so these states are **recurrent**.

**States 1, 2, 3, 4**: These are **transient**. Let's prove this directly:

- **State 4**: From state 4, we might go straight to state 5 (with probability p_45). If we go to state 5, we cannot come back to 4. So m_4 ≤ 1 - p_45 = 2/3 < 1. Therefore state 4 is transient.

- **State 1**: From state 1, we might go to state 4 (with probability p_14) and then to state 5 (with probability p_45). If this happens, we cannot return to 1. So m_1 ≤ 1 - p_14·p_45 = 1 - (1/2)(1/3) = 5/6 < 1. Therefore state 1 is transient.

- **State 3**: Similarly, m_3 ≤ 1 - p_34·p_45 = 1 - (1/2)(1/3) = 5/6 < 1. Therefore state 3 is transient.

- **State 2**: m_2 ≤ 1 - p_21·p_14·p_45 = 1 - (1/2)(1/2)(1/3) = 11/12 < 1. Therefore state 2 is transient.

**Observation**: All states in communicating class {1, 2, 3, 4} are transient, while all states in class {5, 6, 7} are recurrent. This suggests recurrence/transience is a class property.

---

### Topic 2: Recurrent and Transient Classes / 递归类与瞬变类

#### Intuition / 直觉理解

If you can travel between two states (they communicate), they must share the same fate: either both are recurrent or both are transient. This makes sense because if you can go from i to j and back, then visiting i infinitely often means you'll also visit j infinitely often.

#### Formal Definition / 形式化定义

**Theorem 8.2**: Within a communicating class, either every state is transient or every state is recurrent.

Formally: Let i, j ∈ 𝒮 be such that i ↔ j (i communicates with j). If i is recurrent, then j is recurrent also; while if i is transient, then j is transient also.

**Terminology**: We can refer to a communicating class as a "recurrent class (递归类)" or a "transient class (瞬变类)". If a Markov chain is irreducible, we can refer to it as a "recurrent Markov chain" or a "transient Markov chain".

#### Proof / 证明

**Proof of Theorem 8.2**:

**Part 1: If i is recurrent, then j is recurrent**

Step 1: Since i ↔ j, there exist n, m ≥ 1 such that p_ij^(n) > 0 and p_ji^(m) > 0.

Step 2: Using the Chapman-Kolmogorov equations:
∑_{r=1}^∞ p_jj^(n+m+r) ≥ ∑_{r=1}^∞ p_ji^(m) · p_ii^(r) · p_ij^(n)

Explanation: To go from j to j in n+m+r steps, we can:
- First go from j to i in m steps (p_ji^(m))
- Then go from i to i in r steps (p_ii^(r))
- Then go from i to j in n steps (p_ij^(n))

Step 3: This gives:
∑_{r=1}^∞ p_jj^(n+m+r) ≥ p_ji^(m) · (∑_{r=1}^∞ p_ii^(r)) · p_ij^(n)

Step 4: Since i is recurrent, ∑_{r=1}^∞ p_ii^(r) = ∞ (by Theorem 8.1).

Step 5: Since p_ji^(m) > 0 and p_ij^(n) > 0, the right side is ∞.

Step 6: Therefore ∑_{r=1}^∞ p_jj^(n+m+r) = ∞, which means ∑_{s=1}^∞ p_jj^(s) = ∞.

Step 7: By Theorem 8.1, j is recurrent.

**Part 2: If i is transient, then j is transient**

Step 1: Suppose i is transient.
Step 2: If j were recurrent, then by Part 1 (with i and j swapped), i would be recurrent.
Step 3: This contradicts the assumption that i is transient.
Step 4: Therefore j must be transient.

#### Key Properties / 关键性质

**Theorem 8.3**: Classification of communicating classes

1. **Every open communicating class is transient.**
2. **Every finite closed communicating class is recurrent.**

This theorem completely classifies the transience and recurrence of classes, with the rare exception of infinite closed classes, which can require further examination.

**Explanation**:
- An **open class** is one from which we can leave (not closed)
- A **closed class** is one from which we cannot leave
- A **finite closed class** is both closed and has a finite number of states

#### Proof / 证明

**Proof of Theorem 8.3**:

**Part 1: Open classes are transient**

Step 1: Suppose i is in an open communicating class. Then there exists j such that i → j (p_ij^(n) > 0 for some n) but j ↛ i (once we reach j, we cannot return to i).

Step 2: Consider the probability we return to i after time n. We condition on whether X_n = j or not.

ℙ(return to i after time n | X_0 = i) = 
p_ij^(n) · ℙ(return to i after time n | X_n = j, X_0 = i) 
+ (1 - p_ij^(n)) · ℙ(return to i after time n | X_n ≠ j, X_0 = i)

Step 3: Since we cannot get from j to i, the first term is 0.
The second term is at most (1 - p_ij^(n)) because probabilities are ≤ 1.

Step 4: Therefore:
ℙ(return to i after time n | X_0 = i) ≤ 0 + (1 - p_ij^(n)) < 1

This is because p_ij^(n) > 0, so 1 - p_ij^(n) < 1.

Step 5: If i were recurrent, we would certainly return infinitely often, and in particular certainly return after time n. But we just showed this probability is < 1.

Step 6: Therefore i must be transient.

**Part 2: Finite closed classes are recurrent**

Step 1: Suppose class C is finite and closed.

Step 2: Since C is closed, once we enter C, we stay in C forever.

Step 3: Since C is finite, we have infinitely many time steps but only finitely many states. By the pigeonhole principle, there must be at least one state i ∈ C that we visit infinitely often (with positive probability).

Step 4: This state i cannot be transient (because transient states have probability 0 of being visited infinitely often).

Step 5: Therefore i must be recurrent.

Step 6: By Theorem 8.2, since all states in C communicate, the whole class is recurrent.

#### Worked Examples / 例题

**Revisiting Example 8.2**:

Using Theorem 8.3, we can classify the classes much more easily:

- Class {5, 6, 7}: This is **closed** (no transitions leave this class) and **finite** (3 states). Therefore it is **recurrent**.

- Class {1, 2, 3, 4}: This is **open** (transitions leave to class {5, 6, 7}). Therefore it is **transient**.

This is much less effort than the previous method of bounding return probabilities!

---

### Topic 3: Positive and Null Recurrence / 正常递归与零递归

#### Intuition / 直觉理解

Among recurrent states, we can further distinguish based on the **expected return time**:
- **Positive recurrent (正常递归)**: We return, and on average it doesn't take too long (finite expected return time)
- **Null recurrent (零递归)**: We return, but on average it takes forever (infinite expected return time)

Think of it like waiting for a bus: positive recurrent means the bus always comes and the average wait is reasonable; null recurrent means the bus always comes eventually, but the average wait is infinite!

#### Formal Definition / 形式化定义

**Definition 8.2**: Let (X_n) be a Markov chain on a state space 𝒮. Let i ∈ 𝒮 be a recurrent state, so m_i = 1, and let μ_i be the **expected return time (期望返回时间)**:

μ_i = 𝔼[first return time to i | X_0 = i]

If μ_i < ∞, we say state i is **positive recurrent (正常递归的)**.
If μ_i = ∞, we say state i is **null recurrent (零递归的)**.

**Note**: Transient states always have μ_i = ∞ (since they may never return).

#### Key Properties / 关键性质

The following facts can be proven similarly to previous results:

1. **In a recurrent class, either all states are positive recurrent or all states are null recurrent.**
   - This means we can refer to a "positive recurrent class" or a "null recurrent class"
   - An irreducible Markov chain can be "positive recurrent" or "null recurrent"

2. **All finite closed classes are positive recurrent.**

**Complete Classification**:
- Open classes → transient
- Finite closed classes → positive recurrent
- Infinite closed classes → can be positive recurrent, null recurrent, or transient

#### Worked Examples / 例题

**Simple Symmetric Random Walk (简单对称随机游走)**:

We know from Section 7 that:
- The simple symmetric random walk (p = 1/2) is recurrent (m_i = 1)
- The expected return time μ_i = ∞

Therefore, the simple symmetric random walk is **null recurrent**.

**Pólya's Theorem (波利亚定理)**:

Consider the simple symmetric random walk in d-dimensions on ℤ^d. At each step, we pick one of the d coordinates and increase or decrease it by 1; each of the 2d possibilities has probability 1/(2d).

- d = 1: null recurrent
- d = 2: null recurrent
- d ≥ 3: transient

**Famous quote**: "A drunk man will find his way home, but a drunk bird may get lost forever." - Shizuo Kakutani

This means: A drunk person walking randomly in 1D or 2D will eventually return home (recurrent), but a drunk bird flying randomly in 3D may never return (transient).

---

### Topic 4: Strong Markov Property / 强马尔可夫性质 (Optional, Non-examinable)

#### Intuition / 直觉理解

In the proof of Theorem 8.1, we used the Markov property at the "first return to state i". But the first return time is a **random time**, not a fixed time! Did we cheat?

Actually, we didn't cheat because the first return time is a **stopping time**, and the Markov property also applies to stopping times. This is called the **Strong Markov Property**.

#### Formal Definition / 形式化定义

**Definition 8.3**: Let (X_n) be a stochastic process in discrete time, and let T be a random time. Then T is a **stopping time (停时)** if for all n, whether or not the event {T = n} occurs is completely determined by the random variables X_0, X_1, ..., X_n.

**Examples of stopping times**:
- "The first visit to state i" → stopping time (we know immediately when we reach i)
- "Three time-steps after the second visit to j" → stopping time (we count three steps after the second visit)

**Non-examples**:
- "The time-step before the first visit to i" → not a stopping time (we need to go one more step to know)
- "The final visit to j" → not a stopping time (we don't know if we'll come back)

**Theorem 8.4 (Strong Markov Property)**: Let (X_n) be a Markov chain on a state space 𝒮, and let T be a stopping time that is finite with probability 1. Then for all states x_0, ..., x_{T-1}, i, j ∈ 𝒮:

ℙ(X_{T+1} = j | X_T = i, X_{T-1} = x_{T-1}, ..., X_0 = x_0) = p_ij

#### Proof / 证明

**Proof of Theorem 8.4**:

Step 1: Start with the left side and condition on the value of T:

ℙ(X_{T+1} = j | X_T = i, X_{T-1} = x_{T-1}, ..., X_0 = x_0)
= ∑_{n=0}^∞ ℙ(T = n) · ℙ(X_{n+1} = j | X_n = i, X_{n-1} = x_{n-1}, ..., X_0 = x_0, T = n)

Step 2: Since T is a stopping time, the event {T = n} is determined by X_0, ..., X_n. Therefore, conditioning on T = n is redundant given X_0, ..., X_n:

= ∑_{n=0}^∞ ℙ(T = n) · ℙ(X_{n+1} = j | X_n = i, X_{n-1} = x_{n-1}, ..., X_0 = x_0)

Step 3: Apply the (ordinary) Markov property:

= ∑_{n=0}^∞ ℙ(T = n) · ℙ(X_{n+1} = j | X_n = i)

Step 4: By definition, ℙ(X_{n+1} = j | X_n = i) = p_ij:

= ∑_{n=0}^∞ ℙ(T = n) · p_ij

Step 5: Take p_ij out of the sum:

= p_ij · ∑_{n=0}^∞ ℙ(T = n)

Step 6: Since T is finite with probability 1, ∑_{n=0}^∞ ℙ(T = n) = 1:

= p_ij

This completes the proof.

---

### Topic 5: A Useful Lemma / 一个有用的引理 (Optional, Non-examinable)

**Lemma 8.1**: Let (X_n) be an irreducible and recurrent Markov chain. Then for any initial distribution and any state j, we will certainly hit j, so the hitting time H_j is finite with probability 1.

**Proof**:

Step 1: It suffices to prove the lemma when the initial distribution is "start at i". For other initial distributions, we can repeat the argument for all i, then build any initial distribution from a weighted sum.

Step 2: Since the chain is irreducible, we have j → i, so pick m with p_ji^(m) > 0.

Step 3: Since the chain is recurrent, we know the return probability from j to j is 1, and we return infinitely many times with probability 1.

Step 4: We have:
1 = ℙ(X_n = j for infinitely many n | X_0 = j)
= ℙ(X_n = j for some n > m | X_0 = j)

Step 5: Condition on the state at time m:
= ∑_k ℙ(X_m = k | X_0 = j) · ℙ(X_n = j for some n > m | X_m = k, X_0 = j)

Step 6: Using the Markov property:
= ∑_k p_jk^(m) · ℙ(H_j < ∞ | X_0 = k)

Step 7: Note that ∑_k p_jk^(m) = 1 (sum of probabilities of going anywhere in m steps).

Step 8: For this sum to equal 1, we must have ℙ(H_j < ∞ | X_0 = k) = 1 whenever p_jk^(m) > 0.

Step 9: Since p_ji^(m) > 0, we have ℙ(H_j < ∞ | X_0 = i) = 1, as required.

---

## 🔗 Connections / 知识关联

### Previous Topics / 先前知识
- **Section 4 (Stopping Times)**: The concept of stopping times is used in the Strong Markov Property
- **Section 6 (Communicating Classes)**: Understanding classes is essential for Theorem 8.2 and 8.3
- **Section 7 (Return Probabilities)**: Methods for calculating m_i are used in examples

### Future Topics / 后续知识
- **Section 9 (Stationary Distributions)**: Positive recurrent Markov chains settle into stationary distributions
- **Long-term stability**: Understanding recurrence helps predict long-run behavior

### Real-world Applications / 实际应用
- **Queueing theory**: Recurrent/transient classification helps determine if queues grow unbounded
- **Random walks**: Understanding diffusion processes in physics and finance
- **Network analysis**: Identifying important nodes that are visited repeatedly

---

## ⚠️ Common Mistakes / 常见误区

1. **Confusing "expected number of visits" with "probability of return"**
   - Expected number of visits = ∑ p_ii^(n)
   - Return probability = m_i = ℙ(return at some time)
   - They are related but different concepts

2. **Thinking all states in a closed class are recurrent**
   - Only **finite** closed classes are guaranteed recurrent
   - Infinite closed classes can be transient (e.g., 3D random walk)

3. **Forgetting the initial visit in expected number of visits**
   - 𝔼(# visits) = 1 + ∑_{n=1}^∞ p_ii^(n)
   - The "1" accounts for the starting point

4. **Misapplying the Markov property at random times**
   - The ordinary Markov property only applies at fixed times
   - For random times, we need the Strong Markov Property and stopping times

5. **Thinking null recurrent means "never returns"**
   - Null recurrent states DO return with probability 1
   - But the expected return time is infinite

---

## ✍️ Practice / 练习

### Question 1
Consider a Markov chain with state space {1, 2, 3} and transition matrix:
P = [[0.5, 0.5, 0], [0, 0, 1], [0, 1, 0]]

Classify each state as recurrent or transient. Is the chain irreducible?

**Hint**: Draw the transition diagram first. Look for closed communicating classes.

### Question 2
Prove or disprove: If a state i is transient, then ∑_{n=1}^∞ p_ii^(n) < ∞.

**Hint**: Use Theorem 8.1.

### Question 3
Consider the simple random walk with p = 0.3. Is this chain recurrent or transient? What about p = 0.5?

**Hint**: Use Example 8.1.

### Question 4
A Markov chain has two communicating classes: C1 = {1, 2} and C2 = {3, 4, 5}. From state 2,