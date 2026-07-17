# Problem Sheet 9 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:15
> 来源页 / Source Pages: 89-90

---

好的，作为大学随机过程课程的导师，我将为您提供MATH2702课程习题集9的完整、详细的逐步解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Consider a Markov jump process with state space 𝒮 = {0,1,2,…,𝑁} and generator matrix
Q = 
⎛⎜⎜⎜⎜⎜⎜
⎝−𝑞₀ 𝑞₀₁ 𝑞₀₂ ⋯ 𝑞₀ₙ
0 0 0 ⋯ 0
0 0 0 ⋯ 0
⋮ ⋮ ⋮ ⋱ ⋮
0 0 0 ⋯ 0⎞⎟⎟⎟⎟⎟⎟
⎠.
(a) Draw a transition rate diagram for this jump process.
This process is a “multiple decrement model”: there is one “active state” 0 and a number of “exit states” 1,2,…,𝑁 .
(b) What is the probability that the process exits at state 𝑖?
(c) Give a 95% prediction interval for the amount of time spent in the active state. (Your answer will be in terms of 𝑞₀.)

**中文翻译:**
考虑一个状态空间为 𝒮 = {0,1,2,…,𝑁} 的马尔可夫跳跃过程，其生成元矩阵为
Q = 
⎛⎜⎜⎜⎜⎜⎜
⎝−𝑞₀ 𝑞₀₁ 𝑞₀₂ ⋯ 𝑞₀ₙ
0 0 0 ⋯ 0
0 0 0 ⋯ 0
⋮ ⋮ ⋮ ⋱ ⋮
0 0 0 ⋯ 0⎞⎟⎟⎟⎟⎟⎟
⎠。
(a) 画出该跳跃过程的转移速率图。
这个过程是一个“多重减因模型”：有一个“活跃状态”0和多个“退出状态”1,2,…,𝑁。
(b) 过程在状态𝑖退出的概率是多少？
(c) 给出在活跃状态中停留时间的95%预测区间。（你的答案将用𝑞₀表示。）

**Knowledge Points / 考查知识点:**
- 马尔可夫跳跃过程 (Markov Jump Process)
- 生成元矩阵 (Generator Matrix)
- 转移速率图 (Transition Rate Diagram)
- 指数分布与停留时间 (Exponential Distribution and Holding Time)
- 多重减因模型 (Multiple Decrement Model)

**Step-by-Step Solution / 逐步解答:**

**(a) Transition Rate Diagram / 转移速率图**

**Step 1: Interpret the Generator Matrix / 解读生成元矩阵**
The generator matrix Q defines the rates of jumping between states. The off-diagonal entry $q_{ij}$ for $i \neq j$ is the rate of jumping from state $i$ to state $j$. The diagonal entry $q_{ii}$ is defined as $q_{ii} = -\sum_{j \neq i} q_{ij}$.
生成元矩阵Q定义了状态间跳跃的速率。对于$i \neq j$，非对角线元素$q_{ij}$是从状态$i$跳跃到状态$j$的速率。对角线元素$q_{ii}$定义为$q_{ii} = -\sum_{j \neq i} q_{ij}$。

**Step 2: Identify the Rates / 识别速率**
From the given Q matrix:
- Row 0: $q_{00} = -q_0$, and $q_{0i} = q_{0i}$ for $i=1,2,...,N$. This means from state 0, the process can jump to any state $i$ with rate $q_{0i}$. The total rate of leaving state 0 is $q_0 = \sum_{i=1}^N q_{0i}$.
- Rows 1 to N: All entries are 0. This means $q_{ii} = 0$ and $q_{ij} = 0$ for $i \neq j$. A row of all zeros indicates that these are **absorbing states**. Once the process enters any state $i \ge 1$, it stays there forever.
根据给定的Q矩阵：
- 第0行：$q_{00} = -q_0$，且对于$i=1,2,...,N$，$q_{0i} = q_{0i}$。这意味着从状态0，过程可以以速率$q_{0i}$跳跃到任何状态$i$。离开状态0的总速率是$q_0 = \sum_{i=1}^N q_{0i}$。
- 第1到N行：所有元素都是0。这意味着$q_{ii} = 0$且对于$i \neq j$，$q_{ij} = 0$。全零行表示这些是**吸收状态**。一旦过程进入任何$i \ge 1$的状态，它将永远停留在那里。

**Step 3: Draw the Diagram / 画出图形**
The diagram has state 0 as the only non-absorbing state. From state 0, there are arrows pointing to each absorbing state $i$, labeled with the rate $q_{0i}$.
图中，状态0是唯一的非吸收状态。从状态0出发，有指向每个吸收状态$i$的箭头，并标有速率$q_{0i}$。

```
      q_01     q_02     q_03           q_0N
  1 <------ 0 ------> 2 ------> 3 ... ------> N
  (abs.)   (active)  (abs.)   (abs.)        (abs.)
```

**(b) Probability of Exiting at State i / 在状态i退出的概率**

**Step 1: Recall the Jump Chain / 回顾跳跃链**
The probability that the process, upon leaving state 0, jumps to a specific state $i$ is given by the transition probability of the embedded Markov jump chain. This probability is proportional to the jump rate.
过程在离开状态0时，跳跃到特定状态$i$的概率由嵌入的马尔可夫跳跃链的转移概率给出。这个概率与跳跃速率成正比。

**Step 2: Calculate the Probability / 计算概率**
The total rate of leaving state 0 is $q_0 = \sum_{j=1}^N q_{0j}$. The rate of jumping to state $i$ is $q_{0i}$. The probability of the first jump being to state $i$ is:
离开状态0的总速率是$q_0 = \sum_{j=1}^N q_{0j}$。跳跃到状态$i$的速率是$q_{0i}$。第一次跳跃到状态$i$的概率是：
$$P(\text{exit at state } i) = \frac{q_{0i}}{q_0} = \frac{q_{0i}}{\sum_{j=1}^N q_{0j}}$$
Since all other states are absorbing, the process "exits" at the state it first jumps to.
由于所有其他状态都是吸收态，过程在其首次跳跃到的状态“退出”。

**(c) 95% Prediction Interval for Time in Active State / 活跃状态停留时间的95%预测区间**

**Step 1: Identify the Distribution of Holding Time / 确定停留时间的分布**
In a Markov jump process, the time spent in a state $i$ before jumping, $T_i$, is exponentially distributed with parameter $-q_{ii}$ (the total exit rate from that state).
在马尔可夫跳跃过程中，在跳跃前停留在状态$i$的时间$T_i$，服从参数为$-q_{ii}$（离开该状态的总速率）的指数分布。

**Step 2: Apply to State 0 / 应用于状态0**
Here, the total exit rate from state 0 is $q_0 = -q_{00}$. So, the holding time in the active state, $T_0$, is:
这里，离开状态0的总速率是$q_0 = -q_{00}$。所以，在活跃状态的停留时间$T_0$为：
$$T_0 \sim \text{Exp}(q_0)$$
The probability density function (pdf) is $f(t) = q_0 e^{-q_0 t}$ for $t \ge 0$. The mean is $1/q_0$.
概率密度函数为$f(t) = q_0 e^{-q_0 t}$，$t \ge 0$。均值为$1/q_0$。

**Step 3: Find the Quantiles / 找到分位数**
A 95% prediction interval $[a, b]$ for $T_0$ satisfies $P(a \le T_0 \le b) = 0.95$. A common choice is the equal-tailed interval, where $P(T_0 < a) = 0.025$ and $P(T_0 > b) = 0.025$.
一个95%的预测区间$[a, b]$满足$P(a \le T_0 \le b) = 0.95$。一个常见的选择是等尾区间，其中$P(T_0 < a) = 0.025$且$P(T_0 > b) = 0.025$。

**Step 4: Calculate the Lower Bound / 计算下限**
$P(T_0 \le a) = 1 - e^{-q_0 a} = 0.025$
$e^{-q_0 a} = 0.975$
$-q_0 a = \ln(0.975)$
$a = -\frac{\ln(0.975)}{q_0}$

**Step 5: Calculate the Upper Bound / 计算上限**
$P(T_0 \ge b) = e^{-q_0 b} = 0.025$
$-q_0 b = \ln(0.025)$
$b = -\frac{\ln(0.025)}{q_0}$

**Step 6: State the Interval / 写出区间**
The 95% prediction interval for the time spent in the active state is:
在活跃状态中停留时间的95%预测区间为：
$$\left[ -\frac{\ln(0.975)}{q_0}, -\frac{\ln(0.025)}{q_0} \right]$$

**Final Answer / 最终答案:**
(a) Diagram as shown above.
(b) $P(\text{exit at state } i) = \frac{q_{0i}}{q_0}$
(c) 95% prediction interval: $\boxed{\left[ -\frac{\ln(0.975)}{q_0}, -\frac{\ln(0.025)}{q_0} \right]}$

**Key Insight / 解题要点:**
The key is recognizing that the diagonal element $-q_0$ is the total exit rate, which determines the exponential holding time, and the off-diagonal elements $q_{0i}$ determine the probabilities of the embedded jump chain.
关键在于认识到对角线元素$-q_0$是总退出速率，它决定了指数停留时间，而非对角线元素$q_{0i}$决定了嵌入跳跃链的概率。

---

### Question 2 / 第2题

**Problem / 题目原文:**
Consider the Markov jump process $(X(t))$ with state space $\mathcal{S} = \{1,2,3\}$ and generator matrix
$$Q = \begin{pmatrix} -4 & 3 & 1 \\ 2 & -6 & 4 \\ 1 & 2 & -3 \end{pmatrix}.$$
The process begins from the state $X(0) = 1$. Let $(Y_n)$ be the associated Markov jump chain.
(a) Write down the transition matrix $R$ of the jump chain.
(b) What is the expected time of the first jump $J_1$?
(c) What is the probability the first jump is to state 2?
(d) By conditioning on the first jump, calculate the expected time of the second jump time $J_2 = T_1 + T_2$.
(e) What is the probability that the second jump is to state 2?
(f) What is the probability that the third jump is to state 2?

**中文翻译:**
考虑一个马尔可夫跳跃过程$(X(t))$，其状态空间为$\mathcal{S} = \{1,2,3\}$，生成元矩阵为
$$Q = \begin{pmatrix} -4 & 3 & 1 \\ 2 & -6 & 4 \\ 1 & 2 & -3 \end{pmatrix}.$$
过程从状态$X(0) = 1$开始。令$(Y_n)$为相关的马尔可夫跳跃链。
(a) 写出跳跃链的转移矩阵$R$。
(b) 第一次跳跃时间$J_1$的期望是多少？
(c) 第一次跳跃到状态2的概率是多少？
(d) 通过对第一次跳跃进行条件化，计算第二次跳跃时间$J_2 = T_1 + T_2$的期望。
(e) 第二次跳跃到状态2的概率是多少？
(f) 第三次跳跃到状态2的概率是多少？

**Knowledge Points / 考查知识点:**
- 马尔可夫跳跃链 (Markov Jump Chain)
- 转移概率矩阵 (Transition Probability Matrix)
- 指数分布与期望 (Exponential Distribution and Expectation)
- 条件期望 (Conditional Expectation)
- 全概率公式 (Law of Total Probability)

**Step-by-Step Solution / 逐步解答:**

**(a) Transition Matrix R of the Jump Chain / 跳跃链的转移矩阵R**

**Step 1: Recall the Formula for R / 回顾R的公式**
The transition matrix $R$ of the embedded jump chain has entries $r_{ij} = P(Y_{n+1} = j | Y_n = i)$. For $i \neq j$, $r_{ij} = q_{ij} / (-q_{ii})$. For $i = j$, $r_{ii} = 0$ (since the process must jump to a different state).
嵌入跳跃链的转移矩阵$R$的元素为$r_{ij} = P(Y_{n+1} = j | Y_n = i)$。对于$i \neq j$，$r_{ij} = q_{ij} / (-q_{ii})$。对于$i = j$，$r_{ii} = 0$（因为过程必须跳跃到不同的状态）。

**Step 2: Calculate the Rows of R / 计算R的各行**
- **From state 1:** $-q_{11} = 4$. $r_{12} = 3/4$, $r_{13} = 1/4$.
- **From state 2:** $-q_{22} = 6$. $r_{21} = 2/6 = 1/3$, $r_{23} = 4/6 = 2/3$.
- **From state 3:** $-q_{33} = 3$. $r_{31} = 1/3$, $r_{32} = 2/3$.

**Step 3: Write the Matrix / 写出矩阵**
$$R = \begin{pmatrix} 0 & 3/4 & 1/4 \\ 1/3 & 0 & 2/3 \\ 1/3 & 2/3 & 0 \end{pmatrix}$$

**(b) Expected Time of the First Jump / 第一次跳跃的期望时间**

**Step 1: Identify the Distribution / 确定分布**
The first jump time $J_1 = T_1$ is the holding time in the initial state $X(0)=1$. It is exponentially distributed with parameter $\lambda = -q_{11} = 4$.
第一次跳跃时间$J_1 = T_1$是在初始状态$X(0)=1$的停留时间。它服从参数为$\lambda = -q_{11} = 4$的指数分布。

**Step 2: Calculate the Expectation / 计算期望**
The expectation of an exponential random variable with rate $\lambda$ is $1/\lambda$.
参数为$\lambda$的指数随机变量的期望是$1/\lambda$。
$$E[J_1] = E[T_1] = \frac{1}{4}$$

**(c) Probability the First Jump is to State 2 / 第一次跳跃到状态2的概率**

**Step 1: Use the Jump Chain / 使用跳跃链**
This is simply the transition probability $r_{12}$ from the jump chain.
这即是跳跃链中的转移概率$r_{12}$。
$$P(\text{first jump to state 2}) = r_{12} = \frac{3}{4}$$

**(d) Expected Time of the Second Jump / 第二次跳跃的期望时间**

**Step 1: Define the Problem / 定义问题**
$J_2 = T_1 + T_2$. We need $E[J_2] = E[T_1 + T_2] = E[T_1] + E[T_2]$. We know $E[T_1] = 1/4$. We need to find $E[T_2]$.
$J_2 = T_1 + T_2$。我们需要$E[J_2] = E[T_1 + T_2] = E[T_1] + E[T_2]$。我们知道$E[T_1] = 1/4$。我们需要找到$E[T_2]$。

**Step 2: Condition on the First Jump / 对第一次跳跃进行条件化**
$T_2$ is the holding time in the state visited after the first jump, $Y_1$. We use the Law of Total Expectation:
$T_2$是在第一次跳跃后访问的状态$Y_1$中的停留时间。我们使用全期望公式：
$$E[T_2] = E[E[T_2 | Y_1]]$$
$$E[T_2 | Y_1 = i] = \frac{1}{-q_{ii}}$$

**Step 3: Calculate the Conditional Expectations / 计算条件期望**
- If $Y_1 = 1$: $E[T_2 | Y_1=1] = 1/4$
- If $Y_1 = 2$: $E[T_2 | Y_1=2] = 1/6$
- If $Y_1 = 3$: $E[T_2 | Y_1=3] = 1/3$

**Step 4: Apply the Law of Total Expectation / 应用全期望公式**
$$E[T_2] = \sum_{i=1}^3 P(Y_1 = i | X(0)=1) \cdot E[T_2 | Y_1 = i]$$
$$E[T_2] = r_{12} \cdot \frac{1}{6} + r_{13} \cdot \frac{1}{3}$$
$$E[T_2] = \frac{3}{4} \cdot \frac{1}{6} + \frac{1}{4} \cdot \frac{1}{3} = \frac{3}{24} + \frac{1}{12} = \frac{3}{24} + \frac{2}{24} = \frac{5}{24}$$

**Step 5: Sum the Expectations / 求和**
$$E[J_2] = E[T_1] + E[T_2] = \frac{1}{4} + \frac{5}{24} = \frac{6}{24} + \frac{5}{24} = \frac{11}{24}$$

**(e) Probability the Second Jump is to State 2 / 第二次跳跃到状态2的概率**

**Step 1: Condition on the First Jump / 对第一次跳跃进行条件化**
We want $P(Y_2 = 2 | X(0)=1)$. We use the Law of Total Probability:
我们想要$P(Y_2 = 2 | X(0)=1)$。我们使用全概率公式：
$$P(Y_2 = 2 | Y_0=1) = \sum_{i=1}^3 P(Y_1 = i | Y_0=1) \cdot P(Y_2 = 2 | Y_1 = i)$$
$$= \sum_{i=1}^3 r_{1i} \cdot r_{i2}$$

**Step 2: Calculate the Terms / 计算各项**
- $i=1$: $r_{11} \cdot r_{12} = 0 \cdot (3/4) = 0$
- $i=2$: $r_{12} \cdot r_{22} = (3/4) \cdot 0 = 0$
- $i=3$: $r_{13} \cdot r_{32} = (1/4) \cdot (2/3) = 2/12 = 1/6$

**Step 3: Sum the Probabilities / 求和**
$$P(Y_2 = 2 | Y_0=1) = 0 + 0 + \frac{1}{6} = \frac{1}{6}$$

**(f) Probability the Third Jump is to State 2 / 第三次跳跃到状态2的概率**

**Step 1: Use Matrix Powers / 使用矩阵幂**
The $n$-step transition probabilities of the jump chain are given by the $n$-th power of the transition matrix $R$. We need $(R^3)_{12}$.
跳跃链的$n$步转移概率由转移矩阵$R$的$n$次幂给出。我们需要$(R^3)_{12}$。

**Step 2: Calculate $R^2$ / 计算$R^2$**
$$R^2 = R \times R = \begin{pmatrix} 0 & 3/4 & 1/4 \\ 1/3 & 0 & 2/3 \\ 1/3 & 2/3 & 0 \end{pmatrix} \times \begin{pmatrix} 0 & 3/4 & 1/4 \\ 1/3 & 0 & 2/3 \\ 1/3 & 2/3 & 0 \end{pmatrix}$$
Let's calculate the entry $(R^2)_{12}$:
$(R^2)_{12} = (0)(3/4) + (3/4)(0) + (1/4)(2/3) = 0 + 0 + 2/12 = 1/6$
Let's calculate the full matrix to be safe:
- Row 1: $(0, 3/4, 1/4)$
  - Col 1: $0(0) + (3/4)(1/3) + (1/4)(1/3) = 0 + 1/4 + 1/12 = 3/12 + 1/12 = 4/12 = 1/3$
  - Col 2: $0(3/4) + (3/4)(0) + (1/4)(2/3) = 0 + 0 + 2/12 = 1/6$
  - Col 3: $0(1/4) + (3/4)(2/3) + (1/4)(0) = 0 + 1/2 + 0 = 1/2$
- Row 2: $(1/3, 0, 2/3)$
  - Col 1: $(1/3)(0) + 0(1/3) + (2/3)(1/3) = 0 + 0 + 2/9$
  - Col 2: $(1/3)(3/4) + 0(0) + (2/3)(2/3) = 1/4 + 0 + 4/9 = 9/36 + 16/36 = 25/36$
  - Col 3: $(1/3)(1/4) + 0(2/3) + (2/3)(0) = 1/12 + 0 + 0 = 1/12$
- Row 3: $(1/3, 2/3, 0)$
  - Col 1: $(1/3)(0) + (2/3)(1/3) + 0(1/3) = 0 + 2/9 + 0 = 2/9$
  - Col 2: $(1/3)(3/4) + (2/3)(0) + 0(2/3) = 1/4 + 0 + 0 = 1/4$
  - Col 3: $(1/3)(1/4) + (2/3)(2/3) + 0(0) = 1/12 + 4/9 = 3/36 + 16/36 = 19/36$

So $R^2 = \begin{pmatrix} 1/3 & 1/6 & 1/2 \\ 2/9 & 25/36 & 1/12 \\ 2/9 & 1/4 & 19/36 \end{pmatrix}$

**Step 3: Calculate $R^3$ / 计算$R^3$**
We need $(R^3)_{12} = (R^2 \times R)_{12}$.
$(R^3)_{12} = (R^2)_{11} r_{12} + (R^2)_{12} r_{22} + (R^2)_{13} r_{32}$
$(R^3)_{12} = (1/3)(3/4) + (1/6)(0) + (1/2)(2/3)$
$(R^3)_{12} = 1/4 + 0 + 1/3 = 3/12 + 4/12 = 7/12$

**Final Answer / 最终答案:**
(a) $R = \begin{pmatrix} 0 & 3/4 & 1/4 \\ 1/3 & 0 & 2/3 \\ 1/3 & 2/3 & 0 \end{pmatrix}$
(b) $E[J_1] = \boxed{\frac{1}{4}}$
(c) $P(\text{first jump to state 2}) = \boxed{\frac{3}{4}}$
(d) $E[J_2] = \boxed{\frac{11}{24}}$
(e) $P(\text{second jump to state 2}) = \boxed{\frac{1}{6}}$
(f) $P(\text{third jump to state 2}) = \boxed{\frac{7}{12}}$

**Key Insight / 解题要点:**
The jump chain's transition matrix $R$ is derived by normalizing the rows of the generator $Q$. The holding times are independent exponential random variables, and their expectations depend on the state visited.
跳跃链的转移矩阵$R$是通过对生成元$Q$的行进行归一化得到的。停留时间是独立的指数随机变量，它们的期望取决于所访问的状态。

---

### Question 3 / 第3题

**Problem / 题目原文:**
Consider the Markov jump process on $\mathcal{S} = \{1,2\}$ with generator matrix
$$Q = \begin{pmatrix} -\alpha & \alpha \\ \beta & -\beta \end{pmatrix},$$
where $\alpha, \beta > 0$.
(a) Write down the Kolmogorov forward equation for $p_{11}(t)$, including the initial condition.
(b) Hence, show that
$$p'_{11}(t) + (\alpha+\beta)p_{11}(t) = \beta.$$
(c) Solve this differential equation to find $p_{11}(