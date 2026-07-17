# Section 12: End of Part I: Discrete Time Markov Chains

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:51
> 来源页: 67-68

---

好的，同学。你好。我是你的教授。欢迎来到MATH2702的复习与总结部分。我们刚刚完成了课程的第一部分，关于离散时间马尔可夫链。这是一个非常重要的里程碑，在进入第二部分（连续时间过程）之前，我们需要停下来，整理一下所学的内容，确保你已经完全掌握了所有核心概念。

这份学习指南将作为你独立学习的完整资料。请仔细阅读，并按照其中的指引进行复习和练习。我会用中英双语为你解释所有关键术语和概念，确保你理解透彻。

让我们开始吧。

### 📋 Section Overview / 章节概览

**English:**
This section, "End of Part I: Discrete Time Markov Chains," serves as a crucial consolidation point. It contains no new theoretical material. Instead, it provides a structured opportunity for you to review everything learned in the first half of the course (Problem Sheets 1-6, and Sections 1-11). The core of this section is a detailed "Summary of Part I," which lists the key skills and concepts you should master. It also includes Problem Sheet 6, which is a set of comprehensive practice problems covering the major topics. This is your chance to identify any weak areas and solidify your understanding before moving on to the more advanced topic of continuous-time Markov processes.

**Chinese:**
本节，“第一部分结束：离散时间马尔可夫链”，是一个至关重要的巩固环节。它不包含新的理论知识。相反，它为你提供了一个结构化的机会来复习课程前半部分（习题集1-6，以及第1-11节）所学的所有内容。本节的核心是一个详细的“第一部分总结”，其中列出了你应该掌握的关键技能和概念。本节还包括习题集6，这是一套涵盖主要主题的综合性练习题。这是你发现薄弱环节并巩固理解的机会，然后才能进入更高级的连续时间马尔可夫过程的学习。

### 🎯 Learning Objectives / 学习目标

完成本节学习后，你应该能够：

1.  **Self-Assess / 自我评估**: 对照“第一部分总结”中的清单，诚实地评估自己对每个主题的掌握程度。
2.  **Consolidate Knowledge / 巩固知识**: 通过重新阅读笔记、完成未完成的习题或复习难点，主动填补知识空白。
3.  **Apply Core Concepts / 应用核心概念**: 成功解决习题集6中的所有问题，这些问题综合了第一部分的各种概念。
4.  **Prepare for Assessment / 为评估做准备**: 开始或继续完成第一次作业（Assessment 1），该作业基于第一部分的内容。
5.  **Preview Future Topics / 预览未来主题**: 理解第一部分（离散时间）与第二部分（连续时间，以泊松过程开始）之间的逻辑联系。

### 📚 Prerequisites / 前置知识

在开始本节之前，你应该已经：

1.  **Completed / 已完成**: 完成了第1至11节的所有阅读材料。
2.  **Attempted / 已尝试**: 尝试了习题集1至5。
3.  **Understood / 已理解**: 对以下概念有基本理解：
    - 概率论基础（概率空间、条件概率、期望、方差）
    - 随机游走 (Random Walk)
    - 马尔可夫链的定义和性质
    - 转移矩阵 (Transition Matrix) 和转移图 (Transition Diagram)
    - 常返 (Recurrence) 与瞬变 (Transience)
    - 平稳分布 (Stationary Distribution)
    - 细致平衡方程 (Detailed Balance Equations)
    - 鞅 (Martingale) 与可选停止定理 (Optional Stopping Theorem)

### 📖 Core Content / 核心内容

本节内容分为两部分：复习指导和综合练习。

#### Topic 1: Summary of Part I / 第一部分总结

**Intuition / 直觉理解**:
**English:**
Think of this summary as a final exam checklist. It's a list of all the "I can..." statements that, if you can confidently say "yes" to most of them, mean you are well-prepared. It's not just a list of topics; it's a list of *skills* you need to perform. For example, it's not enough to know what a stationary distribution is; you need to be able to *calculate* it.

**Chinese:**
把这个总结想象成期末考试前的检查清单。它是一系列“我能……”的陈述，如果你能对其中大部分自信地回答“是”，那么你就准备得很充分了。这不仅仅是一个主题列表；它是一个你需要掌握的*技能*列表。例如，仅仅知道平稳分布是什么是不够的，你需要能够*计算*它。

**Formal Definition / 形式化定义**:
**English:**
The summary is a list of key competencies from Part I of the module. It is not exhaustive but covers the most critical topics for the exam. The raw material lists these as bullet points. We will expand on each one.

**Chinese:**
这个总结是课程第一部分关键能力的列表。它并非详尽无遗，但涵盖了考试中最关键的主题。原始材料以项目符号列出了这些内容。我们将对每一项进行展开说明。

**Key Properties / 关键性质**:
让我们逐一解析“第一部分总结”中的每个要点。我将为你提供每个要点的中文翻译和简要解释。

1.  **Define the simple random walk and other random walks. / 定义简单随机游走和其他随机游走。**
    - **简单随机游走 (Simple Random Walk)**: 一个随机过程 {Sₙ}, 其中 S₀ = 0, 且 Sₙ = X₁ + X₂ + ... + Xₙ, 其中 Xᵢ 是独立同分布 (i.i.d.) 的随机变量，满足 P(Xᵢ = 1) = p, P(Xᵢ = -1) = q = 1-p。
    - **其他随机游走 (Other Random Walks)**: 步长 (step sizes) 的分布可以更一般化，不限于 ±1。

2.  **Perform elementary calculations for the simple random walk, including by referring to the exact binomial distribution. / 对简单随机游走进行基本计算，包括参考精确的二项分布。**
    - 经过 n 步后，位置 Sₙ 的分布。如果向右走了 k 步，向左走了 n-k 步，则 Sₙ = k - (n-k) = 2k - n。k 服从二项分布 Bin(n, p)。因此 P(Sₙ = 2k - n) = C(n, k) * pᵏ * qⁿ⁻ᵏ。

3.  **Calculate the expectation and variance of general random walks. / 计算一般随机游走的期望和方差。**
    - 如果步长 Xᵢ 的期望为 μ，方差为 σ²，则 E[Sₙ] = nμ，Var(Sₙ) = nσ²。

4.  **Define the gambler’s ruin Markov chain. / 定义赌徒破产马尔可夫链。**
    - 状态空间为 {0, 1, 2, ..., N}，其中 0 和 N 是吸收态 (absorbing states)。从状态 i (1 ≤ i ≤ N-1) 出发，以概率 p 移动到 i+1，以概率 q=1-p 移动到 i-1。

5.  **Find the ruin probability and expected duration for the gambler’s ruin by (i) defining an appropriate martingale (and proving it is a martingale) (ii) Using the optional stopping theorem with an appropriate stopping time. / 通过 (i) 定义一个合适的鞅（并证明它是一个鞅）(ii) 使用可选停止定理和一个合适的停止时间，来找到赌徒破产的破产概率和期望持续时间。**
    - **鞅 (Martingale)**: 一个随机过程 {Mₙ}，满足 E[Mₙ₊₁ | M₀, ..., Mₙ] = Mₙ。
    - **可选停止定理 (Optional Stopping Theorem, OST)**: 在某些条件下，如果 T 是一个停止时间，则 E[M_T] = E[M₀]。
    - **破产概率 (Ruin Probability)**: 从初始资金 i 开始，最终破产（到达状态 0）的概率。常用鞅 Mₙ = (q/p)^(Sₙ) 或 Mₙ = Sₙ - (p-q)n。
    - **期望持续时间 (Expected Duration)**: 从初始资金 i 开始，到被吸收（到达 0 或 N）的期望步数。

6.  **Draw a transition diagram of a Markov chain given the transition matrix. / 给定转移矩阵，画出马尔可夫链的转移图。**
    - 每个状态是一个节点。如果 P(i, j) > 0，则从节点 i 到节点 j 画一条有向边，并标记概率 P(i, j)。

7.  **Calculate n-step transition probabilities by (a) summing the probabilities over all relevant paths or (b) calculating the matrix power. / 通过 (a) 对所有相关路径的概率求和 或 (b) 计算矩阵的幂，来计算 n 步转移概率。**
    - **路径求和 (Path Summation)**: 枚举所有长度为 n 的路径，计算每条路径的概率并求和。
    - **矩阵幂 (Matrix Power)**: P⁽ⁿ⁾ = Pⁿ。P⁽ⁿ⁾(i, j) = P(Xₙ = j | X₀ = i)。

8.  **Find the communicating classes in a Markov chain. / 找到马尔可夫链中的通信类。**
    - 如果状态 i 可以到达 j (i → j) 且 j 可以到达 i (j → i)，则 i 和 j 互通 (communicate)。互通关系是一个等价关系，将状态空间划分为不同的通信类 (communicating classes)。

9.  **Calculate the period of a communicating class. / 计算通信类的周期。**
    - 状态 i 的周期 d(i) = gcd{ n ≥ 1 : P⁽ⁿ⁾(i, i) > 0 }。一个通信类中的所有状态具有相同的周期。

10. **Calculate hitting probabilities and expected hitting times by (i) setting up equations by conditioning on the first step and (ii) solving the resulting simultaneous equations. / 通过 (i) 对第一步进行条件期望来建立方程 (ii) 求解由此产生的联立方程组，来计算 hitting 概率和期望 hitting 时间。**
    - **Hitting 概率 (Hitting Probability)**: hᵢᴬ = P(从 i 出发，最终到达集合 A)。
    - **期望 Hitting 时间 (Expected Hitting Time)**: kᵢᴬ = E[从 i 出发，首次到达集合 A 的时间]。
    - **方法 (Method)**: 使用“对第一步进行条件作用 (conditioning on the first step)”的技巧。例如，对于 hᵢᴬ，有 hᵢᴬ = Σⱼ P(i, j) * hⱼᴬ，并带有边界条件 hᵢᴬ = 1 (若 i ∈ A)，hᵢᴬ = 0 (若 i 属于一个无法到达 A 的吸收类)。

11. **Define positive recurrence, null recurrence and transience, and explain their properties. / 定义正常返、零常返和瞬变性，并解释它们的性质。**
    - **瞬变 (Transient)**: 从状态 i 出发，以正概率永不返回。等价于期望返回时间 μᵢ = ∞。
    - **零常返 (Null Recurrent)**: 从状态 i 出发，一定会返回（常返），但期望返回时间 μᵢ = ∞。
    - **正常返 (Positive Recurrent)**: 从状态 i 出发，一定会返回（常返），且期望返回时间 μᵢ < ∞。

12. **Find the positive recurrence, null recurrence or transience of communicating classes. / 找到通信类的正常返、零常返或瞬变性。**
    - 对于不可约 (irreducible) 的马尔可夫链，所有状态属于同一类型（都是瞬变、零常返或正常返）。

13. **Find the stationary distribution of a Markov chain. / 找到马尔可夫链的平稳分布。**
    - 平稳分布 π 是一个概率向量，满足 π = πP。即 πⱼ = Σᵢ πᵢ P(i, j)。

14. **Give conditions for a stationary distribution to exist and be unique. / 给出平稳分布存在且唯一的条件。**
    - **存在性 (Existence)**: 对于一个不可约、正常返的链，存在唯一的平稳分布。
    - **唯一性 (Uniqueness)**: 如果一个链是不可约的，那么平稳分布如果存在，则唯一。

15. **State the detailed balance equations and (when possible) solve them. / 陈述细致平衡方程，并在可能时求解它们。**
    - **细致平衡方程 (Detailed Balance Equations)**: πᵢ P(i, j) = πⱼ P(j, i) 对所有 i, j 成立。
    - 如果一个概率分布 π 满足细致平衡方程，那么它一定是平稳分布。这通常比直接求解 π = πP 更容易。

16. **Give conditions for convergence to an equilibrium distribution. / 给出收敛到平衡分布的条件。**
    - 对于一个不可约、非周期 (aperiodic)、正常返的马尔可夫链，无论初始分布如何，lim_{n→∞} P⁽ⁿ⁾(i, j) = πⱼ。

17. **Calculate long-term proportions of time using the ergodic theorem. / 使用遍历定理计算长期时间比例。**
    - **遍历定理 (Ergodic Theorem)**: 对于一个不可约、正常返的链，长期来看，在状态 j 上花费的时间比例等于 πⱼ。即 lim_{n→∞} (1/n) * Σ_{k=1}^{n} 1_{X_k = j} = πⱼ (几乎必然)。

---

#### Topic 2: Problem Sheet 6 / 习题集 6

**Intuition / 直觉理解**:
**English:**
This problem sheet is your final exam simulation for Part I. It contains three problems that test a wide range of the skills listed in the summary. Problem 1 is a direct calculation on a small, periodic chain. Problem 2 is a "word problem" where you must model a biological process as a Markov chain. Problem 3 is another "word problem" about an airline loyalty program. Solving these will give you a very good idea of your readiness for the exam.

**Chinese:**
这份习题集是第一部分内容的期末考试模拟。它包含三个问题，测试了总结中列出的广泛技能。问题1是对一个小型周期链的直接计算。问题2是一个“应用题”，你需要将一个生物过程建模为马尔可夫链。问题3是另一个关于航空公司忠诚度计划的“应用题”。解决这些问题会让你很好地了解自己是否为考试做好了准备。

**Formal Definition / 形式化定义**:
**English:**
The problem sheet is a set of three questions designed to be attempted before a workshop in week 7. The answers are discussed in the workshop. The problems are:
1.  A Markov chain with a cyclic transition matrix.
2.  A Markov chain modeling the inheritance of hemophilia.
3.  A Markov chain modeling an airline frequent flyer program.

**Chinese:**
习题集是一套包含三个问题的练习，旨在第7周的工作坊之前完成。答案将在工作坊中讨论。这三个问题是：
1.  一个具有循环转移矩阵的马尔可夫链。
2.  一个模拟血友病遗传的马尔可夫链。
3.  一个模拟航空公司常旅客计划的马尔可夫链。

**Worked Examples / 例题**:
由于这是练习题，我将为你提供每个问题的详细解题思路和关键步骤，而不是完整的答案。这能帮助你独立完成，同时确保你走在正确的轨道上。

---

**Problem 1 Solution Guide / 问题1 解题指南**

**(a) Draw a transition diagram... / 画出转移图...**

- **Transition Matrix / 转移矩阵**: P = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
- **Transition Diagram / 转移图**:
    - 1 → 2 (概率 1)
    - 2 → 3 (概率 1)
    - 3 → 1 (概率 1)
- **Irreducible / 不可约的?**: 是的，因为所有状态都是互通的 (1→2→3→1)。
- **Periodic or Aperiodic / 周期的还是非周期的?**: 周期的。从状态1出发，返回的可能步数是3, 6, 9, ... 所以周期 d(1) = gcd{3, 6, 9, ...} = 3。所有状态周期都是3。

**(b) What is m_i, the return probability... / 什么是 m_i, 返回概率...**

- **Return Probability (m_i) / 返回概率 (m_i)**: 这是从状态 i 出发，最终返回 i 的概率。由于链是不可约的且状态空间有限，所有状态都是常返的 (recurrent)。因此，对于所有 i，m_i = 1。
- **Expected Return Time (μ_i) / 期望返回时间 (μ_i)**: 这是从状态 i 出发，首次返回 i 的期望步数。对于这个确定性的3-cycle，从状态1出发，你将在第3步返回。所以 μ₁ = 3。同理，μ₂ = 3, μ₃ = 3。

**(c) By solving π = πP, find the stationary distribution... / 通过求解 π = πP, 找到平稳分布...**

- 设 π = [π₁, π₂, π₃]。方程 π = πP 给出：
    - π₁ = 0*π₁ + 0*π₂ + 1*π₃  => π₁ = π₃
    - π₂ = 1*π₁ + 0*π₂ + 0*π₃  => π₂ = π₁
    - π₃ = 0*π₁ + 1*π₂ + 0*π₃  => π₃ = π₂
- 加上归一化条件 π₁ + π₂ + π₃ = 1，我们得到 3π₁ = 1，所以 π₁ = 1/3, π₂ = 1/3, π₃ = 1/3。
- **Confirm μ_i / 确认 μ_i**: 对于不可约、正常返的链，有 μᵢ = 1/πᵢ。这里 μ₁ = 1/(1/3) = 3。这与我们在 (b) 中计算的一致。

**(d) For what initial distributions λ do the limits lim_{n→∞} P(X_n = i) exist? / 对于什么初始分布 λ，极限 lim_{n→∞} P(X_n = i) 存在？**

- 这个链是周期的（周期为3）。对于周期链，极限 lim_{n→∞} P⁽ⁿ⁾(i, j) 通常不存在，因为概率会振荡。
- 然而，如果初始分布 λ 恰好是平稳分布 π，那么对于所有 n，P(Xₙ = i) = πᵢ = 1/3，所以极限存在且等于 1/3。
- 更一般地，如果初始分布是平稳分布，则极限存在。对于这个链，这是唯一能使极限存在的初始分布。

**(e) What is the long-run proportion of time spent in each state? / 在每个状态上花费的长期时间比例是多少？**

- **Ergodic Theorem / 遍历定理**: 即使链是周期的，长期时间比例仍然存在，并且等于平稳分布。
- 因此，长期来看，在状态1、2、3上花费的时间比例都是 1/3。

---

**Problem 2 Solution Guide / 问题2 解题指南**

**(a) Show that we can use a Markov chain... / 证明我们可以使用马尔可夫链...**

- **State Space / 状态空间**: 我们需要对每一代第一个孩子的基因型进行建模。可能的基因型是：
    - **XX**: 女性，正常
    - **XX\***: 女性，携带者 (carrier)
    - **X\*X\***: 女性，血友病患者 (haemophiliac) (注意：这在现实中非常罕见，但理论上可能)
    - **XY**: 男性，正常
    - **X\*Y**: 男性，血友病患者
- 然而，问题说“starting with a female carrier (XX\*)”。并且“the partner of each person in the study does not have a defective X chromosome”。这意味着父亲总是提供正常的 X 或 Y 染色体。
- 让我们简化状态。我们关心的是孩子是否患有血友病或是携带者。但为了建模，我们需要跟踪基因型。
- **关键假设 (Key Assumption)**: 每个父母有均等概率传递他们的任一条染色体。
- 让我们定义状态为孩子的基因型。由于母亲是携带者 (XX\*)，父亲是正常的 (XY)。
    - 母亲可以传递 X 或 X\*。
    - 父亲可以传递 X 或 Y。
- 可能的子代基因型：
    - 母亲 X + 父亲 X = XX (正常女性)
    - 母亲 X + 父亲 Y = XY (正常男性)
    - 母亲 X\* + 父亲 X = XX\* (女性携带者)
    - 母亲 X\* + 父亲 Y = X\*Y (男性血友病患者)
- 所以状态空间 S = {XX, XY, XX\*, X\*Y}。注意 X\*X\* 不可能，因为父亲没有 X\*。
- **Transition Diagram / 转移图**: 我们需要找到从一个状态（母亲的基因型）到下一个状态（孩子的基因型）的概率。但问题说“starting with a female carrier”。这意味着我们跟踪的是*母亲*的基因型吗？还是孩子的？问题说“progress of the disease through first-born children”。这意味着我们看每一代的第一个孩子。这个孩子长大后成为下一代的父母之一。
- **重新解释 (Reinterpretation)**: 我们跟踪的是*母亲*的基因型。第一代母亲是 XX\*。她的第一个孩子（可以是男性或女性）长大后会与一个没有缺陷 X 染色体的伴侣结婚。然后这个孩子（现在是父母）的第一个孩子的基因型由我们决定。
- 让我们定义状态为*母亲*的基因型。但母亲必须是女性。所以状态空间是 {XX, XX\*}。注意 X\*X\* 不可能。
    - 如果母亲是 XX (正常)，她只能传递 X。父亲传递 X 或 Y。孩子基因型：XX (女) 或 XY (男)。但孩子长大后，如果是女性，她将成为下一代的母亲。如果是男性，他不是母亲！所以我们需要跟踪女性后代的基因型。
- **更简单的模型 (Simpler Model)**: 我们只跟踪*女性*后代的基因型。因为只有女性才能成为母亲。
    - 从母亲 XX 开始：她传递 X。父亲传递 X 或 Y。孩子是女性当且仅当父亲传递 X。所以孩子是 XX 的概率是 1。所以下一代母亲是 XX。
    - 从母亲 XX\* 开始：她以 1/2 概率传递 X，以 1/2 概率传递 X\*。父亲传递 X 或 Y。孩子是女性当且仅当父亲传递 X (概率 1/2)。所以：
        - P(孩子是女性且是 XX) = P(母亲传递 X) * P(父亲传递 X) = (1/2) * (1/2) = 1/4
        - P(孩子是女性且是 XX\*) = P(母亲传递 X\*) * P(父亲传递 X) = (1/2) * (1/2) = 1/4
        - P(孩子是男性) = 1/2。如果孩子是男性，这一代没有女性后代，过程结束？不，问题说“progress of the disease through first-born children”。这意味着我们只关心第一个孩子。如果第一个孩子是男性，那么这一支就结束了（没有女性来传递基因）。
- **最终模型 (Final Model)**: 状态空间 S = {XX, XX\*, "Line Extinct"}。但更标准的方法是：
    - 状态 0: 母亲是 XX (正常)
    - 状态 1: 母亲是 XX\* (携带者)
    - 状态 2: 血统灭绝 (Line extinct) (例如，第一个孩子是男性，或者没有孩子)
- 从状态 0 (XX 母亲):
    - 孩子一定是 XX 女性 (概率 1/2) 或 XY 男性 (概率 1/2)。
    - 所以 P(0 → 0) = 1/2 (孩子是XX女性，下一代母亲是XX)
    - P(0 → 2) = 1/2 (孩子是男性，血统灭绝)
- 从状态 1 (XX\* 母亲):
    - 孩子是 XX 女性 (概率 1/4), XX\* 女性 (概率 1/4), XY 男性 (概率 1/4), X\*Y 男性 (概率 1/4)。
    - 所以 P(1 → 0) = 1/4 (孩子是XX女性)
    - P(1 → 1) = 1/4 (孩子是XX\*女性)
    - P(1 → 2) = 1/4 + 1/4 = 1/2 (孩子是男性)
- 状态 2 是吸收态 (absorbing state): P(2 → 2) = 1。

**(b) What are the communicating classes? / 什么是通信类？**

- 状态 2 是它自己的一个吸收通信类。
- 状态 0 和 1 是瞬变的 (transient)，因为从它们出发，有正概率进入吸收态 2 并且永不返回。

**(c) Calculate a stationary distribution. / 计算一个平稳分布。**

- 由于存在吸收态，平稳分布不唯一。任何将概率质量全部放在吸收态 2 上的分布都是平稳分布。例如，π = [0, 0, 1]。
- 是否存在其他平稳分布？从瞬变类出发，最终所有概率都会流向吸收态。所以唯一的平稳分布是 π = [0, 0, 1]。

**(d) What is the limiting probability that a child has hemophilia? / 一个孩子患有血友病的极限概率是多少？**

- 在极限情况下，血统要么灭绝（状态 2），要么最终进入一个没有血友病的状态？不，从状态 0 出发，血统可能永远不灭绝吗？状态 0 有 1/2 的概率进入灭绝。所以最终灭绝的概率是 1。
- 因此，在遥远的未来，血统灭绝的概率是 1。所以一个孩子患有血友病的极限概率是 0。

---

**Problem 3 Solution Guide / 问题3 解题指南**

**(a) Show that this system can be modelled using a Markov chain... / 证明这个系统可以用马尔可夫链建模...**

- **State Space / 状态空间**: S = {Ordinary (O), Bronze (B), Silver (S), Gold (G)}。
- **Transition Probabilities / 转移概率**: 会员的行为（订0、1、≥2次航班）是独立