_This file describes what happens when doing a new analysis._

When submitting a new person for analysis, two things can happen:
- The person already exists in the system
- The person does not exist yet in the system.

If the person does not exist yet, the object representing the person is 
created.

From there, the system computes the various values for every numbers.¹

For every number, there has to be a generic explanation and a 
person-specific explanation. If one (or both) of them does not exist, it 
is created on the fly (as empty).

1) It could seem redundant to do it every time, but bear in mind that some 
 numbers such as the universal year or the personal year will change for a 
 same person throughout their life. For these reasons, everything is 
 recomputed.  
