---
title: 第 1 章：线性空间
---
## 标量与向量

### 数的运算

从小学一年级开始我们就接触了整数，并且学会进行加减乘除；长大一些后，我们了解到了分数，将数系扩充到了有理数部分；再后来初中阶段我们遇到了平方根这种运算，接触到了无理数，我们把这些数都统称为实数，后来我们又了解了 $-1$ 也能被开平方根，开创了复数领域；同时在高中阶段，我们也学习了简单的集合论，通常我们会用几个记号来表示这些数域。

::: info 定义：数集的符号

这些数集有着相对应的符号：

- $\mathbb{N}$ 表示所有自然数的集合，其元素是所有非负整数。
- $\mathbb{Z}$ 表示所有整数的集合。
- $\mathbb{Q}$ 表示所有有理数的集合，其中有理数被定义为所有能够表示为 $\frac{m}{n},m\in \mathbb{Z},n\in \mathbb{Z}$ 的数。
- $\mathbb{R}$ 表示所有实数的集合。
- $\mathbb{C}$ 表示所有复数的集合。

:::

由于这门课不是实分析或高等代数，所以不会详细讲解这些数集怎么构造，读者只需要对此有一个简单的认识就可以了。众所周知，数的运算分别有加减乘除四种，如果读者觉得自己小学数学不错的话，一定知道下面的定理。

::: info 公理：域公理

1. **交换律(communitativity)**：对于所有的 $\alpha,\beta \in \mathbb{C}$ 有 $\alpha+\beta=\beta+\alpha,\alpha\beta=\beta\alpha$ ;
2. **结合律(associativity)**：对于所有的 $\alpha,\beta,\gamma \in \mathbb{C}$ 有 $(\alpha+\beta)+\gamma=\alpha+(\beta+\gamma),(\alpha\beta)\gamma=\alpha(\beta\gamma)$ ;
3. **单位元(identities)**：对于所有的 $\lambda \in \mathbb{C}$ 都有 $\lambda+0=\lambda,1\lambda=\lambda$ ; 
4. **加法逆元(additive inverse)**：对于所有的 $\alpha \in \mathbb{C}$ 都存在唯一的 $\beta \in \mathbb{C}$ 使得 $\alpha+\beta=0$ ;
5. **乘法逆元(multiplicative inverse)**：对于每个 $\alpha \in\mathbb{C}$ 且 $\alpha\neq 0$ ，都存在唯一的 $\beta \in \mathbb{C}$ 使得 $\alpha\beta=1$ ;
6. **分配律(distributive)**：对于所有的 $\alpha,\beta,\gamma \in \mathbb{C}$ 都有对于所有的 $\alpha(\beta+\gamma)=\alpha\beta +\alpha\gamma$ .

::: 

如果一个数域 $\mathbb{F}$ 和 $\mathbb{C}$ 一样满足上述性质，我们称 $\mathbb{F}$ 中的元素为标量(scalar)，当然 $\mathbb{C}$ 和 $\mathbb{R}$ 的所有元素也是标量。

### 标量

如上所述，标量通常强调的是，这一个元素是一个数，而不是向量（稍后给出定义），实际上只是``数''的一种花里胡哨的叫法而已。德国数学家Frobenius 已经证明，当下数学体系内再也没有比 $\mathbb{C}$ 更大的数系了，所以我们可以称对于每一个 $\alpha \in \mathbb{C}$ ， $\alpha$ 是标量，例如 $3+4\mathrm{i}$ 是一个标量。

::: tip 练习

前文所述，我们说过复数是最大的数系，请求出 $\sqrt{\mathrm{i}}$ 的两个解，其中 $\mathrm{i}=\sqrt{-1}$ 。

解：设 $\sqrt{\mathrm{i}}=z=(a+b\mathrm{i})$ ，其中 $a,b \in \mathbb{R}$ ，通过两边将其平方可得
$$
\mathrm{i}=(a+b\mathrm{i})^2=a^2-b^2+2ab\mathrm{i}
$$
观察式子联立方程组为
$$
\left\{\begin{matrix}
                a^2-b^2=0 \\
                2ab=1
        \end{matrix}\right.
$$
解此方程组可得
$$
\left\{\begin{matrix}
                a=b \\
                a=\pm \frac{\sqrt{2} }{2}
        \end{matrix}\right.
$$
所以 $\sqrt{\mathrm{i}}$ 的两个解为
$$
z_1=\frac{\sqrt{2}}{2}+\frac{\sqrt{2}}{2}\mathrm{i},z_2=-\frac{\sqrt{2}}{2}-\frac{\sqrt{2}}{2}\mathrm{i}
$$
:::

若 $n\in \mathbb{N}$ ，我们将由 $n$ 个数按顺序排列成为的一个组称之为元组(tuple)，通常的记法为：有小括号包含这 $n$ 个数，且有序排列，中间由逗号隔开，例如 $(a,b)$ 是一个长度为2的元组，如果长度为 $n$ 且由 $z_1,z_2,z_3,\cdots,z_n$ 这些数组成的元组的记法可能如下所示： $\left( z_1,z_2,z_3,\cdots,z_n\right)$ 。

::: tip 思考

集合是元组吗？

:::

对于这个思考题，很显然答案是不对的，因为元组强调以下两点：

- 有序性， $(3,5)$ 和 $(5,3)$ 并不相等，而 $\{3,5\}$ 和 $\{5,3\}$ 是相等的集合；
- 可重复， $(3,3)$ 和 $(3,3,3)$ 并不相等，而 $\{3,3\}$ 和 $\{3,3,3\}$ 是相等的集合，它们等同于 $\{3\}$ ### 笛卡尔积

接下来我们慢慢引入向量的概念，在讲向量之前，笔者想和大家谈一谈如何生成这样的空间来容纳我们向量的概念，这里有一个定义叫做笛卡尔积(Cartesian product)。

::: info 定义：笛卡尔积

两个集合 ${\displaystyle X}$ 和 ${\displaystyle Y}$ 的笛卡尔积是所有可能的有序对组成的集合，其中有序对的第一个对象是 $X$ 的成员，第二个对象是 $Y$ 的成员，记作：
$$
{\displaystyle X\times Y := \left\{\left(x,y\right)\mid x\in X \text{且} y\in Y\right\}}
$$
符号 $:=$ 表示定义为，用来明确地给某个符号或概念赋予一个新的定义，例如：妈妈 $:=$ 养育与教养子女成长的女性
:::

举个很常见的例子，如果集合 $X$ 是13个元素的点数集合 ${\displaystyle \left\{A,K,Q,J,10,9,8,7,6,5,4,3,2\right\}}$ 而集合 $Y$ 是四种花色 $\{\spadesuit, \heartsuit, \diamondsuit, \clubsuit\}$ ，则这两个集合的笛卡尔积是有52个元素的标准扑克牌的集合：
$$
X\times Y = \left\lbrace (A,\spadesuit),(K,\spadesuit),(Q,\spadesuit)\cdots (2,\spadesuit),\cdots,(3,\clubsuit),(2,\clubsuit)\right\rbrace
$$

### 空间 $\mathbb{F}^n$ 

我们定义 $\mathbb{R}^2=\mathbb{R} \times \mathbb{R}$ ，根据笛卡尔积的运算规则，集合 $\mathbb{R}^2$ 为所有有序实数2元组构成，即
$$
\mathbb{R}^2=\{(x,y)\mid x,y \in \mathbb{R}\}
$$
在现实生活中，我们可以将它看成是一个二维平面，而 $\mathbb{R}^3$ 在现实生活中，我们可以将它看成是一个三维空间。

我们上述提到集合 $\mathbb{F}$ 内的元素是一个标量，那么 $\mathbb{F}^n$ 则由无数个的 $n$ 元组构成，例如 $\mathbb{C}^6$ 就是含有6个有序元素构成的一个空间，虽然当 $n>3$ 的时候在实际生活中想象它们绝非易事，但是数学就是一门由具体到抽象的科目，我们可以使用类比的手法，让它们和在 $\mathbb{R}^2$ 与 $\mathbb{R}^3$ 上运算一样有自己的实际意义。

### 向量

如之前所述，我们终于提到了向量(vector)这个概念，只不过可能会令读者失望的是，数学科目上的向量是一个非常抽象的东西，那么我们把目光转换到另外一门和数学紧密相关的科目上：物理。

学基础物理的学生总是很实际，他们将数学转化为解决现实生活中问题的工具，所以在他们眼中，向量一般是一个箭头， 它具有方向和大小，且这两个特征不会随着向量的移动发生变化，因此该形式的向量可以在空间中的任何一个位置。     

所以我们在此非严格定义一个 $n$ 元组被看作箭头时，就是一个 $n$ 维向量(稍后我们会给出它的更准确的定义)；下面是一个二维向量在平面 $\mathbb{R}^2$ 内

![](/root/Documents/vuepress-starter/src/figure/eps/VectorInR2.png)

## 向量的运算法则

### 加法

::: info 定义：向量的加法

若 $x,y\in \mathbb{F}^n,x=(x_1,x_2,x_3,\cdots,x_n),y=(y_1,y_2,y_3,\cdots,y_n)$ 则 $x+y$ 定义为
$$
x+y:=(x_1+y_1,x_2+y_2,x_3+y_3,\cdots x_n+y_n)
$$

:::

实际上两个向量相加，就是将它们元组里面的所有元素依次相加得到一个新的元组。

::: tip 思考

维度不同的向量是否可以相加？

:::

要解答这个问题，我们需要返回到定义中，我们只定义了维度相同都为 $n$ 的向量相加，并没有定义维度不同的向量相加的情况，所以这是一个未定义的行为；所以下面的对向量的运算均是在同一维度下进行。同理，向量与标量无法相加。同样，向量的加法也满足交换律：

::: important 推论

若 $x,y\in \mathbb{F}^n$ ，则 $x+y=y+x$ 。

证明：若 $x,y\in \mathbb{F}^n,x=(x_1,x_2,x_3,\cdots,x_n),y=(y_1,y_2,y_3,\cdots,y_n)$ 则
$$
x+y=(x_1+y_1,x_2+y_2,x_3+y_3,\cdots x_n+y_n)
$$
根据标量加法的交换律可知
$$
x+y=(y_1+x_1,y_2+x_2,y_3+x_3,\cdots y_n+x_n)=y+x
$$
:::

如果我们将其反映在二维坐标系上，那应该是这样的

![](/root/Documents/vuepress-starter/src/figure/eps/SumOf2Vectors.png)

### 0 向量

我们之前说过，向量与标量无法相加，所以在 $\mathbb{F}^n$ 内我们定义 $n$ 维0向量作为加法的单位元，即若 $x,y\in \mathbb{F}^n$ ， $x+y=x$ ，那么 $y$ 就是0 向量。

::: info 定义：0 向量

若 $\alpha,\beta \in \mathbb{F}^n$ 且 $\alpha+\beta = \alpha$ ，那么 $\beta$ 为空间 $\mathbb{F}^n$ 的单位元，我们将其称为0向量，显然0向量就是一个全是由0组成的 $n$ 元组，记作 $\boldsymbol{0}$ \footnote{实际上是以粗体形式出现的0}，那么
$$
\boldsymbol{0}=(0,0,0,\cdots,0)
$$

:::