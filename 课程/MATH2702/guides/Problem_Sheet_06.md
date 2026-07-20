# Problem Sheet 6 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:04
> 来源页 / Source Pages: 68-68

---

好的，作为您的大学随机过程数学导师，我将为您提供MATH2702课程问题集6的完整、逐步的双语（中文/英文）解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Consider a Markov chain (𝑋𝑛) with state space 𝒮= {1, 2, 3} and transition matrix
P = $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
.
(a) Draw a transition diagram for this Markov chain. Is it irreducible? Is each state periodic or aperiodic?
(b) What is 𝑚𝑖, the return probability, for each state? What is 𝜇𝑖, the expected return time for each
state.
(c) By solving 𝜋= 𝜋P, find the stationary distribution. Use this to confirm the values of 𝜇𝑖.
(d) For what initial distributions 𝜆do the limits lim𝑛→∞ℙ(𝑋𝑛= 𝑖) exist?
(e) What is the long-run proportion of time spent in each state?

**中文翻译 / Chinese Translation:**
考虑一个马尔可夫链 (𝑋𝑛)，其状态空间 𝒮= {1, 2, 3}，转移矩阵为
P = $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$
。
(a) 画出该马尔可夫链的转移图。它是不可约的吗？每个状态是周期的还是非周期的？
(b) 每个状态的返回概率 𝑚𝑖 是多少？每个状态的期望返回时间 𝜇𝑖 是多少？
(c) 通过求解 𝜋= 𝜋P，找到平稳分布。并用它来确认 𝜇𝑖 的值。
(d) 对于哪些初始分布 𝜆，极限 lim𝑛→∞ℙ(𝑋𝑛= 𝑖) 存在？
(e) 长期来看，在每个状态上花费的时间比例是多少？

**Knowledge Points / 考查知识点:**
- 马尔可夫链的转移图、不可约性、周期性 (Transition diagram, irreducibility, periodicity)
- 返回概率与期望返回时间 (Return probability and expected return time)
- 平稳分布与全局平衡方程 (Stationary distribution and global balance equations)
- 极限分布的存在性与初始分布的关系 (Existence of limiting distribution and its relation to initial distribution)
- 长期比例与平稳分布的关系 (Long-run proportion and stationary distribution)

**Step-by-Step Solution / 逐步解答:**

**(a) Transition Diagram, Irreducibility, and Periodicity / 转移图、不可约性与周期性**

**Step 1: Draw the transition diagram / 画出转移图**

**中文思路 / Chinese reasoning:**
首先，我们需要根据转移矩阵 P 画出状态转移图。矩阵 P 中的元素 P(i, j) 表示从状态 i 转移到状态 j 的概率。我们逐行分析：
- 从状态 1 (第一行): P(1,1)=0, P(1,2)=1, P(1,3)=0。所以从状态1，一定会转移到状态2。
- 从状态 2 (第二行): P(2,1)=0, P(2,2)=0, P(2,3)=1。所以从状态2，一定会转移到状态3。
- 从状态 3 (第三行): P(3,1)=1, P(3,2)=0, P(3,3)=0。所以从状态3，一定会转移到状态1。

**English reasoning:**
First, we need to draw the state transition diagram based on the transition matrix P. The element P(i, j) in matrix P represents the probability of transitioning from state i to state j. We analyze row by row:
- From state 1 (first row): P(1,1)=0, P(1,2)=1, P(1,3)=0. So from state 1, we always go to state 2.
- From state 2 (second row): P(2,1)=0, P(2,2)=0, P(2,3)=1. So from state 2, we always go to state 3.
- From state 3 (third row): P(3,1)=1, P(3,2)=0, P(3,3)=0. So from state 3, we always go to state 1.

**计算过程 / Working:**
The transition diagram is a directed cycle:
1 → 2 → 3 → 1

**Step 2: Check irreducibility / 检查不可约性**

**中文思路 / Chinese reasoning:**
一个马尔可夫链是“不可约”的，如果从任何一个状态出发，都能以正概率到达任何其他状态。在我们的图中，从状态1可以到2（一步），到3（两步）。从状态2可以到3（一步），到1（两步）。从状态3可以到1（一步），到2（两步）。因此，所有状态都是互通的，这个链是不可约的。

**English reasoning:**
A Markov chain is "irreducible" if it is possible to get from any state to any other state with positive probability. In our diagram, from state 1 we can reach state 2 (in one step) and state 3 (in two steps). From state 2 we can reach state 3 (in one step) and state 1 (in two steps). From state 3 we can reach state 1 (in one step) and state 2 (in two steps). Therefore, all states communicate with each other, and the chain is irreducible.

**计算过程 / Working:**
Since the chain is a single cycle, it is irreducible.

**Step 3: Check periodicity / 检查周期性**

**中文思路 / Chinese reasoning:**
一个状态 i 的周期 d(i) 定义为所有可能的返回步数 n (满足 P(i,i)^(n) > 0) 的最大公约数 (GCD)。对于状态1，可能的返回步数是3（1→2→3→1），6，9，等等。这些步数的最大公约数是3。类似地，状态2和3的返回步数也是3的倍数，所以它们的周期也是3。因为周期大于1，所有状态都是周期的。

**English reasoning:**
The period d(i) of a state i is defined as the greatest common divisor (GCD) of all possible return steps n (such that P(i,i)^(n) > 0). For state 1, the possible return steps are 3 (1→2→3→1), 6, 9, etc. The GCD of these steps is 3. Similarly, the return steps for states 2 and 3 are also multiples of 3, so their period is also 3. Since the period is greater than 1, all states are periodic.

**计算过程 / Working:**
- For state 1: return steps are 3, 6, 9, ... GCD = 3.
- For state 2: return steps are 3, 6, 9, ... GCD = 3.
- For state 3: return steps are 3, 6, 9, ... GCD = 3.
All states have period 3.

**Final Answer for (a) / 第(a)问最终答案:**
- **Transition Diagram / 转移图:** 1 → 2 → 3 → 1
- **Irreducibility / 不可约性:** Yes, the chain is irreducible. / 是的，该链是不可约的。
- **Periodicity / 周期性:** Each state is periodic with period 3. / 每个状态都是周期的，周期为3。

**(b) Return Probability and Expected Return Time / 返回概率与期望返回时间**

**Step 1: Define and calculate the return probability m_i / 定义并计算返回概率 m_i**

**中文思路 / Chinese reasoning:**
返回概率 m_i 是指从状态 i 出发，最终能返回状态 i 的概率。对于不可约的有限状态马尔可夫链，所有状态都是常返的，所以 m_i = 1。我们可以验证一下：从状态1出发，它一定会去2，然后去3，然后回到1。所以返回是必然事件。

**English reasoning:**
The return probability m_i is the probability that, starting from state i, the chain will eventually return to state i. For an irreducible finite Markov chain, all states are recurrent, so m_i = 1. We can verify: starting from state 1, it will certainly go to 2, then to 3, and then back to 1. So return is a certain event.

**计算过程 / Working:**
For an irreducible finite Markov chain, all states are positive recurrent. Therefore, m_i = 1 for all i ∈ {1, 2, 3}.

**Step 2: Define and calculate the expected return time μ_i / 定义并计算期望返回时间 μ_i**

**中文思路 / Chinese reasoning:**
期望返回时间 μ_i 是从状态 i 出发，首次返回状态 i 所需的平均步数。由于链是确定性的循环，从状态1出发，需要恰好3步才能返回。所以 μ_1 = 3。同样地，μ_2 = 3，μ_3 = 3。

**English reasoning:**
The expected return time μ_i is the average number of steps required to return to state i for the first time, starting from state i. Since the chain is a deterministic cycle, starting from state 1, it takes exactly 3 steps to return. So μ_1 = 3. Similarly, μ_2 = 3, μ_3 = 3.

**计算过程 / Working:**
- μ_1 = 3
- μ_2 = 3
- μ_3 = 3

**Final Answer for (b) / 第(b)问最终答案:**
- **Return probability / 返回概率:** m_i = 1 for all i. / 对所有 i，m_i = 1。
- **Expected return time / 期望返回时间:** μ_i = 3 for all i. / 对所有 i，μ_i = 3。

**(c) Stationary Distribution / 平稳分布**

**Step 1: Set up the global balance equations / 建立全局平衡方程**

**中文思路 / Chinese reasoning:**
平稳分布 π = (π₁, π₂, π₃) 是一个概率分布，满足 π = πP。这意味着 π 是转移矩阵 P 的左特征向量，特征值为1。我们写出这个向量方程。

**English reasoning:**
The stationary distribution π = (π₁, π₂, π₃) is a probability distribution that satisfies π = πP. This means π is a left eigenvector of the transition matrix P with eigenvalue 1. We write out this vector equation.

**计算过程 / Working:**
π = πP
(π₁, π₂, π₃) = (π₁, π₂, π₃) $$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{pmatrix}
$$

**Step 2: Derive the system of equations / 推导方程组**

**中文思路 / Chinese reasoning:**
进行矩阵乘法，我们得到三个方程。第一个分量：π₁ = 0*π₁ + 0*π₂ + 1*π₃ = π₃。第二个分量：π₂ = 1*π₁ + 0*π₂ + 0*π₃ = π₁。第三个分量：π₃ = 0*π₁ + 1*π₂ + 0*π₃ = π₂。此外，我们还有归一化条件：所有概率之和为1。

**English reasoning:**
Performing the matrix multiplication, we obtain three equations. The first component: π₁ = 0*π₁ + 0*π₂ + 1*π₃ = π₃. The second component: π₂ = 1*π₁ + 0*π₂ + 0*π₃ = π₁. The third component: π₃ = 0*π₁ + 1*π₂ + 0*π₃ = π₂. Additionally, we have the normalization condition: the sum of all probabilities is 1.

**计算过程 / Working:**
From π = πP, we get:
1. π₁ = π₃
2. π₂ = π₁
3. π₃ = π₂
And the normalization condition:
4. π₁ + π₂ + π₃ = 1

**Step 3: Solve the system / 解方程组**

**中文思路 / Chinese reasoning:**
从方程2，我们有 π₂ = π₁。从方程1，我们有 π₃ = π₁。所以所有三个分量都相等。设 π₁ = c，则 π₂ = c，π₃ = c。代入归一化条件：c + c + c = 3c = 1，所以 c = 1/3。因此平稳分布是 (1/3, 1/3, 1/3)。

**English reasoning:**
From equation 2, we have π₂ = π₁. From equation 1, we have π₃ = π₁. So all three components are equal. Let π₁ = c, then π₂ = c, π₃ = c. Substituting into the normalization condition: c + c + c = 3c = 1, so c = 1/3. Therefore, the stationary distribution is (1/3, 1/3, 1/3).

**计算过程 / Working:**
From (1), (2), (3): π₁ = π₂ = π₃.
Let π₁ = π₂ = π₃ = c.
From (4): 3c = 1 ⇒ c = 1/3.
Thus, π = (1/3, 1/3, 1/3).

**Step 4: Confirm the expected return times / 确认期望返回时间**

**中文思路 / Chinese reasoning:**
对于不可约的马尔可夫链，平稳分布与期望返回时间之间存在一个重要的关系：μᵢ = 1/πᵢ。这里 πᵢ = 1/3，所以 μᵢ = 1/(1/3) = 3。这与我们在(b)部分计算的结果一致，验证了我们的解答。

**English reasoning:**
For an irreducible Markov chain, there is an important relationship between the stationary distribution and the expected return time: μᵢ = 1/πᵢ. Here πᵢ = 1/3, so μᵢ = 1/(1/3) = 3. This matches the result we calculated in part (b), confirming our solution.

**计算过程 / Working:**
μᵢ = 1/πᵢ = 1/(1/3) = 3. This confirms the values from part (b).

**Final Answer for (c) / 第(c)问最终答案:**
- **Stationary distribution / 平稳分布:** π = (1/3, 1/3, 1/3)
- **Confirmation / 确认:** μᵢ = 1/πᵢ = 3, which matches part (b). / μᵢ = 1/πᵢ = 3，与(b)部分一致。

**(d) Existence of Limiting Distribution / 极限分布的存在性**

**Step 1: Recall the condition for the existence of limits / 回顾极限存在的条件**

**中文思路 / Chinese reasoning:**
对于不可约的马尔可夫链，极限 lim_{n→∞} P(X_n = i) 存在且与初始分布无关，当且仅当链是非周期的。如果链是周期的，那么极限通常不存在，因为概率会随着时间振荡。然而，如果初始分布恰好是平稳分布，那么对于所有 n，P(X_n = i) = πᵢ，所以极限存在且等于 πᵢ。

**English reasoning:**
For an irreducible Markov chain, the limit lim_{n→∞} P(X_n = i) exists and is independent of the initial distribution if and only if the chain is aperiodic. If the chain is periodic, the limit generally does not exist because the probabilities oscillate over time. However, if the initial distribution happens to be the stationary distribution, then for all n, P(X_n = i) = πᵢ, so the limit exists and equals πᵢ.

**Step 2: Apply to this chain / 应用于此链**

**中文思路 / Chinese reasoning:**
我们的链是周期的（周期为3），所以对于大多数初始分布，极限 lim_{n→∞} P(X_n = i) 不存在。例如，如果从状态1开始，那么 P(X_n = 1) 在 n=0,3,6,... 时为1，在其他时候为0，所以它不收敛。唯一的例外是当初始分布 λ 等于平稳分布 π = (1/3, 1/3, 1/3) 时。在这种情况下，链是平稳的，所以对于所有 n，P(X_n = i) = 1/3，极限存在。

**English reasoning:**
Our chain is periodic (period 3), so for most initial distributions, the limit lim_{n→∞} P(X_n = i) does not exist. For example, if we start from state 1, then P(X_n = 1) is 1 when n=0,3,6,... and 0 otherwise, so it does not converge. The only exception is when the initial distribution λ equals the stationary distribution π = (1/3, 1/3, 1/3). In this case, the chain is stationary, so P(X_n = i) = 1/3 for all n, and the limit exists.

**Final Answer for (d) / 第(d)问最终答案:**
The limits exist if and only if the initial distribution λ is the stationary distribution π = (1/3, 1/3, 1/3). / 极限存在当且仅当初始分布 λ 是平稳分布 π = (1/3, 1/3, 1/3)。

**(e) Long-run Proportion of Time / 长期时间比例**

**Step 1: Relate long-run proportion to stationary distribution / 将长期比例与平稳分布联系起来**

**中文思路 / Chinese reasoning:**
对于不可约的马尔可夫链，无论初始分布如何，长期来看，在每个状态上花费的时间比例等于该状态的平稳分布概率。这是遍历定理的一个结果。

**English reasoning:**
For an irreducible Markov chain, regardless of the initial distribution, the long-run proportion of time spent in each state equals the stationary distribution probability for that state. This is a result of the ergodic theorem.

**Step 2: State the result / 陈述结果**

**中文思路 / Chinese reasoning:**
因此，长期来看，在状态1、2和3上花费的时间比例都是 1/3。

**English reasoning:**
Therefore, in the long run, the proportion of time spent in states 1, 2, and 3 is each 1/3.

**Final Answer for (e) / 第(e)问最终答案:**
The long-run proportion of time spent in each state is 1/3. / 长期来看，在每个状态上花费的时间比例是 1/3。

**Key Insight / 解题要点:**
This problem demonstrates the relationship between the structure of a Markov chain (irreducibility, periodicity) and its limiting behavior. The stationary distribution exists for all irreducible finite chains, but the limiting distribution only exists if the chain is also aperiodic. The expected return time is the reciprocal of the stationary probability. / 本题展示了马尔可夫链的结构（不可约性、周期性）与其极限行为之间的关系。所有不可约的有限链都存在平稳分布，但极限分布仅当链也是非周期时才存在。期望返回时间是平稳概率的倒数。

---

### Question 2 / 第2题

**Problem / 题目原文:**
This question is a bit more difficult because the underlying Markov chain needs to be extracted from the biological explanation, once this is done it is more straightforward.
Every person has two chromosomes; each chromosome is a copy of a chromosome from one of the person’s parents. There are two types of chromosome, which are conventionally labelled X and Y. A child born with a Y chromosome is male, while a child with two X chromosomes is female.
Haemophilia is a blood-clotting disorder caused by a defective X chromosome (we will label this as X∗). Females with the defective chromosome (X∗X) will not typically show symptoms of the disease but can pass it on to children – they are “carriers”. Males with the defective chromosome (X∗Y) have the disease and its symptoms.
A medical statistician is studying the progress of the disease through first-born children, starting with a female carrier. The statistician makes the following assumptions: First, each parent has an equal probability of passing either of their chromosomes to their children. Second, the partner of each person in the study does not have a defective X chromosome. Third, no new genetic disorders occur.
(a) Show that we can use a Markov chain to model the progress of the disease under the above assumptions. What is the state space? Draw a transition diagram.
(b) What are the communicating classes in the chain? Is each class positive recurrent, null recurrent, or transient?
(c) Calculate a stationary distribution. Is this the only stationary distribution?
(d) Under this model, what is the limiting probability that, in many generations’ time, a child has haemophilia?

**中文翻译 / Chinese Translation:**
这个问题稍微难一些，因为需要从生物学解释中提取出潜在的马尔可夫链，一旦完成这一步，问题就相对直接了。
每个人都有两条染色体；每条染色体都是来自父母一方的一条染色体的副本。染色体有两种类型，通常标记为 X 和 Y。出生时带有 Y 染色体的孩子是男性，而带有两条 X 染色体的孩子是女性。
血友病是一种凝血障碍，由有缺陷的 X 染色体（我们将其标记为 X∗）引起。带有缺陷染色体（X∗X）的女性通常不会表现出疾病症状，但可以将其传给子女——她们是“携带者”。带有缺陷染色体（X∗Y）的男性患有该疾病并表现出症状。
一位医学统计学家正在研究该疾病在头胎子女中的进展，从一位女性携带者开始。统计学家做出以下假设：第一，每个父母有相等的概率将他们的任一条染色体传给子女。第二，研究中每个人的伴侣都没有有缺陷的 X 染色体。第三，不会发生新的遗传疾病。
(a) 证明在上述假设下，我们可以使用马尔可夫链来模拟疾病的进展。状态空间是什么？画出转移图。
(b) 该链中的通信类是什么？每个类是正常返、零常返还是瞬过的？
(c) 计算一个平稳分布。这是唯一的平稳分布吗？
(d) 根据这个模型，在许多代之后，一个孩子患有血友病的极限概率是多少？

**Knowledge Points / 考查知识点:**
- 从现实问题中提取马尔可夫链模型 (Extracting a Markov chain model from a real-world problem)
- 状态空间的定义 (Definition of state space)
- 通信类、常返性与瞬过性 (Communicating classes, recurrence, and transience)
- 平稳分布的计算与唯一性 (Calculation and uniqueness of stationary distribution)
- 吸收概率与极限概率 (Absorption probabilities and limiting probabilities)

**Step-by-Step Solution / 逐步解答:**

**(a) Markov Chain Model, State Space, and Transition Diagram / 马尔可夫链模型、状态空间与转移图**

**Step 1: Define the states / 定义状态**

**中文思路 / Chinese reasoning:**
我们需要定义一个状态，它能捕捉到疾病在代际间传播所需的所有信息。由于我们关注的是头胎子女，并且假设伴侣是健康的（没有缺陷的 X 染色体），所以下一代的基因型完全由当前代的基因型决定。可能的状态是：
- 状态 1: 女性携带者 (X∗X)。她有一条缺陷染色体和一条正常染色体。
- 状态 2: 患病男性 (X∗Y)。他有一条缺陷染色体和一条 Y 染色体。
- 状态 3: 健康女性 (XX)。她有两条正常染色体。
- 状态 4: 健康男性 (XY)。他有一条正常染色体和一条 Y 染色体。
注意：我们不考虑患病女性 (X∗X∗)，因为假设伴侣健康，这不可能发生。我们也不考虑女性携带者与患病男性结婚的情况，因为我们的模型只追踪一条家族线，且伴侣总是健康的。

**English reasoning:**
We need to define a state that captures all the information needed to propagate the disease across generations. Since we focus on first-born children and assume partners are healthy (no defective X chromosome), the genotype of the next generation is completely determined by the genotype of the current generation. The possible states are:
- State 1: Female carrier (X∗X). She has one defective and one normal chromosome.
- State 2: Affected male (X∗Y). He has one defective chromosome and one Y chromosome.
- State 3: Healthy female (XX). She has two normal chromosomes.
- State 4: Healthy male (XY). He has one normal chromosome and one Y chromosome.
Note: We do not consider affected females (X∗X∗) because, given the healthy partner assumption, this is impossible. We also do not consider a female carrier marrying an affected male, as our model follows only one family line and partners are always healthy.

**Step 2: Calculate transition probabilities / 计算转移概率**

**中文思路 / Chinese reasoning:**
现在，对于每个状态，我们计算其头胎子女的基因型概率。记住，每个父母随机传递一条染色体给子女，且伴侣是健康的（XX 或 XY）。
- **从女性携带者 (X∗X) 开始**: 她可以传递 X∗ 或 X，概率各为 1/2。她的健康伴侣 (XY) 可以传递 X 或 Y，概率各为 1/2。所以子女的基因型是：
    - X∗X (女性携带者): 概率 = P(母亲给 X∗) * P(父亲给 X) = (1/2)*(1/2) = 1/4
    - X∗Y (患病男性): 概率 = P(母亲给 X∗) * P(父亲给 Y) = (1/2)*(1/2) = 1/4
    - XX (健康女性): 概率 = P(母亲给 X) * P(父亲给 X) = (1/2)*(1/2) = 1/4
    - XY (健康男性): 概率 = P(母亲给 X) * P(父亲给 Y) = (1/2)*(1/2) = 1/4
- **从患病男性 (X∗Y) 开始**: 他可以传递 X∗ 或 Y，概率各为 1/2。他的健康伴侣 (XX) 只能传递 X。所以子女的基因型是：
    - X∗X (女性携带者): 概率 = P(父亲给 X∗) * P(母亲给 X) = (1/2)*1 = 1/2
    - XY (健康男性): 概率 = P(父亲给 Y) * P(母亲给 X) = (1/2)*1 = 1/2
    - 注意：不可能有患病男性 (X∗Y) 或健康女性 (XX) 作为子女，因为母亲只能给 X。
- **从健康女性 (XX) 开始**: 她只能传递 X。她的健康伴侣 (XY) 可以传递 X 或 Y，概率各为 