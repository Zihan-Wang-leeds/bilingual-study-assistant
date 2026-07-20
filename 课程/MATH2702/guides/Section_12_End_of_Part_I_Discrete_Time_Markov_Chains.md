# Section 12: End of Part I: Discrete time Markov chains

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:42
> 来源页: 67-68

---

# MATH2702: Discrete Time Markov Chains - Part I Review / 离散时间马尔可夫链第一部分复习

## 📋 Section Overview / 章节概览

**中文解释：** 这一节不是新内容，而是一个重要的复习和总结环节。我们已经完成了课程第一部分——离散时间马尔可夫链的学习。在进入第二部分（连续时间过程）之前，我们需要停下来，系统地回顾和巩固所学知识。这一节提供了学习建议、技能检查清单，以及一份练习题（Problem Sheet 6）来检验你的掌握程度。

**English explanation:** This section contains no new material but serves as a crucial review and consolidation point. We have completed Part I of the module on Discrete Time Markov Chains. Before moving to Part II (Continuous Time Processes), we need to pause and systematically review and consolidate what we've learned. This section provides study suggestions, a skills checklist, and a practice problem sheet (Problem Sheet 6) to test your understanding.

**Why this matters / 为什么重要：**
- 离散时间马尔可夫链是随机过程的基础，连续时间过程将在此基础上构建
- 考试将涵盖这部分内容，需要确保完全掌握
- 复习和练习是巩固知识的关键

---

## 🎯 Learning Objectives / 学习目标

完成本复习后，你应该能够：

1. **Define and analyze simple random walks / 定义和分析简单随机游走**：包括计算概率、期望和方差
2. **Analyze gambler's ruin problems / 分析赌徒破产问题**：使用鞅和可选停止定理
3. **Work with Markov chain transition matrices / 处理马尔可夫链转移矩阵**：画转移图、计算n步转移概率
4. **Classify states and communicating classes / 分类状态和通信类**：确定周期性、常返性、瞬变性
5. **Find stationary distributions / 求平稳分布**：使用平衡方程和细致平衡方程
6. **Apply the ergodic theorem / 应用遍历定理**：计算长期比例

---

## 📚 Prerequisites / 前置知识

**中文解释：** 在开始本复习之前，你应该已经完成了Problem Sheets 1-6，并且对以下概念有基本理解：
- 概率论基础（条件概率、期望、方差）
- 矩阵运算（乘法、幂）
- 线性方程组求解

**English explanation:** Before starting this review, you should have completed Problem Sheets 1-6 and have a basic understanding of:
- Probability theory basics (conditional probability, expectation, variance)
- Matrix operations (multiplication, powers)
- Solving systems of linear equations

---

## 📖 Core Content / 核心内容

### Topic 1: Section 12.1 - Things to Do / 要做的事情

**中文解释：** 这一小节给出了学习建议。在继续学习之前，你应该：

1. **完成Problem Sheets 1-6**：确保你已经完成了所有练习题，并重新审视那些你曾经感到困难的题目。这是检验理解程度的最好方式。

2. **开始做Assessment 1**：截止日期是第8周的星期四（11月20日14:00）。不要等到最后一刻才开始。

3. **重读困难的章节**：如果之前对某些部分理解不够深入，现在是最好的复习时机。

4. **阅读可选的非考试内容**：如果你之前跳过了第4、8、10、11节的可选内容，现在可以回头看看。这些内容虽然不考，但能加深理解。

5. **反馈问题**：如果有任何不清楚的地方，可以在习题课上提出来。

**English explanation:** This subsection provides study suggestions. Before continuing, you should:

1. **Complete Problem Sheets 1-6**: Ensure you've finished all practice problems and revisit any questions you struggled with. This is the best way to test your understanding.

2. **Start working on Assessment 1**: Due Thursday of Week 8 at 14:00 (November 20). Don't wait until the last minute.

3. **Re-read difficult sections**: If you didn't fully understand some parts earlier, now is the perfect time to review.

4. **Read optional non-examinable content**: If you skipped Sections 4, 8, 10, 11 earlier, you can now look at them. Though not examinable, they deepen understanding.

5. **Provide feedback**: Let the instructor know if there's anything you'd like to go through in problem classes.

---

### Topic 2: Section 12.2 - Summary of Part I / 第一部分总结

**中文解释：** 这是一个详细的技能检查清单。虽然不完整，但如果你能完成清单上的大部分内容，你就为考试做好了充分准备。下面我们逐一解释每个技能点。

**English explanation:** This is a detailed skills checklist. Though not exhaustive, if you can accomplish most items on this list, you're well-prepared for the exam. Let's explain each skill point in detail.

---

#### Skill 1: Simple Random Walk / 简单随机游走

**Intuition / 直觉理解**

**中文解释：** 简单随机游走是最基本的随机过程模型。想象一个粒子在整数轴上移动，每一步以概率p向右移动1步，以概率q=1-p向左移动1步。经过n步后，粒子的位置是这些随机移动的累计结果。这个模型看似简单，但它是理解更复杂随机过程的基础。

**English explanation:** The simple random walk is the most basic stochastic process model. Imagine a particle moving on the integer line; at each step, it moves right by 1 with probability p, or left by 1 with probability q=1-p. After n steps, the particle's position is the cumulative result of these random moves. Though simple, this model is fundamental for understanding more complex stochastic processes.

**Formal Definition / 形式化定义**

Let \(X_0 = 0\) (starting at 0). For \(n \geq 1\):
\[
X_n = \sum_{i=1}^n Z_i
\]
where \(Z_i\) are i.i.d. (独立同分布) random variables with:
\[
\mathbb{P}(Z_i = 1) = p, \quad \mathbb{P}(Z_i = -1) = q = 1-p
\]

| Symbol | Meaning / 含义 |
|--------|----------------|
| \(X_n\) | Position after n steps / n步后的位置 |
| \(Z_i\) | Step direction / 步的方向 (+1 right, -1 left) |
| \(p\) | Probability of moving right / 向右移动的概率 |
| \(q\) | Probability of moving left / 向左移动的概率 |

**Key Properties / 关键性质**

1. **Binomial distribution / 二项分布**：After n steps, the number of right moves \(R_n \sim \text{Binomial}(n, p)\). So:
   \[
   \mathbb{P}(X_n = k) = \binom{n}{(n+k)/2} p^{(n+k)/2} q^{(n-k)/2}
   \]
   where \(n+k\) must be even (n+k必须为偶数).

2. **Expectation / 期望**：
   \[
   \mathbb{E}[X_n] = n(p - q) = n(2p - 1)
   \]

3. **Variance / 方差**：
   \[
   \text{Var}(X_n) = 4npq
   \]

**Proof of Expectation / 期望的证明**

**中文解释：** 由于 \(X_n = \sum_{i=1}^n Z_i\)，且每个\(Z_i\)的期望是\(\mathbb{E}[Z_i] = 1 \cdot p + (-1) \cdot q = p - q\)，所以总期望是n倍的单步期望。

**English explanation:** Since \(X_n = \sum_{i=1}^n Z_i\), and each \(Z_i\) has expectation \(\mathbb{E}[Z_i] = 1 \cdot p + (-1) \cdot q = p - q\), the total expectation is n times the single-step expectation.

\[
\mathbb{E}[X_n] = \sum_{i=1}^n \mathbb{E}[Z_i] = n(p - q)
\]

---

#### Skill 2: Gambler's Ruin / 赌徒破产

**Intuition / 直觉理解**

**中文解释：** 赌徒破产问题描述了一个赌徒在赌场赌博的场景。赌徒初始有i元，目标是达到N元，但每次赌博可能赢1元（概率p）或输1元（概率q=1-p）。问题是要计算赌徒最终破产（输光所有钱）的概率，以及破产前期望的赌博次数。这是一个经典的随机游走问题，但有吸收边界（0和N）。

**English explanation:** The gambler's ruin problem describes a gambler at a casino. The gambler starts with i dollars, aims to reach N dollars, but each bet may win 1 dollar (probability p) or lose 1 dollar (probability q=1-p). The problem is to calculate the probability of eventual ruin (losing all money) and the expected duration until ruin. This is a classic random walk problem with absorbing boundaries (0 and N).

**Formal Definition / 形式化定义**

Let \(X_n\) be the gambler's fortune after n bets. State space \(\mathcal{S} = \{0, 1, 2, ..., N\}\). Transition probabilities:
- \(p_{i,i+1} = p\) for \(0 < i < N\)
- \(p_{i,i-1} = q\) for \(0 < i < N\)
- \(p_{0,0} = 1\) (absorbing state / 吸收态)
- \(p_{N,N} = 1\) (absorbing state / 吸收态)

**Ruin Probability / 破产概率**

Let \(r_i = \mathbb{P}(\text{ruin starting from } i)\). Then:
\[
r_i = \begin{cases}
\frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N} & \text{if } p \neq q \\
1 - \frac{i}{N} & \text{if } p = q = 1/2
\end{cases}
\]

**Expected Duration / 期望持续时间**

Let \(d_i = \mathbb{E}[\text{time to absorption starting from } i]\). Then:
\[
d_i = \begin{cases}
\frac{i}{q-p} - \frac{N}{q-p} \cdot \frac{1-(q/p)^i}{1-(q/p)^N} & \text{if } p \neq q \\
i(N-i) & \text{if } p = q = 1/2
\end{cases}
\]

**Martingale Method / 鞅方法**

**中文解释：** 一个优雅的解法是使用鞅（martingale）和可选停止定理（Optional Stopping Theorem）。对于赌徒破产问题，我们可以构造一个鞅，然后应用可选停止定理来得到破产概率。

**English explanation:** An elegant solution uses martingales and the Optional Stopping Theorem. For the gambler's ruin, we can construct a martingale, then apply the Optional Stopping Theorem to obtain the ruin probability.

**Step 1: Define a martingale / 定义鞅**

For \(p \neq q\), define \(M_n = (q/p)^{X_n}\). This is a martingale because:
\[
\mathbb{E}[M_{n+1} | X_n] = p \cdot (q/p)^{X_n+1} + q \cdot (q/p)^{X_n-1} = (q/p)^{X_n}(p \cdot q/p + q \cdot p/q) = (q/p)^{X_n} = M_n
\]

**Step 2: Apply Optional Stopping Theorem / 应用可选停止定理**

Let \(T = \min\{n: X_n = 0 \text{ or } X_n = N\}\) (stopping time / 停止时间). Then:
\[
\mathbb{E}[M_T] = \mathbb{E}[M_0] = (q/p)^i
\]

But \(M_T\) takes value \((q/p)^0 = 1\) if ruin occurs, or \((q/p)^N\) if reaching N. So:
\[
r_i \cdot 1 + (1-r_i) \cdot (q/p)^N = (q/p)^i
\]

Solving for \(r_i\) gives the formula above.

---

#### Skill 3: Transition Diagrams and n-Step Probabilities / 转移图和n步转移概率

**中文解释：** 转移图是可视化马尔可夫链的重要工具。每个状态用一个节点表示，转移概率用带箭头的边表示。n步转移概率\(\mathbb{P}(X_n = j | X_0 = i)\)可以通过两种方式计算：(a) 对所有可能路径的概率求和，(b) 计算转移矩阵的n次幂。

**English explanation:** Transition diagrams are important tools for visualizing Markov chains. Each state is represented by a node, and transition probabilities by directed edges. The n-step transition probability \(\mathbb{P}(X_n = j | X_0 = i)\) can be calculated in two ways: (a) summing probabilities over all relevant paths, or (b) computing the n-th power of the transition matrix.

**Example / 示例**

Given transition matrix:
\[
P = $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
\]

The transition diagram would show:
- State 1 → State 2 (probability 1)
- State 2 → State 3 (probability 1)
- State 3 → State 1 (probability 1)

This is a deterministic cycle / 这是一个确定性循环。

---

#### Skill 4: Communicating Classes and Periodicity / 通信类和周期性

**中文解释：** 通信类（communicating class）是马尔可夫链中相互可达的状态集合。如果从状态i可以到达状态j，且从j可以到达i，则它们属于同一个通信类。周期性（period）是指返回同一状态所需步数的最大公约数。如果周期为1，则称为非周期（aperiodic）。

**English explanation:** A communicating class is a set of states that are mutually reachable. States i and j belong to the same class if i can reach j and j can reach i. Periodicity refers to the greatest common divisor of the number of steps needed to return to the same state. If the period is 1, the state is called aperiodic.

**How to find communicating classes / 如何找通信类：**
1. Draw the transition diagram / 画转移图
2. Find states that can reach each other / 找相互可达的状态
3. Group them into classes / 分组

**How to calculate period / 如何计算周期：**
1. Find all n such that \(p_{ii}^{(n)} > 0\) / 找所有使得\(p_{ii}^{(n)} > 0\)的n
2. Compute GCD of these n / 计算这些n的最大公约数

---

#### Skill 5: Hitting Probabilities and Expected Hitting Times / 击中概率和期望击中时间

**中文解释：** 击中概率是指从状态i出发，最终到达某个目标状态集合A的概率。期望击中时间是指从状态i出发，首次到达A所需的期望步数。这两种量都可以通过"对第一步取条件"（conditioning on the first step）来建立方程求解。

**English explanation:** Hitting probability is the probability of eventually reaching a target set A starting from state i. Expected hitting time is the expected number of steps to first reach A starting from i. Both quantities can be found by setting up equations through "conditioning on the first step" and solving the resulting system.

**Method / 方法：**

For hitting probability \(h_i = \mathbb{P}_i(\text{hit } A)\):
\[
h_i = \begin{cases}
1 & \text{if } i \in A \\
0 & \text{if } i \text{ is absorbing and } i \notin A \\
\sum_{j \in \mathcal{S}} p_{ij} h_j & \text{otherwise}
\end{cases}
\]

For expected hitting time \(g_i = \mathbb{E}_i[T_A]\):
\[
g_i = \begin{cases}
0 & \text{if } i \in A \\
1 + \sum_{j \in \mathcal{S}} p_{ij} g_j & \text{otherwise}
\end{cases}
\]

---

#### Skill 6: Recurrence and Transience / 常返性和瞬变性

**中文解释：** 状态可以分为三类：
- **正常返（positive recurrent）**：返回概率为1，且期望返回时间有限
- **零常返（null recurrent）**：返回概率为1，但期望返回时间无限
- **瞬变（transient）**：返回概率小于1

对于有限状态马尔可夫链，所有常返状态都是正常返的。

**English explanation:** States can be classified into three types:
- **Positive recurrent**: Return probability is 1, and expected return time is finite
- **Null recurrent**: Return probability is 1, but expected return time is infinite
- **Transient**: Return probability is less than 1

For finite state Markov chains, all recurrent states are positive recurrent.

**How to determine / 如何判断：**
1. Find communicating classes / 找通信类
2. For each class, check if it's closed (no transitions out) / 检查是否封闭
3. Closed classes are recurrent, open classes are transient / 封闭类常返，开放类瞬变
4. For finite chains, recurrent classes are positive recurrent / 有限链中常返类正常返

---

#### Skill 7: Stationary Distribution / 平稳分布

**中文解释：** 平稳分布\(\pi\)是一个概率分布，满足\(\pi = \pi P\)，即如果初始分布是\(\pi\)，那么所有后续时间的分布都是\(\pi\)。平稳分布描述了马尔可夫链的长期行为。

**English explanation:** A stationary distribution \(\pi\) is a probability distribution satisfying \(\pi = \pi P\), meaning if the initial distribution is \(\pi\), then the distribution at all future times is also \(\pi\). The stationary distribution describes the long-term behavior of the Markov chain.

**Conditions for existence and uniqueness / 存在性和唯一性的条件：**
- **Existence / 存在性**：If the chain is irreducible and positive recurrent / 如果链不可约且正常返
- **Uniqueness / 唯一性**：If the chain is irreducible / 如果链不可约

**How to find / 如何求：**
Solve the system of equations:
\[
\pi_j = \sum_{i \in \mathcal{S}} \pi_i p_{ij} \quad \text{for all } j
\]
with \(\sum_j \pi_j = 1\).

---

#### Skill 8: Detailed Balance Equations / 细致平衡方程

**中文解释：** 细致平衡方程（detailed balance equations）是寻找平稳分布的一个简便方法。如果存在一个分布\(\pi\)满足\(\pi_i p_{ij} = \pi_j p_{ji}\)对所有i,j成立，那么\(\pi\)就是平稳分布。满足这个条件的链称为可逆的（reversible）。

**English explanation:** The detailed balance equations provide a convenient method for finding stationary distributions. If there exists a distribution \(\pi\) satisfying \(\pi_i p_{ij} = \pi_j p_{ji}\) for all i,j, then \(\pi\) is a stationary distribution. Chains satisfying this condition are called reversible.

**Detailed Balance Equations / 细致平衡方程：**
\[
\pi_i p_{ij} = \pi_j p_{ji} \quad \text{for all } i, j
\]

**中文解释：** 这个方程的含义是：从状态i到状态j的概率流等于从状态j到状态i的概率流。这比直接解\(\pi = \pi P\)更容易求解。

**English explanation:** This equation means: the probability flow from state i to state j equals the probability flow from state j to state i. This is often easier to solve than directly solving \(\pi = \pi P\).

---

#### Skill 9: Convergence to Equilibrium / 收敛到平衡分布

**中文解释：** 对于不可约、非周期、正常返的马尔可夫链，无论初始分布如何，n步转移概率都会收敛到平稳分布：
\[
\lim_{n \to \infty} p_{ij}^{(n)} = \pi_j
\]

**English explanation:** For an irreducible, aperiodic, positive recurrent Markov chain, regardless of the initial distribution, the n-step transition probabilities converge to the stationary distribution:
\[
\lim_{n \to \infty} p_{ij}^{(n)} = \pi_j
\]

**Conditions / 条件：**
1. Irreducible / 不可约
2. Aperiodic / 非周期
3. Positive recurrent / 正常返

---

#### Skill 10: Ergodic Theorem / 遍历定理

**中文解释：** 遍历定理告诉我们，长期来看，马尔可夫链在每个状态上花费的时间比例等于该状态的平稳分布概率。即使链是周期的，这个结论也成立。

**English explanation:** The ergodic theorem tells us that, in the long run, the proportion of time spent in each state equals the stationary distribution probability for that state. This holds even if the chain is periodic.

**Ergodic Theorem / 遍历定理：**
\[
\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \mathbf{1}_{\{X_k = j\}} = \pi_j \quad \text{almost surely}
\]

where \(\mathbf{1}_{\{X_k = j\}}\) is the indicator function (指示函数) that equals 1 if \(X_k = j\) and 0 otherwise.

---

### Topic 3: Problem Sheet 6 / 练习题6

**中文解释：** 这是第6套练习题，包含3个问题。你应该在第七周的研讨会之前完成所有题目并写出解答。下面我们详细分析每个问题。

**English explanation:** This is Problem Sheet 6, containing 3 questions. You should attempt all questions and write up your solutions before the workshop in Week 7. Let's analyze each question in detail.

---

#### Question 1: Three-State Markov Chain / 三状态马尔可夫链

**中文解释：** 这个问题考察转移图、不可约性、周期性、返回概率、期望返回时间、平稳分布和极限分布。

**English explanation:** This question tests transition diagrams, irreducibility, periodicity, return probabilities, expected return times, stationary distributions, and limiting distributions.

**Given / 已知：**
\[
P = $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
\]

**Part (a): Transition diagram / 转移图**

**中文解释：** 从矩阵可以看出：状态1以概率1转到状态2，状态2以概率1转到状态3，状态3以概率1转到状态1。这是一个确定性循环。

**English explanation:** From the matrix: State 1 goes to State 2 with probability 1, State 2 goes to State 3 with probability 1, State 3 goes to State 1 with probability 1. This is a deterministic cycle.

Transition diagram / 转移图:
```
1 → 2 → 3 → 1
```

**Irreducibility / 不可约性：**

**中文解释：** 从任何状态都可以到达任何其他状态（通过循环），所以链是不可约的。

**English explanation:** From any state, you can reach any other state (through the cycle), so the chain is irreducible.

**Periodicity / 周期性：**

**中文解释：** 从状态1出发，返回状态1需要3步（1→2→3→1），或者6步、9步等。可能的步数是3, 6, 9, ...，最大公约数是3。所以每个状态的周期都是3。

**English explanation:** Starting from State 1, returning to State 1 takes 3 steps (1→2→3→1), or 6, 9 steps, etc. The possible numbers are 3, 6, 9, ..., with GCD = 3. So each state has period 3.

**Part (b): Return probability and expected return time / 返回概率和期望返回时间**

**中文解释：** 返回概率\(m_i\)是指从状态i出发，最终返回状态i的概率。由于链是确定性的循环，从任何状态出发都必然返回，所以\(m_i = 1\)。

期望返回时间\(\mu_i\)是指从状态i出发，首次返回状态i所需的期望步数。由于链是确定性的，从状态1出发，3步后必然返回，所以\(\mu_1 = 3\)。同理，\(\mu_2 = 3\)，\(\mu_3 = 3\)。

**English explanation:** The return probability \(m_i\) is the probability of eventually returning to state i starting from i. Since the chain is a deterministic cycle, return is certain, so \(m_i = 1\).

The expected return time \(\mu_i\) is the expected number of steps to first return to state i starting from i. Since the chain is deterministic, starting from State 1, return occurs exactly after 3 steps, so \(\mu_1 = 3\). Similarly, \(\mu_2 = 3\), \(\mu_3 = 3\).

**Part (c): Stationary distribution / 平稳分布**

**中文解释：** 解方程\(\pi = \pi P\)：
\[
(\pi_1, \pi_2, \pi_3) = (\pi_1, \pi_2, \pi_3) $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
\]

得到：
\[
\pi_1 = \pi_3, \quad \pi_2 = \pi_1, \quad \pi_3 = \pi_2
\]

所以\(\pi_1 = \pi_2 = \pi_3\)。加上归一化条件\(\pi_1 + \pi_2 + \pi_3 = 1\)，得到：
\[
\pi = \left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right)
\]

**English explanation:** Solve \(\pi = \pi P\):
\[
(\pi_1, \pi_2, \pi_3) = (\pi_1, \pi_2, \pi_3) $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
\]

This gives:
\[
\pi_1 = \pi_3, \quad \pi_2 = \pi_1, \quad \pi_3 = \pi_2
\]

So \(\pi_1 = \pi_2 = \pi_3\). With normalization \(\pi_1 + \pi_2 + \pi_3 = 1\):
\[
\pi = \left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right)
\]

**Confirm \(\mu_i\) / 验证\(\mu_i\)：**

**中文解释：** 对于不可约正常返链，有\(\mu_i = 1/\pi_i\)。这里\(\pi_i = 1/3\)，所以\(\mu_i = 3\)，与之前的结果一致。

**English explanation:** For an irreducible positive recurrent chain, \(\mu_i = 1/\pi_i\). Here \(\pi_i = 1/3\), so \(\mu_i = 3\), consistent with our earlier result.

**Part (d): Existence of limits / 极限的存在性**

**中文解释：** 极限\(\lim_{n \to \infty