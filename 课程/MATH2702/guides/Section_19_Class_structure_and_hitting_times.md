# Section 19: Class structure and hitting times

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:57
> 来源页: 91-93

---

# 📚 Section 19: Class Structure and Hitting Times / 类结构与击中时间

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是连续时间马尔可夫跳跃过程理论的延续。我们之前学习了离散时间马尔可夫链中的通信类、周期性、击中概率和期望击中时间、常返性和瞬变性、平稳分布、收敛到平衡以及遍历定理。现在，我们将把这些理论扩展到连续时间马尔可夫跳跃过程中。好消息是，由于我们可以利用跳跃链（discrete time jump chain）来简化问题，连续时间的情况实际上比离散时间更简单。本章节将重点讨论通信类、击中概率和期望击中时间，以及常返性和瞬变性。

**English explanation:** This section continues the theory of continuous-time Markov jump processes. We previously studied communicating classes, periodicity, hitting probabilities and expected hitting times, recurrence and transience, stationary distributions, convergence to equilibrium, and the ergodic theorem for discrete-time Markov chains. Now, we will extend these concepts to continuous-time Markov jump processes. Fortunately, things will be simpler this time because we can often use the same techniques as in the discrete-time case, often by looking at the discrete-time jump chain. This section focuses on communicating classes, hitting probabilities and expected hitting times, and recurrence and transience.

## 🎯 Learning Objectives / 学习目标

完成本章节后，学生应能够：

1. **识别通信类**：能够从生成矩阵Q或转移率图中识别马尔可夫跳跃过程的通信类，并判断它们是否封闭。
2. **理解无周期性**：解释为什么连续时间马尔可夫过程不需要考虑周期性。
3. **计算击中概率**：利用跳跃链的转移矩阵R计算从任意状态出发击中特定状态集的概率。
4. **计算期望击中时间**：考虑在每个状态中的指数分布停留时间，计算期望击中时间。
5. **区分常返与瞬变**：根据返回概率判断状态是常返还是瞬变，并进一步区分正常返和零常返。

After completing this section, students should be able to:

1. **Identify communicating classes**: Identify communicating classes from the generator matrix Q or transition rate diagram, and determine if they are closed.
2. **Understand aperiodicity**: Explain why continuous-time Markov processes do not need to consider periodicity.
3. **Calculate hitting probabilities**: Use the jump chain's transition matrix R to calculate the probability of hitting a specific set of states from any starting state.
4. **Calculate expected hitting times**: Account for exponential holding times in each state to calculate expected hitting times.
5. **Distinguish recurrence and transience**: Determine if a state is recurrent or transient based on return probability, and further distinguish positive recurrence and null recurrence.

## 📚 Prerequisites / 前置知识

**中文解释：** 在学习本章节之前，学生需要掌握以下内容：

1. **离散时间马尔可夫链基础**：理解状态空间、转移概率、通信类、击中概率、期望击中时间、常返性和瞬变性等概念。
2. **连续时间马尔可夫跳跃过程基础**：理解生成矩阵Q、转移率qᵢⱼ、跳跃链（jump chain）及其转移矩阵R、指数分布停留时间等概念。
3. **指数分布**：了解指数分布的性质，特别是其无记忆性和期望值1/λ。
4. **条件期望**：能够使用条件期望方法（即"对第一步进行条件化"）建立方程。

**English explanation:** Before studying this section, students need to master the following:

1. **Discrete-time Markov chain basics**: Understand state space, transition probabilities, communicating classes, hitting probabilities, expected hitting times, recurrence and transience.
2. **Continuous-time Markov jump process basics**: Understand generator matrix Q, transition rates qᵢⱼ, jump chain and its transition matrix R, exponential holding times.
3. **Exponential distribution**: Know properties of exponential distribution, especially its memoryless property and expected value 1/λ.
4. **Conditional expectation**: Be able to use conditional expectation methods (conditioning on the first step) to set up equations.

## 📖 Core Content / 核心内容

### Topic 19.1: Communicating Classes / 通信类

#### Intuition / 直觉理解

**中文解释：** 在离散时间马尔可夫链中，我们说状态j从状态i可达（accessible），如果存在某个步数n使得从i出发经过n步后到达j的概率大于0。这个概念在连续时间中完全类似：我们说状态j从状态i可达，如果存在某个时间t≥0使得从i出发经过时间t后到达j的概率大于0。如果i和j互相可达，则它们属于同一个通信类（communicating class）。通信类将状态空间划分为互不相交的等价类。

**English explanation:** In discrete-time Markov chains, we say state j is accessible from state i if there exists some number of steps n such that the probability of going from i to j in n steps is positive. This concept is completely analogous in continuous time: we say state j is accessible from state i if there exists some time t≥0 such that the probability of going from i to j in time t is positive. If i and j are mutually accessible, they belong to the same communicating class. Communicating classes partition the state space into disjoint equivalence classes.

**关键洞察：** 对于马尔可夫跳跃过程，通信类完全由跳跃链（jump chain）决定。这是因为pᵢⱼ(t) > 0当且仅当在跳跃链中存在某个步数n使得rᵢⱼ⁽ⁿ⁾ > 0。而rᵢⱼ > 0当且仅当qᵢⱼ > 0，所以我们可以直接从转移率图中看出通信类。

**Key insight:** For Markov jump processes, communicating classes are completely determined by the jump chain. This is because pᵢⱼ(t) > 0 if and only if there exists some n such that rᵢⱼ⁽ⁿ⁾ > 0 in the jump chain. And rᵢⱼ > 0 if and only if qᵢⱼ > 0, so we can directly read off communicating classes from the transition rate diagram.

#### Formal Definition / 形式化定义

**Definition 19.1 (Accessibility and Communication / 可达性与通信).** Let (X(t)) be a Markov jump process on a state space S with transition semigroup (P(t)). We say that a state j ∈ S is **accessible** from another state i ∈ S, and write i → j if pᵢⱼ(t) > 0 for some t ≥ 0. If i → j and j → i, we say that i **communicates** with j and write i ↔ j.

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| X(t) | Markov jump process at time t | 时间t时的马尔可夫跳跃过程 |
| S | State space | 状态空间 |
| P(t) | Transition semigroup (matrix of pᵢⱼ(t)) | 转移半群（pᵢⱼ(t)的矩阵） |
| pᵢⱼ(t) | Probability of being in state j at time t given start in state i | 从i出发在时间t到达j的概率 |
| i → j | j is accessible from i | j从i可达 |
| i ↔ j | i and j communicate | i和j互相通信 |

**Definition (Communicating Class / 通信类).** The equivalence relation ↔ partitions S into equivalence classes, which we call **communicating classes**. If all states are in the same class, the jump process is **irreducible**. A class C is **closed** if i → j for i ∈ C means that j ∈ C also. If i is a closed class {i} by itself, then i is an **absorbing state**.

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| ↔ | Communication relation | 通信关系 |
| C | A communicating class | 一个通信类 |
| irreducible | All states in one class | 所有状态在同一类中（不可约） |
| closed class | Cannot leave this class | 不能离开这个类 |
| absorbing state | A closed class consisting of a single state | 由单个状态组成的封闭类 |

#### Key Properties / 关键性质

**中文解释：** 通信类具有以下重要性质：

1. **划分性质**：每个状态恰好属于一个通信类，该通信类是所有与它互相通信的状态的集合。
2. **与跳跃链的关系**：马尔可夫跳跃过程的通信类完全等同于其离散时间跳跃链的通信类。这是因为pᵢⱼ(t) > 0当且仅当在跳跃链中存在某个n使得rᵢⱼ⁽ⁿ⁾ > 0。
3. **从生成矩阵判断**：由于rᵢⱼ > 0当且仅当qᵢⱼ > 0，我们可以直接从转移率图（transition rate diagram）中看出通信类。
4. **封闭类**：如果从一个类出发无法到达类外的状态，则该类是封闭的。封闭类中的状态只能在该类内部转移。

**English explanation:** Communicating classes have the following important properties:

1. **Partition property**: Each state belongs to exactly one communicating class, which is the set of all states that communicate with it.
2. **Relation to jump chain**: The communicating classes of a Markov jump process are exactly the same as the communicating classes of its discrete-time jump chain. This is because pᵢⱼ(t) > 0 if and only if there exists some n such that rᵢⱼ⁽ⁿ⁾ > 0 in the jump chain.
3. **From generator matrix**: Since rᵢⱼ > 0 if and only if qᵢⱼ > 0, we can directly read off communicating classes from the transition rate diagram.
4. **Closed classes**: If from a class we cannot reach states outside the class, then the class is closed. States in a closed class can only transition within that class.

#### Worked Example / 例题

**Example 19.1 / 例19.1.** Write down the communicating classes for the Markov jump process with generator matrix

Q = $$
\begin{pmatrix}
-2   2   0 \\
1  -3   2 \\
0   0   0
\end{pmatrix}
$$

**Step-by-step solution / 逐步解答：**

**Step 1: Draw the transition rate diagram / 绘制转移率图**

**中文解释：** 从生成矩阵Q中，我们可以读出转移率：
- q₁₂ = 2（从状态1到状态2的转移率为2）
- q₂₁ = 1（从状态2到状态1的转移率为1）
- q₂₃ = 2（从状态2到状态3的转移率为2）
- q₃₃ = 0（状态3的离开率为0，即q₃ = 0，所以状态3是吸收态）

转移率图如图17所示：
```
1 ←→ 2 → 3
```
其中状态1和2之间有双向箭头（1→2的率为2，2→1的率为1），状态2到3有单向箭头（率为2），状态3没有出去的箭头。

**English explanation:** From the generator matrix Q, we can read off the transition rates:
- q₁₂ = 2 (rate from state 1 to state 2 is 2)
- q₂₁ = 1 (rate from state 2 to state 1 is 1)
- q₂₃ = 2 (rate from state 2 to state 3 is 2)
- q₃₃ = 0 (leaving rate from state 3 is 0, so q₃ = 0, meaning state 3 is absorbing)

The transition rate diagram is:
```
1 ←→ 2 → 3
```
where states 1 and 2 have bidirectional arrows (1→2 with rate 2, 2→1 with rate 1), state 2 to 3 has a one-way arrow (rate 2), and state 3 has no outgoing arrows.

**Step 2: Identify communicating classes / 识别通信类**

**中文解释：** 
- 状态1和2互相可达：从1可以到2（q₁₂ > 0），从2可以到1（q₂₁ > 0），所以1 ↔ 2。
- 状态3从状态2可达（q₂₃ > 0），但状态3不能回到状态2或1（q₃₁ = q₃₂ = 0），所以3不从1或2可达。
- 因此，通信类是{1, 2}和{3}。

**English explanation:**
- States 1 and 2 are mutually accessible: from 1 we can go to 2 (q₁₂ > 0), from 2 we can go to 1 (q₂₁ > 0), so 1 ↔ 2.
- State 3 is accessible from state 2 (q₂₃ > 0), but state 3 cannot go back to states 2 or 1 (q₃₁ = q₃₂ = 0), so 3 is not accessible from 1 or 2.
- Therefore, the communicating classes are {1, 2} and {3}.

**Step 3: Determine if classes are closed / 判断类是否封闭**

**中文解释：**
- 类{1, 2}：从状态1或2可以到达状态3（q₂₃ > 0），而状态3不在该类中，所以{1, 2}不是封闭类。
- 类{3}：从状态3不能到达任何其他状态（q₃₁ = q₃₂ = 0），所以{3}是封闭类。由于它只有一个状态，状态3是吸收态（absorbing state）。

**English explanation:**
- Class {1, 2}: From state 1 or 2 we can reach state 3 (q₂₃ > 0), and state 3 is not in this class, so {1, 2} is not a closed class.
- Class {3}: From state 3 we cannot reach any other state (q₃₁ = q₃₂ = 0), so {3} is a closed class. Since it consists of a single state, state 3 is an absorbing state.

**Final answer / 最终答案：** The communicating classes are {1, 2} (not closed) and {3} (closed, absorbing). The process is not irreducible.

### Topic 19.2: A Brief Note on Periodicity / 关于周期性的简要说明

#### Intuition / 直觉理解

**中文解释：** 在离散时间马尔可夫链中，我们不得不担心周期性（periodicity）问题，特别是当我们考虑长期行为（如平衡分布的存在性）时。周期性意味着状态只能在某些特定的时间步长（如2, 4, 6, ...）被访问。然而，在连续时间马尔可夫跳跃过程中，我们可以在一个状态中停留任意正实数长度的时间。因此，几乎必然地（with probability 1），我们永远不会观察到周期性行为。这是连续时间过程比离散时间过程更令人愉快的一个方面。

**English explanation:** In discrete-time Markov chains, we had to worry about periodic behavior, especially when considering long-term behavior like the existence of an equilibrium distribution. Periodicity means that a state can only be visited at certain specific time steps (e.g., 2, 4, 6, ...). However, for a continuous-time Markov jump process, it is possible to stay in a state for any positive real-number amount of time. Thus, with probability 1, we never see periodic behavior. This is one way in which continuous-time processes are actually more pleasant to deal with than discrete-time processes.

**关键洞察：** 为什么连续时间没有周期性？因为指数分布的支持集是整个[0, ∞)，所以从任何状态出发，我们可以选择任意长度的停留时间。这意味着即使跳跃链有周期性，连续时间过程本身也不会表现出周期性行为。

**Key insight:** Why is there no periodicity in continuous time? Because the exponential distribution has support [0, ∞), so from any state, we can choose any positive real length of stay. This means that even if the jump chain has periodicity, the continuous-time process itself will not exhibit periodic behavior.

#### Formal Statement / 形式化说明

**中文解释：** 在离散时间中，状态i的周期定义为d(i) = gcd{n ≥ 1 : pᵢᵢ⁽ⁿ⁾ > 0}。如果d(i) > 1，则状态i是周期的。但在连续时间中，由于我们可以停留任意时间长度，pᵢᵢ(t) > 0对所有t > 0成立（只要状态i不是吸收态且可以从自身出发返回），因此周期总是1。所以我们不需要担心周期性。

**English explanation:** In discrete time, the period of state i is defined as d(i) = gcd{n ≥ 1 : pᵢᵢ⁽ⁿ⁾ > 0}. If d(i) > 1, state i is periodic. But in continuous time, since we can stay for any length of time, pᵢᵢ(t) > 0 for all t > 0 (as long as state i is not absorbing and can return to itself), so the period is always 1. Therefore, we don't need to worry about periodicity.

### Topic 19.3: Hitting Probabilities and Expected Hitting Times / 击中概率与期望击中时间

#### Intuition / 直觉理解

**中文解释：** 击中概率（hitting probability）hᵢᴬ是从状态i出发，最终到达集合A中任意状态的概率。期望击中时间（expected hitting time）ηᵢᴬ是从状态i出发，到达集合A所需的期望时间。在离散时间中，我们通过对第一步进行条件化来建立方程求解这些量。在连续时间中，对于击中概率，我们只关心跳到哪里，而不关心等待多长时间，所以我们可以只考虑跳跃链。对于期望击中时间，我们需要更小心，因为我们在每个状态中会停留随机长度的时间（服从指数分布）。

**English explanation:** The hitting probability hᵢᴬ is the probability of reaching some state in set A at any point in the future starting from state i. The expected hitting time ηᵢᴬ is the expected amount of time to get there. In discrete time, we found these by forming simultaneous equations by conditioning on the first step. In continuous time, for hitting probabilities, we only care about where we jump to, not how long we wait, so we can consider only the jump chain. For expected hitting times, we need to be more careful because we spend a random amount of time in each state (exponentially distributed).

#### Formal Definitions / 形式化定义

**Definition (Hitting Probability / 击中概率).** For a Markov jump process (X(t)) on state space S, the hitting probability of set A ⊆ S starting from state i is:

hᵢᴬ = ℙ(X(t) ∈ A for some t ≥ 0 | X(0) = i)

**Definition (Expected Hitting Time / 期望击中时间).** The expected hitting time of set A ⊆ S starting from state i is:

ηᵢᴬ = 𝔼[min{t ≥ 0 : X(t) ∈ A} | X(0) = i]

**Definition (Return Time, Return Probability, Expected Return Time / 返回时间、返回概率、期望返回时间).** For a state i, define:

Mᵢ = min{t > T₁ : X(t) = i}  (first return time after leaving)
mᵢ = ℙ(X(t) = i for some t > T₁ | X(0) = i) = ℙ(Mᵢ < ∞ | X(0) = i)  (return probability)
μᵢ = 𝔼(Mᵢ | X(0) = i)  (expected return time)

where T₁ ∼ Exp(qᵢ) is the first time we leave state i.

**Important note / 重要说明：** If qᵢ = 0 (state i is absorbing), then T₁ = ∞ and we never leave state i. In this case, the return time, return probability, and expected return time are not defined (we will have no use for them).

#### Key Formulas / 关键公式

**中文解释：** 通过条件化第一步，我们可以得到以下公式：

对于返回概率：
mᵢ = Σⱼ rᵢⱼ hⱼᵢ = Σⱼ≠ᵢ (qᵢⱼ/qᵢ) hⱼᵢ

对于期望返回时间：
μᵢ = 1/qᵢ + Σⱼ rᵢⱼ ηⱼᵢ = (1/qᵢ)(1 + Σⱼ≠ᵢ qᵢⱼ ηⱼᵢ)

其中hⱼᵢ是从状态j出发击中状态i的概率，ηⱼᵢ是从状态j出发击中状态i的期望时间。

**English explanation:** By conditioning on the first step, we obtain the following formulas:

For return probability:
mᵢ = Σⱼ rᵢⱼ hⱼᵢ = Σⱼ≠ᵢ (qᵢⱼ/qᵢ) hⱼᵢ

For expected return time:
μᵢ = 1/qᵢ + Σⱼ rᵢⱼ ηⱼᵢ = (1/qᵢ)(1 + Σⱼ≠ᵢ qᵢⱼ ηⱼᵢ)

where hⱼᵢ is the probability of hitting state i starting from state j, and ηⱼᵢ is the expected time to hit state i starting from state j.

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| hᵢᴬ | Hitting probability of set A from state i | 从i出发击中集合A的概率 |
| ηᵢᴬ | Expected hitting time of set A from state i | 从i出发击中集合A的期望时间 |
| mᵢ | Return probability to state i | 返回状态i的概率 |
| μᵢ | Expected return time to state i | 返回状态i的期望时间 |
| Mᵢ | First return time to state i after leaving | 离开后首次返回状态i的时间 |
| T₁ | First time leaving the initial state | 首次离开初始状态的时间 |
| qᵢ | Total rate of leaving state i (qᵢ = -qᵢᵢ) | 离开状态i的总率 |
| rᵢⱼ | Jump chain transition probability from i to j | 跳跃链中从i到j的转移概率 |
| qᵢⱼ | Transition rate from i to j | 从i到j的转移率 |

#### Worked Examples / 例题

**Example 19.2 / 例19.2 (Hitting Probability / 击中概率).** Continuing with Example 19.1, calculate h₂₁, the probability of hitting state 1 starting from state 2.

**Step-by-step solution / 逐步解答：**

**Step 1: Write down the jump chain transition matrix / 写出跳跃链转移矩阵**

**中文解释：** 跳跃链的转移矩阵R由rᵢⱼ = qᵢⱼ/qᵢ给出，其中qᵢ = -qᵢᵢ。

对于状态1：q₁ = 2，所以r₁₂ = q₁₂/q₁ = 2/2 = 1，r₁₁ = 0。
对于状态2：q₂ = 3，所以r₂₁ = q₂₁/q₂ = 1/3，r₂₃ = q₂₃/q₂ = 2/3，r₂₂ = 0。
对于状态3：q₃ = 0（吸收态），所以r₃₃ = 1。

因此：
R = $$
\begin{pmatrix}
0    1    0 \\
1/3  0    2/3 \\
0    0    1
\end{pmatrix}
$$

**English explanation:** The jump chain transition matrix R is given by rᵢⱼ = qᵢⱼ/qᵢ, where qᵢ = -qᵢᵢ.

For state 1: q₁ = 2, so r₁₂ = q₁₂/q₁ = 2/2 = 1, r₁₁ = 0.
For state 2: q₂ = 3, so r₂₁ = q₂₁/q₂ = 1/3, r₂₃ = q₂₃/q₂ = 2/3, r₂₂ = 0.
For state 3: q₃ = 0 (absorbing), so r₃₃ = 1.

Therefore:
R = $$
\begin{pmatrix}
0    1    0 \\
1/3  0    2/3 \\
0    0    1
\end{pmatrix}
$$

**Step 2: Condition on the first step / 对第一步进行条件化**

**中文解释：** 从状态2出发，第一步跳跃到状态1的概率是r₂₁ = 1/3，跳跃到状态3的概率是r₂₃ = 2/3。如果跳到状态1，则立即击中（h₁₁ = 1）。如果跳到状态3，则永远无法击中状态1（因为状态3是吸收态且不是状态1，所以h₃₁ = 0）。

因此：
h₂₁ = r₂₁ × h₁₁ + r₂₃ × h₃₁
    = (1/3) × 1 + (2/3) × 0
    = 1/3

**English explanation:** Starting from state 2, the first jump goes to state 1 with probability r₂₁ = 1/3, and to state 3 with probability r₂₃ = 2/3. If we jump to state 1, we immediately hit it (h₁₁ = 1). If we jump to state 3, we can never hit state 1 (since state 3 is absorbing and not state 1, so h₃₁ = 0).

Therefore:
h₂₁ = r₂₁ × h₁₁ + r₂₃ × h₃₁
    = (1/3) × 1 + (2/3) × 0
    = 1/3

**Final answer / 最终答案：** h₂₁ = 1/3

---

**Example 19.3 / 例19.3 (Expected Hitting Time / 期望击中时间).** Continuing with Example 19.1, find the expected hitting time η₁₃ (expected time to hit state 3 starting from state 1).

**Step-by-step solution / 逐步解答：**

**Step 1: