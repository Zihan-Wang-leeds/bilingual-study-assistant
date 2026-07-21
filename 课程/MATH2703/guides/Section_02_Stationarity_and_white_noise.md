# Section 2: Stationarity and white noise

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:08
> 来源页: 13-20

---

# MATH2703: Time Series / 时间序列分析

## Section 2: Stationary Processes and White Noise / 平稳过程与白噪声

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节是时间序列分析的基础核心内容。我们将学习什么是平稳过程（stationary processes），为什么平稳性如此重要，以及如何判断一个时间序列是否平稳。我们还会介绍自协方差函数（autocovariance function）和自相关函数（autocorrelation function），它们是描述时间序列内部结构的关键工具。最后，我们将学习白噪声（white noise）——这是构建更复杂时间序列模型的基础构件。

**English explanation:** This section forms the foundational core of time series analysis. We will learn what stationary processes are, why stationarity is so important, and how to determine whether a time series is stationary. We will also introduce the autocovariance function and autocorrelation function, which are key tools for describing the internal structure of a time series. Finally, we will study white noise — the fundamental building block for constructing more complex time series models.

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解平稳性的概念**：能够区分强平稳（strong stationarity）和弱平稳（weak stationarity），并解释它们之间的区别与联系。
2. **计算和解释自协方差与自相关函数**：能够根据定义计算给定过程的均值、方差、自协方差和自相关函数。
3. **判断时间序列的平稳性**：能够通过均值和自协方差的性质判断一个随机过程是否平稳。
4. **理解白噪声过程**：掌握白噪声的定义、性质及其在时间序列分析中的作用。
5. **解释样本自相关函数**：理解如何从数据中估计自相关函数，以及如何解读自相关图（correlogram）。
6. **应用Bartlett带**：能够使用Bartlett带判断样本自相关是否显著。

After completing this section, you should be able to:

1. **Understand the concept of stationarity**: Distinguish between strong stationarity and weak stationarity, and explain their differences and relationships.
2. **Compute and interpret autocovariance and autocorrelation functions**: Calculate the mean, variance, autocovariance, and autocorrelation function for a given process based on definitions.
3. **Determine stationarity of time series**: Judge whether a stochastic process is stationary based on its mean and autocovariance properties.
4. **Understand white noise process**: Master the definition, properties, and role of white noise in time series analysis.
5. **Interpret sample autocorrelation function**: Understand how to estimate the autocorrelation function from data and how to interpret a correlogram.
6. **Apply Bartlett bands**: Use Bartlett bands to determine whether sample autocorrelations are statistically significant.

---

### 📚 Prerequisites / 前置知识

**中文解释：** 在学习本章之前，你需要掌握以下基础知识：

- **概率论基础**：随机变量、期望（expectation）、方差（variance）、协方差（covariance）、相关性（correlation）
- **统计推断基础**：样本均值、样本方差、正态分布
- **基本数学**：求和符号、数列、极限概念

**English explanation:** Before studying this chapter, you need to master the following prerequisite knowledge:

- **Basic probability theory**: Random variables, expectation, variance, covariance, correlation
- **Basic statistical inference**: Sample mean, sample variance, normal distribution
- **Basic mathematics**: Summation notation, sequences, limit concepts

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Introduction to Stationarity / 平稳性导论

**Intuition / 直觉理解**

**中文解释：** 让我们先看一个直观的问题。观察下面四个时间序列图（a、b、c、d），你认为哪些是平稳的，哪些不是？

平稳性的直观理解是：**时间序列的统计性质不随时间变化**。具体来说：
- 均值（mean）不随时间变化（没有趋势）
- 方差（variance）不随时间变化
- 周期性变化已经被移除

换句话说，数据中任何一段的性质都与另一段非常相似。

**English explanation:** Let's start with an intuitive question. Look at the four time series plots below (a, b, c, d). Which ones do you think are stationary and which are not?

The intuitive understanding of stationarity is: **The statistical properties of the time series do not change over time**. Specifically:
- The mean does not change over time (no trend)
- The variance does not change over time
- Periodic variations have been removed

In other words, the properties of one section of the data are much like those of any other section.

**The Four Time Series / 四个时间序列：**

(Note: The original material shows four plots labeled a, b, c, d. We describe them conceptually:)

- **Series a**: Appears to have a clear upward trend — mean is increasing over time. → **Non-stationary / 非平稳**
- **Series b**: Fluctuates around a constant mean with roughly constant variance. → **Possibly stationary / 可能平稳**
- **Series c**: Shows clear seasonal/periodic patterns. → **Non-stationary / 非平稳**
- **Series d**: Fluctuates around zero with constant variance, no obvious pattern. → **Possibly stationary / 可能平稳**

**Why Stationarity Matters / 为什么平稳性重要**

**中文解释：** 引用Chatfield and Xing (2019)的话："广义地说，如果一个时间序列没有均值的系统性变化（没有趋势），没有方差的系统性变化，并且严格的周期性变化已被移除，那么该时间序列被称为平稳的。换句话说，数据中任何一段的性质都与另一段非常相似。"

"时间序列的概率理论大部分涉及平稳时间序列，因此时间序列分析通常需要将非平稳序列转换为平稳序列，以便使用这些理论。例如，可能感兴趣的是从数据中移除趋势和季节性变化，然后尝试用平稳随机过程来建模残差的变化。然而，也值得强调的是，非平稳成分（如趋势）可能比平稳残差更有趣。"

**English explanation:** As Chatfield and Xing (2019) states: "Broadly speaking a time series is said to be stationary if there is no systematic change in mean (no trend), if there is no systematic change in variance and if strictly periodic variations have been removed. In other words, the properties of one section of the data are much like those of any other section."

"Much of the probability theory of time series is concerned with stationary time series, and for this reason time series analysis often requires one to transform a non-stationary series into a stationary one so as to use this theory. For example, it may be of interest to remove the trend and seasonal variation from a set of data and then try to model the variation in the residuals by means of a stationary stochastic process. However, it is also worth stressing that the non-stationary components, such as the trend, may be of more interest than the stationary residuals."

---

#### Topic 2: Stochastic Process / 随机过程

**Formal Definition / 形式化定义**

**中文解释：** 为了建立时间序列的模型，我们将每个时间点t上的观测值X_t视为一个随机变量。这些随机变量的集合称为一个（离散时间）随机过程。

**English explanation:** To build a model of a time series, we consider the X_t to be random variables. The collection of these random variables is called a (discrete-time) stochastic process.

**Definition 2.1 / 定义2.1**

For a stochastic process $\{X_t\}$, we use the following definitions:

**Mean / 均值：**
$$\mu(t) = E[X_t]$$

**Variance / 方差：**
$$\sigma^2(t) = \text{var}(X_t)$$

**Auto-covariance / 自协方差：**
$$\gamma(s, t) = \text{cov}(X_s, X_t) = E[(X_s - \mu(s))(X_t - \mu(t))]$$

**Auto-correlation / 自相关：**
$$\rho(s,t) = \text{corr}(X_s, X_t) = \frac{\gamma(s,t)}{\sqrt{\sigma^2(s)\sigma^2(t)}}$$

**Symbol Explanation Table / 符号解释表：**

| Symbol / 符号 | Meaning / 含义 | Chinese Explanation / 中文解释 |
|:---:|:---|:---|
| $X_t$ | Random variable at time t | 时间t处的随机变量 |
| $\mu(t)$ | Mean function at time t | 时间t处的均值函数 |
| $\sigma^2(t)$ | Variance function at time t | 时间t处的方差函数 |
| $\gamma(s,t)$ | Auto-covariance between $X_s$ and $X_t$ | $X_s$和$X_t$之间的自协方差 |
| $\rho(s,t)$ | Auto-correlation between $X_s$ and $X_t$ | $X_s$和$X_t$之间的自相关 |
| $E[\cdot]$ | Expectation operator | 期望算子 |
| $\text{cov}(\cdot,\cdot)$ | Covariance | 协方差 |
| $\text{corr}(\cdot,\cdot)$ | Correlation | 相关 |

**Remarks / 备注：**

**中文解释：** 自相关函数（autocorrelation function）是对自协方差函数的标准化，它不依赖于X_t的测量单位。它衡量的是X_s和X_t之间的相关性。

**English explanation:** The autocorrelation function, which does not depend on the units in which X_t is measured, is a standardisation of the autocovariance function. It measures the correlation between X_s and X_t.

---

#### Topic 3: Stationarity / 平稳性

**Definition 2.2: Strong Stationarity / 强平稳（严格平稳）**

**中文解释：** 一个随机过程$\{X_t\}$被称为**强平稳**或**严格平稳**，如果对于任意$k, n \in \mathbb{N}$，$\{X_1, ..., X_n\}$和$\{X_{1+k}, ..., X_{n+k}\}$具有相同的分布。

**English explanation:** The stochastic process $\{X_t\}$ is **strongly stationary** or **strictly stationary** if $\{X_1, ..., X_n\}$ and $\{X_{1+k}, ..., X_{n+k}\}$ have the same distribution for all $k, n \in \mathbb{N}$.

**Remarks / 备注：**

1. **中文解释：** 强平稳的含义是：当我们沿着时间轴移动时，随机过程中任意多个随机变量的联合分布保持不变。

   **English explanation:** The meaning of strong stationarity is that the distribution of a number of random variables of the stochastic process is the same as we shift them along the time index axis.

2. **中文解释：** 如果$\{X_t\}$是强平稳的，取$n=1$，则$X_t$与$X_{t+k}$具有相同的分布。特别地，如果前两阶矩有限，则$\mu(t) = E[X_t] = \mu$且$\sigma^2(t) = \text{var}(X_t) = \sigma^2$对所有t成立。因此，具有趋势或季节效应的过程不可能是强平稳的。

   **English explanation:** If $\{X_t\}$ is strongly stationary, for $n=1$, then $X_t$ has the same distribution as $X_{t+k}$ for all $k \in \mathbb{N}$. In particular, if the first two moments are finite then $\mu(t) = E[X_t] = \mu$ and $\sigma^2(t) = \text{var}(X_t) = \sigma^2$ for all $t$. Therefore, a process with trend or seasonal effects cannot be strongly stationary.

3. **中文解释：** 如果$\{X_t\}$是强平稳的，$X_s$和$X_t$的联合分布与$X_{s+k}$和$X_{t+k}$的联合分布相同，这意味着联合分布只依赖于时间差（称为滞后lag）。因此，自协方差和自相关函数也只依赖于滞后（假设它们有限）。

   **English explanation:** If $\{X_t\}$ is strongly stationary, the joint distribution of $X_s$ and $X_t$ is the same as the joint distribution of $X_{s+k}$ and $X_{t+k}$ for all $k, n \in \mathbb{N}$, which implies the joint distribution depends only on the time difference (called lag) $k$. Thus the auto-covariance and auto-correlation functions also depend only on the lag, provided that they are finite.

**Definition 2.3: Weak Stationarity / 弱平稳（二阶平稳）**

**中文解释：** 强平稳对于大多数应用来说过于严格。而且，从单一数据集很难判断强平稳性。因此，我们引入**弱平稳**（也称为二阶平稳），它只对前两阶矩施加条件。

**English explanation:** Strong stationarity is too strong for most applications. Moreover, it is difficult to assess strong stationarity from a single dataset. Instead, we introduce **weak stationarity** (also called second-order stationarity) which imposes conditions only on the first and second moments.

**Formal Definition / 形式化定义：**

A stochastic process $\{X_t\}$ is **weakly stationary** or **second order stationary** if:

1. $\mu(t)$ is constant, i.e. $\mu(t) = \mu$ for all $t$;
2. $\gamma(s, t)$ only depends on the times $t, s$ via the lag $t - s$, and thus $\gamma(s,t)$ can be written as $\gamma_{t-s}$.

**中文解释：** 从今以后，我们使用"平稳"一词来指代弱平稳；如果一个过程是强平稳的，我们会明确使用"强平稳"一词。

注意：$\sigma^2(t) = \sigma^2 = \gamma_0$。

**English explanation:** From now on, we will use the term "stationary" to mean weakly stationary; if a process is strongly stationary, we will use the term "strongly stationary".

Note that $\sigma^2(t) = \sigma^2 = \gamma_0$.

**Example 2.1: White Noise / 白噪声**

**中文解释：** 对于序列$X_t \overset{i.i.d.}{\sim} N(0, 1)$，解释它是否是强平稳的？是否是平稳的？

**English explanation:** For a series $X_t \overset{i.i.d.}{\sim} N(0, 1)$, explain if it is strongly stationary and if it is stationary?

**Solution / 解答：**

**中文解释：** 由于$\mu(t) = 0$，$\sigma^2(t) = 1$，$\gamma(s,t) = 0$对所有$s \neq t$成立，因此$\{X_t\}$是弱平稳的。

集合$\{X_{1+k}, ..., X_{n+k}\}$是独立同分布的标准正态随机变量，对任意偏移$k \in \mathbb{N}$成立，所以$\{X_t\}$是强平稳的。

**English explanation:** Since $\mu(t) = 0$, $\sigma^2(t) = 1$, $\gamma(s,t) = 0$ for all $s \neq t \in \mathbb{N}$, $\{X_t\}$ is weakly stationary.

The collection $\{X_{1+k}, ..., X_{n+k}\}$ is an i.i.d. collection of $N(0, 1)$ random variables for any shift $k \in \mathbb{N}$, so $\{X_t\}$ is strongly stationary.

**Example 2.2: Simple Symmetric Random Walk / 简单对称随机游走**

**中文解释：** 设$X_0 = 0$且$X_t = \sum_{i=1}^t Z_i$，其中$Z_i$独立地以1/2的概率取+1或-1。证明：
- $\{X_t\}$既不是弱平稳也不是强平稳的
- 对于$s < t$，$\gamma(s,t) = s$且$\rho(s,t) = \sqrt{s/t}$

**English explanation:** Let $X_0 = 0$ and $X_t = \sum_{i=1}^t Z_i$, where $Z_i$ independently takes values $+1, -1$ with probability $1/2$ each. Show that:
- $\{X_t\}$ is neither weakly nor strongly stationary
- For $s < t$, $\gamma(s,t) = s$ and $\rho(s,t) = \sqrt{s/t}$

**Solution / 解答：**

**Step 1: Compute the mean / 计算均值**

$$\mu(t) = E[X_t] = E\left[\sum_{i=1}^t Z_i\right] = \sum_{i=1}^t E[Z_i] = \sum_{i=1}^t \left(1 \times \frac{1}{2} + (-1) \times \frac{1}{2}\right) = \sum_{i=1}^t 0 = 0$$

**Step 2: Compute the variance / 计算方差**

$$\sigma^2(t) = \text{var}(X_t) = \sum_{i=1}^t \text{var}(Z_i) = \sum_{i=1}^t (E[Z_i^2] - (E[Z_i])^2) = \sum_{i=1}^t \left(1 \times \frac{1}{2} + (-1)^2 \times \frac{1}{2} - 0\right) = \sum_{i=1}^t 1 = t$$

**中文解释：** 方差依赖于时间t（$\sigma^2(t) = t$），因此该过程既不是弱平稳也不是强平稳的。

**English explanation:** The variance depends on time t ($\sigma^2(t) = t$), therefore the process is neither weakly nor strongly stationary.

**Step 3: Compute the auto-covariance / 计算自协方差**

对于$s < t$：

$$\gamma(s,t) = \text{cov}(X_s, X_t) = E[X_s X_t] = E\left[\left(\sum_{i=1}^s Z_i\right)\left(\sum_{j=1}^t Z_j\right)\right]$$

**中文解释：** 由于$Z_i$是独立的，$E[Z_i Z_j] = 0$当$i \neq j$，且$E[Z_i^2] = 1$。因此：

**English explanation:** Since $Z_i$ are independent, $E[Z_i Z_j] = 0$ when $i \neq j$, and $E[Z_i^2] = 1$. Therefore:

$$E\left[\sum_{i=1}^s \sum_{j=1}^t Z_i Z_j\right] = \sum_{i=1}^s \sum_{j=1}^t E[Z_i Z_j] = \sum_{i=1}^s E[Z_i^2] = \sum_{i=1}^s 1 = s$$

所以$\gamma(s,t) = s$。

**Step 4: Compute the auto-correlation / 计算自相关**

$$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\sigma^2(s)\sigma^2(t)}} = \frac{s}{\sqrt{s \cdot t}} = \sqrt{\frac{s}{t}}$$

**Important Remarks on Stationarity / 关于平稳性的重要备注**

1. **中文解释：** 每个具有有限二阶矩的强平稳过程都是弱平稳的，因为对所有t，$\mu(t) = E[X_t] = E[X_1]$且$\gamma(t, t+k) = \text{cov}(X_t, X_{t+k}) = \text{cov}(X_1, X_{1+k})$。因此这两个量都不依赖于t。

   **English explanation:** Every strongly stationary process with finite second moment is weakly stationary since, for all $t$, $\mu(t) = E[X_t] = E[X_1]$ and $\gamma(t, t+k) = \text{cov}(X_t, X_{t+k}) = \text{cov}(X_1, X_{1+k})$. Therefore, both quantities are independent of $t$.

2. **中文解释：** 强平稳并不意味着弱平稳。例如，独立同分布的标准柯西分布过程是强平稳的，但不是弱平稳的，因为该过程的二阶矩不存在（无穷大）。

   **English explanation:** Strong stationarity does not imply weak stationarity. For example, an i.i.d. process with standard Cauchy distribution is strongly stationary but not weakly stationary because the second moment of the process is not finite.

3. **中文解释：** 弱平稳并不意味着强平稳。例如，定义$X_t$如下：
   $$X_t = \begin{cases} u_t, & \text{如果}t\text{是偶数} \\ \frac{1}{\sqrt{2}}(u_t^2 - 1), & \text{如果}t\text{是奇数} \end{cases}$$
   其中$u_t \overset{i.i.d.}{\sim} N(0, 1)$。（提示：可以使用矩生成函数来找到标准正态随机变量的高阶矩。）

   **English explanation:** Weak stationarity does not imply strong stationarity. For example, let $X_t$ be defined by:
   $$X_t = \begin{cases} u_t, & \text{if }t\text{ is even} \\ \frac{1}{\sqrt{2}}(u_t^2 - 1), & \text{if }t\text{ is odd} \end{cases}$$
   where $u_t \overset{i.i.d.}{\sim} N(0, 1)$. (Hint: can use moment generating function to find higher order moments of standard normal random variable.)

4. **中文解释：** 注意，对于高斯随机过程（Gaussian stochastic process），强平稳和弱平稳是等价的。

   **English explanation:** Notice that for Gaussian stochastic process the strong stationarity and weak stationarity are equivalent.

5. **中文解释：** 如果$\{X_t\}$是弱平稳的，则：
   - $\gamma_0 = \text{cov}(X_t, X_t) = \text{var}(X_t) = \sigma^2$ 对所有t成立
   - $\gamma_k = \text{cov}(X_t, X_{t+k}) = \text{cov}(X_{t-k}, X_t) = \gamma_{-k}$
   
   因此只需考虑滞后$k > 0$。另外：
   $$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\sigma^2(s)\sigma^2(t)}} = \frac{\gamma_{t-s}}{\sqrt{\gamma_0 \gamma_0}} = \frac{\gamma_{t-s}}{\gamma_0}$$
   
   且$\rho(t,t) = \rho_0 = 1$。

   **English explanation:** If $\{X_t\}$ is weakly stationary:
   - $\gamma_0 = \text{cov}(X_t, X_t) = \text{var}(X_t) = \sigma^2$ for all $t$
   - $\gamma_k = \text{cov}(X_t, X_{t+k}) = \text{cov}(X_{t-k}, X_t) = \gamma_{-k}$
   
   So it is enough to consider lags $k > 0$. Also note that:
   $$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\sigma^2(s)\sigma^2(t)}} = \frac{\gamma_{t-s}}{\sqrt{\gamma_0 \gamma_0}} = \frac{\gamma_{t-s}}{\gamma_0}$$
   
   and hence $\rho(t,t) = \rho_0 = 1$.

---

#### Topic 4: Autocorrelation Function (ACF) / 自相关函数

**Definition 2.4 / 定义2.4**

**中文解释：** 量$\rho_k$称为滞后k自相关（lag k autocorrelation）；$\rho_k$作为k的函数称为**自相关函数**（autocorrelation function, acf）。$\rho_k$对k的图称为**相关图**（correlogram）或**acf图**。

**English explanation:** The quantity $\rho_k$ is called the lag $k$ autocorrelation; $\rho_k$ as a function of $k$ is the **autocorrelation function** (acf). A plot of $\rho_k$ against $k$ is called a **correlogram** or **acf plot**.

**Remarks / 备注：**

1. **中文解释：** 严格来说，只有对弱平稳过程计算acf才有意义。然而，我们将会看到，我们可以使用acf来判断一个过程是否平稳。

   **English explanation:** Note that, strictly speaking, it only makes sense to compute the acf for weakly stationary processes. However, we shall see that we can use the acf to diagnose whether a process is stationary or not.

2. $\rho_k = \rho_{-k}$

3. $|\rho_k| \leq 1$。证明见Chatfield and Xing (2019)第3.3节。

4. **中文解释：** acf不能唯一确定底层模型。虽然给定的随机过程有唯一的协方差结构，但反过来一般不成立。

   **English explanation:** The acf does not uniquely identify the underlying model. Although a given stochastic process has a unique covariance structure, the converse is not in general true.

**Estimating the ACF from Data / 从数据估计ACF**

**中文解释：** 如何从数据估计$\mu, \gamma_k, \rho_k$？通常我们会使用：
$$\text{cov}(X,Y) = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$
其中$X_i, Y_i$是独立同分布的X和Y的副本。

但对于时间序列，我们通常只有一个实现$X_1, X_2, ..., X_n$，所以我们不能像上面那样估计$\text{cov}(X_1, X_2)$。然而，如果$\{X_t\}$是平稳的，我们可以使用：

**English explanation:** How can we estimate $\mu, \gamma_k, \rho_k$ from data? Normally we would use:
$$\text{cov}(X,Y) = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$
where $X_i, Y_i$ are i.i.d. copies of $X,Y$.

For a time series, we typically have only one realisation $X_1, X_2, ..., X_n$, so we can't estimate $\text{cov}(X_1, X_2)$ as above. However, if $\{X_t\}$ is stationary, we can use:

**Sample Mean / 样本均值：**
$$\hat{\mu} = \frac{1}{n}\sum_{i=1}^n X_i \approx \mu$$

**Sample Autocovariance / 样本自协方差：**
$$\hat{\gamma}_k = \frac{1}{n}\sum_{i=1}^{n-k} (X_i - \hat{\mu})(X_{i+k} - \hat{\mu}) \approx \gamma_k$$

**Sample Autocorrelation / 样本自相关：**
$$\hat{\rho}_k = \frac{\hat{\gamma}_k}{\hat{\gamma}_0}$$

**中文解释：** 注意对于$\hat{\gamma}_k$，我们