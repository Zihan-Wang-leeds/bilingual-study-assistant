# Problem Sheet 3 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:02
> 来源页 / Source Pages: 38-39

---

好的，作为一名大学数学导师，我将为您提供MATH2702: 随机过程 习题集3的完整双语解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Consider the two-state “broken printer” Markov chain, with state space 𝑆= {0, 1}, transition matrix
P = (1 −𝛼 𝛼; 𝛽 1 −𝛽) with 0 < 𝛼, 𝛽< 1, and initial distribution 𝜆= (𝜆0, 𝜆1). Write 𝜇𝑛= ℙ(𝑋𝑛= 0).
(a) By writing 𝜇𝑛+1 in terms of 𝜇𝑛, show that we have 𝜇𝑛+1 −(1 −(𝛼+ 𝛽))𝜇𝑛= 𝛽.
(b) By solving this linear difference equation using the initial condition 𝜇0 = 𝜆0, or otherwise, show that
𝜇𝑛= 𝛽/(𝛼+ 𝛽) + (𝜆0 − 𝛽/(𝛼+ 𝛽)) (1 −(𝛼+ 𝛽))^𝑛.
(c) What, therefore, are lim𝑛→∞ℙ(𝑋𝑛= 0) and lim𝑛→∞ℙ(𝑋𝑛= 1)?
(d) Explain what happens if the Markov chain is started in the distribution 𝜆0 = 𝛽/(𝛼+ 𝛽), 𝜆1 = 𝛼/(𝛼+ 𝛽).

**中文翻译 / Chinese Translation:**
考虑一个两状态的“坏打印机”马尔可夫链，其状态空间为 𝑆 = {0, 1}，转移矩阵为
P = (1 −𝛼 𝛼; 𝛽 1 −𝛽)，其中 0 < 𝛼, 𝛽< 1，初始分布为 𝜆= (𝜆0, 𝜆1)。定义 𝜇𝑛= ℙ(𝑋𝑛= 0)。
(a) 通过写出 𝜇𝑛+1 关于 𝜇𝑛 的表达式，证明我们有 𝜇𝑛+1 −(1 −(𝛼+ 𝛽))𝜇𝑛= 𝛽。
(b) 通过使用初始条件 𝜇0 = 𝜆0 求解这个线性差分方程，或以其他方式，证明
𝜇𝑛= 𝛽/(𝛼+ 𝛽) + (𝜆0 − 𝛽/(𝛼+ 𝛽)) (1 −(𝛼+ 𝛽))^𝑛。
(c) 因此，lim𝑛→∞ℙ(𝑋𝑛= 0) 和 lim𝑛→∞ℙ(𝑋𝑛= 1) 是什么？
(d) 解释如果马尔可夫链以分布 𝜆0 = 𝛽/(𝛼+ 𝛽), 𝜆1 = 𝛼/(𝛼+ 𝛽) 启动，会发生什么。

**Knowledge Points / 考查知识点:**
- 马尔可夫链的边际分布 / Marginal distribution of a Markov chain
- 全概率公式 / Law of total probability
- 一阶线性差分方程 / First-order linear difference equation
- 平稳分布 / Stationary distribution

**Step-by-Step Solution / 逐步解答:**

**(a)**

**Step 1: 建立 𝜇𝑛+1 的表达式 / Establish the expression for 𝜇𝑛+1**

**中文思路 / Chinese reasoning:**
我们想找到 𝜇𝑛+1 = ℙ(𝑋𝑛+1 = 0) 与 𝜇𝑛 = ℙ(𝑋𝑛 = 0) 之间的关系。这可以通过在给定 𝑋𝑛 的状态下，对 𝑋𝑛+1 的状态应用全概率公式来实现。因为马尔可夫链的性质，𝑋𝑛+1 的概率只依赖于 𝑋𝑛。

**English reasoning:**
We want to find a relationship between 𝜇𝑛+1 = ℙ(𝑋𝑛+1 = 0) and 𝜇𝑛 = ℙ(𝑋𝑛 = 0). This is done by applying the law of total probability to the state of 𝑋𝑛+1, conditioning on the state of 𝑋𝑛. Due to the Markov property, the probability of 𝑋𝑛+1 depends only on 𝑋𝑛.

**计算过程 / Working:**
根据全概率公式，我们有：
𝜇𝑛+1 = ℙ(𝑋𝑛+1 = 0) = ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 0)ℙ(𝑋𝑛 = 0) + ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 1)ℙ(𝑋𝑛 = 1)

**Explanation of working / 过程解释:**
这里我们使用了全概率公式，将事件 {𝑋𝑛+1 = 0} 的概率分解为基于 𝑋𝑛 所有可能状态的加权和。权重是条件概率 ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = i) 和边际概率 ℙ(𝑋𝑛 = i) 的乘积。ℙ(𝑋𝑛 = 1) 可以表示为 1 − 𝜇𝑛。

**Step 2: 代入转移概率 / Substitute transition probabilities**

**中文思路 / Chinese reasoning:**
现在我们从转移矩阵 P 中读取条件概率。P 的第一行第一列元素是 ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 0) = 1 − 𝛼。P 的第二行第一列元素是 ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 1) = 𝛽。将这些值和 ℙ(𝑋𝑛 = 1) = 1 − 𝜇𝑛 代入方程。

**English reasoning:**
Now we read the conditional probabilities from the transition matrix P. The (1,1) entry is ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 0) = 1 − 𝛼. The (2,1) entry is ℙ(𝑋𝑛+1 = 0 | 𝑋𝑛 = 1) = 𝛽. Substitute these values and ℙ(𝑋𝑛 = 1) = 1 − 𝜇𝑛 into the equation.

**计算过程 / Working:**
代入后得到：
𝜇𝑛+1 = (1 − 𝛼)𝜇𝑛 + 𝛽(1 − 𝜇𝑛)

**Explanation of working / 过程解释:**
这个方程直接来自于上一步的全概率公式。它表达了 𝜇𝑛+1 是 𝜇𝑛 的一个线性函数。

**Step 3: 化简方程 / Simplify the equation**

**中文思路 / Chinese reasoning:**
我们展开并合并 𝜇𝑛 的项，以得到一个更简洁的线性差分方程形式。

**English reasoning:**
We expand and combine the terms involving 𝜇𝑛 to get a cleaner form of the linear difference equation.

**计算过程 / Working:**
𝜇𝑛+1 = (1 − 𝛼)𝜇𝑛 + 𝛽 − 𝛽𝜇𝑛
𝜇𝑛+1 = 𝛽 + (1 − 𝛼 − 𝛽)𝜇𝑛
𝜇𝑛+1 = 𝛽 + (1 − (𝛼 + 𝛽))𝜇𝑛

**Explanation of working / 过程解释:**
展开括号得到 (1−𝛼)𝜇𝑛 + 𝛽 − 𝛽𝜇𝑛。合并 𝜇𝑛 的系数：1−𝛼−𝛽 = 1−(𝛼+𝛽)。最后，将常数项 𝛽 移到左边，𝜇𝑛 项移到右边，得到所需的形式。

**Step 4: 重写为所需形式 / Rewrite to the required form**

**中文思路 / Chinese reasoning:**
将上一步得到的方程稍作整理，将 𝜇𝑛+1 项和 𝜇𝑛 项放在等号左边，常数项放在右边。

**English reasoning:**
Rearrange the equation from the previous step to put the terms involving 𝜇𝑛+1 and 𝜇𝑛 on the left-hand side and the constant term on the right.

**计算过程 / Working:**
将 𝜇𝑛+1 = 𝛽 + (1 − (𝛼 + 𝛽))𝜇𝑛 移项，得到：
𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 𝛽

**Explanation of working / 过程解释:**
这完成了 (a) 部分的证明。我们展示了 𝜇𝑛+1 和 𝜇𝑛 满足这个一阶线性非齐次差分方程。

**(b)**

**Step 1: 识别差分方程类型 / Identify the type of difference equation**

**中文思路 / Chinese reasoning:**
我们有一个一阶线性非齐次差分方程：𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 𝛽。解这个方程的标准方法是先找到齐次解，再找到一个特解，然后应用初始条件。

**English reasoning:**
We have a first-order linear non-homogeneous difference equation: 𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 𝛽. The standard method to solve this is to find the homogeneous solution, then a particular solution, and then apply the initial condition.

**Step 2: 求齐次解 / Find the homogeneous solution**

**中文思路 / Chinese reasoning:**
首先考虑齐次方程：𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 0。这是一个几何级数形式，其解为 𝜇𝑛^(h) = 𝐶(1 − (𝛼 + 𝛽))^𝑛，其中 𝐶 是常数。

**English reasoning:**
First, consider the homogeneous equation: 𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 0. This is a geometric progression, and its solution is of the form 𝜇𝑛^(h) = 𝐶(1 − (𝛼 + 𝛽))^𝑛, where 𝐶 is a constant.

**计算过程 / Working:**
齐次方程：𝜇𝑛+1 = (1 − (𝛼 + 𝛽))𝜇𝑛
解的形式：𝜇𝑛^(h) = 𝐶(1 − (𝛼 + 𝛽))^𝑛

**Explanation of working / 过程解释:**
齐次解描述了系统的“自然”动态，即没有外部“驱动”项 𝛽 时的行为。

**Step 3: 求特解 / Find a particular solution**

**中文思路 / Chinese reasoning:**
由于非齐次项是常数 𝛽，我们尝试一个常数特解，设 𝜇𝑛^(p) = 𝐾。将其代入原非齐次方程，解出 𝐾。

**English reasoning:**
Since the non-homogeneous term is a constant 𝛽, we try a constant particular solution, let 𝜇𝑛^(p) = 𝐾. Substitute this into the original non-homogeneous equation to solve for 𝐾.

**计算过程 / Working:**
设 𝜇𝑛^(p) = 𝐾。代入 𝜇𝑛+1 − (1 − (𝛼 + 𝛽))𝜇𝑛 = 𝛽：
𝐾 − (1 − (𝛼 + 𝛽))𝐾 = 𝛽
𝐾(1 − 1 + (𝛼 + 𝛽)) = 𝛽
𝐾(𝛼 + 𝛽) = 𝛽
𝐾 = 𝛽/(𝛼 + 𝛽)

**Explanation of working / 过程解释:**
常数特解对应于系统的长期平衡或稳态行为，前提是它存在。

**Step 4: 写出通解 / Write the general solution**

**中文思路 / Chinese reasoning:**
通解是齐次解和特解之和：𝜇𝑛 = 𝜇𝑛^(h) + 𝜇𝑛^(p)。

**English reasoning:**
The general solution is the sum of the homogeneous solution and the particular solution: 𝜇𝑛 = 𝜇𝑛^(h) + 𝜇𝑛^(p).

**计算过程 / Working:**
𝜇𝑛 = 𝐶(1 − (𝛼 + 𝛽))^𝑛 + 𝛽/(𝛼 + 𝛽)

**Explanation of working / 过程解释:**
这个通解包含了任意常数 𝐶，它由初始条件确定。

**Step 5: 应用初始条件 / Apply the initial condition**

**中文思路 / Chinese reasoning:**
我们已知初始条件 𝜇0 = ℙ(𝑋0 = 0) = 𝜆0。将 𝑛 = 0 代入通解，解出常数 𝐶。

**English reasoning:**
We are given the initial condition 𝜇0 = ℙ(𝑋0 = 0) = 𝜆0. Substitute 𝑛 = 0 into the general solution to solve for the constant 𝐶.

**计算过程 / Working:**
当 𝑛 = 0 时：
𝜇0 = 𝐶(1 − (𝛼 + 𝛽))^0 + 𝛽/(𝛼 + 𝛽)
𝜆0 = 𝐶 + 𝛽/(𝛼 + 𝛽)
𝐶 = 𝜆0 − 𝛽/(𝛼 + 𝛽)

**Explanation of working / 过程解释:**
因为 (1 − (𝛼 + 𝛽))^0 = 1，所以方程简化为 𝜆0 = 𝐶 + 𝛽/(𝛼 + 𝛽)。移项即可得到 𝐶 的值。

**Step 6: 写出最终解 / Write the final solution**

**中文思路 / Chinese reasoning:**
将求得的常数 𝐶 代回通解，得到满足初始条件的特解。

**English reasoning:**
Substitute the found constant 𝐶 back into the general solution to obtain the particular solution that satisfies the initial condition.

**计算过程 / Working:**
𝜇𝑛 = (𝜆0 − 𝛽/(𝛼 + 𝛽)) (1 − (𝛼 + 𝛽))^𝑛 + 𝛽/(𝛼 + 𝛽)

**Explanation of working / 过程解释:**
这完成了 (b) 部分的证明。这个公式给出了在任意时间步 𝑛，链处于状态 0 的概率。

**(c)**

**Step 1: 求极限 / Find the limit**

**中文思路 / Chinese reasoning:**
因为 0 < 𝛼, 𝛽 < 1，所以 0 < 𝛼 + 𝛽 < 2。因此，|1 − (𝛼 + 𝛽)| < 1 当且仅当 0 < 𝛼 + 𝛽 < 2。由于 𝛼, 𝛽 是正数且小于 1，它们的和可能小于 2，但我们需要检查是否可能大于 1。如果 𝛼 + 𝛽 > 1，那么 1 − (𝛼 + 𝛽) 是负数，但其绝对值仍小于 1。所以，当 𝑛 → ∞ 时，(1 − (𝛼 + 𝛽))^𝑛 → 0。

**English reasoning:**
Since 0 < 𝛼, 𝛽 < 1, we have 0 < 𝛼 + 𝛽 < 2. Therefore, |1 − (𝛼 + 𝛽)| < 1 if and only if 0 < 𝛼 + 𝛽 < 2. Since 𝛼, 𝛽 are positive and less than 1, their sum could be less than 2, but we need to check if it can be greater than 1. If 𝛼 + 𝛽 > 1, then 1 − (𝛼 + 𝛽) is negative, but its absolute value is still less than 1. So, as 𝑛 → ∞, (1 − (𝛼 + 𝛽))^𝑛 → 0.

**计算过程 / Working:**
lim_{𝑛→∞} 𝜇𝑛 = lim_{𝑛→∞} [𝛽/(𝛼 + 𝛽) + (𝜆0 − 𝛽/(𝛼 + 𝛽)) (1 − (𝛼 + 𝛽))^𝑛]
由于 |1 − (𝛼 + 𝛽)| < 1，lim_{𝑛→∞} (1 − (𝛼 + 𝛽))^𝑛 = 0。
因此，lim_{𝑛→∞} 𝜇𝑛 = 𝛽/(𝛼 + 𝛽)。

**Explanation of working / 过程解释:**
当 𝑛 趋于无穷大时，包含 (1 − (𝛼 + 𝛽))^𝑛 的项衰减到零。因此，ℙ(𝑋𝑛 = 0) 的极限是 𝛽/(𝛼 + 𝛽)，它与初始分布 𝜆0 无关。

**Step 2: 求另一个极限 / Find the other limit**

**中文思路 / Chinese reasoning:**
由于链必须处于状态 0 或状态 1，所以 ℙ(𝑋𝑛 = 1) = 1 − ℙ(𝑋𝑛 = 0)。因此，我们可以直接计算其极限。

**English reasoning:**
Since the chain must be in either state 0 or state 1, ℙ(𝑋𝑛 = 1) = 1 − ℙ(𝑋𝑛 = 0). Therefore, we can directly compute its limit.

**计算过程 / Working:**
lim_{𝑛→∞} ℙ(𝑋𝑛 = 1) = 1 − lim_{𝑛→∞} ℙ(𝑋𝑛 = 0) = 1 − 𝛽/(𝛼 + 𝛽) = (𝛼 + 𝛽 − 𝛽)/(𝛼 + 𝛽) = 𝛼/(𝛼 + 𝛽)

**Explanation of working / 过程解释:**
这个极限分布 (𝛽/(𝛼+𝛽), 𝛼/(𝛼+𝛽)) 是马尔可夫链的平稳分布。

**(d)**

**Step 1: 分析初始分布 / Analyze the initial distribution**

**中文思路 / Chinese reasoning:**
如果链以分布 (𝜆0, 𝜆1) = (𝛽/(𝛼+𝛽), 𝛼/(𝛼+𝛽)) 启动，那么这个分布正是我们在 (c) 部分找到的极限分布（平稳分布）。

**English reasoning:**
If the chain is started with the distribution (𝜆0, 𝜆1) = (𝛽/(𝛼+𝛽), 𝛼/(𝛼+𝛽)), this distribution is exactly the limiting distribution (stationary distribution) we found in part (c).

**Step 2: 解释结果 / Explain the result**

**中文思路 / Chinese reasoning:**
当链从平稳分布开始时，它在所有未来时间步都保持这个分布。这意味着对于所有 𝑛，ℙ(𝑋𝑛 = 0) = 𝛽/(𝛼+𝛽) 且 ℙ(𝑋𝑛 = 1) = 𝛼/(𝛼+𝛽)。链是平稳的。

**English reasoning:**
When the chain starts from the stationary distribution, it remains in this distribution for all future time steps. This means that for all 𝑛, ℙ(𝑋𝑛 = 0) = 𝛽/(𝛼+𝛽) and ℙ(𝑋𝑛 = 1) = 𝛼/(𝛼+𝛽). The chain is stationary.

**计算过程 / Working:**
将 𝜆0 = 𝛽/(𝛼+𝛽) 代入 (b) 部分的公式：
𝜇𝑛 = 𝛽/(𝛼+𝛽) + (𝛽/(𝛼+𝛽) − 𝛽/(𝛼+𝛽)) (1 − (𝛼+𝛽))^𝑛 = 𝛽/(𝛼+𝛽)
因此，对于所有 𝑛，𝜇𝑛 = 𝛽/(𝛼+𝛽)，并且 ℙ(𝑋𝑛 = 1) = 1 − 𝛽/(𝛼+𝛽) = 𝛼/(𝛼+𝛽)。

**Explanation of working / 过程解释:**
因为初始条件等于特解，所以齐次部分的系数为零。因此，概率不随时间变化，链立即进入稳态。

**Final Answer / 最终答案:**
(a) 证明完成 / Proof complete.
(b) 证明完成 / Proof complete.
(c) lim_{𝑛→∞} ℙ(𝑋𝑛 = 0) = 𝛽/(𝛼+𝛽), lim_{𝑛→∞} ℙ(𝑋𝑛 = 1) = 𝛼/(𝛼+𝛽)
(d) 如果链从分布 (𝛽/(𝛼+𝛽), 𝛼/(𝛼+𝛽)) 启动，那么对于所有 𝑛，ℙ(𝑋𝑛 = 0) = 𝛽/(𝛼+𝛽) 且 ℙ(𝑋𝑛 = 1) = 𝛼/(𝛼+𝛽)。链是平稳的。 / If the chain is started from the distribution (𝛽/(𝛼+𝛽), 𝛼/(𝛼+𝛽)), then for all 𝑛, ℙ(𝑋𝑛 = 0) = 𝛽/(𝛼+𝛽) and ℙ(𝑋𝑛 = 1) = 𝛼/(𝛼+𝛽). The chain is stationary.

**Key Insight / 解题要点:**
这个问题的核心是理解如何通过全概率公式推导出边际概率的递推关系，然后将其作为差分方程求解。关键概念是，对于不可约且非周期的有限状态马尔可夫链，边际分布收敛到一个唯一的平稳分布，该分布与初始分布无关。如果链从该平稳分布启动，则它立即处于稳态。 / The core of this problem is understanding how to derive a recurrence relation for marginal probabilities using the law of total probability, and then solving it as a difference equation. The key concept is that for an irreducible, aperiodic finite-state Markov chain, the marginal distribution converges to a unique stationary distribution independent of the initial distribution. If the chain starts in this stationary distribution, it is immediately in steady state.

---

### Question 2 / 第2题

**Problem / 题目原文:**
Let (𝑋𝑛) be a Markov chain. Show that, for any 𝑚≥1, we have
ℙ(𝑋𝑛+𝑚= 𝑥𝑛+𝑚∣𝑋𝑛= 𝑥𝑛, 𝑋𝑛−1 = 𝑥𝑛−1, … , 𝑋0 = 𝑥0) = ℙ(𝑋𝑛+𝑚= 𝑥𝑛+𝑚∣𝑋𝑛= 𝑥𝑛).
Hint: The case 𝑚= 1 is the usual Markov property. Using the Markov property you can proceed via induction on 𝑚.

**中文翻译 / Chinese Translation:**
设 (𝑋𝑛) 是一个马尔可夫链。证明对于任意 𝑚≥1，我们有
ℙ(𝑋𝑛+𝑚= 𝑥𝑛+𝑚∣𝑋𝑛= 𝑥𝑛, 𝑋𝑛−1 = 𝑥𝑛−1, … , 𝑋0 = 𝑥0) = ℙ(𝑋𝑛+𝑚= 𝑥𝑛+𝑚∣𝑋𝑛= 𝑥𝑛)。
提示：𝑚= 1 的情况就是通常的马尔可夫性质。利用马尔可夫性质，你可以通过对 𝑚 进行归纳来证明。

**Knowledge Points / 考查知识点:**
- 马尔可夫性质 / Markov property
- 数学归纳法 / Mathematical induction
- 条件概率 / Conditional probability

**Step-by-Step Solution / 逐步解答:**

**Step 1: 基础情况 (𝑚 = 1) / Base Case (𝑚 = 1)**

**中文思路 / Chinese reasoning:**
题目提示我们，𝑚=1 的情况就是标准的马尔可夫性质。这是马尔可夫链的定义的一部分，所以我们直接陈述它作为归纳的基础。

**English reasoning:**
The problem hints that the case 𝑚=1 is the standard Markov property. This is part of the definition of a Markov chain, so we state it directly as the base of our induction.

**计算过程 / Working:**
对于 𝑚=1，根据马尔可夫性质的定义，我们有：
ℙ(𝑋𝑛+1 = 𝑥𝑛+1 | 𝑋𝑛 = 𝑥𝑛, 𝑋𝑛−1 = 𝑥𝑛−1, …, 𝑋0 = 𝑥0) = ℙ(𝑋𝑛+1 = 𝑥𝑛+1 | 𝑋𝑛 = 𝑥𝑛)

**Explanation of working / 过程解释:**
这直接来自马尔可夫链的定义：给定当前状态，未来状态与过去状态条件独立。

**Step 2: 归纳假设 / Inductive Hypothesis**

**中文思路 / Chinese reasoning:**
我们假设对于某个 𝑚 = 𝑘 (𝑘 ≥ 1)，该性质成立。也就是说，给定 𝑋𝑛，未来 𝑘 步后的状态 𝑋𝑛+𝑘 与过去的状态 𝑋0, …, 𝑋𝑛−1 条件独立。

**English reasoning:**
We assume the property holds for some 𝑚 = 𝑘 (𝑘 ≥ 1). That is, given 𝑋𝑛, the state 𝑋𝑛+𝑘 after 𝑘 steps is conditionally independent of the past states 𝑋0, …, 𝑋𝑛−1.

**计算过程 / Working:**
归纳假设：对于某个 𝑘 ≥ 1，
ℙ(𝑋𝑛+𝑘 = 𝑥𝑛+𝑘 | 𝑋𝑛 = 𝑥𝑛, 𝑋𝑛−1 = 𝑥𝑛−1, …, 𝑋0 = 𝑥0) = ℙ(𝑋𝑛+𝑘 = 𝑥𝑛+𝑘 | 𝑋𝑛 = 𝑥𝑛)

**Explanation of working / 过程解释:**
这是我们在归纳步骤中要使用的假设。

**Step 3: 归纳步骤 (证明 𝑚 = 𝑘+1 成立) / Inductive Step (Prove for 𝑚 = 𝑘+1)**

**中文思路 / Chinese reasoning:**
我们需要证明该性质对 𝑚 = 𝑘+1 也成立。我们从条件概率 ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1 | 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0) 开始。我们的策略是引入中间状态 𝑋𝑛+𝑘，并使用全概率公式和马尔可夫性质。

**English reasoning:**
We need to prove the property holds for 𝑚 = 𝑘+1. We start with the conditional probability ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1 | 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0). Our strategy is to introduce the intermediate state 𝑋𝑛+𝑘 and use the law of total probability and the Markov property.

**计算过程 / Working:**
考虑 ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1 | 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0)。我们可以通过对 𝑋𝑛+𝑘 的所有可能状态求和来边缘化：
ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1 | 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0)
= Σ_{𝑥𝑛+𝑘} ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1, 𝑋𝑛+𝑘 = 𝑥𝑛+𝑘 | 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0)

**Explanation of working / 过程解释:**
这里我们使用了全概率公式的变体，通过对联合事件 {𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1, 𝑋𝑛+𝑘 = 𝑥𝑛+𝑘} 在所有可能的 𝑥𝑛+𝑘 上求和来引入中间状态。

**Step 4: 使用条件概率的链式法则 / Use the chain rule of conditional probability**

**中文思路 / Chinese reasoning:**
我们将联合条件概率分解为两个条件概率的乘积：一个是关于 𝑋𝑛+𝑘+1 给定 𝑋𝑛+𝑘 和过去，另一个是关于 𝑋𝑛+𝑘 给定过去。

**English reasoning:**
We decompose the joint conditional probability into a product of two conditional probabilities: one for 𝑋𝑛+𝑘+1 given 𝑋𝑛+𝑘 and the past, and one for 𝑋𝑛+𝑘 given the past.

**计算过程 / Working:**
= Σ_{𝑥𝑛+𝑘} ℙ(𝑋𝑛+𝑘+1 = 𝑥𝑛+𝑘+1 | 𝑋𝑛+𝑘 = 𝑥𝑛+𝑘, 𝑋𝑛 = 𝑥𝑛, …, 𝑋0 = 𝑥0) × ℙ(𝑋𝑛+𝑘 = 𝑥𝑛+