# Modeling Electricity Costs from Public Outlet Usage through a Battery-Adjusted Pseudo-Memory Markov Chains

Don't worry if some of the terms in the title seem alien to you, we will hopefully go over each one in this guide. 

## I. Purpose

This code uses altered Markov Chains to predict how many hours people charged their phones at a public place based on two key features:
1.  An average number of devices typically in the public place ( `numOfDevices` )
2.  A certain time interval measured in days ( `days` )

## II. Limitations
Other possible variables such as number of outlets; accessibility of outlets; varying number of devices at the public place based on the weather, seasons, holidays; etc. were considered leading to a number of assumptions and justification for these assumptions. The fully-worded and justified assumptions can be found <a href="https://drive.google.com/file/d/1VrkC2M26mnis0jesCBb7r3mjHWoVoSTI/view?usp=sharing" target="_blank">here</a> but below is a topical glance:
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
False-memory, or *pseudo-memory* was a term created to describe the behavior of later models, where the *transition matrix* was adjusted based on rate of battery loss over time ( **Time-Adjusted Model** - look at: `increment` )  and likely action due to battery charge ( **Battery-Adjusted Model** - look at: `batterycharge` ). In these models, the model's previous iterations had impacted the probabilities of the current *transition matrix*, but the *transition matrix* was adjusted based only on its current state. It was termed *psuedo* because memory demands (1) storage of the information and (2) the ability to recall the information. Though the model weakly satisfied (1) in how past iterations influenced the current *transition matrix* in a manner which the model's previous states could be deduced, the model could not actively recall this information to inform the current iteration, therefore model's memory is more pretense than actuality.

### iii. Battery-Adjusted
The current battery charge influences whether the device is in a [Not Charging] or [Charging] state. When in it is in a [Charging] state, the float point type variable ( `batterycharge` ) increases by a certain amount, whereas this variable decreases in a [Not Charging] state. Based on the variable `batterycharge` , transition matrix probabilities could intuitively finetune to simulate actual behaviors (i.e. you're more likely to continue charging when you have 20% than 99%, so the probability of leaving the [Charging] to a [Not Charging State] should be higher at 99% than at 20%). 

### iv. Electricity Costs
