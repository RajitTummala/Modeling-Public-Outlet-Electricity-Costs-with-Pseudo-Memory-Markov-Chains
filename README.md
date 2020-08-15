# Modeling Electricity Costs from Public Outlet Usage through a Battery-Adjusted Pseudo-Memory Markov Chains

Don't worry if some of the terms in the title seem alien to you, we will hopefully go over each one in this guide. 

## I. Purpose

This code uses altered Markov Chains to predict how many hours people charged their phones at a public place based on two key features:
1.  An average number of devices typically in the public place ( `numOfDevices` )
2.  A certain time interval measured in days ( `days` )

## II. Limitations
Other possible variables such as number of outlets; accessibility of outlets; varying number of devices at the public place based on the weather, seasons, holidays; etc. were considered leading to a number of assumptions and justification for these assumptions. The fully-worded and justified assumptions can be found in the full paper <a href="https://drive.google.com/file/d/1VrkC2M26mnis0jesCBb7r3mjHWoVoSTI/view?usp=sharing" target="_blank">here</a> but below is a topical glance:
* Two States: (1) **Charging** or (2) **Not Charging**
* Number of devices remains constant at a public place
* If a person needs to charge, then he or she will be able to and will
* At the start of the day, devices are at 100% charge which decreases every hour unless in a charging state
* Maximum amount of hours spent at a public place could be no more than 16

## III. Terminology

### i. Markov Chain

It is a *memoryless*, *stochastic* model to describe the *state* of an object over a given interval.
Let's break this down:
* memoryless = it does not remember previous iterations
* stochastic = each time you run the model, you could get a different result even if the model's properties remain constant
* state = think binary numbers, either [0] or [1], 1 and 2 are mutually exclusive (cannot occur concurrently) states

Before you look at Figure 1, I would reccommend visiting [this website](https://setosa.io/blog/2014/07/26/markov-chains/index.html) for a general visualization and intuitive understanding of Markov Chains.

#### *Figure 1. Problem-Specific Markov Chain Model*

<img src="https://github.com/rajtum/Modeling-Public-Outlet-Electricity-Costs-with-Pseudo-Memory-Markov-Chains/blob/master/Models/General%20Markov%20Model.PNG" width="700">

### ii. Pseudo-Memory
False-memory, or *pseudo-memory* was a term created to describe the behavior of later models, where the *transition matrix* was adjusted based on generalized likelihood for the need to charge increasing over the course of a day ( **Time-Adjusted Model** - look at: `increment` )  and likely action due to battery charge ( **Battery-Adjusted Model** - look at: `batterycharge` ). In these models, the model's previous iterations had impacted the probabilities of the current *transition matrix*, but the *transition matrix* was adjusted based only on its current state. It was termed *psuedo* because memory demands (1) storage of the information and (2) the ability to recall the information. Though the model weakly satisfied (1) in how past iterations influenced the current *transition matrix* in a manner which the model's previous states could be deduced, the model could not actively recall this information to inform the current iteration, therefore model's memory is more pretense than actuality.

### iii. Battery-Adjusted
The current battery charge influences whether the device is in a [Not Charging] or [Charging] state. When in it is in a [Charging] state, the float point type variable ( `batterycharge` ) increases by a certain amount, whereas this variable decreases in a [Not Charging] state. Based on the variable `batterycharge` , transition matrix probabilities could intuitively finetune to simulate actual human behaviors (i.e. you're more likely to continue charging when you have 5% than 99%, so the probability of leaving the [Charging] to a [Not Charging State] should be higher at 99% than at 20%).

Based on this behavior, this function, where `batterycharge` was x, was developed:

<img src="https://github.com/rajtum/Modeling-Public-Outlet-Electricity-Costs-with-Pseudo-Memory-Markov-Chains/blob/master/Appendix/Model%204%20-%20Battery-Adjusted%20Conversion.png" width="300"> 

***
<img src="https://github.com/rajtum/Modeling-Public-Outlet-Electricity-Costs-with-Pseudo-Memory-Markov-Chains/blob/master/Appendix/Model%204%20-%20Battery-Adjusted%20Conversion%20Graph.PNG" width="500"> 

The function takes inspiration from the sigmoid neuron in machine learning, where graphed functions can provide deeper insight into complex behaviors and fine-tune modeling. When the executed via the function `probofcharging(batterycharge)` , the y-value corresponds to `X1` and `Y1`, which is respectively the probability to remain charging and the probability to began charging depending on the current state.


| `battery charge`| x | F(x) | Likelihood of entering ( `Y1` ) or remaining ( `X1` ) in a [Charging] state |
| ------------- |-------------| -----| ------------- |
| 1%  | .01 | .95| 95% |
| 99% | .99 | .17| 17% |
| 50% | .50 | .29| 29% | 

As you can see, the function predicts that a person still at 50% will be less likely to enter a charging state than a 50-50 previous models predictions. The magnitude for the rate of change for the battery charge over the probability of `X1` or `Y1` decreases to represent a less of a call to action to charge when the battery changes from %80 to %60 than from %30 to %10. A further improvement of the model would be to implement an `if` statement so that the reverse behavior would hold true in a [Charging] state but the same would still apply in a [Not Charging State], but due to time constraints, the improvement did not materialize.

### iv. Electricity Costs
This is simply the total hours of charging with the outlets from a public place. Conversions to cost to more conventional units of cost were performed in the paper hyperlinked above and now <a href="https://drive.google.com/file/d/1VrkC2M26mnis0jesCBb7r3mjHWoVoSTI/view?usp=sharing" target="_blank">here</a>
