# Section 7: Model selection

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:11
> 来源页: 63-75

---

# MATH2703: Time Series / 时间序列分析

## Chapter 7: Model Selection / 模型选择

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章是时间序列分析的核心章节之一。在前几章中，我们学习了如何识别时间序列中的趋势和季节性（第1章），如何获得平稳时间序列（第2章），以及各种概率模型如AR、MA、ARMA和ARIMA模型（第3-5章）。第6章介绍了如何估计模型参数。现在，我们面临一个关键问题：**如何选择最适合数据的模型？** 本章将系统地介绍模型选择的工具和方法，包括自相关函数（ACF）、偏自相关函数（PACF）、模型诊断检查和信息准则（如AIC）。

**English explanation:** This chapter is one of the core chapters in time series analysis. In previous chapters, we learned how to identify trends and seasonality (Chapter 1), how to obtain stationary time series (Chapter 2), and various probability models such as AR, MA, ARMA, and ARIMA models (Chapters 3-5). Chapter 6 introduced methods for estimating model parameters. Now we face a critical question: **How do we select the most appropriate model for our data?** This chapter systematically introduces tools and methods for model selection, including the autocorrelation function (ACF), partial autocorrelation function (PACF), model diagnostic checking, and information criteria (such as AIC).

---

### 🎯 Learning Objectives / 学习目标

By the end of this chapter, you should be able to / 学完本章后，你应该能够：

1. **Use ACF and PACF plots to identify appropriate ARMA models** / 使用ACF和PACF图识别合适的ARMA模型
2. **Distinguish between AR, MA, ARMA, and ARIMA processes using their ACF/PACF patterns** / 通过ACF/PACF模式区分AR、MA、ARMA和ARIMA过程
3. **Interpret sample ACF and PACF plots in practice** / 在实践中解释样本ACF和PACF图
4. **Perform model diagnostic checking using residual analysis** / 使用残差分析进行模型诊断检查
5. **Apply the Ljung-Box test to check residual independence** / 应用Ljung-Box检验检查残差独立性
6. **Use AIC (Akaike Information Criterion) for model comparison** / 使用AIC（赤池信息准则）进行模型比较

---

### 📚 Prerequisites / 前置知识

Before starting this chapter, you should be familiar with / 开始本章之前，你应该熟悉：

- **Stationarity (Chapter 2)** / 平稳性（第2章）：Understand what makes a time series stationary
- **AR, MA, ARMA models (Chapters 3-5)** / AR、MA、ARMA模型（第3-5章）：Know the definitions and properties
- **Parameter estimation (Chapter 6)** / 参数估计（第6章）：Understand how to estimate model parameters
- **Basic R programming** / 基本的R编程：Ability to run R commands for time series analysis

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Introduction to Model Selection / 模型选择简介

**Intuition / 直觉理解**

**中文解释：** 想象你是一位侦探，面对一组时间序列数据，你需要找出"凶手"——即最适合描述这些数据的模型。这个过程类似于侦探破案：首先收集线索（观察数据），然后提出嫌疑人（候选模型），接着收集证据（诊断检查），最后做出判断（选择模型）。模型选择不是一次性完成的，而是一个迭代过程：提出模型→估计参数→检查模型→如果模型不合适，重新提出模型。

**English explanation:** Imagine you are a detective faced with a set of time series data, and you need to find the "culprit" — the model that best describes the data. This process is like solving a crime: first collect clues (observe the data), then identify suspects (candidate models), gather evidence (diagnostic checking), and finally make a judgment (select the model). Model selection is not a one-time process but an iterative one: propose model → estimate parameters → check model → if inadequate, propose a new model.

**The Model Building Process / 模型构建过程**

The raw material describes three main steps / 原始材料描述了三个主要步骤：

```
[Model Identification / 模型识别] → [Model Estimation / 模型估计] → [Model Checking / 模型检查]
```

**中文解释：** 这三个步骤构成了一个循环。首先，我们通过观察数据的ACF和PACF图来识别可能的模型（模型识别）。然后，使用第6章的方法估计模型参数（模型估计）。最后，通过检查残差来验证模型是否合适（模型检查）。如果模型不合适，我们回到第一步重新识别。

**English explanation:** These three steps form a cycle. First, we identify possible models by examining the ACF and PACF plots of the data (model identification). Then, we estimate the model parameters using methods from Chapter 6 (model estimation). Finally, we verify whether the model is adequate by examining the residuals (model checking). If the model is inadequate, we return to the first step and re-identify.

---

#### Topic 2: Using ACF for Model Identification / 使用ACF进行模型识别

**Intuition / 直觉理解**

**中文解释：** 自相关函数（ACF）就像是时间序列的"指纹"。不同类型的模型会产生不同形状的ACF。通过观察样本ACF的形状，我们可以初步判断数据可能来自哪种模型。例如，MA(q)过程的ACF在滞后q之后突然截断（变为零），而AR(p)过程的ACF则缓慢衰减（拖尾）。

**English explanation:** The autocorrelation function (ACF) is like a "fingerprint" of the time series. Different types of models produce different shapes of ACF. By observing the shape of the sample ACF, we can make an initial judgment about which model the data might come from. For example, the ACF of an MA(q) process "cuts off" (becomes zero) after lag q, while the ACF of an AR(p) process decays slowly (attenuates).

**Formal Properties / 形式化性质**

The raw material summarizes the ACF properties of different models / 原始材料总结了不同模型的ACF性质：

1. **For MA(q) processes / 对于MA(q)过程：**
   - ρ_k = 0 for all k > q (the "cuts off" property / "截断"性质)
   - 中文解释：MA(q)过程的ACF在滞后q之后全部为零，这是一个非常明显的特征，使得MA模型很容易被识别。
   - English explanation: The ACF of an MA(q) process is zero for all lags beyond q, which is a very distinctive feature that makes MA models easy to identify.

2. **For AR(p) processes / 对于AR(p)过程：**
   - ρ_k = φ_1 ρ_{k-1} + φ_2 ρ_{k-2} + ... + φ_p ρ_{k-p} for k ≥ 1
   - 中文解释：AR(p)过程的ACF满足Yule-Walker方程，表现为混合的衰减指数和正弦波，缓慢衰减（拖尾）。
   - English explanation: The ACF of an AR(p) process satisfies the Yule-Walker equations and exhibits a mixture of damped exponentials and sinusoids, decaying slowly (attenuating).

3. **For ARMA(p,q) processes / 对于ARMA(p,q)过程：**
   - Its ACF behaves the same as that of AR(p), except for the first q values
   - 中文解释：ARMA(p,q)过程的ACF与AR(p)类似，但前q个值可能不同。总体上也表现为拖尾而非截断。
   - English explanation: The ACF of an ARMA(p,q) process behaves similarly to that of an AR(p), except for the first q values. It also generally attenuates rather than cuts off.

**Specific ACF Patterns / 具体的ACF模式**

For AR(1) processes / 对于AR(1)过程：
- ρ_k = α^k (where α is the AR coefficient / 其中α是AR系数)
- If α > 0: exponential decay / 指数衰减
- If α < 0: exponential decay with alternating signs / 交替符号的指数衰减

For AR(p) processes with p > 1 / 对于p > 1的AR(p)过程：
- ρ_k = c * r^k * cos(ωk + θ) for some constants c, r, ω, θ, with |r| < 1
- 中文解释：高阶AR过程的ACF表现为阻尼振荡（damped oscillations），即振幅逐渐减小的波动。
- English explanation: Higher-order AR processes exhibit damped oscillations in their ACF, meaning oscillations with decreasing amplitude.

**For ARIMA(p,d,q) processes / 对于ARIMA(p,d,q)过程：**
- ρ_k decays very slowly / ACF衰减非常缓慢
- 中文解释：如果ACF衰减非常缓慢，这通常表明数据是非平稳的，需要进行差分。d的值通过反复差分直到ACF表现出AR、MA或ARMA的特征来确定。
- English explanation: If the ACF decays very slowly, this usually indicates that the data is non-stationary and requires differencing. The value of d is found by differencing repeatedly (i.e., considering ∇X_t, ∇²X_t, ...) until the ACF behaves like that of AR, MA, or ARMA.

**⚠️ Warning about overdifferencing / 关于过度差分的警告：**
- 中文解释：不要过度差分，因为这可能会引入原本不存在的依赖关系。例如，如果对白噪声进行一次差分，我们会得到一个MA(1)过程。
- English explanation: Be careful not to overdifference because this may introduce dependence where none exists. For example, if we difference white noise once, we will end up with an MA(1) process.

---

#### Topic 3: Worked Example - ACF Pattern Recognition / 例题：ACF模式识别

**Example 7.1 / 例7.1**

**中文解释：** 这个例子展示了如何通过观察时间序列图和对应的ACF图来建议合适的模型。原始材料中包含了多个时间序列（X, Y, Z, W）的图形，我们需要根据ACF的形状来判断模型类型。

**English explanation:** This example demonstrates how to suggest appropriate models by examining time series plots and their corresponding ACF plots. The raw material contains plots of multiple time series (X, Y, Z, W), and we need to determine the model type based on the ACF shape.

**Solution / 解答：**

1. **Series X / 序列X：**
   - ACF decays exponentially / ACF呈指数衰减
   - Suggestion: AR(1) with α > 0 / 建议：AR(1)模型，α > 0
   - 中文解释：指数衰减是AR(1)过程的典型特征。由于衰减是正的（没有交替符号），所以α > 0。
   - English explanation: Exponential decay is a typical feature of AR(1) processes. Since the decay is positive (no alternating signs), α > 0.

2. **Series Y / 序列Y：**
   - ACF cuts off at lag 1 / ACF在滞后1处截断
   - Suggestion: MA(1) / 建议：MA(1)模型
   - 中文解释：ACF在滞后1之后突然变为零，这是MA(1)过程的典型特征。
   - English explanation: The ACF suddenly becomes zero after lag 1, which is a typical feature of MA(1) processes.

3. **Series Z / 序列Z：**
   - ACF has damped oscillations / ACF呈阻尼振荡
   - Suggestion: AR model with order > 1 / 建议：阶数大于1的AR模型
   - 中文解释：阻尼振荡表明可能是高阶AR过程，但仅凭ACF很难确定具体阶数。
   - English explanation: Damped oscillations suggest a higher-order AR process, but it's difficult to determine the exact order from ACF alone.

4. **Series W / 序列W：**
   - ACF decays very slowly / ACF衰减非常缓慢
   - Suggestion: ARIMA with d > 0 / 建议：d > 0的ARIMA模型
   - After first-order differencing: ACF cuts off at lag 0 (white noise) / 一阶差分后：ACF在滞后0处截断（白噪声）
   - Final suggestion: ARIMA(0,1,0) / 最终建议：ARIMA(0,1,0)模型
   - 中文解释：缓慢衰减表明非平稳性。一阶差分后ACF在滞后0处截断，说明差分后的序列是白噪声，因此不需要二阶差分。
   - English explanation: Slow decay indicates non-stationarity. After first-order differencing, the ACF cuts off at lag 0, indicating the differenced series is white noise, so second-order differencing is not needed.

---

#### Topic 4: Partial Autocorrelation Function (PACF) / 偏自相关函数

**Intuition / 直觉理解**

**中文解释：** 前面我们看到，ACF可以帮助我们区分非平稳序列、MA模型和可能的AR模型。但是，仅凭ACF很难确定AR过程的阶数。例如，AR(2)和AR(3)的ACF看起来可能非常相似。这时我们需要一个新的工具——偏自相关函数（PACF）。PACF衡量的是在消除了中间滞后项的影响后，两个观测值之间的"纯"相关性。

**English explanation:** As we saw earlier, ACF can help distinguish non-stationary series, MA models, and possibly AR models. However, it's difficult to determine the order of an AR process from ACF alone. For example, AR(2) and AR(3) may have very similar ACF patterns. This is where we need a new tool — the Partial Autocorrelation Function (PACF). PACF measures the "pure" correlation between two observations after removing the effects of intermediate lags.

**Motivating Example / 动机示例**

**Example 7.2 / 例7.2**

**中文解释：** 这个例子通过R模拟展示了PACF的直观意义。我们分别对白噪声拟合AR(1)，对AR(1)序列拟合AR(2)，对AR(2)序列拟合AR(3)，观察估计出的AR系数。

**English explanation:** This example demonstrates the intuitive meaning of PACF through R simulations. We fit AR(1) to white noise, AR(2) to an AR(1) series, and AR(3) to an AR(2) series, and observe the estimated AR coefficients.

**R Code and Results / R代码和结果：**

```r
set.seed(123)
n <- 500

# Fit AR(1) to white noise / 对白噪声拟合AR(1)
wn <- rnorm(122)
arima(wn, order = c(1,0,0), include.mean = FALSE)
# Result: φ̂₁ ≈ -0.0138 ≈ 0

# Fit AR(2) to AR(1) series / 对AR(1)序列拟合AR(2)
X.ar1 <- arima.sim(n, model=list(ar=c(0.8)))
arima(X.ar1, order = c(2,0,0), include.mean = FALSE)
# Result: φ̂₁ ≈ 0.7199, φ̂₂ ≈ 0.0101 ≈ 0

# Fit AR(3) to AR(2) series / 对AR(2)序列拟合AR(3)
X.ar2 <- arima.sim(n, model=list(ar=c(1, -0.5)))
arima(X.ar2, order = c(3,0,0), include.mean = FALSE)
# Result: φ̂₁ ≈ 0.9901, φ̂₂ ≈ -0.4982, φ̂₃ ≈ 0.0119 ≈ 0
```

**中文解释：** 观察结果：当我们对白噪声拟合AR(1)时，φ̂₁ ≈ 0；对AR(1)序列拟合AR(2)时，φ̂₂ ≈ 0；对AR(2)序列拟合AR(3)时，φ̂₃ ≈ 0。这说明，如果我们拟合的阶数超过了真实阶数，多余的系数会接近零。这正是PACF的核心思想。

**English explanation:** Observing the results: when we fit AR(1) to white noise, φ̂₁ ≈ 0; when we fit AR(2) to an AR(1) series, φ̂₂ ≈ 0; when we fit AR(3) to an AR(2) series, φ̂₃ ≈ 0. This shows that if we fit an order higher than the true order, the extra coefficients will be close to zero. This is the core idea of PACF.

**Formal Definition / 形式化定义**

**Definition 7.1 (Partial Autocorrelation / 偏自相关)**

For k > 0, we use the Yule-Walker equations to fit an AR(k) model (using φ̂_{k1}, ..., φ̂_{kk}), then φ̂_{kk} is called the **lag-k partial autocorrelation (PACF)** of {X_t}.

**中文解释：** 对于每个滞后k，我们拟合一个AR(k)模型，得到系数φ̂_{k1}, ..., φ̂_{kk}。其中最后一个系数φ̂_{kk}就是滞后k的偏自相关。它衡量的是在控制了中间滞后（1到k-1）的影响后，X_t和X_{t-k}之间的相关性。

**English explanation:** For each lag k, we fit an AR(k) model and obtain coefficients φ̂_{k1}, ..., φ̂_{kk}. The last coefficient φ̂_{kk} is the lag-k partial autocorrelation. It measures the correlation between X_t and X_{t-k} after controlling for the effects of intermediate lags (1 to k-1).

**Interpretation of PACF / PACF的解释：**

When fitting an AR(k) model, the last coefficient α_k (now denoted by φ_{kk}, the lag-k PACF) measures the **excess correlation** at lag k which is not accounted for by an AR(k-1) model.

**中文解释：** PACF衡量的是在已经考虑了AR(k-1)模型后，滞后k处还剩余多少相关性。如果这个值显著非零，说明我们需要更高的阶数。

**English explanation:** PACF measures how much correlation remains at lag k after accounting for an AR(k-1) model. If this value is significantly non-zero, it suggests we need a higher order.

**Key Properties of PACF / PACF的关键性质**

1. **For AR(p) processes / 对于AR(p)过程：**
   - The PACF **cuts off** at lag p / PACF在滞后p处截断
   - 中文解释：这是AR模型最重要的识别特征。如果PACF在滞后p之后突然变为零，那么数据可能来自AR(p)模型。
   - English explanation: This is the most important identifying feature of AR models. If the PACF suddenly becomes zero after lag p, the data likely comes from an AR(p) model.

2. **For MA(q) and ARMA(p,q) processes / 对于MA(q)和ARMA(p,q)过程：**
   - The PACF has exponential decay or damped oscillations / PACF呈指数衰减或阻尼振荡
   - 中文解释：MA和ARMA过程的PACF表现为拖尾（缓慢衰减），而不是截断。
   - English explanation: MA and ARMA processes exhibit PACF that attenuates (decays slowly) rather than cuts off.

**Summary Table: ACF vs PACF Patterns / ACF与PACF模式总结表**

| Model / 模型 | ACF Pattern / ACF模式 | PACF Pattern / PACF模式 |
|-------------|----------------------|----------------------|
| AR(p) | Attenuates (拖尾) | Cuts off at lag p (在滞后p截断) |
| MA(q) | Cuts off at lag q (在滞后q截断) | Attenuates (拖尾) |
| ARMA(p,q) | Attenuates (拖尾) | Attenuates (拖尾) |
| ARIMA(p,d,q) | Decays very slowly (衰减非常缓慢) | - |

**Computing PACF in R / 在R中计算PACF**

```r
# Method 1: Using acf() with type="partial"
acf(series, type="partial")

# Method 2: Using pacf()
pacf(series)
```

**中文解释：** 注意，样本ACF和样本PACF的截断只是近似截断，不是精确的零。我们需要结合置信区间来判断。

**English explanation:** Note that the sample ACF and sample PACF only cut off approximately, not exactly at zero. We need to consider confidence intervals when making judgments.

---

#### Topic 5: Worked Example - ACF and PACF Analysis / 例题：ACF和PACF分析

**Example 7.3 / 例7.3**

**中文解释：** 这个例子展示了如何结合ACF和PACF图来识别模型，并估计参数。原始材料中包含了三个序列（X, Y, Z）的时间图、ACF图和PACF图。

**English explanation:** This example demonstrates how to combine ACF and PACF plots to identify models and estimate parameters. The raw material contains time plots, ACF plots, and PACF plots for three series (X, Y, Z).

**Part 1: Series X / 第一部分：序列X**

**Given statistics / 已知统计量：**
- Sample mean / 样本均值: x̄ = -0.39
- Sample variance / 样本方差: s²_x = 3.87
- Sample autocorrelation at lag 1 / 滞后1样本自相关: ρ̂₁ = 0.874

**Solution / 解答：**

**中文解释：** 
1. **模型识别：** ACF图呈指数衰减，这排除了MA模型（MA模型的ACF会截断）。PACF图在滞后1处截断，这强烈表明是AR(1)模型，且系数为正（因为ACF衰减是正的）。
2. **参数估计：** 使用矩估计法（MOM）：
   - α̂₁ = ρ̂₁ = 0.874
   - σ̂² = (1 - α̂₁²) × s²_x = (1 - 0.874²) × 3.87 = 0.914

**English explanation:**
1. **Model identification:** The ACF plot shows exponential decay, which rules out MA models (MA models would have a cutting-off ACF). The PACF plot cuts off at lag 1, strongly suggesting an AR(1) model with a positive coefficient (since the ACF decay is positive).
2. **Parameter estimation:** Using Method of Moments (MOM):
   - α̂₁ = ρ̂₁ = 0.874
   - σ̂² = (1 - α̂₁²) × s²_x = (1 - 0.874²) × 3.87 = 0.914

**Part 2: Series Y / 第二部分：序列Y**

**Given statistics / 已知统计量：**
- Sample mean / 样本均值: ȳ = 0.002
- Sample variance / 样本方差: s²_y = 1.50
- Sample autocorrelation at lag 1 / 滞后1样本自相关: ρ̂₁ = -0.472

**Solution / 解答：**

**中文解释：**
1. **模型识别：** ACF图在滞后1处截断，这强烈表明是MA(1)过程。注意，我们不需要检查PACF，因为ACF已经给出了明确的信号。
2. **参数估计：** 对于MA(1)模型，矩估计公式为：
   - θ̂₁ = (-1 ± √(1 - 4ρ̂₁²)) / (2ρ̂₁)
   - 代入ρ̂₁ = -0.472：θ̂₁ = (-1 ± √(1 - 4×(-0.472)²)) / (2×(-0.472))
   - 选择满足可逆性条件的解：θ̂₁ = -0.71
   - σ̂² = (1 + θ̂₁²)⁻¹ × s²_y = (1 + (-0.71)²)⁻¹ × 1.5 = 0.997

**English explanation:**
1. **Model identification:** The ACF plot cuts off at lag 1, strongly suggesting an MA(1) process. Note that we don't need to examine the PACF since the ACF gives a clear signal.
2. **Parameter estimation:** For MA(1) models, the MOM formula is:
   - θ̂₁ = (-1 ± √(1 - 4ρ̂₁²)) / (2ρ̂₁)
   - Substituting ρ̂₁ = -0.472: θ̂₁ = (-1 ± √(1 - 4×(-0.472)²)) / (2×(-0.472))
   - Choose the solution satisfying invertibility: θ̂₁ = -0.71
   - σ̂² = (1 + θ̂₁²)⁻¹ × s²_y = (1 + (-0.71)²)⁻¹ × 1.5 = 0.997

**Part 3: Series Z / 第三部分：序列Z**

**Solution / 解答：**

**中文解释：**
1. **模型识别：** ACF图呈阻尼振荡，这排除了MA模型。PACF图在滞后2处截断，这强烈表明是AR(2)过程。
2. **注意：** 这里没有给出具体的统计量，所以我们只做模型识别，不做参数估计。

**English explanation:**
1. **Model identification:** The ACF plot shows damped oscillations, ruling out MA models. The PACF plot cuts off at lag 2, strongly suggesting an AR(2) process.
2. **Note:** No specific statistics are given here, so we only perform model identification, not parameter estimation.

---

#### Topic 6: Model Diagnostic Checking / 模型诊断检查

**⚠️ Note from the raw material / 原始材料说明：**
"This subsection (subsection 7.4) is not examinable in the final exam, but examinable in the coursework."
"本小节（7.4节）不在期末考试范围内，但在课程作业中会考到。"

**Intuition / 直觉理解**

**中文解释：** 在选择了模型并估计了参数之后，我们需要检查这个模型是否真的合适。这就像医生给病人开药后需要复查一样。模型诊断检查主要通过分析残差（residuals）来进行。残差是观测值与模型拟合值之间的差异。如果模型是合适的，残差应该表现得像白噪声——没有明显的模式，没有自相关。

**English explanation:** After selecting a model and estimating parameters, we need to check whether the model is actually appropriate. This is like a doctor checking on a patient after prescribing medication. Model diagnostic checking is primarily done by analyzing the residuals — the differences between observed values and model-fitted values. If the model is adequate, the residuals should behave like white noise — no obvious patterns, no autocorrelation.

**Definition of Residuals / 残差的定义**

For a time series X_t, suppose a model has been fitted:
- α(B)Y_t = β(B