# Problem Sheet 5 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:12
> 来源页 / Source Pages: 60-61

---

好的，作为大学随机过程课程的导师，我将为您提供这份习题集的完整、详细的解答。我将遵循您的要求，使用中英双语，并展示所有步骤。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Find a stationary distribution for the Markov chain with transition matrix
\[
P = \begin{pmatrix}
\frac{1}{3} & \frac{2}{3} & 0 \\
\frac{1}{6} & \frac{1}{3} & \frac{1}{2} \\
0 & \frac{1}{3} & \frac{2}{3}
\end{pmatrix}.
\]
Is the Markov chain reversible?

**中文翻译:**
求具有转移矩阵 \(P\) 的马尔可夫链的平稳分布。该马尔可夫链是否可逆？

**Knowledge Points / 考查知识点:**
- Stationary distribution (平稳分布)
- Detailed balance equations (细致平衡方程)
- Reversibility (可逆性)

**Step-by-Step Solution / 逐步解答:**

**Step 1: Set up the equations for the stationary distribution.**
We need to find a probability vector \(\pi = (\pi_1, \pi_2, \pi_3)\) such that \(\pi P = \pi\) and \(\sum_{i=1}^3 \pi_i = 1\). The equation \(\pi P = \pi\) gives us a system of linear equations.

Let's write out \(\pi P = \pi\):
\[
(\pi_1, \pi_2, \pi_3) \begin{pmatrix}
\frac{1}{3} & \frac{2}{3} & 0 \\
\frac{1}{6} & \frac{1}{3} & \frac{1}{2} \\
0 & \frac{1}{3} & \frac{2}{3}
\end{pmatrix} = (\pi_1, \pi_2, \pi_3)
\]

This yields three equations, one for each column of \(P\):
- For state 1: \(\pi_1 \cdot \frac{1}{3} + \pi_2 \cdot \frac{1}{6} + \pi_3 \cdot 0 = \pi_1\)  (Equation 1)
- For state 2: \(\pi_1 \cdot \frac{2}{3} + \pi_2 \cdot \frac{1}{3} + \pi_3 \cdot \frac{1}{3} = \pi_2\)  (Equation 2)
- For state 3: \(\pi_1 \cdot 0 + \pi_2 \cdot \frac{1}{2} + \pi_3 \cdot \frac{2}{3} = \pi_3\)  (Equation 3)

**Step 2: Solve the system of linear equations.**
We also have the normalization condition:
- \(\pi_1 + \pi_2 + \pi_3 = 1\) (Equation 4)

Let's simplify Equation 1:
\[
\frac{1}{3}\pi_1 + \frac{1}{6}\pi_2 = \pi_1
\]
Multiply by 6: \(2\pi_1 + \pi_2 = 6\pi_1 \Rightarrow \pi_2 = 4\pi_1\).
So, \(\pi_2 = 4\pi_1\).  (Result 1)

Now simplify Equation 3:
\[
\frac{1}{2}\pi_2 + \frac{2}{3}\pi_3 = \pi_3
\]
Multiply by 6: \(3\pi_2 + 4\pi_3 = 6\pi_3 \Rightarrow 3\pi_2 = 2\pi_3 \Rightarrow \pi_3 = \frac{3}{2}\pi_2\).
Substitute \(\pi_2 = 4\pi_1\): \(\pi_3 = \frac{3}{2} \cdot 4\pi_1 = 6\pi_1\).
So, \(\pi_3 = 6\pi_1\). (Result 2)

Now use the normalization condition (Equation 4):
\[
\pi_1 + \pi_2 + \pi_3 = \pi_1 + 4\pi_1 + 6\pi_1 = 11\pi_1 = 1
\]
Thus, \(\pi_1 = \frac{1}{11}\).

Then, \(\pi_2 = 4 \cdot \frac{1}{11} = \frac{4}{11}\).
And \(\pi_3 = 6 \cdot \frac{1}{11} = \frac{6}{11}\).

The stationary distribution is \(\pi = (\frac{1}{11}, \frac{4}{11}, \frac{6}{11})\).

We should verify this with Equation 2 as a check:
LHS of Eq 2: \(\frac{2}{3}\pi_1 + \frac{1}{3}\pi_2 + \frac{1}{3}\pi_3 = \frac{2}{3}\cdot\frac{1}{11} + \frac{1}{3}\cdot\frac{4}{11} + \frac{1}{3}\cdot\frac{6}{11} = \frac{2+4+6}{33} = \frac{12}{33} = \frac{4}{11}\).
RHS of Eq 2: \(\pi_2 = \frac{4}{11}\). The equation holds.

**Step 3: Check for reversibility.**
A Markov chain is reversible if it satisfies the detailed balance equations: \(\pi_i P_{ij} = \pi_j P_{ji}\) for all \(i, j\).

Let's check for all pairs:
- For \((i,j) = (1,2)\): \(\pi_1 P_{12} = \frac{1}{11} \cdot \frac{2}{3} = \frac{2}{33}\). \(\pi_2 P_{21} = \frac{4}{11} \cdot \frac{1}{6} = \frac{4}{66} = \frac{2}{33}\). **Holds.**
- For \((i,j) = (1,3)\): \(\pi_1 P_{13} = \frac{1}{11} \cdot 0 = 0\). \(\pi_3 P_{31} = \frac{6}{11} \cdot 0 = 0\). **Holds.**
- For \((i,j) = (2,3)\): \(\pi_2 P_{23} = \frac{4}{11} \cdot \frac{1}{2} = \frac{4}{22} = \frac{2}{11}\). \(\pi_3 P_{32} = \frac{6}{11} \cdot \frac{1}{3} = \frac{6}{33} = \frac{2}{11}\). **Holds.**

Since the detailed balance equations hold for all pairs of states, the Markov chain is reversible.

**Final Answer / 最终答案:**
The stationary distribution is \(\boxed{\pi = \left(\frac{1}{11}, \frac{4}{11}, \frac{6}{11}\right)}\).
The Markov chain is \(\boxed{\text{reversible}}\).

**Key Insight / 解题要点:**
Solving \(\pi P = \pi\) yields the stationary distribution, and verifying \(\pi_i P_{ij} = \pi_j P_{ji}\) for all \(i,j\) determines reversibility.

---

### Question 2 / 第2题

**Problem / 题目原文:**
Consider a Markov chain with state space \(S = \{1,2,3,4\}\) and transition matrix
\[
P = \begin{pmatrix}
\frac{1}{4} & \frac{1}{2} & \frac{1}{4} & 0 \\
\frac{1}{4} & \frac{1}{4} & \frac{1}{2} & 0 \\
\frac{1}{2} & \frac{1}{2} & 0 & 0 \\
\frac{1}{4} & 0 & \frac{1}{4} & \frac{1}{2}
\end{pmatrix}.
\]
(a) Draw a transition diagram for this Markov chain.
(b) Identify the communicating classes. State whether each class is closed or not. State whether each class is positive recurrent, null recurrent, or transient.
(c) Find a stationary distribution for this Markov chain. Is the Markov chain reversible?
(d) Is this the only stationary distribution?

**中文翻译:**
考虑一个状态空间为 \(S = \{1,2,3,4\}\)，转移矩阵为 \(P\) 的马尔可夫链。
(a) 画出该马尔可夫链的转移图。
(b) 识别所有通信类。说明每个类是否是封闭的。说明每个类是正常返、零常返还是瞬时的。
(c) 求该马尔可夫链的一个平稳分布。该马尔可夫链是否可逆？
(d) 这是唯一的平稳分布吗？

**Knowledge Points / 考查知识点:**
- Transition diagram (转移图)
- Communicating classes (通信类), closed class (封闭类)
- Recurrence and transience (常返性与瞬时性)
- Stationary distribution (平稳分布)
- Reversibility (可逆性)
- Uniqueness of stationary distribution (平稳分布的唯一性)

**Step-by-Step Solution / 逐步解答:**

**(a) Transition Diagram**

**Step 1: Interpret the transition matrix.**
The matrix \(P\) gives the probabilities of moving from one state to another. For example, \(P_{12} = \frac{1}{2}\) means from state 1, the probability to go to state 2 is 1/2.

**Step 2: Draw the diagram.**
We draw four nodes (1, 2, 3, 4) and directed edges with the corresponding probabilities.
- From 1: to 1 (1/4), to 2 (1/2), to 3 (1/4).
- From 2: to 1 (1/4), to 2 (1/4), to 3 (1/2).
- From 3: to 1 (1/2), to 2 (1/2).
- From 4: to 1 (1/4), to 3 (1/4), to 4 (1/2).

The diagram is as follows (described textually, as I cannot draw images):
- State 1 has a self-loop (1/4), an arrow to 2 (1/2), and an arrow to 3 (1/4).
- State 2 has a self-loop (1/4), an arrow to 1 (1/4), and an arrow to 3 (1/2).
- State 3 has an arrow to 1 (1/2) and an arrow to 2 (1/2).
- State 4 has a self-loop (1/2), an arrow to 1 (1/4), and an arrow to 3 (1/4).

**(b) Communicating Classes, Closedness, and Recurrence/Transience**

**Step 1: Identify communicating classes.**
A communicating class is a set of states that all communicate with each other (i.e., for any \(i, j\) in the class, \(i\) can reach \(j\) and \(j\) can reach \(i\)).

- **States 1, 2, 3:** From the diagram, we can see that 1, 2, and 3 can all reach each other. For example, 1→2, 2→3, 3→1. So {1, 2, 3} is a communicating class.
- **State 4:** Can state 4 reach states 1, 2, 3? Yes, 4→1, 4→3. Can states 1, 2, 3 reach state 4? No, there is no path from 1, 2, or 3 to 4. Therefore, state 4 is in its own communicating class {4}.

**Step 2: Determine if classes are closed.**
A class is closed if there is no way to leave it.
- **Class {1, 2, 3}:** From states 1, 2, 3, can we reach state 4? No. So this class is **closed**.
- **Class {4}:** From state 4, can we reach states 1, 2, 3? Yes. So this class is **not closed**.

**Step 3: Determine recurrence/transience.**
- **Closed class {1, 2, 3}:** Since the state space is finite and the class is closed, all states in this class are **positive recurrent**. (A finite, closed, irreducible class is always positive recurrent).
- **Not closed class {4}:** Since state 4 can leave its class and never return (it's not closed), it is **transient**. (A state that can leave its class with positive probability and never come back is transient).

**(c) Stationary Distribution and Reversibility**

**Step 1: Find a stationary distribution.**
Since the chain has a closed, irreducible class {1, 2, 3} and a transient state 4, any stationary distribution must assign probability 0 to the transient state. The stationary distribution is supported on the closed class. We need to find the stationary distribution for the sub-chain on {1, 2, 3}.

The transition matrix for the sub-chain on {1, 2, 3} is:
\[
Q = \begin{pmatrix}
\frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\
\frac{1}{4} & \frac{1}{4} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & 0
\end{pmatrix}
\]

Let \(\pi = (\pi_1, \pi_2, \pi_3)\) be the stationary distribution for this sub-chain. Solve \(\pi Q = \pi\) and \(\pi_1 + \pi_2 + \pi_3 = 1\).

Equations from \(\pi Q = \pi\):
- State 1: \(\frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 + \frac{1}{2}\pi_3 = \pi_1\)  (Eq 1)
- State 2: \(\frac{1}{2}\pi_1 + \frac{1}{4}\pi_2 + \frac{1}{2}\pi_3 = \pi_2\)  (Eq 2)
- State 3: \(\frac{1}{4}\pi_1 + \frac{1}{2}\pi_2 + 0\cdot\pi_3 = \pi_3\)  (Eq 3)

Simplify Eq 1: Multiply by 4: \(\pi_1 + \pi_2 + 2\pi_3 = 4\pi_1 \Rightarrow \pi_2 + 2\pi_3 = 3\pi_1\). (R1)

Simplify Eq 3: Multiply by 4: \(\pi_1 + 2\pi_2 = 4\pi_3\). (R3)

From R3, \(\pi_1 = 4\pi_3 - 2\pi_2\).
Substitute into R1: \(\pi_2 + 2\pi_3 = 3(4\pi_3 - 2\pi_2) = 12\pi_3 - 6\pi_2\).
Bring terms together: \(\pi_2 + 6\pi_2 = 12\pi_3 - 2\pi_3 \Rightarrow 7\pi_2 = 10\pi_3 \Rightarrow \pi_2 = \frac{10}{7}\pi_3\).

Now substitute \(\pi_2\) back into R3: \(\pi_1 = 4\pi_3 - 2(\frac{10}{7}\pi_3) = 4\pi_3 - \frac{20}{7}\pi_3 = \frac{28-20}{7}\pi_3 = \frac{8}{7}\pi_3\).

Now use normalization: \(\pi_1 + \pi_2 + \pi_3 = \frac{8}{7}\pi_3 + \frac{10}{7}\pi_3 + \pi_3 = \frac{8+10+7}{7}\pi_3 = \frac{25}{7}\pi_3 = 1\).
Thus, \(\pi_3 = \frac{7}{25}\).

Then, \(\pi_2 = \frac{10}{7} \cdot \frac{7}{25} = \frac{10}{25} = \frac{2}{5}\).
And \(\pi_1 = \frac{8}{7} \cdot \frac{7}{25} = \frac{8}{25}\).

So the stationary distribution for the whole chain is \(\pi = (\frac{8}{25}, \frac{2}{5}, \frac{7}{25}, 0)\).

**Step 2: Check reversibility.**
We need to check detailed balance for the whole chain. Since \(\pi_4 = 0\), any equation involving state 4 will hold (0 = 0). We only need to check states 1, 2, 3.

- For (1,2): \(\pi_1 P_{12} = \frac{8}{25} \cdot \frac{1}{2} = \frac{8}{50} = \frac{4}{25}\). \(\pi_2 P_{21} = \frac{2}{5} \cdot \frac{1}{4} = \frac{2}{20} = \frac{1}{10} = \frac{2.5}{25}\). Not equal (\(\frac{4}{25} \neq \frac{2.5}{25}\)).
Since the detailed balance fails for (1,2), the chain is **not reversible**.

**(d) Uniqueness of Stationary Distribution**

**Step 1: Analyze the structure.**
The chain has one closed, irreducible, positive recurrent class {1, 2, 3} and one transient state {4}. For such a chain, the stationary distribution is unique and is supported entirely on the closed class.

**Step 2: Conclusion.**
Yes, this is the only stationary distribution.

**Final Answer / 最终答案:**
(a) Transition diagram described in solution.
(b) Communicating classes: {1, 2, 3} (closed, positive recurrent), {4} (not closed, transient).
(c) Stationary distribution: \(\boxed{\pi = \left(\frac{8}{25}, \frac{2}{5}, \frac{7}{25}, 0\right)}\). The chain is \(\boxed{\text{not reversible}}\).
(d) \(\boxed{\text{Yes}}\), this is the only stationary distribution.

**Key Insight / 解题要点:**
For a chain with a single closed recurrent class and transient states, the unique stationary distribution is found by solving for the stationary distribution of the recurrent class and assigning zero probability to transient states.

---

### Question 3 / 第3题

**Problem / 题目原文:**
Consider a Markov chain with state space \(S = \{1,2,3,4,5\}\) and transition matrix
\[
P = \begin{pmatrix}
\frac{1}{3} & \frac{2}{3} & 0 & 0 & 0 \\
\frac{1}{3} & \frac{2}{3} & 0 & 0 & 0 \\
0 & \frac{3}{5} & \frac{1}{5} & \frac{1}{5} & 0 \\
0 & 0 & 0 & \frac{1}{4} & \frac{3}{4} \\
0 & 0 & 0 & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}.
\]
(a) Draw a transition diagram for this Markov chain.
(b) Identify the communicating classes. State whether each class is closed or not. State if each class is positive recurrent, null recurrent, or transient.
(c) Find all of the stationary distributions for this Markov chain.

**中文翻译:**
考虑一个状态空间为 \(S = \{1,2,3,4,5\}\)，转移矩阵为 \(P\) 的马尔可夫链。
(a) 画出该马尔可夫链的转移图。
(b) 识别所有通信类。说明每个类是否是封闭的。说明每个类是正常返、零常返还是瞬时的。
(c) 求该马尔可夫链的所有平稳分布。

**Knowledge Points / 考查知识点:**
- Transition diagram (转移图)
- Communicating classes (通信类), closed class (封闭类)
- Recurrence and transience (常返性与瞬时性)
- Stationary distributions for reducible chains (可约链的平稳分布)
- Convex combinations of stationary distributions (平稳分布的凸组合)

**Step-by-Step Solution / 逐步解答:**

**(a) Transition Diagram**

**Step 1: Interpret the transition matrix.**
- From 1: to 1 (1/3), to 2 (2/3).
- From 2: to 1 (1/3), to 2 (2/3).
- From 3: to 2 (3/5), to 3 (1/5), to 4 (1/5).
- From 4: to 4 (1/4), to 5 (3/4).
- From 5: to 4 (1/2), to 5 (1/2).

**Step 2: Draw the diagram.**
- States 1 and 2 have arrows between each other and self-loops.
- State 3 has an arrow to 2, a self-loop, and an arrow to 4.
- States 4 and 5 have arrows between each other and self-loops.

**(b) Communicating Classes, Closedness, and Recurrence/Transience**

**Step 1: Identify communicating classes.**
- **States 1, 2:** They can reach each other (1↔2) and cannot reach any other state. So {1, 2} is a class.
- **State 3:** Can 3 reach 1 or 2? Yes, 3→2. Can 1 or 2 reach 3? No. Can 3 reach 4 or 5? Yes, 3→4. Can 4 or 5 reach 3? No. So state 3 is in its own class {3}.
- **States 4, 5:** They can reach each other (4↔5) and cannot reach any other state. So {4, 5} is a class.

**Step 2: Determine if classes are closed.**
- **Class {1, 2}:** Can we leave this class? No, all transitions stay within {1, 2}. **Closed.**
- **Class {3}:** Can we leave this class? Yes, to 2 and 4. **Not closed.**
- **Class {4, 5}:** Can we leave this class? No, all transitions stay within {4, 5}. **Closed.**

**Step 3: Determine recurrence/transience.**
- **Closed class {1, 2}:** Finite, closed, irreducible. **Positive recurrent.**
- **Not closed class {3}:** Can leave and never return. **Transient.**
- **Closed class {4, 5}:** Finite, closed, irreducible. **Positive recurrent.**

**(c) All Stationary Distributions**

**Step 1: Understand the structure.**
The chain has two closed, irreducible, positive recurrent classes: \(C_1 = \{1, 2\}\) and \(C_2 = \{4, 5\}\), and one transient state \(\{3\}\). Any stationary distribution is a convex combination of the stationary distributions of the closed classes. The transient state gets probability 0.

**Step 2: Find stationary distribution for class \(C_1 = \{1, 2\}\).**
The sub-matrix is:
\[
Q_1 = \begin{pmatrix}
\frac{1}{3} & \frac{2}{3} \\
\frac{1}{3} & \frac{2}{3}
\end{pmatrix}
\]
Let \(\pi^{(1)} = (\pi_1, \pi_2)\). Solve \(\pi^{(1)} Q_1 = \pi^{(1)}\) and \(\pi_1 + \pi_2 = 1\).
Equation for state 1: \(\frac{1}{3}\pi_1 + \frac{1}{3}\pi_2 = \pi_1 \Rightarrow \pi_1 + \pi_2 = 3\pi_1 \Rightarrow \pi_2 = 2\pi_1\).
Normalization: \(\pi_1 + 2\pi_1 = 3\pi_1 = 1 \Rightarrow \pi_1 = \frac{1}{3}, \pi_2 = \frac{2}{3}\).
So the stationary distribution for \(C_1\) is \(\pi^{(1)} = (\frac{1}{3}, \frac{2}{3})\).

**Step 3: Find stationary distribution for class \(C_2 = \{4, 5\}\).**
The sub-matrix is:
\[
Q_2 = \begin{pmatrix}
\frac{1}{4} & \frac{3}{4} \\
\frac{1}{2} & \frac{1}{2}
\end{pmatrix}
\]
Let \(\pi^{(2)} = (\pi_4, \pi_5)\). Solve \(\pi^{(2)} Q_2 = \pi^{(2)}\) and \(\pi_4 + \pi_5 = 1\).
Equation for state 4: \(\frac{1}{4}\pi_4 + \frac{1}{2}\pi_5 = \pi_4 \Rightarrow \pi_4 + 2\pi_5 = 4\pi_4 \Rightarrow 2\pi_5 = 3\pi_4 \Rightarrow \pi_5 = \frac{3}{2}\pi_4\).
Normalization: \(\pi_4 + \frac{3}{2}\pi_4 = \frac{5}{2}\pi_4 = 1 \Rightarrow \pi_4 = \frac{2}{5}, \pi_5 = \frac{3}{5}\).
So the stationary distribution for \(C_2\) is \(\pi^{(2)} = (\frac{2}{5}, \frac{3}{5})\).

**Step 4: Combine to get all stationary distributions.**
Any stationary distribution \(\pi\) for the whole chain is a convex combination of the stationary distributions of the two closed classes. Let \(\alpha \in [0, 1]\) be the weight on class \(C_1\). Then:
\[
\pi = \alpha \cdot (\pi_1, \pi_2, 0, 0, 0) + (1-\alpha) \cdot (0, 0, 0, \pi_4, \pi_5)
\]
This gives:
\[
\pi = \left( \frac{\alpha}{3}, \frac{2\alpha}{3}, 0, \frac{2(1-\alpha)}{5}, \frac{3(1-\alpha)}{5} \right)
\]
for any \(\alpha \in [0, 1]\).

**Final Answer / 最终答案:**
(a) Transition diagram described in solution.
(b) Communicating classes: {1, 2} (closed, positive recurrent), {3} (not closed, transient), {4, 5} (closed, positive recurrent).
(c) All stationary distributions are given by \(\boxed{\pi = \left