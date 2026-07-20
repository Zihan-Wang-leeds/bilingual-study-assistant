# Problem Sheet 5 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:04
> 来源页 / Source Pages: 60-61

---

好的，作为您的大学随机过程数学导师，我将为您提供MATH2702课程问题集5的完整、详细的双语解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Find a stationary distribution for the Markov chain with transition matrix
P = $$
\begin{pmatrix}
1/3 & 2/3 & 0 \\
1/6 & 1/3 & 1/2 \\
0 & 1/3 & 2/3
\end{pmatrix}
$$
.
Is the Markov chain reversible?

**中文翻译 / Chinese Translation:**
求具有以下转移矩阵的马尔可夫链的平稳分布：
P = $$
\begin{pmatrix}
1/3 & 2/3 & 0 \\
1/6 & 1/3 & 1/2 \\
0 & 1/3 & 2/3
\end{pmatrix}
$$
.
这个马尔可夫链是可逆的吗？

**Knowledge Points / 考查知识点:**
- **平稳分布 (Stationary Distribution):** 求解满足 πP = π 且 ∑πᵢ = 1 的概率分布向量 π。
- **细致平衡条件 (Detailed Balance Condition):** 判断马尔可夫链是否可逆的条件：πᵢ Pᵢⱼ = πⱼ Pⱼᵢ 对所有 i, j 成立。

**Step-by-Step Solution / 逐步解答:**

**Step 1: 建立方程求解平稳分布 / Set up equations to find the stationary distribution**

1.  **中文思路 / Chinese reasoning:**
    平稳分布 π = (π₁, π₂, π₃) 是一个行向量，满足 πP = π。这意味着 π 是转移矩阵 P 的左特征向量，对应特征值为1。我们将写出这个向量方程，并将其转化为一个线性方程组。同时，由于 π 是一个概率分布，我们还需要满足归一化条件 π₁ + π₂ + π₃ = 1。

2.  **English reasoning:**
    The stationary distribution π = (π₁, π₂, π₃) is a row vector that satisfies πP = π. This means π is a left eigenvector of the transition matrix P corresponding to eigenvalue 1. We will write out this vector equation and convert it into a system of linear equations. Additionally, since π is a probability distribution, it must satisfy the normalization condition π₁ + π₂ + π₃ = 1.

3.  **计算过程 / Working:**
    方程 πP = π 可以写成：
    \[
    (\pi_1, \pi_2, \pi_3) $$
\begin{pmatrix} 1/3 & 2/3 & 0 \\ 1/6 & 1/3 & 1/2 \\ 0 & 1/3 & 2/3 \end{pmatrix}
$$ = (\pi_1, \pi_2, \pi_3)
    \]
    这给出了三个方程：
    - 对于状态1 (j=1): π₁*(1/3) + π₂*(1/6) + π₃*(0) = π₁
    - 对于状态2 (j=2): π₁*(2/3) + π₂*(1/3) + π₃*(1/3) = π₂
    - 对于状态3 (j=3): π₁*(0) + π₂*(1/2) + π₃*(2/3) = π₃

4.  **过程解释 / Explanation of working:**
    矩阵乘法 πP 的结果是一个行向量，其第 j 个分量是 ∑ᵢ πᵢ Pᵢⱼ。这个分量必须等于 πⱼ。我们根据这个规则写出了每个状态的方程。

**Step 2: 化简方程组 / Simplify the system of equations**

1.  **中文思路 / Chinese reasoning:**
    我们可以简化这些方程。注意，这三个方程并不是线性独立的（因为转移矩阵的每一行和为1，导致它们线性相关）。我们可以使用其中两个方程，并结合归一化条件来求解。

2.  **English reasoning:**
    We can simplify these equations. Note that these three equations are not linearly independent (because each row of the transition matrix sums to 1, they are linearly dependent). We can use two of them along with the normalization condition to solve for the unknowns.

3.  **计算过程 / Working:**
    从第一个方程开始：
    \[
    \frac{1}{3}\pi_1 + \frac{1}{6}\pi_2 = \pi_1
    \]
    两边乘以6：
    \[
    2\pi_1 + \pi_2 = 6\pi_1 \implies \pi_2 = 4\pi_1
    \]
    从第三个方程：
    \[
    \frac{1}{2}\pi_2 + \frac{2}{3}\pi_3 = \pi_3
    \]
    两边乘以6：
    \[
    3\pi_2 + 4\pi_3 = 6\pi_3 \implies 3\pi_2 = 2\pi_3 \implies \pi_3 = \frac{3}{2}\pi_2
    \]
    将 π₂ = 4π₁ 代入 π₃ 的表达式：
    \[
    \pi_3 = \frac{3}{2} (4\pi_1) = 6\pi_1
    \]
    现在使用归一化条件：
    \[
    \pi_1 + \pi_2 + \pi_3 = 1 \implies \pi_1 + 4\pi_1 + 6\pi_1 = 1 \implies 11\pi_1 = 1 \implies \pi_1 = \frac{1}{11}
    \]
    因此：
    \[
    \pi_2 = 4\pi_1 = \frac{4}{11}, \quad \pi_3 = 6\pi_1 = \frac{6}{11}
    \]

4.  **过程解释 / Explanation of working:**
    我们通过代数操作将方程简化为变量之间的关系。π₂ = 4π₁ 和 π₃ = 6π₁。然后，我们利用所有概率之和必须为1这一事实来求解 π₁，进而得到其他分量。我们可以用第二个方程来验证我们的解：π₁*(2/3) + π₂*(1/3) + π₃*(1/3) = (1/11)*(2/3) + (4/11)*(1/3) + (6/11)*(1/3) = (2+4+6)/(33) = 12/33 = 4/11 = π₂。结果正确。

**Step 3: 检查可逆性 / Check for reversibility**

1.  **中文思路 / Chinese reasoning:**
    一个马尔可夫链是可逆的，如果它存在一个平稳分布 π，使得对所有状态 i, j，细致平衡条件 πᵢ Pᵢⱼ = πⱼ Pⱼᵢ 都成立。我们只需要检查一个不满足该条件的例子，就可以证明链不可逆。

2.  **English reasoning:**
    A Markov chain is reversible if there exists a stationary distribution π such that the detailed balance condition πᵢ Pᵢⱼ = πⱼ Pⱼᵢ holds for all states i, j. We only need to find one pair (i, j) for which this condition fails to prove the chain is not reversible.

3.  **计算过程 / Working:**
    检查状态1和状态2 (i=1, j=2):
    \[
    \pi_1 P_{12} = \frac{1}{11} \times \frac{2}{3} = \frac{2}{33}
    \]
    \[
    \pi_2 P_{21} = \frac{4}{11} \times \frac{1}{6} = \frac{4}{66} = \frac{2}{33}
    \]
    对于 (1,2)，细致平衡成立。
    检查状态2和状态3 (i=2, j=3):
    \[
    \pi_2 P_{23} = \frac{4}{11} \times \frac{1}{2} = \frac{4}{22} = \frac{2}{11}
    \]
    \[
    \pi_3 P_{32} = \frac{6}{11} \times \frac{1}{3} = \frac{6}{33} = \frac{2}{11}
    \]
    对于 (2,3)，细致平衡也成立。
    检查状态1和状态3 (i=1, j=3):
    \[
    \pi_1 P_{13} = \frac{1}{11} \times 0 = 0
    \]
    \[
    \pi_3 P_{31} = \frac{6}{11} \times 0 = 0
    \]
    对于 (1,3)，细致平衡也成立。

4.  **过程解释 / Explanation of working:**
    我们检查了所有非零转移概率的对。由于 P₁₃ = 0 且 P₃₁ = 0，条件自动满足。对于其他对，我们代入计算出的 π 值，发现等式成立。因此，对于这个特定的链，细致平衡条件对所有 i, j 都成立。

**Final Answer / 最终答案:**
- **平稳分布 (Stationary Distribution):** 平稳分布为 π = (1/11, 4/11, 6/11)。
    The stationary distribution is π = (1/11, 4/11, 6/11).
- **可逆性 (Reversibility):** 是的，这个马尔可夫链是可逆的，因为它满足细致平衡条件。
    Yes, the Markov chain is reversible because it satisfies the detailed balance condition.

**Key Insight / 解题要点:**
- 求解平稳分布的核心是解线性方程组 πP = π 和 ∑πᵢ = 1。
    The core of finding a stationary distribution is solving the linear system πP = π and ∑πᵢ = 1.
- 可逆性由细致平衡条件 πᵢ Pᵢⱼ = πⱼ Pⱼᵢ 判定。如果链是可逆的，那么从平稳分布出发，正向和反向过程的概率流是平衡的。
    Reversibility is determined by the detailed balance condition πᵢ Pᵢⱼ = πⱼ Pⱼᵢ. If a chain is reversible, starting from the stationary distribution, the probability flow forward and backward is balanced.

---

### Question 2 / 第2题

**Problem / 题目原文:**
Consider a Markov chain with state space 𝑆= {1, 2, 3, 4} and transition matrix
P =
$$
\begin{pmatrix}
1/4   1/2   1/4   0 \\
1/4   1/4   1/2   0 \\
1/2   1/2   0     0 \\
1/4   0     1/4   1/2
\end{pmatrix}
$$
.
(a) Draw a transition diagram for this Markov chain.
(b) Identify the communicating classes. State whether each class is closed or not. State whether each class is positive recurrent, null recurrent, or transient.
(c) Find a stationary distribution for this Markov chain. Is the Markov chain reversible?
(d) Is this the only stationary distribution?

**中文翻译 / Chinese Translation:**
考虑一个状态空间为 𝑆= {1, 2, 3, 4} 的马尔可夫链，其转移矩阵为
P =
$$
\begin{pmatrix}
1/4   1/2   1/4   0 \\
1/4   1/4   1/2   0 \\
1/2   1/2   0     0 \\
1/4   0     1/4   1/2
\end{pmatrix}
$$
.
(a) 画出这个马尔可夫链的转移图。
(b) 识别出所有通信类。说明每个类是否是封闭的。说明每个类是正常返的、零常返的还是瞬过的。
(c) 求这个马尔可夫链的一个平稳分布。这个马尔可夫链是可逆的吗？
(d) 这是唯一的平稳分布吗？

**Knowledge Points / 考查知识点:**
- **转移图 (Transition Diagram):** 用节点表示状态，用有向边和概率表示转移。
- **通信类 (Communicating Classes):** 状态之间的可达与互通关系。
- **封闭类 (Closed Class):** 从类中任何状态出发，都无法到达类外的状态。
- **常返性与瞬过性 (Recurrence and Transience):** 基于有限状态空间马尔可夫链的性质：所有状态要么都是正常返的，要么都是瞬过的。封闭类中的状态是正常返的，非封闭类中的状态是瞬过的。
- **平稳分布 (Stationary Distribution):** 求解 πP = π。
- **可逆性 (Reversibility):** 检查细致平衡条件。
- **平稳分布的唯一性 (Uniqueness of Stationary Distribution):** 一个不可约的马尔可夫链有唯一的平稳分布。如果链是可约的，则可能有多个平稳分布。

**Step-by-Step Solution / 逐步解答:**

**(a) 转移图 / Transition Diagram**

1.  **中文思路 / Chinese reasoning:**
    我们根据转移矩阵 P 来画图。矩阵的第 i 行第 j 列的元素 Pᵢⱼ 表示从状态 i 转移到状态 j 的概率。我们画出4个节点，分别代表状态1、2、3、4。然后，对于每个非零的 Pᵢⱼ，我们从节点 i 画一条带箭头的边到节点 j，并在边上标出概率 Pᵢⱼ。

2.  **English reasoning:**
    We draw the diagram based on the transition matrix P. The element Pᵢⱼ in the i-th row and j-th column represents the probability of transitioning from state i to state j. We draw 4 nodes representing states 1, 2, 3, and 4. Then, for each non-zero Pᵢⱼ, we draw a directed edge from node i to node j, labeling it with the probability Pᵢⱼ.

3.  **计算过程 / Working:**
    - 从状态1: P₁₁=1/4, P₁₂=1/2, P₁₃=1/4, P₁₄=0
    - 从状态2: P₂₁=1/4, P₂₂=1/4, P₂₃=1/2, P₂₄=0
    - 从状态3: P₃₁=1/2, P₃₂=1/2, P₃₃=0, P₃₄=0
    - 从状态4: P₄₁=1/4, P₄₂=0, P₄₃=1/4, P₄₄=1/2

    **转移图 (Transition Diagram):**
    ```
        1/2
      ┌─────┐
      │     ▼
      │   1/4
    ┌─┴─┐     ┌───┐
    │ 1 │◄────│ 2 │
    └─┬─┘ 1/4 └─┬─┘
      │1/4      │1/4
      │   1/2   │
      ▼         ▼
    ┌───┐     ┌───┐
    │ 3 │◄────│ 4 │
    └───┘ 1/4 └───┘
      │         │
      │1/2      │1/2
      └─────────┘
    ```
    *(Note: A more standard diagram would have arrows. Let's describe it clearly:)*
    - 1 → 1 (1/4), 1 → 2 (1/2), 1 → 3 (1/4)
    - 2 → 1 (1/4), 2 → 2 (1/4), 2 → 3 (1/2)
    - 3 → 1 (1/2), 3 → 2 (1/2)
    - 4 → 1 (1/4), 4 → 3 (1/4), 4 → 4 (1/2)

4.  **过程解释 / Explanation of working:**
    我们逐行读取转移矩阵，为每个非零概率绘制一条有向边。注意，从状态3出发，只能到达状态1和2。从状态4出发，可以到达状态1、3和自己。

**(b) 通信类 / Communicating Classes**

1.  **中文思路 / Chinese reasoning:**
    我们通过分析转移图来找出通信类。状态 i 和 j 是互通的，如果从 i 可以到达 j，并且从 j 也可以到达 i。我们检查每个状态对。

2.  **English reasoning:**
    We identify communicating classes by analyzing the transition diagram. States i and j communicate if i can reach j and j can reach i. We check each pair of states.

3.  **计算过程 / Working:**
    - **状态1, 2, 3:** 从图上看，1→2, 2→1, 1→3, 3→1, 2→3, 3→2。所以状态1, 2, 3 两两互通。它们构成一个通信类 C₁ = {1, 2, 3}。
    - **状态4:** 从4可以到达1 (4→1)。但是，从1, 2, 3 能到达4吗？从转移矩阵看，P₁₄=0, P₂₄=0, P₃₄=0。所以从C₁中的任何状态都无法到达状态4。因此，状态4自成一个通信类 C₂ = {4}。
    - **封闭性 (Closedness):**
        - C₁ = {1, 2, 3}: 从C₁中的状态出发，能到达C₁外的状态吗？从1, 2, 3出发，只能到达1, 2, 3 (P₁₄=P₂₄=P₃₄=0)。所以C₁是封闭的。
        - C₂ = {4}: 从状态4出发，可以到达状态1 (P₄₁=1/4)，而状态1在C₁中。所以C₂不是封闭的。
    - **常返/瞬过 (Recurrence/Transience):**
        - 由于状态空间是有限的，所有封闭类中的状态都是正常返的。因此，C₁中的状态1, 2, 3是正常返的。
        - 非封闭类中的状态是瞬过的。因此，C₂中的状态4是瞬过的。

4.  **过程解释 / Explanation of working:**
    我们通过检查可达性来划分通信类。一个类如果无法离开，就是封闭的。在有限状态空间中，封闭类中的状态是正常返的（因为链最终会进入并停留在某个封闭类中），而非封闭类中的状态是瞬过的（因为链最终会离开它并进入一个封闭类）。

**(c) 平稳分布与可逆性 / Stationary Distribution and Reversibility**

1.  **中文思路 / Chinese reasoning:**
    我们求解平稳分布 π = (π₁, π₂, π₃, π₄)，满足 πP = π 和 ∑πᵢ = 1。由于状态4是瞬过的，其平稳概率应为0，即 π₄ = 0。我们只需要对封闭类 C₁ = {1, 2, 3} 求解平稳分布。然后检查细致平衡条件。

2.  **English reasoning:**
    We solve for the stationary distribution π = (π₁, π₂, π₃, π₄) satisfying πP = π and ∑πᵢ = 1. Since state 4 is transient, its stationary probability should be 0, i.e., π₄ = 0. We only need to find the stationary distribution for the closed class C₁ = {1, 2, 3}. Then we check the detailed balance condition.

3.  **计算过程 / Working:**
    **求解平稳分布 (Finding Stationary Distribution):**
    设 π₄ = 0。对于状态1, 2, 3，其转移矩阵的子矩阵为：
    \[
    P' = $$
\begin{pmatrix} 1/4 & 1/2 & 1/4 \\ 1/4 & 1/4 & 1/2 \\ 1/2 & 1/2 & 0 \end{pmatrix}
$$
    \]
    方程 (π₁, π₂, π₃)P' = (π₁, π₂, π₃) 给出：
    - 状态1: (1/4)π₁ + (1/4)π₂ + (1/2)π₃ = π₁
    - 状态2: (1/2)π₁ + (1/4)π₂ + (1/2)π₃ = π₂
    - 状态3: (1/4)π₁ + (1/2)π₂ + 0*π₃ = π₃
    从状态3的方程：π₁/4 + π₂/2 = π₃。两边乘以4：π₁ + 2π₂ = 4π₃。 (1)
    从状态1的方程：π₁/4 + π₂/4 + π₃/2 = π₁。两边乘以4：π₁ + π₂ + 2π₃ = 4π₁ → π₂ + 2π₃ = 3π₁。 (2)
    从状态2的方程：π₁/2 + π₂/4 + π₃/2 = π₂。两边乘以4：2π₁ + π₂ + 2π₃ = 4π₂ → 2π₁ + 2π₃ = 3π₂。 (3)
    从(1)式，π₃ = (π₁ + 2π₂)/4。
    代入(2)式：π₂ + 2*(π₁ + 2π₂)/4 = 3π₁ → π₂ + (π₁ + 2π₂)/2 = 3π₁ → 两边乘以2：2π₂ + π₁ + 2π₂ = 6π₁ → 4π₂ = 5π₁ → π₂ = (5/4)π₁。
    代入π₃表达式：π₃ = (π₁ + 2*(5/4)π₁)/4 = (π₁ + (5/2)π₁)/4 = ((7/2)π₁)/4 = (7/8)π₁。
    归一化条件：π₁ + π₂ + π₃ = 1 → π₁ + (5/4)π₁ + (7/8)π₁ = 1。
    通分乘以8：8π₁ + 10π₁ + 7π₁ = 8 → 25π₁ = 8 → π₁ = 8/25。
    所以 π₂ = (5/4)*(8/25) = 40/100 = 2/5 = 10/25。
    π₃ = (7/8)*(8/25) = 7/25。
    因此，平稳分布为 π = (8/25, 10/25, 7/25, 0) = (8/25, 2/5, 7/25, 0)。

    **检查可逆性 (Checking Reversibility):**
    检查状态1和2：π₁ P₁₂ = (8/25)*(1/2) = 4/25。π₂ P₂₁ = (10/25)*(1/4) = 10/100 = 1/10 = 2.5/25。4/25 ≠ 2.5/25。细致平衡条件不成立。因此，链不可逆。

4.  **过程解释 / Explanation of working:**
    我们首先认识到瞬过状态在平稳分布中概率为0。然后，我们专注于封闭的通信类，并求解其上的平稳分布。我们通过代数消元法求解了线性方程组。最后，我们通过检查一个反例（状态1和2）来证明链不满足细致平衡条件。

**(d) 平稳分布的唯一性 / Uniqueness of Stationary Distribution**

1.  **中文思路 / Chinese reasoning:**
    一个马尔可夫链的平稳分布不一定唯一。唯一性通常与链的不可约性相关。这个链是可约的，因为它有多个通信类。封闭类 C₁ = {1, 2, 3} 本身是一个不可约的马尔可夫链（在其上限制时），因此它在C₁上有唯一的平稳分布。瞬过状态4在平稳分布中概率为0。那么，是否存在其他平稳分布呢？例如，如果链从状态4出发，它最终会进入C₁，所以任何平稳分布都必须将全部概率质量放在C₁上。由于C₁上的平稳分布是唯一的，整个链的平稳分布也是唯一的。

2.  **English reasoning:**
    A Markov chain does not necessarily have a unique stationary distribution. Uniqueness is usually related to the irreducibility of the chain. This chain is reducible because it has multiple communicating classes. The closed class C₁ = {1, 2, 3} is itself an irreducible Markov chain (when restricted to it), so it has a unique stationary distribution on C₁. The transient state 4 has probability 0 in any stationary distribution. Are there other stationary distributions? For instance, if the chain starts in state 4, it will eventually enter C₁, so any stationary distribution must place all probability mass on C₁. Since the stationary distribution on C₁ is unique, the stationary distribution for the whole chain is also unique.

3.  **计算过程 / Working:**
    是的，这是唯一的平稳分布。理由如下：链中唯一的封闭通信类是 C₁ = {1, 2, 3}。任何平稳分布都必须将概率质量仅分配给封闭类中的状态。由于C₁是不可约的，其上的平稳分布是唯一的。瞬过状态4在任何平稳分布中的概率必须为0。因此，整个链的平稳分布是唯一的。

4.  **过程解释 / Explanation of working:**
    平稳分布只存在于封闭的常返类上。如果只有一个封闭类，并且该类是不可约的，那么平稳分布就是唯一的。如果有多个封闭类，那么平稳分布可以是将概率任意分配在这些类上（每个类内部由其唯一的平稳分布决定）的凸组合。

**Final Answer / 最终答案:**
- (a) **转移图 (Transition Diagram):** [见上方图示 / See diagram above]
- (b) **通信类 (Communicating Classes):**
    - C₁ = {1, 2, 3}，