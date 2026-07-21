# Section 8: Forecasting

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:12
> 来源页: 76-82

---

# 📘 MATH2703: Time Series - Chapter 8: Forecasting / 时间序列预测

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是时间序列分析中最重要的应用之一——预测。当我们已经建立了一个满意的模型（包括确定性部分和随机性部分）后，就可以利用这个模型来预测未来的数值。本章将介绍两种主要的预测方法：最小均方误差（MMSE）方法和基于模型的方法。我们将学习如何计算预测值、如何评估预测误差，以及如何构建预测区间。

**English explanation:** This chapter covers one of the most important applications of time series analysis—forecasting. Once we have built a satisfactory model (including both deterministic and stochastic components), we can use this model to predict future values. This chapter introduces two main forecasting methods: the Minimum Mean Square Error (MMSE) method and the model-based method. We will learn how to compute forecasts, how to evaluate forecast errors, and how to construct prediction intervals.

**Why this matters / 为什么重要：**
- Forecasting is the ultimate goal of many time series analyses / 预测是许多时间序列分析的最终目标
- Understanding forecast uncertainty is crucial for decision-making / 理解预测的不确定性对决策至关重要
- These methods apply to economics, finance, weather prediction, and many other fields / 这些方法适用于经济学、金融学、天气预报等许多领域

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解MMSE预测的基本原理**：能够解释为什么条件期望是最小均方误差预测
2. **计算ARMA模型的MMSE预测**：能够使用MA表示形式计算预测值
3. **计算预测误差的方差**：能够推导和理解预测误差的方差如何随预测步长增加
4. **构建预测区间**：能够在正态假设下构建95%预测区间
5. **应用基于模型的方法**：能够使用ARIMA模型方程进行预测
6. **处理实际数据**：能够使用残差估计未知的误差项

After completing this chapter, you should be able to:
1. **Understand the principle of MMSE forecasting**: Explain why conditional expectation is the minimum mean square error forecast
2. **Compute MMSE forecasts for ARMA models**: Use the MA representation to calculate forecasts
3. **Compute forecast error variances**: Derive and understand how forecast error variance increases with lead time
4. **Construct prediction intervals**: Build 95% prediction intervals under the normality assumption
5. **Apply model-based methods**: Use ARIMA model equations for forecasting
6. **Handle real data**: Use residuals to estimate unknown error terms

## 📚 Prerequisites / 前置知识

在开始本章之前，你应该已经掌握：

**中文解释：**
- 时间序列的基本概念（平稳性、自相关函数）
- ARMA(p,q)模型的定义和性质
- MA(∞)表示形式（Wold分解定理）
- 白噪声过程的性质（均值0，方差σ²，不相关）
- 条件期望的基本概念
- 正态分布和分位数

**English explanation:**
- Basic concepts of time series (stationarity, autocorrelation function)
- Definition and properties of ARMA(p,q) models
- MA(∞) representation (Wold decomposition theorem)
- Properties of white noise processes (mean 0, variance σ², uncorrelated)
- Basic concepts of conditional expectation
- Normal distribution and quantiles

## 📖 Core Content / 核心内容

### 8.1 Introduction / 引言

#### Intuition / 直觉理解

**中文解释：** 想象你正在观察一个时间序列，比如某只股票每日的收盘价。你已经收集了n天的数据：X₁, X₂, ..., Xₙ。现在你想预测未来第l天的价格Xₙ₊ₗ。这个预测值我们记为X̂ₙ(l)，其中l称为"超前时间"（lead time）。我们希望这个预测值尽可能接近真实值，并且我们还需要知道这个预测有多可靠——这就是预测区间的作用。

**English explanation:** Imagine you're observing a time series, such as the daily closing price of a stock. You've collected n days of data: X₁, X₂, ..., Xₙ. Now you want to predict the price l days into the future, Xₙ₊ₗ. We denote this forecast as X̂ₙ(l), where l is called the "lead time." We want this forecast to be as close as possible to the true value, and we also need to know how reliable this forecast is—this is where prediction intervals come in.

#### Formal Definition / 形式化定义

**中文解释：** 给定数据值X₁, X₂, ..., Xₙ，我们想要：
1. 预测未来值Xₙ₊ₗ（真实值），使用预测值X̂ₙ(l)，其中l是预测的超前时间
2. 为X̂ₙ(l)构建置信区间
3. 确保预测误差eₙ(l) = Xₙ₊ₗ - X̂ₙ(l)尽可能小

**English explanation:** Given data values X₁, X₂, ..., Xₙ, we want to:
1. Predict a future value Xₙ₊ₗ (true value) by a forecast X̂ₙ(l), where l is the lead time
2. Have confidence limits for X̂ₙ(l)
3. Ensure the forecast error eₙ(l) = Xₙ₊ₗ - X̂ₙ(l) is as small as possible

**Notation Table / 符号表：**

| Symbol | Meaning (中文) | Meaning (English) |
|--------|----------------|-------------------|
| Xₜ | 时间t的观测值 | Observation at time t |
| n | 当前时间点 | Current time point |
| l | 超前时间（预测步长） | Lead time (forecast horizon) |
| X̂ₙ(l) | 基于n个观测值对Xₙ₊ₗ的预测 | Forecast of Xₙ₊ₗ based on n observations |
| eₙ(l) | 预测误差 = Xₙ₊ₗ - X̂ₙ(l) | Forecast error = Xₙ₊ₗ - X̂ₙ(l) |

### 8.2 Forecasting using MMSE / 使用最小均方误差进行预测

#### Intuition / 直觉理解

**中文解释：** 最小均方误差（MMSE）方法的核心思想是：我们想要选择一个预测值X̂ₙ(l)，使得预测误差的平方的期望值最小。也就是说，我们要最小化：

E[(eₙ(l))²] = E[(Xₙ₊ₗ - X̂ₙ(l))²]

这就像是在射箭——我们希望箭（预测值）尽可能接近靶心（真实值）。均方误差衡量的是"偏离程度"的平方的平均值。

**English explanation:** The core idea of the Minimum Mean Square Error (MMSE) method is: we want to choose a forecast X̂ₙ(l) that minimizes the expected squared forecast error. That is, we minimize:

E[(eₙ(l))²] = E[(Xₙ₊ₗ - X̂ₙ(l))²]

This is like archery—we want the arrow (forecast) to be as close as possible to the bullseye (true value). The mean square error measures the average squared deviation.

#### Formal Definition / 形式化定义

**中文解释：** 对于平稳可逆的ARMA(p,q)过程Xₜ，MMSE预测由以下公式给出：

X̂ₙ(l) = ∑ⱼ₌ₗ^∞ βⱼεₙ₊ₗ₋ⱼ

其中{εₜ}是ARMA模型中的白噪声过程，方差为σ²。

**English explanation:** For a stationary and invertible ARMA(p,q) process Xₜ, the MMSE forecast is given by:

X̂ₙ(l) = ∑ⱼ₌ₗ^∞ βⱼεₙ₊ₗ₋ⱼ

where {εₜ} is the white noise process with variance σ² in the ARMA model.

**Key insight / 关键洞察：** 这个公式告诉我们，MMSE预测只使用到时间n为止的误差项（εₙ, εₙ₋₁, ...），而不使用未来的误差项（εₙ₊₁, εₙ₊₂, ...）。这是因为未来的误差项是未知的，我们无法预测它们。

#### Proof / 证明 (Example 8.1)

**中文解释：** 让我们一步步证明MMSE预测的公式。

**步骤1：** 将Xₜ写成MA(∞)形式
假设Xₜ可以写成（可能无限阶的）MA模型：
Xₜ = β₀εₜ + β₁εₜ₋₁ + β₂εₜ₋₂ + β₃εₜ₋₃ + ...

其中β₀ = 1（标准化）。

**步骤2：** 写出Xₙ₊ₗ的表达式
Xₙ₊ₗ = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + β₂εₙ₊ₗ₋₂ + ... + βₗ₋₁εₙ₊₁ + βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ...

注意：前l项（β₀到βₗ₋₁）涉及未来的ε（εₙ₊₁到εₙ₊ₗ），后面的项涉及已知的ε（εₙ, εₙ₋₁, ...）。

**步骤3：** 写出预测值的形式
我们想要将X̂ₙ(l)写成{εₜ}到时间n的线性组合：
X̂ₙ(l) = β₀*εₙ + β₁*εₙ₋₁ + β₂*εₙ₋₂ + ...

其中β₀*, β₁*, β₂*, ...是我们需要选择的系数。

**步骤4：** 写出预测误差
eₙ(l) = Xₙ₊ₗ - X̂ₙ(l)
= [β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁] + [(βₗ - β₀*)εₙ + (βₗ₊₁ - β₁*)εₙ₋₁ + ...]

**步骤5：** 计算均方误差
由于E[εₜεₛ] = 0（当t≠s时）且E[εₜ²] = σ²，我们有：
E[(Xₙ₊ₗ - X̂ₙ(l))²] = σ²[∑ₖ₌₀^(l-1) βₖ² + ∑ₛ₌₀^∞ (βₗ₊ₛ - βₛ*)²]

**步骤6：** 最小化
要使这个表达式最小，我们需要选择βₛ* = βₗ₊ₛ（对所有s≥0）。这样第二项就变为0。

**步骤7：** 得到MMSE预测
X̂ₙ(l) = βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ...
= ∑ⱼ₌ₗ^∞ βⱼεₙ₊ₗ₋ⱼ

**English explanation:** Let's prove the MMSE forecast formula step by step.

**Step 1:** Write Xₜ in MA(∞) form
Assume Xₜ can be written as a (possibly infinite order) MA model:
Xₜ = β₀εₜ + β₁εₜ₋₁ + β₂εₜ₋₂ + β₃εₜ₋₃ + ...

where β₀ = 1 (standardization).

**Step 2:** Write the expression for Xₙ₊ₗ
Xₙ₊ₗ = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + β₂εₙ₊ₗ₋₂ + ... + βₗ₋₁εₙ₊₁ + βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ...

Note: The first l terms (β₀ to βₗ₋₁) involve future ε's (εₙ₊₁ to εₙ₊ₗ), while the remaining terms involve known ε's (εₙ, εₙ₋₁, ...).

**Step 3:** Write the forecast form
We want to write X̂ₙ(l) as a linear combination of {εₜ} up to time n:
X̂ₙ(l) = β₀*εₙ + β₁*εₙ₋₁ + β₂*εₙ₋₂ + ...

where β₀*, β₁*, β₂*, ... are coefficients we need to choose.

**Step 4:** Write the forecast error
eₙ(l) = Xₙ₊ₗ - X̂ₙ(l)
= [β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁] + [(βₗ - β₀*)εₙ + (βₗ₊₁ - β₁*)εₙ₋₁ + ...]

**Step 5:** Compute the mean square error
Since E[εₜεₛ] = 0 (when t≠s) and E[εₜ²] = σ², we have:
E[(Xₙ₊ₗ - X̂ₙ(l))²] = σ²[∑ₖ₌₀^(l-1) βₖ² + ∑ₛ₌₀^∞ (βₗ₊ₛ - βₛ*)²]

**Step 6:** Minimize
To minimize this expression, we need to choose βₛ* = βₗ₊ₛ (for all s≥0). This makes the second term zero.

**Step 7:** Obtain the MMSE forecast
X̂ₙ(l) = βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ...
= ∑ⱼ₌ₗ^∞ βⱼεₙ₊ₗ₋ⱼ

#### Key Properties of Forecast Error / 预测误差的关键性质

**中文解释：** 当使用最优系数βₛ* = βₗ₊ₛ时，预测误差有以下重要性质：

**性质1：** 预测误差形成一个MA(l-1)过程
eₙ(l) = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁

这意味着预测误差只依赖于未来l-1个白噪声项。

**性质2：** 预测误差的方差
var(eₙ(l)) = σ²∑ₖ₌₀^(l-1) βₖ²

这个方差随着l增加而增加——预测得越远，不确定性越大。

**性质3：** 预测误差的自协方差
对于m > 0：
cov(eₙ(l), eₙ(l+m)) = σ²∑ₖ₌₀^(l-1) βₖβₖ₊ₘ

这意味着不同超前时间的预测误差是相关的。

**English explanation:** When using the optimal coefficients βₛ* = βₗ₊ₛ, the forecast error has the following important properties:

**Property 1:** The forecast error forms an MA(l-1) process
eₙ(l) = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁

This means the forecast error depends only on the next l-1 white noise terms.

**Property 2:** Variance of forecast error
var(eₙ(l)) = σ²∑ₖ₌₀^(l-1) βₖ²

This variance increases as l increases—the further we forecast, the greater the uncertainty.

**Property 3:** Autocovariance of forecast errors
For m > 0:
cov(eₙ(l), eₙ(l+m)) = σ²∑ₖ₌₀^(l-1) βₖβₖ₊ₘ

This means forecast errors at different lead times are correlated.

### 8.3 Conditional Mean Interpretation / 条件均值解释

#### Intuition / 直觉理解

**中文解释：** MMSE预测有一个非常重要的性质：它等于给定已知观测值条件下的条件期望。也就是说：

X̂ₙ(l) = E[Xₙ₊ₗ | X₁, X₂, ..., Xₙ]

这很直观——给定我们已经知道的所有信息，对未来值的最佳猜测就是条件期望。同时，这也意味着所有未来的白噪声项εₜ（t > n）的最佳预测就是0，因为我们没有任何关于它们的信息。

**English explanation:** The MMSE forecast has a very important property: it equals the conditional expectation given the known observations. That is:

X̂ₙ(l) = E[Xₙ₊ₗ | X₁, X₂, ..., Xₙ]

This is intuitive—given all the information we already know, the best guess for a future value is the conditional expectation. This also means that the best forecast for all future white noise terms εₜ (t > n) is simply 0, since we have no information about them.

#### Formal Result / 形式化结果

**中文解释：** 在正态假设下，我们可以证明：
1. X̂ₙ(l) = E[Xₙ₊ₗ | X₁, ..., Xₙ]
2. var(Xₙ₊ₗ | X₁, ..., Xₙ) = var(eₙ(l))
3. 95%预测区间为：X̂ₙ(l) ± 1.96√(var(eₙ(l)))

**English explanation:** Under the normality assumption, we can show that:
1. X̂ₙ(l) = E[Xₙ₊ₗ | X₁, ..., Xₙ]
2. var(Xₙ₊ₗ | X₁, ..., Xₙ) = var(eₙ(l))
3. The 95% prediction interval is: X̂ₙ(l) ± 1.96√(var(eₙ(l)))

**Where does 1.96 come from? / 1.96从哪里来？**
- 1.96是标准正态分布的97.5%分位数（z₀.₉₇₅）
- 这意味着P(-1.96 < Z < 1.96) = 0.95，其中Z ~ N(0,1)
- 所以95%的观测值落在均值±1.96个标准差范围内

#### Proof / 证明 (Example 8.2)

**中文解释：** 证明X̂ₙ(l) = E[Xₙ₊ₗ | X₁, ..., Xₙ]

**步骤1：** 写出Xₙ₊ₗ的MA表示
Xₙ₊ₗ = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁ + βₗεₙ + βₗ₊₁εₙ₋₁ + ...

**步骤2：** 取条件期望
E[Xₙ₊ₗ | X₁, ..., Xₙ] = β₀E[εₙ₊ₗ|X₁,...,Xₙ] + β₁E[εₙ₊ₗ₋₁|X₁,...,Xₙ] + ... + βₗ₋₁E[εₙ₊₁|X₁,...,Xₙ] + βₗE[εₙ|X₁,...,Xₙ] + βₗ₊₁E[εₙ₋₁|X₁,...,Xₙ] + ...

**步骤3：** 利用"未来ε的最佳预测为0"
对于t > n，E[εₜ|X₁,...,Xₙ] = 0（未来值未知）
对于t ≤ n，E[εₜ|X₁,...,Xₙ] = εₜ（过去值已知）

**步骤4：** 得到结果
E[Xₙ₊ₗ | X₁, ..., Xₙ] = βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ... = X̂ₙ(l)

**English explanation:** Proving X̂ₙ(l) = E[Xₙ₊ₗ | X₁, ..., Xₙ]

**Step 1:** Write Xₙ₊ₗ in MA representation
Xₙ₊ₗ = β₀εₙ₊ₗ + β₁εₙ₊ₗ₋₁ + ... + βₗ₋₁εₙ₊₁ + βₗεₙ + βₗ₊₁εₙ₋₁ + ...

**Step 2:** Take conditional expectation
E[Xₙ₊ₗ | X₁, ..., Xₙ] = β₀E[εₙ₊ₗ|X₁,...,Xₙ] + β₁E[εₙ₊ₗ₋₁|X₁,...,Xₙ] + ... + βₗ₋₁E[εₙ₊₁|X₁,...,Xₙ] + βₗE[εₙ|X₁,...,Xₙ] + βₗ₊₁E[εₙ₋₁|X₁,...,Xₙ] + ...

**Step 3:** Use "best forecast of future ε is 0"
For t > n, E[εₜ|X₁,...,Xₙ] = 0 (future values unknown)
For t ≤ n, E[εₜ|X₁,...,Xₙ] = εₜ (past values known)

**Step 4:** Obtain the result
E[Xₙ₊ₗ | X₁, ..., Xₙ] = βₗεₙ + βₗ₊₁εₙ₋₁ + βₗ₊₂εₙ₋₂ + ... = X̂ₙ(l)

#### Prediction Interval / 预测区间

**中文解释：** 在正态假设下，95%预测区间为：
Xₙ₊ₗ ∈ X̂ₙ(l) ± 1.96√(var(eₙ(l)))

其中var(eₙ(l)) = σ²∑ₖ₌₀^(l-1) βₖ²

注意：在实际应用中，模型参数需要估计，所以真实的95%区间会稍微宽一些。

**English explanation:** Under the normality assumption, the 95% prediction interval is:
Xₙ₊ₗ ∈ X̂ₙ(l) ± 1.96√(var(eₙ(l)))

where var(eₙ(l)) = σ²∑ₖ₌₀^(l-1) βₖ²

Note: In practice, model parameters need to be estimated, so the true 95% interval is slightly wider.

### Worked Examples / 例题

#### Example 8.3: MA(1) Process / MA(1)过程

**中文解释：** 考虑MA(1)过程：Xₜ = εₜ + 0.7εₜ₋₁，其中εₜ ~ iid N(0, σ²=1)。我们有4个观测值：x₁ = -0.6, x₂ = 1.4, x₃ = 1.2, x₄ = 0.18。

**English explanation:** Consider the MA(1) process: Xₜ = εₜ + 0.7εₜ₋₁, where εₜ ~ iid N(0, σ²=1). We have 4 observations: x₁ = -0.6, x₂ = 1.4, x₃ = 1.2, x₄ = 0.18.

**Step 1: Compute the MMSE forecast / 计算MMSE预测**

**中文解释：** 对于MA(1)过程，β₀ = 1, β₁ = 0.7, βⱼ = 0（对于j ≥ 2）。所以：
- X̂₄(1) = β₁ε₄ = 0.7ε₄
- X̂₄(l) = 0（对于l > 1）

我们需要估计ε₄。使用MA(1)模型的残差递推公式：
ε₄ = x₄ - 0.7ε₃
ε₃ = x₃ - 0.7ε₂
ε₂ = x₂ - 0.7ε₁
ε₁ = x₁（假设ε₀ = 0）

计算：
ε₁ = -0.6
ε₂ = 1.4 - 0.7(-0.6) = 1.4 + 0.42 = 1.82
ε₃ = 1.2 - 0.7(1.82) = 1.2 - 1.274 = -0.074
ε₄ = 0.18 - 0.7(-0.074) = 0.18 + 0.0518 = 0.2318

所以X̂₄(1) = 0.7 × 0.2318 = 0.1623

**English explanation:** For the MA(1) process, β₀ = 1, β₁ = 0.7, βⱼ = 0 (for j ≥ 2). So:
- X̂₄(1) = β₁ε₄ = 0.7ε₄
- X̂₄(l) = 0 (for l > 1)

We need to estimate ε₄. Using the recursive formula for MA(1) residuals:
ε₄ = x₄ - 0.7ε₃
ε₃ = x₃ - 0.7ε₂
ε₂ = x₂ - 0.7ε₁
ε₁ = x₁ (assuming ε₀ = 0)

Computing:
ε₁ = -0.6
ε₂ = 1.4 - 0.7(-0.6) = 1.4 + 0.42 = 1.82
ε₃ = 1.2 - 0.7(1.82) = 1.2 - 1.274 = -0.074
ε₄ = 0.18 - 0.7(-0.074) = 0.18 + 0.0518 =