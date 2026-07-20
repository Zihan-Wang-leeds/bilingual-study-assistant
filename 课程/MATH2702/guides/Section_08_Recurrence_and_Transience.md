# Section 8: Recurrence and transience

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:40
> 来源页: 44-50

---

# 📘 Section 8: Recurrence and Transience / 递归性与瞬变性

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是马尔可夫链理论中最重要的部分之一。我们将学习如何对马尔可夫链中的状态进行分类，判断哪些状态会"永远回来"（递归状态），哪些状态会"一去不复返"（瞬变状态）。这种分类对于理解马尔可夫链的长期行为至关重要。我们还将进一步区分"正递归"和"零递归"状态，并学习如何利用通信类（communicating classes）的性质快速判断整个类的递归性或瞬变性。

**English explanation:** This section is one of the most important parts of Markov chain theory. We will learn how to classify states in a Markov chain, determining which states "keep coming back forever" (recurrent states) and which states "leave and never return" (transient states). This classification is crucial for understanding the long-run behavior of Markov chains. We will further distinguish between "positive recurrent" and "null recurrent" states, and learn how to use the properties of communicating classes to quickly determine the recurrence or transience of an entire class.

**Why this matters / 为什么重要：**
- 递归性决定了马尔可夫链是否会在某个状态无限次访问
- 瞬变性意味着状态最终会被永久离开
- 正递归与零递归的区分对于后续学习平稳分布（stationary distribution）至关重要
- 这些概念在排队论、金融建模、物理系统等众多领域都有应用

---

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义** 递归状态和瞬变状态，并解释它们之间的区别
2. **计算** 返回概率 \(m_i\) 并据此判断状态类型
3. **应用** 定理8.1，利用 \( \sum p_{ii}^{(n)} \) 的收敛性判断状态类型
4. **利用** 定理8.2和8.3，通过通信类的性质快速判断递归性或瞬变性
5. **区分** 正递归和零递归状态
6. **理解** 强马尔可夫性质及其在证明中的应用

---

## 📚 Prerequisites / 前置知识

在开始本章之前，请确保你已掌握以下内容：

| 概念 | 中文 | English |
|------|------|---------|
| 马尔可夫链定义 | 马尔可夫链的基本定义和转移概率 | Markov chain definition and transition probabilities |
| 转移矩阵 | 转移矩阵 \(P\) 及其元素 \(p_{ij}\) | Transition matrix and its elements |
| n步转移概率 | \(p_{ij}^{(n)}\) 的含义和计算 | n-step transition probabilities |
| 通信类 | 状态之间的可达性和通信关系 | Communicating classes, accessibility and communication |
| 闭类 | 封闭的通信类 | Closed communicating classes |
| 期望值 | 随机变量的期望值计算 | Expected value of random variables |

---

## 📖 Core Content / 核心内容

### Topic 8.1: Recurrent and Transient States / 递归状态与瞬变状态

#### Intuition / 直觉理解

**中文解释：** 想象你是一个旅行者，在一个由不同城市（状态）组成的网络中旅行。有些城市你去了之后会不断回来——就像你的家乡，你总是会回去。这些城市就是"递归状态"。另一些城市你去了之后可能再也不回来——就像你度假时路过的一个小镇，你只去一次就永远离开了。这些城市就是"瞬变状态"。

更精确地说：
- **递归状态（Recurrent state）**：从该状态出发，你几乎肯定会再次回到该状态，而且会无限次地回来。
- **瞬变状态（Transient state）**：从该状态出发，你可能会回来几次，但最终会永远离开，再也不会回来。

**English explanation:** Imagine you are a traveler moving through a network of cities (states). Some cities you keep returning to — like your hometown, you always come back. These are "recurrent states." Other cities you might visit and never return — like a small town you pass through on vacation, you visit once and leave forever. These are "transient states."

More precisely:
- **Recurrent state**: Starting from this state, you will almost surely return to it again, and you will return infinitely many times.
- **Transient state**: Starting from this state, you might return a few times, but eventually you will leave forever and never come back.

**Key intuition table / 关键直觉表：**

| Property / 性质 | Recurrent / 递归 | Transient / 瞬变 |
|-----------------|------------------|------------------|
| 返回次数 | 无限次 | 有限次 |
| 期望返回次数 | 无穷大 | 有限 |
| 返回概率 \(m_i\) | 1 | < 1 |

---

#### Formal Definition / 形式化定义

**Definition 8.1 / 定义8.1**

Let \((X_n)\) be a Markov chain on a state space \(\mathcal{S}\). For \(i \in \mathcal{S}\), let \(m_i\) be the **return probability (返回概率)**:

\[
m_i = \mathbb{P}(X_n = i \text{ for some } n \ge 1 \mid X_0 = i)
\]

If \(m_i = 1\), we say that state \(i\) is **recurrent (递归的)**; if \(m_i < 1\), we say that state \(i\) is **transient (瞬变的)**.

**Symbol explanation / 符号解释：**

| Symbol | 中文含义 | English meaning |
|--------|----------|-----------------|
| \(X_n\) | 第n步的状态 | State at step n |
| \(\mathcal{S}\) | 状态空间 | State space |
| \(i\) | 某个特定状态 | A particular state |
| \(m_i\) | 从状态i出发，最终返回i的概率 | Probability of eventually returning to state i |
| \(\mathbb{P}(\cdot \mid X_0 = i)\) | 给定初始状态为i的条件概率 | Conditional probability given initial state i |

**Important note / 重要说明：** 注意定义中的"for some \(n \ge 1\)"意味着我们在至少一步之后返回。我们不考虑 \(n=0\) 的情况（即一开始就在状态i不算返回）。

---

#### Key Properties / 关键性质

**Theorem 8.1 / 定理8.1**

Consider a Markov chain with transition matrix \(P\).

- If state \(i\) is **recurrent**, then \(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \infty\), and we return to state \(i\) infinitely many times with probability 1.
  
  如果状态 \(i\) 是递归的，那么 \(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \infty\)，并且我们以概率1无限次返回状态 \(i\)。

- If state \(i\) is **transient**, then \(\sum_{n=1}^{\infty} p_{ii}^{(n)} < \infty\), and we return to state \(i\) infinitely many times with probability 0.
  
  如果状态 \(i\) 是瞬变的，那么 \(\sum_{n=1}^{\infty} p_{ii}^{(n)} < \infty\)，并且我们以概率0无限次返回状态 \(i\)。

**Symbol explanation / 符号解释：**

| Symbol | 中文含义 | English meaning |
|--------|----------|-----------------|
| \(p_{ii}^{(n)}\) | 从状态i出发，n步后回到i的概率 | Probability of being at state i after n steps, starting from i |
| \(\sum_{n=1}^{\infty} p_{ii}^{(n)}\) | 所有n步返回概率之和 | Sum of all n-step return probabilities |

**Why this matters / 为什么重要：** 这个定理给出了判断递归性和瞬变性的另一种方法。我们不需要直接计算返回概率 \(m_i\)，而是可以通过检查 \(\sum p_{ii}^{(n)}\) 是否收敛来判断。

**Expected number of visits / 期望访问次数：**

Starting from state \(i\), the expected number of visits to state \(i\) is:

\[
\mathbb{E}(\# \text{ visits to } i \mid X_0 = i) = \sum_{n=0}^{\infty} \mathbb{P}(X_n = i \mid X_0 = i) = 1 + \sum_{n=1}^{\infty} p_{ii}^{(n)}
\]

从状态 \(i\) 出发，访问状态 \(i\) 的期望次数为 \(1 + \sum_{n=1}^{\infty} p_{ii}^{(n)}\)。注意这里 \(n=0\) 时我们已经在状态 \(i\)，所以贡献了1次访问。

---

#### Proof of Theorem 8.1 / 定理8.1的证明

**Proof / 证明：**

**Part 1: Recurrent case / 递归情况**

**中文解释：** 假设状态 \(i\) 是递归的，即 \(m_i = 1\)。从状态 \(i\) 出发，我们第一次返回的概率是1。根据马尔可夫性质，返回之后，链重新从状态 \(i\) 开始，所以再次返回的概率仍然是 \(m_i = 1\)。重复这个过程，我们一定会无限次返回（概率为1）。因此，访问次数是无限的，期望值也是无限的，所以 \(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \infty\)。

**English explanation:** Suppose state \(i\) is recurrent, so \(m_i = 1\). Starting from state \(i\), the probability we return is 1. After that return, by the Markov property, the chain restarts from state \(i\), so the probability of returning again is still \(m_i = 1\). Repeating this, we keep on returning, definitely visiting infinitely often (with probability 1). Since the number of visits is always infinite, its expectation is infinite too, and this expectation is \(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \infty\).

**Part 2: Transient case / 瞬变情况**

**中文解释：** 假设状态 \(i\) 是瞬变的，即 \(m_i < 1\)。那么，我们恰好返回 \(r\) 次然后永远不再返回的概率是：

\[
\mathbb{P}(\text{number of returns} = r) = m_i^r (1 - m_i)
\]

这是因为我们必须在前 \(r\) 次都返回（概率 \(m_i^r\)），然后在第 \(r+1\) 次不再返回（概率 \(1 - m_i\)）。这是一个几何分布 \(\text{Geom}(1 - m_i)\)（支持集为 \(\{0, 1, 2, \ldots\}\) 的版本）。

对于这种几何分布，期望值为 \(\frac{1 - (1 - m_i)}{1 - m_i} = \frac{m_i}{1 - m_i}\)。由于 \(m_i < 1\)，这个期望值是有限的。因此，\(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \frac{m_i}{1 - m_i} < \infty\)。由于期望返回次数是有限的，无限次返回的概率必须为0。

**English explanation:** Suppose state \(i\) is transient, so \(m_i < 1\). The probability we return exactly \(r\) times before never coming back is:

\[
\mathbb{P}(\text{number of returns} = r) = m_i^r (1 - m_i)
\]

This is because we must return on the first \(r\) occasions (probability \(m_i^r\)), but then fail to return on the next occasion (probability \(1 - m_i\)). This is a geometric distribution \(\text{Geom}(1 - m_i)\) (the version with support \(\{0, 1, 2, \ldots\}\)).

For this type of geometric distribution, the expectation is \(\frac{1 - (1 - m_i)}{1 - m_i} = \frac{m_i}{1 - m_i}\). Since \(m_i < 1\), this expectation is finite. Therefore, \(\sum_{n=1}^{\infty} p_{ii}^{(n)} = \frac{m_i}{1 - m_i} < \infty\). Since the expected number of returns is finite, the probability of returning infinitely many times must be 0.

**Key insight / 关键洞察：** 这个证明巧妙地利用了"返回后重新开始"的思想，这是马尔可夫性质的核心应用。注意在证明中我们使用了"强马尔可夫性质"（将在8.4节讨论），因为返回时间是一个随机时间，而不是固定时间。

---

#### Worked Examples / 例题

**Example 8.1: Simple Random Walk / 简单随机游走**

**中文解释：** 考虑简单随机游走。在上一节中，我们看到对于简单对称随机游走（\(p = \frac{1}{2}\)），我们有 \(m_i = 1\)，所以简单对称随机游走是递归的。但对于 \(p \neq \frac{1}{2}\)，我们有 \(m_i < 1\)，所以所有其他简单随机游走都是瞬变的。

**English explanation:** Consider the simple random walk. In the last section we saw that for the simple symmetric random walk with \(p = \frac{1}{2}\) we have \(m_i = 1\), so the simple symmetric random walk is recurrent. But for \(p \neq \frac{1}{2}\) we have \(m_i < 1\), so all other simple random walks are transient.

**Intuition / 直觉理解：** 对称随机游走（向左向右概率相等）就像一个醉汉，他最终总会回到原点。但如果有偏向（比如向右的概率更大），那么他最终会越走越远，再也回不来了。

---

**Example 8.2: A More Complex Chain / 一个更复杂的链**

**中文解释：** 考虑我们在例6.7中见过的链（如图9所示）：

对于状态5、6和7，很明显返回概率为1，因为马尔可夫链在三角形中循环，所以这些状态是递归的。

状态1、2、3和4是瞬变的。我们马上会看到一种快速判断的方法，但在此之前，我们可以通过直接计算来证明。

从状态4出发，我们可能直接去状态5，在这种情况下我们无法回来，所以 \(m_4 \le 1 - p_{45} = \frac{2}{3}\)，状态4是瞬变的。类似地，如果从1到4再到5，我们肯定无法回到1，所以 \(m_1 \le 1 - p_{14}p_{45} = \frac{5}{6}\)，状态1是瞬变的。通过类似的论证，\(m_3 \le 1 - p_{34}p_{45} = \frac{5}{6}\)，\(m_2 \le 1 - p_{21}p_{14}p_{45} = \frac{11}{12}\)，所以这些状态也都是瞬变的。

注意通信类 \(\{1, 2, 3, 4\}\) 中的所有状态都是瞬变的，而通信类 \(\{5, 6, 7\}\) 中的所有状态都是递归的。我们很快就会回到这个重要观察。

**English explanation:** Consider the chain we saw previously as Example 6.7 (shown in Figure 9):

For states 5, 6, and 7, it is clear that the return probability is 1, since the Markov chain cycles around the triangle, so these states are recurrent.

States 1, 2, 3, and 4 are transient. We will see a very quick way to show this shortly, but in the meantime we can prove it directly.

From state 4, we might go straight to state 5, in which case we cannot come back, so \(m_4 \le 1 - p_{45} = \frac{2}{3}\), and state 4 is transient. Similarly, if we move from 1 to 4 to 5, we definitely will not come back to 1, so \(m_1 \le 1 - p_{14}p_{45} = \frac{5}{6}\), and state 1 is transient. By similar arguments, \(m_3 \le 1 - p_{34}p_{45} = \frac{5}{6}\), and \(m_2 \le 1 - p_{21}p_{14}p_{45} = \frac{11}{12}\), so these states are all transient too.

Notice that all states in the communicating class \(\{1, 2, 3, 4\}\) are transient, while all states in the communicating class \(\{5, 6, 7\}\) are recurrent. We shall return to this point shortly.

**Figure 9 / 图9：** (The transition diagram from Subsection 7.2)

```
    2 ←→ 1 ←→ 4 → 5 ←→ 6
    ↑         ↓   ↑     ↓
    └── 3 ←──┘   └── 7 ←┘
```

(Note: The actual diagram has specific transition probabilities as shown in the original material.)

---

### Topic 8.2: Recurrent and Transient Classes / 递归类与瞬变类

#### Intuition / 直觉理解

**中文解释：** 在例8.2中，我们观察到同一个通信类中的所有状态要么都是递归的，要么都是瞬变的。这不是巧合！这是一个普遍规律：递归性和瞬变性是"类性质"（class property），意味着在一个通信类中，所有状态共享相同的递归/瞬变性质。

**English explanation:** In Example 8.2, we observed that all states in the same communicating class are either all recurrent or all transient. This is not a coincidence! This is a general rule: recurrence and transience are "class properties," meaning that within a communicating class, all states share the same recurrence/transience property.

---

#### Formal Definition / 形式化定义

**Theorem 8.2 / 定理8.2**

Within a communicating class, either every state is transient or every state is recurrent.

在一个通信类中，要么所有状态都是瞬变的，要么所有状态都是递归的。

**Formally / 形式化地：** Let \(i, j \in \mathcal{S}\) be such that \(i \leftrightarrow j\). If \(i\) is recurrent, then \(j\) is recurrent also; while if \(i\) is transient, then \(j\) is transient also.

如果 \(i\) 和 \(j\) 相互可达（属于同一个通信类），那么它们要么都是递归的，要么都是瞬变的。

**Consequence / 推论：** For this reason, we can refer to a communicating class as a "recurrent class" or a "transient class." If a Markov chain is irreducible, we can refer to it as a "recurrent Markov chain" or a "transient Markov chain."

因此，我们可以称一个通信类为"递归类"或"瞬变类"。如果马尔可夫链是不可约的，我们可以称它为"递归马尔可夫链"或"瞬变马尔可夫链"。

---

#### Proof of Theorem 8.2 / 定理8.2的证明

**Proof / 证明：**

**Part 1 / 第一部分：** Suppose \(i \leftrightarrow j\) and \(i\) is recurrent. Then, for some \(n, m\) we have \(p_{ij}^{(n)} > 0\) and \(p_{ji}^{(m)} > 0\).

假设 \(i \leftrightarrow j\) 且 \(i\) 是递归的。那么存在正整数 \(n, m\) 使得 \(p_{ij}^{(n)} > 0\) 和 \(p_{ji}^{(m)} > 0\)。

By the Chapman–Kolmogorov equations (查普曼-科尔莫戈罗夫方程):

\[
\sum_{r=1}^{\infty} p_{jj}^{(n+m+r)} \ge \sum_{r=1}^{\infty} p_{ji}^{(m)} p_{ii}^{(r)} p_{ij}^{(n)}
\]

**中文解释：** 这个不等式告诉我们，从 \(j\) 出发经过 \(n+m+r\) 步回到 \(j\) 的概率，至少等于从 \(j\) 到 \(i\)（\(m\) 步），然后在 \(i\) 处经过 \(r\) 步回到 \(i\)，再从 \(i\) 回到 \(j\)（\(n\) 步）的概率。

**English explanation:** This inequality tells us that the probability of returning from \(j\) to \(j\) in \(n+m+r\) steps is at least the probability of going from \(j\) to \(i\) (in \(m\) steps), then returning to \(i\) in \(r\) steps, then going from \(i\) back to \(j\) (in \(n\) steps).

\[
= p_{ji}^{(m)} \left( \sum_{r=1}^{\infty} p_{ii}^{(r)} \right) p_{ij}^{(n)}
\]

If \(i\) is recurrent, then \(\sum_{r} p_{ii}^{(r)} = \infty\). Then from the above equation, we also have \(\sum_{r} p_{jj}^{(n+m+r)} = \infty\), meaning \(\sum_{s} p_{jj}^{(s)} = \infty\), and \(j\) is recurrent.

如果 \(i\) 是递归的，那么 \(\sum_{r} p_{ii}^{(r)} = \infty\)。从上面的不等式，我们也有 \(\sum_{r} p_{jj}^{(n+m+r)} = \infty\)，这意味着 \(\sum_{s} p_{jj}^{(s)} = \infty\)，所以 \(j\) 也是递归的。

**Part 2 / 第二部分：** Suppose \(i\) is transient. Then \(j\) cannot be recurrent, because if it were, the previous argument with \(i\) and \(j\) swapped over would force \(i\) to in fact be recurrent also. So \(j\) must be transient.

假设 \(i\) 是瞬变的。那么 \(j\) 不可能是递归的，因为如果 \(j\) 是递归的，那么将第一部分论证中的 \(i\) 和 \(j\) 互换，就会迫使 \(i\) 也是递归的（矛盾）。所以 \(j\) 必须是瞬变的。

---

**Theorem 8.3 / 定理8.3**

- **Every open communicating class is transient.**
  
  每个开放的通信类都是瞬变的。

- **Every finite closed communicating class is recurrent.**
  
  每个有限封闭的通信类都是递归的。

**Important note / 重要说明：** This theorem completely classifies the transience and recurrence of classes, with the rare exception of infinite closed classes, which can require further examination.

这个定理完全分类了类的瞬变性和递归性，唯一的例外是无限封闭类，这需要进一步检查。

---

#### Proof of Theorem 8.3 / 定理8.3的证明

**Part 1: Open classes are transient / 开放类是瞬变的**

**中文解释：** 假设 \(i\) 在一个开放的通信类中，所以存在某个 \(j\) 使得 \(i \rightarrow j\)（即存在 \(n\) 使得 \(p_{ij}^{(n)} > 0\)），但 \(j \not\rightarrow i\)（即一旦到达 \(j\) 就无法返回 \(i\)）。我们需要证明 \(i\) 是瞬变的。

考虑在时间 \(n\) 之后返回 \(i\) 的概率。我们根据 \(X_n = j\) 与否进行条件化：

\[
\mathbb{P}(\text{return to } i \text{ after time } n \mid X_0 = i)
\]

\[
= p_{ij}^{(n)} \cdot \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n = j, X_0 = i) + (1 - p_{ij}^{(n)}) \cdot \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n \neq j, X_0 = i)
\]

\[
\le \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n = j, X_0 = i) + (1 - p_{ij}^{(n)})
\]

\[
= 0 + (1 - p_{ij}^{(n)}) < 1
\]

**English explanation:** Suppose \(i\) is in an open communicating class, so for some \(j\) we have \(i \rightarrow j\), meaning \(p_{ij}^{(n)} > 0\) for some \(n\), but \(j \not\rightarrow i\), meaning that once we reach \(j\) we cannot return to \(i\). We need to show that \(i\) is transient.

Consider the probability we return to \(i\) after time \(n\). We condition on whether \(X_n = j\) or not:

\[
\mathbb{P}(\text{return to } i \text{ after time } n \mid X_0 = i)
\]

\[
= p_{ij}^{(n)} \cdot \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n = j, X_0 = i) + (1 - p_{ij}^{(n)}) \cdot \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n \neq j, X_0 = i)
\]

\[
\le \mathbb{P}(\text{return to } i \text{ after time } n \mid X_n = j, X_0 = i) + (1 - p_{ij}^{(n)})
\]

\[
= 0 + (1 - p_{ij}^{(n)}) < 1
\]

**Key reasoning / 关键推理：** 由于从 \(j\) 无法到达 \(i\)，所以给定 \(X_n = j\) 后返回 \(i\) 的概率为0。而 \(p_{ij}^{(n)} > 0\)，所以 \(1 - p_{ij}^{(n)} < 1\)。因此，在时间 \(n\) 之后返回 \(i\) 的概率严格小于1。如果 \(i\) 是递归的，那么它肯定会无限次返回，特别地，在时间 \(n\) 之后也肯定会返回。所以 \(i\) 必须是瞬变的。

**English explanation of reasoning:** Since we cannot get from \(j\) to \(i\), the probability of returning to \(i\) given \(X_n = j\) is 0. And since \(p_{ij}^{(n)} > 0\), we have \(1 - p_{ij}^{(n)} < 1\). Therefore, the probability of returning to \(i\) after time \(n\) is strictly less than 1. If \(i\) were recurrent, we would certainly return infinitely often, and in particular certainly return after time \(n\). So \(i\) must be transient instead.

---

**Part 2: Finite closed classes are recurrent / 有限封闭类是递归的**

**中文解释：** 假设类 \(C\) 是有限且封闭的。那么必然存在某个 \(i \in C\)，使得一旦我们访问 \(i\)，我们无限次返回 \(i\) 的概率严格为正。这是因为我们将在有限个状态 \(C\) 中停留无限多个时间步。那么状态 \(i\) 不是瞬变的，所以它必须是递归的，这意味着整个类都是递归的。

**English explanation:** Suppose the class \(C\) is finite and closed. Then there must be an \(i \in C\) such that, once we visit \(i\), the probability that we return to \(i\) infinitely many times is strictly positive; this is because we are going to stay in the finitely many states of \(C\) for infinitely many time steps. Then that state \(i\) is not transient, so it must be recurrent, which means that the whole class is recurrent.

**Intuition / 直觉理解：** 在一个有限封闭类中，我们只能在这些有限个状态