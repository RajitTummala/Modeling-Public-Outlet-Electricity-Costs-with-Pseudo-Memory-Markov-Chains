# Modeling Electricity Costs from Public Outlet Usage through a Battery-Adjusted Pseudo-Memory Markov Chains

This code uses altered Markov Chains to predict how many hours people charged their phones at a public place based on two key features:
1.  An average number of devices typically in the public place ( `numOfDevices` )
2.  A certain time interval measured in days ( `days` )

Other possible variables such as number of outlets; accessibility of outlets; varying number of devices at the public place based on the weather, seasons, holidays; etc. were considered leading to a number of assumptions and justification for these assumptions. The fully-worded and justified assumptions can be found <a href="https://drive.google.com/file/d/1VrkC2M26mnis0jesCBb7r3mjHWoVoSTI/view?usp=sharing" target="_blank">here</a> but below is a topical glance:
* Two States: (1) Charging or (2) Not Charging
* Number of devices remain constant
* If a person needs to charge, then he or she will be able to and will
* At the start of the day, devices are at 100% charge which decreases every hour unless in a charging state
* Maximum amount of hours spent at a public place could be no more than 16



Don't worry if some of the terms in the title seem alien to you, we will hopefully go over each one here:

