# Section 3: Autoregressive (AR) model

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:08
> 来源页: 21-32

---

# MATH2703: Time Series / 时间序列分析

## Chapter 3: Autoregressive Models / 自回归模型

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章我们将学习一类非常重要的时间序列模型——自回归模型（Autoregressive models，简称AR模型）。在上一章中，我们学习了如何通过相关图（correlogram）来区分白噪声（white noise）和具有依赖关系的过程。现在，我们将深入探讨一种能够捕捉时间序列中"今天依赖于昨天"这种自然现象的数学模型。自回归模型是时间序列分析中最基础、最常用的工具之一，广泛应用于经济学、金融学、气象学等领域。

**English explanation:** In this chapter, we will study a very important class of time series models — Autoregressive models (AR models). In the previous chapter, we learned how to use the correlogram to distinguish between white noise and processes with dependence. Now, we will delve into a mathematical model that captures the natural phenomenon of "today depends on yesterday" in time series. Autoregressive models are among the most fundamental and commonly used tools in time series analysis, widely applied in economics, finance, meteorology, and other fields.

---

### 🎯 Learning Objectives / 学习目标

After completing this chapter, you should be able to / 完成本章学习后，你应该能够：

1. **理解自回归模型的基本概念**：掌握AR(p)模型的定义、形式和直观含义
   **Understand the basic concepts of autoregressive models**: Grasp the definition, form, and intuitive meaning of AR(p) models

2. **分析AR(1)过程的平稳性条件**：理解并推导AR(1)过程平稳的充要条件
   **Analyze stationarity conditions for AR(1) processes**: Understand and derive necessary and sufficient conditions for AR(1) stationarity

3. **判断AR(p)过程的平稳性**：使用AR多项式根的条件判断高阶自回归过程的平稳性
   **Determine stationarity of AR(p) processes**: Use the root condition of the AR polynomial to assess stationarity of higher-order autoregressive processes

4. **计算自相关函数**：推导AR(1)和AR(2)过程的自相关函数
   **Compute autocorrelation functions**: Derive ACF for AR(1) and AR(2) processes

5. **应用Yule-Walker方程**：使用Yule-Walker方程从自相关函数估计模型参数
   **Apply Yule-Walker equations**: Use Yule-Walker equations to estimate model parameters from the autocorrelation function

6. **使用R语言模拟AR过程**：能够用R生成和分析AR过程
   **Simulate AR processes in R**: Generate and analyze AR processes using R

---

### 📚 Prerequisites / 前置知识

**中文解释：** 在学习本章之前，请确保你已经掌握了以下概念：

**English explanation:** Before studying this chapter, please ensure you have mastered the following concepts:

| Concept / 概念 | Description / 描述 |
|---------------|-------------------|
| White noise / 白噪声 | A sequence of uncorrelated random variables with zero mean and constant variance / 均值为零、方差为常数的无相关随机变量序列 |
| Stationarity / 平稳性 | A stochastic process whose statistical properties do not change over time / 统计性质不随时间变化的随机过程 |
| Autocorrelation function (ACF) / 自相关函数 | Measures the correlation between observations at different time lags / 衡量不同时间滞后观测值之间的相关性 |
| Correlogram / 相关图 | A plot of the autocorrelation function / 自相关函数的图形表示 |
| Variance and covariance / 方差和协方差 | Basic statistical measures of dispersion and dependence / 离散程度和依赖关系的基本统计度量 |

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Using Correlograms to Distinguish Processes / 使用相关图区分不同过程

**Intuition / 直觉理解**

**中文解释：** 在开始学习自回归模型之前，我们先回顾一下如何通过相关图（correlogram）来区分不同类型的时间序列过程。相关图是自相关函数（ACF）的图形表示，它展示了不同时间滞后（lag）下的自相关系数。通过观察相关图的形状和衰减模式，我们可以初步判断时间序列是白噪声还是具有某种依赖结构的过程。

**English explanation:** Before diving into autoregressive models, let's review how to use the correlogram to distinguish different types of time series processes. The correlogram is a graphical representation of the autocorrelation function (ACF), showing autocorrelation coefficients at different time lags. By observing the shape and decay pattern of the correlogram, we can preliminarily determine whether a time series is white noise or has some dependence structure.

**Key Insight / 关键洞察：**
- **White noise / 白噪声**：ACF在滞后0处为1，在其他所有滞后处都接近0（在置信区间内）
- **Processes with dependence / 具有依赖关系的过程**：ACF呈现某种模式，如指数衰减、周期性振荡等

**Formal Definition / 形式化定义**

**中文解释：** 教材中给出了三个序列（series a、series b、series c）的相关图。通过观察这些图形，我们可以看到不同序列的自相关结构差异很大。例如，有些序列的ACF迅速衰减到零，而有些则缓慢衰减或呈现周期性模式。

**English explanation:** The textbook presents correlograms for three series (series a, series b, series c). By observing these plots, we can see that different series have very different autocorrelation structures. For example, some series have ACF that decays quickly to zero, while others decay slowly or show periodic patterns.

**Note / 注意：** 教材中的相关图（第21页）展示了三种不同类型的序列。虽然具体的图形细节在文本中难以完全重现，但关键点是：通过观察ACF的衰减模式，我们可以初步判断序列是否具有自相关结构。

---

#### Topic 2: Introduction to Autoregressive Models / 自回归模型简介

**Intuition / 直觉理解**

**中文解释：** 自回归模型的核心思想是：今天的值可以用过去的值加上一个随机误差来表示。这种"今天依赖于昨天"的现象在生活中非常普遍和自然。让我们看两个生动的例子：

**English explanation:** The core idea of autoregressive models is: today's value can be expressed in terms of past values plus a random error. This phenomenon of "today depends on yesterday" is very common and natural in real life. Let's look at two vivid examples:

**Example 1: Room Temperature with a Heater / 带暖气的房间温度**

**中文解释：** 想象一个装有恒温器的房间，恒温器试图将温度保持在20°C左右。如果昨天很暖和，今天仍然会有些暖和；如果昨天很冷，今天仍然会有些冷。随机误差可能来自开窗、阳光照射等因素。这遵循以下关系：
- 今天 = 昨天的一部分 + 今天的随机误差

**English explanation:** Imagine a room with a thermostat that tries to keep the temperature near 20°C. If yesterday was warm, today will still be somewhat warm; if yesterday was cold, today will still be somewhat cold. Random error might come from opening a window, sunlight, etc. This follows the relation:
- today = a fraction of yesterday + a random error today

**Example 2: Mood / 情绪**

**中文解释：** 我今天的情绪受到昨天情绪的影响。如果我昨天很开心，我今天更有可能也开心。但随机事件（好消息、坏消息）可能会让我今天的心情上下波动。

**English explanation:** My mood today is influenced by how I felt yesterday. If I was happy yesterday, I am more likely to be happy today. But random events (good news, bad news) can push me up or down today.

**Formal Definition / 形式化定义**

**Definition 3.1 (Autoregressive processes / 自回归过程)**

**中文解释：** 一个随机过程 {X_t} 被称为p阶自回归过程（或AR(p)过程），如果它满足以下方程：

**English explanation:** A stochastic process {X_t} is called an autoregressive process of order p (or AR(p) process) if it satisfies the following equation:

$$X_t = \sum_{k=1}^{p} a_k X_{t-k} + \varepsilon_t \quad \forall t$$

where / 其中：
- $a_1, \ldots, a_p \in \mathbb{R}$ are the autoregressive coefficients / 自回归系数
- $\{\varepsilon_t\}$ is white noise / 是白噪声
- $\varepsilon_t$ is independent of $X_s$ for all $s < t$ / $\varepsilon_t$ 与所有 $s < t$ 的 $X_s$ 独立

**Symbol Table / 符号表：**

| Symbol / 符号 | Meaning / 含义 |
|---------------|----------------|
| $X_t$ | The value of the process at time t / 过程在时间t的值 |
| $p$ | The order of the autoregressive model / 自回归模型的阶数 |
| $a_k$ | The coefficient for lag k / 第k个滞后的系数 |
| $\varepsilon_t$ | White noise error term at time t / 时间t的白噪声误差项 |
| $\forall t$ | For all t / 对所有t成立 |

**Remarks / 注释：**

1. **中文解释：** 就像多元回归模型一样，但这里X_t是回归到它自己的过去值（即X_{t-1}, X_{t-2}, ..., X_{t-p}）上，而不是回归到其他预测变量上。这就是"自回归"（auto-regressive）这个前缀的由来——"auto"表示"自身"。

   **English explanation:** Like a multiple regression model, but X_t is regressed on past values of X_t, i.e., X_{t-1}, X_{t-2}, ..., X_{t-p}, rather than on separate predictors. This explains the prefix "auto" — meaning "self".

2. **中文解释：** AR过程已经应用于许多情境中，在这些情境中，合理地假设时间序列的当前值线性地依赖于最近的过去值加上一个随机误差。为简单起见，我们只考虑均值为零的过程，但非零均值可以通过将定义改写为以下形式来处理：

   **English explanation:** AR processes have been applied to many situations in which it is reasonable to assume that the present value of a time series depends linearly on the immediate past values together with a random error. For simplicity we will only consider processes with mean zero, but non-zero means may be dealt with by rewriting the definition in the form:

   $$X_t - \mu = \sum_{k=1}^{p} a_k (X_{t-k} - \mu) + \varepsilon_t$$

   where $\mu$ is the mean of the process / 其中 $\mu$ 是过程的均值

---

#### Topic 3: AR(1) Processes / 一阶自回归过程

**Intuition / 直觉理解**

**中文解释：** AR(1)是最简单的自回归模型，其中当前值只依赖于前一个时间点的值。方程形式为：

**English explanation:** AR(1) is the simplest autoregressive model, where the current value depends only on the value at the previous time point. The equation is:

$$X_t = a X_{t-1} + \varepsilon_t \tag{3.1}$$

**中文解释：** 一个重要的问题是：AR(1)过程是否总是平稳的？答案是否定的。让我们通过一个反例来说明。

**English explanation:** An important question is: Are AR(1) processes always stationary? The answer is no. Let's illustrate this with a counterexample.

**Example 3.1: Random Walk / 随机游走**

**中文解释：** 考虑过程 {X_t}，其中 X_0 = 0，X_t = X_{t-1} + \varepsilon_t，对于所有 t = 1, 2, ...，且 {ε_t} 是方差为 σ² 的白噪声过程。这是一个AR(1)过程，其中 a = 1。这种过程被称为随机游走（random walk）。我们需要证明它不是平稳的。

**English explanation:** Consider the process {X_t} given by X_0 = 0, X_t = X_{t-1} + ε_t, for all t = 1, 2, ..., with {ε_t} a white noise process with variance σ². This is an AR(1) process with a = 1. Such a process is called a random walk. We need to show it is not stationary.

**Solution / 解答：**

**Step 1: Express X_t in terms of ε's / 用ε表示X_t**

**中文解释：** 通过递归展开，我们可以得到：

**English explanation:** By recursive expansion, we obtain:

$$X_t = \sum_{k=1}^{t} \varepsilon_k$$

**Step 2: Compute the mean / 计算均值**

**中文解释：** 由于每个ε_k的期望为零，所以：

**English explanation:** Since each ε_k has zero expectation:

$$\mathbb{E}[X_t] = \sum_{k=1}^{t} \mathbb{E}[\varepsilon_k] = 0$$

**Step 3: Compute the variance / 计算方差**

**中文解释：** 由于ε_k是独立同分布的白噪声，方差为σ²，所以：

**English explanation:** Since ε_k are i.i.d. white noise with variance σ²:

$$\text{var}(X_t) = \sum_{k=1}^{t} \text{var}(\varepsilon_k) = t\sigma^2$$

**Conclusion / 结论：**

**中文解释：** 方差随时间t增加而增加，因此 {X_t} 不是平稳的。平稳性要求方差不随时间变化，但这里 var(X_t) = tσ² 依赖于t。

**English explanation:** The variance increases with time t, therefore {X_t} is not stationary. Stationarity requires the variance to be constant over time, but here var(X_t) = tσ² depends on t.

---

#### Topic 4: Stationarity Condition for AR(1) / AR(1)的平稳性条件

**Intuition / 直觉理解**

**中文解释：** 既然不是所有的AR(1)过程都是平稳的，那么我们需要找出在什么条件下AR(1)过程是平稳的。为此，我们首先引入后移算子（backshift operator）的概念。

**English explanation:** Since not all AR(1) processes are stationary, we need to find the conditions under which AR(1) processes are stationary. For this, we first introduce the concept of the backshift operator.

**Definition 3.2: Backshift Operator / 后移算子**

**中文解释：** 我们定义后移算子B为：

**English explanation:** We define the backshift operator B by:

$$B X_t = X_{t-1}$$

**中文解释：** 并将其扩展到幂次：B²X_t = B(B X_t) = B X_{t-1} = X_{t-2}。一般地：

**English explanation:** And extend it to powers: B²X_t = B(B X_t) = B X_{t-1} = X_{t-2}. In general:

$$B^p X_t = X_{t-p}$$

**Derivation of Stationarity Condition / 平稳性条件的推导**

**中文解释：** 使用后移算子，AR(1)方程 X_t = a X_{t-1} + ε_t 可以改写为：

**English explanation:** Using the backshift operator, the AR(1) equation X_t = a X_{t-1} + ε_t can be rewritten as:

$$X_t = a B X_t + \varepsilon_t$$

$$X_t - a B X_t = \varepsilon_t$$

$$(1 - aB) X_t = \varepsilon_t$$

$$X_t = (1 - aB)^{-1} \varepsilon_t$$

**中文解释：** 利用几何级数展开（当 |a| < 1 时）：

**English explanation:** Using the geometric series expansion (when |a| < 1):

$$(1 - aB)^{-1} = \sum_{i=0}^{\infty} (aB)^i = \sum_{i=0}^{\infty} a^i B^i$$

**中文解释：** 因此：

**English explanation:** Therefore:

$$X_t = \sum_{i=0}^{\infty} a^i B^i \varepsilon_t = \sum_{i=0}^{\infty} a^i \varepsilon_{t-i}$$

$$X_t = \varepsilon_t + a\varepsilon_{t-1} + a^2\varepsilon_{t-2} + \cdots$$

**Computing the Variance / 计算方差**

**中文解释：** 假设X_t是平稳的。由于ε_t是独立的，我们可以计算：

**English explanation:** Assume X_t is stationary. By the independence of ε_t, we can compute:

$$\mathbb{E}[X_t] = 0$$

$$\text{var}(X_t) = \sigma^2 (1 + a^2 + a^4 + \cdots)$$

**中文解释：** 这个无穷级数收敛当且仅当 |a| < 1，此时：

**English explanation:** This infinite series converges if and only if |a| < 1, in which case:

$$\text{var}(X_t) = \frac{\sigma^2}{1 - a^2}$$

**Computing the Autocovariance Function / 计算自协方差函数**

**中文解释：** 滞后k的自协方差函数为：

**English explanation:** The autocovariance function at lag k is given by:

$$\gamma_k = \mathbb{E}[X_t X_{t+k}]$$

$$= \mathbb{E}\left[\sum_{i=0}^{\infty} a^i \varepsilon_{t-i} \sum_{j=0}^{\infty} a^j \varepsilon_{t+k-j}\right]$$

**中文解释：** 由于ε_t是独立的，只有当两个ε的下标相同时，期望才非零。这发生在 t-i = t+k-j，即 j = i+k 时：

**English explanation:** Since ε_t are independent, the expectation is non-zero only when the indices of the two ε's match. This occurs when t-i = t+k-j, i.e., j = i+k:

$$\gamma_k = \sigma^2 \sum_{i=0}^{\infty} a^i a^{i+k} = \sigma^2 a^k \sum_{i=0}^{\infty} a^{2i} = \frac{\sigma^2 a^k}{1 - a^2}$$

**中文解释：** 因此自相关函数（ACF）为：

**English explanation:** Therefore the autocorrelation function (ACF) is:

$$\rho_k = \frac{\gamma_k}{\gamma_0} = a^k$$

**Stationarity Condition Summary / 平稳性条件总结**

**中文解释：** 因此，AR(1)过程是平稳的当且仅当 |a| < 1。此时，对于所有t，有 E[X_t] = 0 且 var(X_t) = σ²/(1-a²)。

**English explanation:** Thus, an AR(1) process is stationary if and only if |a| < 1. In this case, E[X_t] = 0 and var(X_t) = σ²/(1-a²) for all t.

**Symbol Table / 符号表：**

| Symbol / 符号 | Meaning / 含义 |
|---------------|----------------|
| $a$ | AR(1) coefficient / AR(1)系数 |
| $\sigma^2$ | Variance of white noise / 白噪声的方差 |
| $\gamma_k$ | Autocovariance at lag k / 滞后k的自协方差 |
| $\rho_k$ | Autocorrelation at lag k / 滞后k的自相关 |
| $B$ | Backshift operator / 后移算子 |

---

#### Topic 5: Example 3.2 - Simulating AR(1) Processes in R / 在R中模拟AR(1)过程

**中文解释：** 现在我们通过一个具体的R示例来观察不同参数下AR(1)过程的行为。

**English explanation:** Now let's observe the behavior of AR(1) processes with different parameters through a concrete R example.

**Example 3.2 / 例题3.2**

**中文解释：** 考虑由以下R命令定义的三个过程 X1.ar1、X2.ar1、X3.ar1。写出它们的数学表达式，绘制时间序列图和ACF图，并给出评论。

**English explanation:** Consider the processes X1.ar1, X2.ar1, X3.ar1 defined by the following R commands. Write down their mathematical expressions, plot their time plot and acf plot, and comment.

```r
set.seed(1234)
n <- 500
epsilon <- rnorm(n)
X1.ar1 <- X2.ar1 <- X3.ar1 <- rep(0, n)
X1.ar1[1] <- X2.ar1[1] <- X3.ar1[1] <- epsilon[1]
for (i in 2:n) {
  X1.ar1[i] <- 0.8 * X1.ar1[i-1] + epsilon[i]
  X2.ar1[i] <- -0.8 * X2.ar1[i-1] + epsilon[i]
  X3.ar1[i] <- 0.4 * X3.ar1[i-1] + epsilon[i]
}
```

**Solution / 解答：**

**中文解释：** 这三个过程都是平稳的AR(1)过程，参数分别为 a = 0.8, -0.8, 0.4。它们的数学表达式为：

**English explanation:** The processes are all stationary AR(1) processes with a = 0.8, -0.8, 0.4 respectively. Their mathematical expressions are:

$$X_t = a X_{t-1} + \varepsilon_t$$

where / 其中：
- $\varepsilon_t \sim \text{i.i.d. } N(0, 1)$
- $\varepsilon_t$ is independent of $X_s$ for $s < t$

**R Code for Plotting / 绘图R代码：**

```r
par(mfrow = c(3, 2), mar = c(1, 4, 1, 1))
plot(X1.ar1, type = "l", xlab = "Time", ylab = "Series X1.ar1")
acf(X1.ar1, xlab = "Lag", ylab = "ACF")
plot(X2.ar1, type = "l", xlab = "Time", ylab = "Series X2.ar1")
acf(X2.ar1, xlab = "Lag", ylab = "ACF")
plot(X3.ar1, type = "l", xlab = "Time", ylab = "Series X3.ar1")
acf(X3.ar1, xlab = "Lag", ylab = "ACF")
```

**Comments / 评论：**

**中文解释：** 从ACF图中我们可以观察到：
1. 当 a = 0.4 时，ACF迅速衰减到零
2. 当 a 为负数时（a = -0.8），ACF呈现交替正负的模式
3. 当 |a| 较大时（a = 0.8），ACF衰减较慢

这些现象与自相关函数 ρ_k = a^k 的理论结果完全一致。

**English explanation:** From the ACF plots we can observe:
1. When a = 0.4, the ACF decays quickly to zero
2. When a is negative (a = -0.8), the ACF shows alternating positive and negative patterns
3. When |a| is large (a = 0.8), the ACF decays more slowly

These phenomena are completely consistent with the theoretical result ρ_k = a^k.

**Using arima.sim() Function / 使用arima.sim()函数**

**中文解释：** R语言提供了一个更方便的函数 arima.sim() 来模拟AR过程：

**English explanation:** R provides a more convenient function arima.sim() to simulate AR processes:

```r
set.seed(123)
n <- 500
X1.ar1.2 <- arima.sim(n, model = list(ar = c(0.8)))
X2.ar1.2 <- arima.sim(n, model = list(ar = c(-0.8)))
par(mfrow = c(2, 2), mar = c(1, 4, 1, 1))
plot(X1.ar1.2, type = "l", xlab = "Time", ylab = "Series X1.ar1.2")
acf(X1.ar1.2, xlab = "Lag", ylab = "ACF")
plot(X2.ar1.2, type = "l", xlab = "Time", ylab = "Series X2.ar1.2")
acf(X2.ar1.2, xlab = "Lag", ylab = "ACF")
```

---

#### Topic 6: Stationarity for AR(p) / AR(p)的平稳性

**Intuition / 直觉理解**

**中文解释：** 类似于AR(1)过程，高阶AR(p)过程也不总是平稳的。我们需要一个一般的条件来判断AR(p)过程的平稳性。这个条件涉及AR多项式的根。

**English explanation:** Similar to AR(1) processes, higher-order AR(p) processes are not always stationary. We need a general condition to determine the stationarity of AR(p) processes. This condition involves the roots of the AR polynomial.

**Proposition 3.1: Stationarity Condition for AR(p) / AR(p)的平稳性条件**

**中文解释：** 一个AR(p)过程是渐近平稳的（asymptotically stationary）当且仅当AR多项式 a(y) = 1 - a₁y - ... - a_p y^p 的所有根 γ₁, ..., γ_p 都满足 |γ_i| > 1。

**English explanation:** An AR(p) process is asymptotically stationary if and only if all the roots γ₁, ..., γ_p of the AR polynomial a(y) = 1 - a₁y - ... - a_p y^p satisfy |γ_i| > 1.

$$a(y) = 1 - a_1 y - a_2 y^2 - \cdots - a_p y^p = 0$$

**中文解释：** 证明见本章附录（不考试）。证明的思路分为三步：
1. 用后移算子将X_t表示为a(B)⁻¹ε_t
2. 将X_t展开为ε_t的无穷级数
3. 检查系数是否平方可和

**English explanation:** The proof is given in the appendix at the end of this chapter (not examinable). The proof proceeds in three steps:
1. Express X_t in terms of a(B)⁻¹ using the backshift operator
2. Expand X_t as an infinite series of ε_t
3. Check whether the coefficients are square-summable

**Remarks / 注释：**

1. **中文解释：** 算子 a(B) = 1 - a₁B - ... - a_p B^p 被称为AR算子（AR operator）。

   **English explanation:** The operator a(B) = 1 - a₁B - ... - a_p B^p is called the AR operator.

2. **中文解释：** 对于AR(1)过程，a(y) = 1 - ay = 0 的根为 y = 1/a。平稳性要求 |y| > 1，即 |1/a| > 