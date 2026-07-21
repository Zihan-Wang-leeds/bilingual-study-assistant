# Section 6: Parameter estimation: MOM, LSE, MLE

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:10
> 来源页: 49-62

---

# 📚 Chapter 6: Parameter Estimation / 参数估计

## 📋 Section Overview / 章节概览

**中文解释：**
本章是时间序列分析课程的核心章节之一。在前面的章节中，我们学习了如何识别时间序列中的趋势、季节性等效应（第1章），如何获得平稳时间序列（第2章），以及各种概率模型如AR、MA、ARMA模型（第3-5章）。现在，我们面临一个实际问题：给定一个时间序列数据，我们如何确定模型中的具体参数值？这就是参数估计问题。

本章将介绍三种主要的参数估计方法：
1. 矩估计法（Method of Moments, MOM）
2. 最小二乘法（Least Squares Estimation, LSE）
3. 极大似然估计法（Maximum Likelihood Estimation, MLE）

我们将分别讨论这些方法在AR模型和MA模型中的应用，并通过R语言实现来展示实际操作。

**English explanation:**
This chapter is one of the core chapters in the time series analysis course. In previous chapters, we learned how to identify trends, seasonality, and other effects in time series (Chapter 1), how to obtain stationary time series (Chapter 2), and various probability models such as AR, MA, and ARMA models (Chapters 3-5). Now we face a practical problem: given a time series dataset, how do we determine the specific parameter values in the model? This is the parameter estimation problem.

This chapter introduces three main parameter estimation methods:
1. Method of Moments (MOM)
2. Least Squares Estimation (LSE)
3. Maximum Likelihood Estimation (MLE)

We will discuss the application of these methods to AR and MA models separately, and demonstrate practical implementation using R.

**本章在课程中的位置 / Position in the course:**
```
Chapter 1: 描述模式 (Describe patterns) ✓
Chapter 2: 平稳性 (Stationarity) ✓
Chapters 3-5: 模型介绍 (Model introduction) ✓
Chapter 6: 参数估计 (Parameter estimation) ← 我们现在在这里
Chapter 7: 模型选择 (Model selection) → 下一章
Chapter 8: 预测 (Forecasting) → 未来章节
```

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解三种估计方法的基本原理**：掌握矩估计法、最小二乘法和极大似然估计法的核心思想及其适用条件。

2. **对AR(p)模型进行参数估计**：能够使用三种方法估计AR模型的自回归系数和噪声方差。

3. **对MA(q)模型进行参数估计**：理解MA模型参数估计的复杂性，掌握矩估计法在MA模型中的应用。

4. **在R中实现参数估计**：能够使用R的`ar()`和`arima()`函数对时间序列进行参数估计。

5. **解释估计结果**：能够解读R输出中的系数、标准误、对数似然值等信息。

6. **处理实际数据**：能够对实际时间序列数据（如航空乘客数据）进行完整的参数估计流程。

**English explanation:**
After completing this chapter, you should be able to:

1. **Understand the basic principles of three estimation methods**: Grasp the core ideas of MOM, LSE, and MLE and their applicability conditions.

2. **Estimate parameters for AR(p) models**: Use all three methods to estimate autoregressive coefficients and noise variance.

3. **Estimate parameters for MA(q) models**: Understand the complexity of MA parameter estimation and apply MOM to MA models.

4. **Implement parameter estimation in R**: Use R's `ar()` and `arima()` functions for time series parameter estimation.

5. **Interpret estimation results**: Read and understand coefficients, standard errors, log-likelihood values, etc., from R output.

6. **Handle real data**: Perform complete parameter estimation procedures on real time series data (such as airline passenger data).

## 📚 Prerequisites / 前置知识

在学习本章之前，你需要掌握以下内容：

**1. 时间序列基础概念 / Basic Time Series Concepts**
- 平稳性 (Stationarity)
- 自相关函数 (ACF)
- 白噪声过程 (White noise process)

**2. ARMA模型 / ARMA Models**
- AR(p)模型的定义和性质
- MA(q)模型的定义和性质
- ARMA(p,q)模型的定义和性质
- Yule-Walker方程

**3. 统计学基础 / Statistical Foundations**
- 矩的概念 (Moments)
- 最小二乘法 (Least squares)
- 极大似然估计 (Maximum likelihood estimation)
- 正态分布 (Normal distribution)

**4. R语言基础 / Basic R**
- 基本R操作
- 时间序列对象 (`ts` object)
- 基本绘图功能

**5. 数学基础 / Mathematical Foundations**
- 方差、协方差计算
- 求导和优化
- 线性代数基础

## 📖 Core Content / 核心内容

### 6.1 Introduction / 引言

#### Intuition / 直觉理解

**中文解释：**
想象你有一组观测数据，比如过去100天的股票价格。你已经通过前面的分析知道这些数据可以用AR(2)模型来描述（即今天的价格与过去两天的价格有关）。但是，你还需要知道具体的系数是多少——比如，今天的价格与昨天的价格相关程度有多强？与前天呢？噪声的方差有多大？

这就是参数估计要解决的问题：给定数据和模型结构，找出最合适的参数值。

**English explanation:**
Imagine you have a set of observed data, such as stock prices from the past 100 days. Through previous analysis, you know these data can be described by an AR(2) model (today's price depends on the past two days' prices). However, you still need to know the specific coefficient values — how strongly does today's price correlate with yesterday's price? What about the day before yesterday? How large is the noise variance?

This is what parameter estimation solves: given data and model structure, find the most appropriate parameter values.

#### Formal Definition / 形式化定义

**中文解释：**
假设我们有一个时间序列 $X_1, X_2, \ldots, X_n$，其中趋势和/或季节性效应（如果存在）已经被移除。我们想要将前面章节中的某个模型拟合到这些数据上。这个问题包含两个部分：

1. **模型选择 (Model selection)**：选择适当的模型类型和阶数（将在第7章讨论）
2. **参数估计 (Parameter estimation)**：在已知模型类型和阶数的情况下，估计参数值（本章内容）

在本章中，我们假设观测数据来自一个平稳且可逆的ARMA(p,q)过程，其中阶数参数p和q是已知的。我们的目标是估计参数：
- 自回归系数：$\alpha_1, \alpha_2, \ldots, \alpha_p$
- 移动平均系数：$\beta_1, \beta_2, \ldots, \beta_q$
- 噪声方差：$\sigma^2$

**English explanation:**
Suppose we have a time series $X_1, X_2, \ldots, X_n$, with trend and/or seasonal effects (if they exist) having been removed. We want to fit one of the models from previous chapters to these data. This problem has two components:

1. **Model selection**: Selecting the appropriate model type and order (to be discussed in Chapter 7)
2. **Parameter estimation**: Estimating parameter values given known model type and order (this chapter)

In this chapter, we assume the observed data come from a stationary and invertible ARMA(p,q) process, where the order parameters p and q are known. Our goal is to estimate:
- Autoregressive coefficients: $\alpha_1, \alpha_2, \ldots, \alpha_p$
- Moving average coefficients: $\beta_1, \beta_2, \ldots, \beta_q$
- Noise variance: $\sigma^2$

#### Symbol Table / 符号表

| 符号 | 含义 (中文) | Meaning (English) |
|------|-------------|-------------------|
| $X_t$ | 时间序列在时刻t的观测值 | Time series observation at time t |
| $\alpha_i$ | 第i个自回归系数 | i-th autoregressive coefficient |
| $\beta_j$ | 第j个移动平均系数 | j-th moving average coefficient |
| $\sigma^2$ | 白噪声方差 | White noise variance |
| $p$ | AR部分的阶数 | Order of AR part |
| $q$ | MA部分的阶数 | Order of MA part |
| $n$ | 样本量 | Sample size |
| $\epsilon_t$ | 白噪声过程 | White noise process |

---

### 6.2 Estimating Parameters of an AR(p) / AR(p)模型的参数估计

#### Intuition / 直觉理解

**中文解释：**
对于AR(p)模型，我们有三种不同的参数估计方法，每种方法都有其独特的思路：

1. **矩估计法 (MOM)**：就像"用样本特征推断总体特征"。我们计算样本的自相关系数，然后利用Yule-Walker方程反推出参数值。

2. **最小二乘法 (LSE)**：就像"找到一条最合适的线"。我们选择参数使得预测误差的平方和最小。

3. **极大似然估计法 (MLE)**：就像"找到最可能产生观测数据的参数值"。我们假设数据服从某种分布，然后找到使观测数据出现概率最大的参数值。

**English explanation:**
For AR(p) models, we have three different parameter estimation methods, each with its unique approach:

1. **Method of Moments (MOM)**: Like "inferring population characteristics from sample characteristics." We calculate sample autocorrelation coefficients and then use Yule-Walker equations to back-calculate parameter values.

2. **Least Squares Estimation (LSE)**: Like "finding the best-fitting line." We choose parameters to minimize the sum of squared prediction errors.

3. **Maximum Likelihood Estimation (MLE)**: Like "finding the parameter values most likely to produce the observed data." We assume the data follows some distribution and find parameter values that maximize the probability of observing our data.

---

### 6.2.1 Method of Moments (MOM) / 矩估计法

#### Formal Definition / 形式化定义

**中文解释：**
矩估计法的核心思想是：用样本矩（如样本均值、样本方差、样本自相关系数）替换总体矩（理论值），然后解方程得到未知参数的估计值。

对于AR(p)模型，矩估计法直接使用Yule-Walker方程（第3.5节中的方程(3.2)）：

$$\rho_k = \alpha_1\rho_{k-1} + \alpha_2\rho_{k-2} + \ldots + \alpha_p\rho_{k-p}, \quad k = 1, 2, \ldots, p$$

其中 $\rho_k$ 是理论自相关函数（ACF）。矩估计法将理论 $\rho_k$ 替换为样本自相关函数 $\hat{\rho}_k$，然后解这个线性方程组得到 $\alpha_1, \alpha_2, \ldots, \alpha_p$ 的估计值。

**English explanation:**
The core idea of MOM is: replace population moments (theoretical values) with sample moments (sample mean, sample variance, sample autocorrelation coefficients), then solve the equations to obtain parameter estimates.

For AR(p) models, MOM directly uses the Yule-Walker equations (Equation (3.2) in Section 3.5):

$$\rho_k = \alpha_1\rho_{k-1} + \alpha_2\rho_{k-2} + \ldots + \alpha_p\rho_{k-p}, \quad k = 1, 2, \ldots, p$$

where $\rho_k$ is the theoretical autocorrelation function (ACF). MOM replaces the theoretical $\rho_k$ with the sample autocorrelation function $\hat{\rho}_k$, then solves this linear system to obtain estimates of $\alpha_1, \alpha_2, \ldots, \alpha_p$.

#### Symbol Table / 符号表

| 符号 | 含义 (中文) | Meaning (English) |
|------|-------------|-------------------|
| $\rho_k$ | 滞后k的理论自相关系数 | Theoretical autocorrelation at lag k |
| $\hat{\rho}_k$ | 滞后k的样本自相关系数 | Sample autocorrelation at lag k |
| $\alpha_i$ | 第i个自回归系数 | i-th autoregressive coefficient |
| $\sigma_X^2$ | 时间序列的理论方差 | Theoretical variance of the time series |
| $\hat{\sigma}_X^2$ | 时间序列的样本方差 | Sample variance of the time series |
| $\sigma^2$ | 白噪声方差 | White noise variance |
| $\hat{\sigma}^2$ | 白噪声方差的估计值 | Estimated white noise variance |

---

#### Worked Example 6.1: AR(1) MOM Estimation / 例题6.1: AR(1)的矩估计

**Problem / 问题：**
假设 $X_t = \alpha X_{t-1} + \epsilon_t$ 是平稳的，$\epsilon_t$ 是方差为 $\sigma^2$ 的白噪声。求参数 $\alpha$ 和 $\sigma^2$ 的矩估计。

**Solution / 解答：**

**Step 1: 估计 $\alpha$ / Estimate $\alpha$**

**中文解释：**
对于AR(1)模型，Yule-Walker方程给出：
$$\rho_1 = \alpha$$

这里 $\rho_1$ 是滞后1的理论自相关系数。矩估计法用样本自相关系数 $\hat{\rho}_1$ 替换理论值，得到：
$$\hat{\alpha} = \hat{\rho}_1$$

其中 $\hat{\rho}_1$ 是样本自相关系数，计算公式为：
$$\hat{\rho}_1 = \frac{\sum_{t=2}^n (X_t - \bar{X})(X_{t-1} - \bar{X})}{\sum_{t=1}^n (X_t - \bar{X})^2}$$

**English explanation:**
For the AR(1) model, the Yule-Walker equation gives:
$$\rho_1 = \alpha$$

Here $\rho_1$ is the theoretical autocorrelation at lag 1. MOM replaces the theoretical value with the sample autocorrelation $\hat{\rho}_1$, giving:
$$\hat{\alpha} = \hat{\rho}_1$$

where $\hat{\rho}_1$ is the sample autocorrelation, calculated as:
$$\hat{\rho}_1 = \frac{\sum_{t=2}^n (X_t - \bar{X})(X_{t-1} - \bar{X})}{\sum_{t=1}^n (X_t - \bar{X})^2}$$

**Step 2: 估计 $\sigma^2$ / Estimate $\sigma^2$**

**中文解释：**
对于AR(1)模型，$X_t = \alpha X_{t-1} + \epsilon_t$，两边取方差。注意 $\epsilon_t$ 与 $X_{t-1}$ 独立（由定义），所以：
$$\text{var}(X_t) = \alpha^2 \text{var}(X_{t-1}) + \text{var}(\epsilon_t)$$

由于 $\{X_t\}$ 是平稳的，$\text{var}(X_t) = \text{var}(X_{t-1}) = \sigma_X^2$，所以：
$$\sigma_X^2 = \alpha^2 \sigma_X^2 + \sigma^2$$

解出 $\sigma^2$：
$$\sigma^2 = \sigma_X^2 (1 - \alpha^2)$$

用样本方差 $\hat{\sigma}_X^2$ 替换理论方差 $\sigma_X^2$，用 $\hat{\alpha}$ 替换 $\alpha$，得到：
$$\hat{\sigma}^2 = \hat{\sigma}_X^2 (1 - \hat{\alpha}^2)$$

其中 $\hat{\sigma}_X^2$ 是样本方差：
$$\hat{\sigma}_X^2 = \frac{1}{n-1} \sum_{t=1}^n (X_t - \bar{X})^2$$

**English explanation:**
For the AR(1) model, $X_t = \alpha X_{t-1} + \epsilon_t$, take variance on both sides. Note that $\epsilon_t$ is independent of $X_{t-1}$ by definition, so:
$$\text{var}(X_t) = \alpha^2 \text{var}(X_{t-1}) + \text{var}(\epsilon_t)$$

Since $\{X_t\}$ is stationary, $\text{var}(X_t) = \text{var}(X_{t-1}) = \sigma_X^2$, so:
$$\sigma_X^2 = \alpha^2 \sigma_X^2 + \sigma^2$$

Solving for $\sigma^2$:
$$\sigma^2 = \sigma_X^2 (1 - \alpha^2)$$

Replace the theoretical variance $\sigma_X^2$ with the sample variance $\hat{\sigma}_X^2$, and $\alpha$ with $\hat{\alpha}$, giving:
$$\hat{\sigma}^2 = \hat{\sigma}_X^2 (1 - \hat{\alpha}^2)$$

where $\hat{\sigma}_X^2$ is the sample variance:
$$\hat{\sigma}_X^2 = \frac{1}{n-1} \sum_{t=1}^n (X_t - \bar{X})^2$$

**Summary / 总结：**
AR(1)模型的矩估计为：
$$\hat{\alpha} = \hat{\rho}_1$$
$$\hat{\sigma}^2 = \hat{\sigma}_X^2 (1 - \hat{\alpha}^2)$$

---

### 6.2.2 Least Squares Estimation (LSE) / 最小二乘法

#### Formal Definition / 形式化定义

**中文解释：**
最小二乘法的核心思想是：选择参数使得残差平方和（Residual Sum of Squares, RSS）最小化。对于AR(p)模型，残差是实际观测值与模型预测值之间的差异。

对于AR(1)模型 $X_t = \alpha X_{t-1} + \epsilon_t$，残差平方和为：
$$S(\alpha) = \sum_{t=2}^n (X_t - \alpha X_{t-1})^2$$

注意：由于 $X_0$ 通常未知，我们从 $t=2$ 开始求和，并将 $X_0$ 设为0。

**English explanation:**
The core idea of LSE is: choose parameters to minimize the Residual Sum of Squares (RSS). For AR(p) models, residuals are the differences between actual observations and model predictions.

For the AR(1) model $X_t = \alpha X_{t-1} + \epsilon_t$, the residual sum of squares is:
$$S(\alpha) = \sum_{t=2}^n (X_t - \alpha X_{t-1})^2$$

Note: Since $X_0$ is usually unknown, we start the sum from $t=2$ and set $X_0$ to 0.

---

#### Worked Example 6.2: AR(1) LSE Estimation / 例题6.2: AR(1)的最小二乘估计

**Problem / 问题：**
假设 $X_t = \alpha X_{t-1} + \epsilon_t$，$\epsilon_t$ 是方差为 $\sigma^2$ 的白噪声。求参数 $\alpha$ 和 $\sigma^2$ 的最小二乘估计。

**Solution / 解答：**

**Step 1: 估计 $\alpha$ / Estimate $\alpha$**

**中文解释：**
我们通过最小化 $S(\alpha)$ 来估计 $\alpha$。对 $S(\alpha)$ 求导并令导数为0：

$$\frac{\partial S(\alpha)}{\partial \alpha} = 2\sum_{t=2}^n (X_t - \alpha X_{t-1})(-X_{t-1}) = 0$$

展开：
$$-2\sum_{t=2}^n X_t X_{t-1} + 2\alpha\sum_{t=2}^n X_{t-1}^2 = 0$$

解出 $\alpha$：
$$\hat{\alpha} = \frac{\sum_{t=2}^n X_t X_{t-1}}{\sum_{t=2}^n X_{t-1}^2}$$

注意，这个估计量与样本自相关系数 $\hat{\rho}_1$ 非常相似，但不完全相同（因为分母不同，且没有减去均值）。

**English explanation:**
We estimate $\alpha$ by minimizing $S(\alpha)$. Take the derivative of $S(\alpha)$ and set it to zero:

$$\frac{\partial S(\alpha)}{\partial \alpha} = 2\sum_{t=2}^n (X_t - \alpha X_{t-1})(-X_{t-1}) = 0$$

Expanding:
$$-2\sum_{t=2}^n X_t X_{t-1} + 2\alpha\sum_{t=2}^n X_{t-1}^2 = 0$$

Solving for $\alpha$:
$$\hat{\alpha} = \frac{\sum_{t=2}^n X_t X_{t-1}}{\sum_{t=2}^n X_{t-1}^2}$$

Note that this estimator is very similar to the sample autocorrelation $\hat{\rho}_1$, but not exactly the same (different denominator and no mean subtraction).

**Step 2: 估计 $\sigma^2$ / Estimate $\sigma^2$**

**中文解释：**
给定 $\hat{\alpha}$，我们可以估计 $\sigma^2$ 为：
$$\hat{\sigma}^2 = \frac{1}{n-1} \sum_{t=2}^n (X_t - \hat{\alpha} X_{t-1})^2$$

这里分母用 $n-1$ 是因为我们估计了一个参数（$\alpha$）。

展开这个表达式：
$$\hat{\sigma}^2 = \frac{1}{n-1} \left[ \sum_{t=2}^n X_t^2 - 2\hat{\alpha}\sum_{t=2}^n X_t X_{t-1} + \hat{\alpha}^2\sum_{t=2}^n X_{t-1}^2 \right]$$

代入 $\hat{\alpha}$ 的表达式，可以证明：
$$\hat{\sigma}^2 = \hat{\sigma}_X^2 (1 - \hat{\alpha}^2)$$

这与矩估计法的结果相同！

**English explanation:**
Given $\hat{\alpha}$, we can estimate $\sigma^2$ as:
$$\hat{\sigma}^2 = \frac{1}{n-1} \sum_{t=2}^n (X_t - \hat{\alpha} X_{t-1})^2$$

Here we use $n-1$ in the denominator because we estimated one parameter ($\alpha$).

Expanding this expression:
$$\hat{\sigma}^2 = \frac{1}{n-1} \left[ \sum_{t=2}^n X_t^2 - 2\hat{\alpha}\sum_{t=2}^n X_t X_{t-1} + \hat{\alpha}^2\sum_{t=2}^n X_{t-1}^2 \right]$$

Substituting the expression for $\hat{\alpha}$, it can be shown that:
$$\hat{\sigma}^2 = \hat{\sigma}_X^2 (1 - \hat{\alpha}^2)$$

This is the same result as from MOM!

**Key Insight / 关键洞察：**
对于AR(1)模型，矩估计法和最小二乘法得到的 $\sigma^2$ 估计是相同的。这并非巧合——对于AR模型，这两种方法往往给出相似的结果。

---

### 6.2.3 Maximum Likelihood Estimation (MLE) / 极大似然估计法

#### Formal Definition / 形式化定义

**中文解释：**
极大似然估计法的核心思想是：似然函数表达了在给定不同参数值时，观测到当前数据的可能性有多大。似然函数是数据的联合密度函数，但将其视为未知参数的函数（给定观测数据）。极大似然估计就是使这个似然函数最大化的参数值，即给定观测数据，最"可能"的参数值。

要使用这种方法，我们需要假设 $\epsilon_t$ 的分布（通常假设为正态分布），然后找到似然函数并最大化它。

**English explanation:**
The core idea of MLE is: the likelihood function expresses how probable a given set of observed data is for different values of parameters. The likelihood function is the joint density function of the data, but treated as a function of the unknown parameters, given the observed data. The maximum likelihood estimates (MLEs) are the values of the parameters that maximize this likelihood function, i.e., that are the most "likely" parameter values given the data we actually observed.

To use this method, we need to assume a distribution for $\epsilon_t$ (usually normal distribution), then find the likelihood function and maximize it.

---

#### Worked Example 6.3: AR(1) MLE Estimation / 例题6.3: AR(1)的极大似然估计

**Problem / 问题：**
假设 $X_0 = 0$，$X_t = \alpha X_{t-1} + \epsilon_t$，$\epsilon_t \sim N(0, \sigma^2)$。求参数 $\alpha$ 和 $\sigma^2$ 的极大似然估计。

**Solution / 解答：**

**Step 1: 写出条件分布 / Write the conditional distribution**

**中文解释：**
给定 $X_{t-1}$，$X_t$ 的条件分布为：
$$X_t | X_{t-1} \sim N(\alpha X_{t-1}, \sigma^2)$$

所以条件密度函数为：
$$f(X_t | X_{t-1}) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(X_t - \alpha X_{t-1})^2}{2\sigma^2}\right)$$

**English explanation:**
Given $X_{t-1}$, the conditional distribution of $X_t$ is:
$$X_t | X_{t-1} \sim N(\alpha X_{t-1}, \sigma^2)$$

So the conditional density function is:
$$f(X_t | X_{t-1}) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(X_t - \alpha X_{t-1})^2}{2\sigma^2}\right)$$

**Step 2: 写出联合密度 / Write the joint density**

**中文解释：**
利用条件概率的链式法则，$X_1, X_2, \ldots, X_n$ 的联合密度为：
$$f(X_1, \ldots, X_n) = f(X_1) \cdot f(X_2|X_1) \cdot \ldots \cdot f(X_n|X_{n-1})$$

由于我们假设 $X_0 = 0$，$X_1 = \epsilon_1 \sim N(0, \sigma^2)$，所以：
$$f(X_1, \ldots, X_n) = (2\pi\sigma^2)^{-n/2} \exp\left(-\frac{1}{2\sigma^2} \sum_{t=1}^n (X_t - \alpha X_{t-1})^2\right)$$

这就是似然函数 $L(\alpha, \sigma^2)$。

**English explanation:**
Using the chain rule of conditional probability