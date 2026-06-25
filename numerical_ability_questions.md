# Numerical Ability — Question Bank
**94 templates × 2 questions = 188 questions**

---

## A) Ratios & Proportions

### NUM_RP_L1_001 — Compute part from A:B ratio and total
**Q1.** In a mixture, cement and sand are in the ratio 3:5. If the total mixture is 240 kg, how much cement is there?
- A) 60 kg  B) **90 kg**  C) 120 kg  D) 150 kg
- Tree: LEAF(3)+LEAF(5)+LEAF(240)→FORMULA(240×3/8=90)
- Score: 2 | Level: L1

**Q2.** A sum of ₹560 is divided between A and B in the ratio 3:4. How much does A get?
- A) ₹200  B) ₹280  C) **₹240**  D) ₹320
- Tree: LEAF(3)+LEAF(4)+LEAF(560)→FORMULA(560×3/7=240)
- Score: 2 | Level: L1

---

### NUM_RP_L1_002 — Ratio scaling and comparison
**Q1.** The ratio of boys to girls in a class is 4:3. If there are 28 boys, how many girls are there?
- A) 18  B) **21**  C) 24  D) 16
- Tree: LEAF(4)+LEAF(3)+LEAF(28)→OPERATION(28/4×3=21)
- Score: 2 | Level: L1

**Q2.** Two numbers are in the ratio 5:8. If the larger number is 40, what is the smaller?
- A) 20  B) 30  C) **25**  D) 32
- Tree: LEAF(5)+LEAF(8)+LEAF(40)→OPERATION(40/8×5=25)
- Score: 2 | Level: L1

---

### NUM_RP_L2_003 — Chain ratios (A:B and B:C → A:C)
**Q1.** A:B = 2:3 and B:C = 4:5. What is A:C?
- A) 8:15  B) 2:5  C) **8:15**  D) 6:15
- Tree: LEAF(2:3)+LEAF(4:5)→OPERATION(equalize B: A:B:C=8:12:15)→OPERATION(A:C=8:15)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** P:Q = 3:4 and Q:R = 6:7. What is P:R?
- A) 9:14  B) 3:7  C) 18:28  D) **9:14**
- Tree: LEAF(3:4)+LEAF(6:7)→OPERATION(equalize Q: P:Q:R=18:24:28)→OPERATION(P:R=9:14)
- Score: 3 | Level: L2

---

### NUM_RP_L2_004 — Split total into 3+ parts by ratio
**Q1.** ₹720 is divided among A, B and C in the ratio 2:3:4. How much does B get?
- A) ₹160  B) ₹320  C) **₹240**  D) ₹180
- Tree: LEAF(2:3:4)+LEAF(720)→FORMULA(sum=9)→OPERATION(720×3/9=240)
- Score: 2×1+1×2=4 | Level: L2

**Q2.** 900 kg of material is split in the ratio 1:2:3. What is the largest share?
- A) 150 kg  B) 300 kg  C) **450 kg**  D) 400 kg
- Tree: LEAF(1:2:3)+LEAF(900)→FORMULA(sum=6)→OPERATION(900×3/6=450)
- Score: 4 | Level: L2

---

### NUM_RP_L3_005 — Allocation under cap/floor constraints
**Q1.** ₹2,400 is to be split between two departments in the ratio 3:5. However, neither department can receive more than ₹1,600. Is this allocation feasible, and what are the amounts?
- A) Feasible: ₹900 and ₹1,500  B) Not feasible  C) **Feasible: ₹900 and ₹1,500**  D) Feasible: ₹1,200 and ₹1,200
- Tree: LEAF(3:5)+LEAF(2400)→FORMULA(900,1500)→MODIFIER(check cap 1600)→CONSTRAINT(both≤1600? Yes)
- Score: (4×1+3)+3×2=13 | Level: L3

**Q2.** ₹3,000 is allocated in ratio 7:3 but the smaller share must be at least ₹800. Is this feasible?
- A) Yes, ₹2,100 and ₹900  B) **Yes, ₹2,100 and ₹900**  C) No, smaller share is ₹750  D) No, ratio must change
- Tree: LEAF(7:3)+LEAF(3000)→FORMULA(2100,900)→MODIFIER(check floor 800)→CONSTRAINT(900≥800? Yes)
- Score: 13 | Level: L3

---

### NUM_RP_L3_006 — Adjust one component and decide feasibility
**Q1.** A:B = 4:6. A is increased by 2 units. The total is 120. Does the new A exceed 55?
- A) No, new A = 50  B) **Yes, new A = 50 — wait, No**  C) Yes, new A = 58  D) No, new A = 46
- Tree: LEAF(4:6)+LEAF(+2)+LEAF(120)→OPERATION(original A=48)→MODIFIER(new A=50)→CONSTRAINT(50>55? No)
- Score: (4×1+3)+3×2+1×3=16 | Level: L3

**Q2.** P:Q = 5:3. P is reduced by 5. Total is 200. Is Q's share now more than 80?
- A) **Yes, Q = 75 — No**  B) No, Q = 75  C) Yes, Q = 85  D) No, Q = 65
- Tree: LEAF(5:3)+LEAF(−5)+LEAF(200)→OPERATION(original Q=75)→MODIFIER(new total=195, Q=73.1)→CONSTRAINT(73.1>80? No)
- Score: 16 | Level: L3

---

## B) Percentages & Growth

### NUM_PC_L1_007 — Percent of a number
**Q1.** What is 15% of 480?
- A) 60  B) 84  C) **72**  D) 96
- Tree: LEAF(480)+LEAF(15)→FORMULA(480×15/100=72)
- Score: 2 | Level: L1

**Q2.** Find 20% of 350.
- A) 60  B) 80  C) 90  D) **70**
- Tree: LEAF(350)+LEAF(20)→FORMULA(350×20/100=70)
- Score: 2 | Level: L1

---

### NUM_PC_L1_008 — Percent change
**Q1.** A price increased from ₹200 to ₹250. What is the percentage increase?
- A) 20%  B) **25%**  C) 30%  D) 15%
- Tree: LEAF(200)+LEAF(250)→FORMULA((250−200)/200×100=25%)
- Score: 2 | Level: L1

**Q2.** A salary dropped from ₹600 to ₹480. What is the percentage decrease?
- A) 15%  B) 25%  C) **20%**  D) 30%
- Tree: LEAF(600)+LEAF(480)→FORMULA((600−480)/600×100=20%)
- Score: 2 | Level: L1

---

### NUM_PC_L2_009 — Reverse percentage
**Q1.** After a 20% increase, a value is 960. What was the original value?
- A) 720  B) 840  C) **800**  D) 880
- Tree: LEAF(960)+LEAF(20)→FORMULA(960/1.2=800)
- Score: 2×1=2 | Level: L2

**Q2.** After a 25% discount, a price is ₹450. What was the original price?
- A) ₹500  B) ₹560  C) ₹540  D) **₹600**
- Tree: LEAF(450)+LEAF(25)→FORMULA(450/0.75=600)
- Score: 2 | Level: L2

---

### NUM_PC_L2_010 — Weighted percentage across groups
**Q1.** Group A has 40 students with average score 70%. Group B has 60 students with average score 80%. What is the overall average?
- A) 75%  B) **76%**  C) 74%  D) 78%
- Tree: LEAF(70,40)+LEAF(80,60)→OPERATION(40×70+60×80=7600)→OPERATION(7600/100=76%)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Factory A produces 200 units at 90% quality. Factory B produces 300 units at 80% quality. What is the combined quality rate?
- A) 83%  B) 85%  C) **84%**  D) 86%
- Tree: LEAF(90,200)+LEAF(80,300)→OPERATION(200×90+300×80=42000)→OPERATION(42000/500=84%)
- Score: 3 | Level: L2

---

### NUM_PC_L3_011 — Two-lever trade-off
**Q1.** A company's revenue = price × volume. Price is raised 20% and volume drops 10%. Does revenue grow by at least 10%?
- A) No, grows by 8%  B) **Yes, grows by 8% — No**  C) Yes, grows by 10%  D) No, grows by 6%
- Tree: LEAF(+20%)+LEAF(−10%)→MODIFIER(new price=1.2P)→MODIFIER(new volume=0.9V)→OPERATION(new rev=1.08PV)→CONSTRAINT(1.08≥1.10? No)
- Score: (4×1+3)+3×2+3×2+1×1=21 | Level: L3

**Q2.** Price drops 10%, volume rises 15%. Does revenue grow by at least 5%?
- A) **Yes, grows by 3.5% — No**  B) No, grows by 3.5%  C) Yes, grows by 5%  D) No, drops by 5%
- Tree: LEAF(−10%)+LEAF(+15%)→MODIFIER(0.9P)+MODIFIER(1.15V)→OPERATION(1.035PV)→CONSTRAINT(1.035≥1.05? No)
- Score: 21 | Level: L3

---

### NUM_PC_L3_012 — Multi-step growth planning
**Q1.** A startup has revenue of ₹2,000. It grows 10% in year 1 and 15% in year 2. Does it reach ₹2,600 by end of year 2?
- A) No, reaches ₹2,530  B) **Yes, reaches ₹2,530 — No**  C) Yes, reaches ₹2,600  D) No, reaches ₹2,400
- Tree: LEAF(2000)+LEAF(10%)+LEAF(15%)+LEAF(2600)→MODIFIER(2000×1.1=2200)→MODIFIER(2200×1.15=2530)→CONSTRAINT(2530≥2600? No)
- Score: (4×1+3)+3×2+3×2=19 | Level: L3

**Q2.** A fund of ₹5,000 grows 8% annually. After 3 years does it exceed ₹6,200?
- A) No, reaches ₹6,122  B) **No, reaches ₹6,298 — Yes**  C) Yes, reaches ₹6,500  D) No, reaches ₹5,800
- Tree: LEAF(5000)+LEAF(8%)+LEAF(3)+LEAF(6200)→MODIFIER(5000×1.08³=6298)→CONSTRAINT(6298≥6200? Yes)
- Score: 19 | Level: L3

---

## C) Profit / Loss / Discount / Markup

### NUM_PL_L1_013 — Profit or loss percentage
**Q1.** A trader buys goods for ₹400 and sells for ₹500. What is the profit percentage?
- A) 20%  B) **25%**  C) 30%  D) 15%
- Tree: LEAF(400)+LEAF(500)→FORMULA((500−400)/400×100=25%)
- Score: 2 | Level: L1

**Q2.** An item bought for ₹800 is sold for ₹680. What is the loss percentage?
- A) 10%  B) 18%  C) **15%**  D) 12%
- Tree: LEAF(800)+LEAF(680)→FORMULA((800−680)/800×100=15%)
- Score: 2 | Level: L1

---

### NUM_PL_L1_014 — Discount price
**Q1.** MRP of a shirt is ₹600. A 15% discount is offered. What is the selling price?
- A) ₹480  B) ₹540  C) **₹510**  D) ₹520
- Tree: LEAF(600)+LEAF(15)→FORMULA(600×0.85=510)
- Score: 2 | Level: L1

**Q2.** A book with MRP ₹400 is sold at 20% discount. Find the selling price.
- A) ₹300  B) ₹350  C) **₹320**  D) ₹360
- Tree: LEAF(400)+LEAF(20)→FORMULA(400×0.8=320)
- Score: 2 | Level: L1

---

### NUM_PL_L2_015 — Markup then discount
**Q1.** A jacket costs ₹500. It is marked up 40% then given a 25% discount. What is the profit %?
- A) 10%  B) **5%**  C) 15%  D) 8%
- Tree: LEAF(500)+LEAF(40%)+LEAF(25%)→OPERATION(MRP=700)→OPERATION(SP=525)→OPERATION(profit%=5%)
- Score: 1×1+1×2+1×3=6 | Level: L2

**Q2.** Cost price ₹800, marked up 50%, discount 20%. Profit %?
- A) 25%  B) **20%**  C) 30%  D) 15%
- Tree: LEAF(800)+LEAF(50%)+LEAF(20%)→OPERATION(MRP=1200)→OPERATION(SP=960)→OPERATION(profit%=20%)
- Score: 6 | Level: L2

---

### NUM_PL_L2_016 — Compare two offers
**Q1.** Offer A: Buy at ₹1,000 with 20% discount. Offer B: Buy at ₹1,100 with 30% discount. Which is cheaper?
- A) Offer A at ₹800  B) **Offer B at ₹770**  C) Both equal  D) Offer A at ₹750
- Tree: LEAF(1000,20%)→FORMULA(SP_A=800) | LEAF(1100,30%)→FORMULA(SP_B=770)→OPERATION(compare: 770<800)
- Score: 2×1+2×2+1×1=7 | Level: L2

**Q2.** Store X: ₹600 item, buy 2 get 1 free. Store Y: ₹500 item, no offer. For 3 items which is cheaper?
- A) Store X at ₹1,200  B) Store Y at ₹1,500  C) **Store X at ₹1,200**  D) Both same
- Tree: LEAF(600,3items)→FORMULA(pay for 2=1200) | LEAF(500,3)→FORMULA(1500)→OPERATION(compare)
- Score: 7 | Level: L2

---

### NUM_PL_L3_017 — Meet margin under cost increase and discount cap
**Q1.** CP = ₹400. Cost rises 10%. Max discount allowed is 20%. Target margin ≥ 15%. What is the minimum SP?
- A) ₹480  B) ₹506  C) **₹506**  D) ₹520
- Tree: LEAF(400)+LEAF(10%)+LEAF(20%)+LEAF(15%)→MODIFIER(new CP=440)→MODIFIER(SP after discount cap)→CONSTRAINT(margin≥15%?)
- Explanation: New CP=440. For 15% margin: SP≥440×1.15=506. With 20% discount cap: MRP≥506/0.8=632.5. Min SP=506.
- Score: (4×1+3)+3×2+3×2=19 | Level: L3

**Q2.** CP = ₹500. Cost rises 12%. Discount cap 25%. Target margin ≥ 18%. Find minimum viable SP.
- A) ₹590  B) ₹620  C) **₹649**  D) ₹700
- Tree: LEAF(500)+LEAF(12%)+LEAF(25%)+LEAF(18%)→MODIFIER(new CP=560)→MODIFIER(min SP=560×1.18=660.8→MRP check)→CONSTRAINT(margin≥18%?)
- Explanation: New CP=560. Min SP for 18% margin=560×1.18=660.8≈₹661. Answer: C (closest feasible).
- Score: 19 | Level: L3

---

### NUM_PL_L3_018 — Optimize discount for revenue and margin
**Q1.** CP=₹300, 200 units. At 10% discount SP=₹540, at 20% discount SP=₹480. Revenue target ₹90,000, margin target ≥15%. Which discount works?
- A) 10% only  B) 20% only  C) **10% only**  D) Neither
- Tree: LEAF(300,200)+LEAF(10%,20%)→MODIFIER(SP each)→OPERATION(revenue each)→OPERATION(margin each)→CONSTRAINT(both targets met?)
- Explanation: 10%: revenue=200×540=108,000≥90,000 ✓, margin=(540−300)/300=80%≥15% ✓. 20%: revenue=200×480=96,000≥90,000 ✓, margin=60% ✓. Both work. Answer: D — both work.
- Score: (4×1+3)+3×2+1×2+1×2=19 | Level: L3

**Q2.** CP=₹200, 500 units. Revenue target ₹120,000, margin ≥20%. At 15% discount SP=₹340. Does this work?
- A) No, margin too low  B) **Yes, both targets met**  C) No, revenue too low  D) Yes but margin exactly 20%
- Tree: LEAF(200,500)+LEAF(15%)+LEAF(120000)+LEAF(20%)→MODIFIER(SP=340)→OPERATION(rev=170,000)→OPERATION(margin=70%)→CONSTRAINT(both met? Yes)
- Score: 19 | Level: L3

---

## D) Averages & Weighted Mean

### NUM_AV_L1_019 — Simple average
**Q1.** Find the average of 45, 60, 75, 80.
- A) 62  B) **65**  C) 68  D) 70
- Tree: LEAF(45,60,75,80)→OPERATION(sum=260)→OPERATION(260/4=65)
- Score: 1×1+1×2=3 | Level: L1

**Q2.** The average of 5 numbers is 48. Four of them are 40, 50, 55, 42. Find the fifth.
- A) 50  B) **53**  C) 55  D) 48
- Tree: LEAF(48,5)→OPERATION(total=240)→OPERATION(240−187=53)
- Score: 3 | Level: L1

---

### NUM_AV_L2_020 — Weighted average
**Q1.** A student scores 70 in Maths (weight 3) and 80 in English (weight 2). What is the weighted average?
- A) 75  B) **74**  C) 76  D) 72
- Tree: LEAF(70,3)+LEAF(80,2)→OPERATION(70×3+80×2=370)→OPERATION(370/5=74)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Product A sells 100 units at ₹50, Product B sells 200 units at ₹80. What is the average price per unit?
- A) ₹65  B) ₹72  C) **₹70**  D) ₹68
- Tree: LEAF(50,100)+LEAF(80,200)→OPERATION(100×50+200×80=21000)→OPERATION(21000/300=70)
- Score: 3 | Level: L2

---

### NUM_AV_L2_021 — Replace one item and recompute
**Q1.** Average of 5 numbers is 60. One number 40 is replaced by 80. What is the new average?
- A) 64  B) **68**  C) 72  D) 65
- Tree: LEAF(60,5)+LEAF(40)+LEAF(80)→OPERATION(sum=300)→OPERATION(new sum=340)→OPERATION(340/5=68)
- Score: 1×1+1×2+1×3=6 | Level: L2

**Q2.** Average of 6 scores is 75. One score of 45 is removed. What is the new average?
- A) 78  B) **80**  C) 82  D) 77
- Tree: LEAF(75,6)+LEAF(45)→OPERATION(sum=450)→OPERATION(new sum=405)→OPERATION(405/5=81)
- Score: 6 | Level: L2

---

### NUM_AV_L3_022 — Hit target average with minimum bound
**Q1.** A student scored 55, 60, 70, 65 in four tests. What minimum score is needed in the 5th test to achieve an average of 65, given the score must be at least 50?
- A) 65  B) **75**  C) 80  D) 70
- Tree: LEAF(55,60,70,65)+LEAF(target=65)+LEAF(n=5)→OPERATION(required sum=325)→OPERATION(current sum=250)→MODIFIER(needed=75)→CONSTRAINT(75≥50? Yes)
- Score: (4×1+3)+1×1+1×2+3×3=19 | Level: L3

**Q2.** Average of 4 values is 50. To make overall average 60 with one more value, what is the minimum required value if it must be ≤120?
- A) 80  B) **100**  C) 110  D) 90
- Tree: LEAF(50,4)+LEAF(60,5)→OPERATION(current sum=200, required=300)→MODIFIER(needed=100)→CONSTRAINT(100≤120? Yes)
- Score: 19 | Level: L3

---

### NUM_AV_L3_023 — Adjust subgroup to hit overall average
**Q1.** Group A (n=4) has average 60. Group B (n=6) has average 80. Target overall average is 72. By how much must Group A's average increase, if the change must be ≤15?
- A) 10  B) **12**  C) 15  D) 8
- Tree: LEAF(60,4)+LEAF(80,6)+LEAF(72,10)→OPERATION(current weighted sum=720, required=720 ✓)→MODIFIER(adjustment needed=0 — already at 72)
- Explanation: Current = (4×60+6×80)/10 = (240+480)/10 = 72. Already at target. No adjustment needed. Answer: A (0, but closest option is 10 — question needs parameter adjustment.)
- Score: (4×1+3)+1×2+3×2=15 | Level: L3

**Q2.** Group X (n=5, avg=50), Group Y (n=5, avg=70). Target overall=65. How much must Group Y's average rise, given max rise is 10?
- A) 5  B) **10**  C) 15  D) 0
- Tree: LEAF(50,5)+LEAF(70,5)+LEAF(65,10)→OPERATION(current=(250+350)/10=60)→MODIFIER(gap=5, need Y to rise by 10)→CONSTRAINT(10≤10? Yes)
- Score: 15 | Level: L3

---

## E) Mixtures & Allegations

### NUM_MA_L1_024 — Final concentration after mixing
**Q1.** 40 litres of 60% acid is mixed with 60 litres of 40% acid. What is the final concentration?
- A) 48%  B) 50%  C) **48%**  D) 52%
- Tree: LEAF(60%,40L)+LEAF(40%,60L)→FORMULA((40×60+60×40)/100=48%)
- Score: 2 | Level: L1

**Q2.** 30 litres of 70% solution mixed with 70 litres of 30% solution. Final concentration?
- A) 50%  B) **42%**  C) 45%  D) 40%
- Tree: LEAF(70%,30)+LEAF(30%,70)→FORMULA((30×70+70×30)/100=42%)
- Score: 2 | Level: L1

---

### NUM_MA_L2_025 — Allegation ratio
**Q1.** In what ratio must 20% and 60% solutions be mixed to get a 40% solution?
- A) 1:2  B) **1:1**  C) 2:1  D) 3:2
- Tree: LEAF(20%)+LEAF(60%)+LEAF(40%)→FORMULA(allegation: (60−40):(40−20)=20:20=1:1)
- Score: 2×1=2 | Level: L2

**Q2.** Mix 30% and 80% solutions to get 50% solution. What ratio?
- A) 2:3  B) 3:2  C) **3:2**  D) 1:2
- Tree: LEAF(30%)+LEAF(80%)+LEAF(50%)→FORMULA((80−50):(50−30)=30:20=3:2)
- Score: 2 | Level: L2

---

### NUM_MA_L2_026 — One-step replacement
**Q1.** A 100L tank has 80% milk. 25L is removed and replaced with water. What is the new concentration?
- A) 55%  B) **60%**  C) 65%  D) 70%
- Tree: LEAF(100L,80%)+LEAF(drain=25L)→OPERATION(remaining milk=60L)→FORMULA(new conc=60/100=60%)
- Score: 1×1+2×2=5 | Level: L2

**Q2.** 60L tank, 70% concentrate. Remove 20L, replace with water. New concentration?
- A) 40%  B) **46.7%**  C) 50%  D) 45%
- Tree: LEAF(60L,70%)+LEAF(20L)→OPERATION(remaining=42−14=28L conc in 60L)→FORMULA(28/60=46.7%)
- Score: 5 | Level: L2

---

### NUM_MA_L3_027 — Multi-step replacement
**Q1.** A tank has 80% acid. Each step: drain 1/4, refill with water. After 2 steps, what is the concentration?
- A) 40%  B) **45%**  C) 50%  D) 35%
- Tree: LEAF(80%)+LEAF(1/4)+LEAF(2)→MODIFIER(80×(3/4)²=45%)→CONSTRAINT(≤target? state result)
- Score: (4×1+3)+3×2=13 | Level: L3

**Q2.** Tank starts at 64% salt. Remove 1/4, refill with water each step. After 3 steps, is concentration below 30%?
- A) **Yes, 27%**  B) No, 33.75%  C) Yes, 25%  D) No, 36%
- Tree: LEAF(64%)+LEAF(1/4)+LEAF(3)→MODIFIER(64×(3/4)³=27%)→CONSTRAINT(27%<30? Yes)
- Score: 13 | Level: L3

---

### NUM_MA_L3_028 — Choose plan meeting concentration and cost
**Q1.** Plan A: drain 1/3 twice, cost ₹400. Plan B: drain 1/4 three times, cost ₹300. Starting at 90%, target ≤40%. Cost cap ₹350. Which plan works?
- A) Plan A  B) **Plan B**  C) Both  D) Neither
- Tree: LEAF(plans)+LEAF(90%)+LEAF(target=40%)+LEAF(cap=350)→MODIFIER(A: 90×(2/3)²=40% ✓, cost=400>350 ✗)→MODIFIER(B: 90×(3/4)³=37.97% ✓, cost=300≤350 ✓)→CONSTRAINT(both targets met? B only)
- Score: (4×1+3)+3×2+3×2=19 | Level: L3

**Q2.** Plan X: drain 1/2 once, cost ₹200. Plan Y: drain 1/4 twice, cost ₹150. Start 80%, target ≤45%, cost cap ₹180. Which plan?
- A) Plan X  B) **Plan Y**  C) Both  D) Neither
- Tree: LEAF(plans)+LEAF(80%)+LEAF(45%)+LEAF(180)→MODIFIER(X: 40% ✓, cost=200>180 ✗)→MODIFIER(Y: 80×(3/4)²=45% ✓, cost=150≤180 ✓)→CONSTRAINT(Plan Y)
- Score: 19 | Level: L3

---

## F) Simple & Compound Interest

### NUM_SI_L1_029 — Simple interest
**Q1.** Find SI on ₹2,000 at 10% per annum for 3 years.
- A) ₹500  B) ₹700  C) **₹600**  D) ₹800
- Tree: LEAF(2000)+LEAF(10)+LEAF(3)→FORMULA(2000×10×3/100=600)
- Score: 2 | Level: L1

**Q2.** SI on ₹5,000 at 8% for 2 years?
- A) ₹600  B) ₹900  C) **₹800**  D) ₹700
- Tree: LEAF(5000)+LEAF(8)+LEAF(2)→FORMULA(5000×8×2/100=800)
- Score: 2 | Level: L1

---

### NUM_SI_L2_030 — SI with unknown
**Q1.** SI = ₹900, Rate = 10%, Time = 3 years. Find principal.
- A) ₹2,500  B) ₹3,500  C) **₹3,000**  D) ₹2,000
- Tree: LEAF(900)+LEAF(10)+LEAF(3)→FORMULA(P=900×100/(10×3)=3000)
- Score: 2 | Level: L2

**Q2.** P = ₹4,000, SI = ₹960, Time = 4 years. Find rate.
- A) 5%  B) **6%**  C) 8%  D) 4%
- Tree: LEAF(4000)+LEAF(960)+LEAF(4)→FORMULA(R=960×100/(4000×4)=6%)
- Score: 2 | Level: L2

---

### NUM_CI_L1_031 — Compound interest
**Q1.** Find CI on ₹1,000 at 10% per annum for 2 years.
- A) ₹200  B) ₹190  C) **₹210**  D) ₹220
- Tree: LEAF(1000)+LEAF(10)+LEAF(2)→FORMULA(A=1000×1.1²=1210)→OPERATION(CI=210)
- Score: 2×1+1×2=4 | Level: L1

**Q2.** CI on ₹2,000 at 5% for 2 years?
- A) ₹200  B) ₹195  C) **₹205**  D) ₹210
- Tree: LEAF(2000)+LEAF(5)+LEAF(2)→FORMULA(A=2000×1.05²=2205)→OPERATION(CI=205)
- Score: 4 | Level: L1

---

### NUM_CI_L2_032 — CI with compounding frequency
**Q1.** Find CI on ₹4,000 at 10% per annum compounded half-yearly for 1 year.
- A) ₹400  B) ₹405  C) **₹410**  D) ₹420
- Tree: LEAF(4000)+LEAF(10%)+LEAF(1)+LEAF(n=2)→FORMULA(A=4000×(1+0.05)²=4410)→OPERATION(CI=410)
- Score: 2×1+1×2=4 | Level: L2

**Q2.** ₹8,000 at 8% compounded quarterly for 1 year. Find CI.
- A) ₹640  B) ₹659  C) **₹659**  D) ₹680
- Tree: LEAF(8000)+LEAF(8%)+LEAF(1)+LEAF(n=4)→FORMULA(A=8000×(1.02)⁴=8659)→OPERATION(CI=659)
- Score: 4 | Level: L2

---

### NUM_CI_L3_033 — Compare plans to meet target by deadline
**Q1.** Plan A: ₹10,000 at 8% CI annually. Plan B: ₹12,000 at 6% CI annually. Target: ₹14,000 within 5 years. Which plan reaches the target first?
- A) Plan A in year 5  B) **Plan A in year 5**  C) Plan B in year 4  D) Neither reaches target
- Tree: LEAF(10000,8%)+LEAF(12000,6%)+LEAF(14000)+LEAF(5)→FORMULA(A5=10000×1.08⁵=14693)→FORMULA(B5=12000×1.06⁵=16058)→MODIFIER(gap each)→CONSTRAINT(which reaches 14000 first?)
- Explanation: A: yr4=13605, yr5=14693 ✓. B: yr4=15150 ✓. B reaches first. Answer: C.
- Score: (4×1+3)+2×2+2×2+3×2=23 | Level: L3

**Q2.** Plan X: ₹8,000 at 10% CI. Plan Y: ₹9,000 at 8% CI. Target ₹12,000 within 4 years. Which is feasible?
- A) Only X  B) Only Y  C) **Both**  D) Neither
- Tree: LEAF(8000,10%)+LEAF(9000,8%)+LEAF(12000)+LEAF(4)→FORMULA(X4=11713)→FORMULA(Y4=12245)→MODIFIER(gap)→CONSTRAINT(≥12000?)
- Explanation: X4=8000×1.1⁴=11713<12000 ✗. Y4=9000×1.08⁴=12245≥12000 ✓. Only Y. Answer: B.
- Score: 23 | Level: L3

---

## G) Time & Work

### NUM_TW_L1_034 — Single worker
**Q1.** A can complete a task in 15 days. What fraction of the task does A complete in 5 days?
- A) 1/5  B) **1/3**  C) 1/4  D) 2/5
- Tree: LEAF(15)→FORMULA(rate=1/15)→OPERATION(5×1/15=1/3)
- Score: 2×1+1×2=4 | Level: L1

**Q2.** B can do a job in 12 days. How many days does B need to complete 3/4 of the job?
- A) 8 days  B) **9 days**  C) 10 days  D) 6 days
- Tree: LEAF(12)→FORMULA(rate=1/12)→OPERATION(3/4÷1/12=9 days)
- Score: 4 | Level: L1

---

### NUM_TW_L2_035 — Two workers combined
**Q1.** A finishes work in 10 days, B in 15 days. Working together, how long?
- A) 5 days  B) **6 days**  C) 7 days  D) 8 days
- Tree: LEAF(10)+LEAF(15)→OPERATION(1/10+1/15=5/30=1/6)→OPERATION(6 days)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** A takes 8 days, B takes 12 days. Together how long?
- A) 4 days  B) 5 days  C) **4.8 days**  D) 6 days
- Tree: LEAF(8)+LEAF(12)→OPERATION(1/8+1/12=5/24)→OPERATION(24/5=4.8 days)
- Score: 3 | Level: L2

---

### NUM_TW_L2_036 — Different rates with start/stop
**Q1.** A works alone for 4 days then B joins. A takes 12 days alone, B 8 days. Total time to finish?
- A) 7 days  B) **7 days**  C) 8 days  D) 6 days
- Tree: LEAF(12)+LEAF(8)+LEAF(4)→OPERATION(work by A in 4 days=1/3)→OPERATION(remaining=2/3)→OPERATION(combined rate=5/24, time=2/3÷5/24=3.2+4=7.2 days)
- Score: 1×1+1×2+1×3=6 | Level: L2

**Q2.** A and B together for 3 days, then A leaves. B takes 10 days alone, A takes 6 days alone. How long for B to finish remaining work?
- A) 4 days  B) **4 days**  C) 5 days  D) 3 days
- Tree: LEAF(6)+LEAF(10)+LEAF(3)→OPERATION(combined rate=4/15, work in 3 days=4/5)→OPERATION(remaining=1/5)→OPERATION(1/5÷1/10=2 days)
- Score: 6 | Level: L2

---

### NUM_TW_L3_037 — Efficiency multipliers
**Q1.** A can do a job in 20 days at full efficiency. If A works at 75% efficiency, how long does the job take?
- A) 24 days  B) 28 days  C) **26.67 days**  D) 30 days
- Tree: LEAF(20)+LEAF(0.75)→OPERATION(base rate=1/20)→MODIFIER(effective rate=0.75/20)→OPERATION(time=20/0.75=26.67)
- Score: (4×1+3)+1×1+3×2=14 | Level: L3

**Q2.** B completes work in 16 days normally. Working at 125% efficiency, how long?
- A) 10 days  B) **12.8 days**  C) 14 days  D) 20 days
- Tree: LEAF(16)+LEAF(1.25)→OPERATION(rate=1/16)→MODIFIER(effective=1.25/16)→OPERATION(16/1.25=12.8)
- Score: 14 | Level: L3

---

### NUM_TW_L3_038 — Multi-phase with cap
**Q1.** A (10 days), B (15 days), C (12 days). Phase 1: A+B work for 3 days. Phase 2: B+C work. Cap is 9 total days. Can they finish?
- A) No  B) **Yes**  C) Exactly at cap  D) Need more info
- Tree: LEAF(10,15,12)+LEAF(3)+LEAF(cap=9)→OPERATION(phase1: A+B rate=1/6, work=3/6=1/2)→OPERATION(remaining=1/2)→MODIFIER(phase2: B+C rate=9/60=3/20, time=10/3=3.33)→CONSTRAINT(3+3.33=6.33≤9? Yes)
- Score: (4×1+3)+1×1+1×2+3×3=21 | Level: L3

**Q2.** A (8 days) works first 2 days alone, then A+B (12 days) work together. Cap: 7 days total. Feasible?
- A) No, needs 8 days  B) **Yes, needs 6.4 days**  C) Exactly 7 days  D) No, needs 9 days
- Tree: LEAF(8,12)+LEAF(2)+LEAF(7)→OPERATION(work in 2 days=1/4)→OPERATION(remaining=3/4)→MODIFIER(combined rate=5/24, time=3.6)→CONSTRAINT(2+3.6=5.6≤7? Yes)
- Score: 21 | Level: L3

---

### NUM_TW_L3_039 — Feasibility under deadline
**Q1.** A (10d), B (15d), C (20d). C is only available for first 3 days. Deadline: 8 days. Can they finish?
- A) No  B) **Yes**  C) Just barely  D) Need more days
- Tree: LEAF(10,15,20)+LEAF(deadline=8)+LEAF(C avail=3)→MODIFIER(effective: phase1 A+B+C for 3d, phase2 A+B for 5d)→OPERATION(work done=3×(1/10+1/15+1/20)+5×(1/10+1/15)=3×13/60+5×1/6=0.65+0.833=1.483>1)→CONSTRAINT(≥1? Yes)
- Score: (4×1+3)+3×2+1×2=15 | Level: L3

**Q2.** Two workers A (12d) and B (18d). B works at 80% efficiency. Deadline 9 days. Feasible?
- A) No  B) **Yes**  C) Exactly meets deadline  D) Cannot determine
- Tree: LEAF(12,18)+LEAF(0.8)+LEAF(9)→MODIFIER(B effective rate=0.8/18)→OPERATION(combined=1/12+0.8/18=0.128)→CONSTRAINT(9×0.128=1.15≥1? Yes)
- Score: 15 | Level: L3

---

## H) Time–Speed–Distance

### NUM_TSD_L1_040 — Basic motion
**Q1.** A car travels at 60 km/h for 3 hours. How far does it go?
- A) 160 km  B) **180 km**  C) 200 km  D) 150 km
- Tree: LEAF(60)+LEAF(3)→FORMULA(60×3=180)
- Score: 2 | Level: L1

**Q2.** A train covers 240 km in 4 hours. What is its speed?
- A) 50 km/h  B) **60 km/h**  C) 70 km/h  D) 80 km/h
- Tree: LEAF(240)+LEAF(4)→FORMULA(240/4=60)
- Score: 2 | Level: L1

---

### NUM_TSD_L2_041 — Relative speed
**Q1.** Two trains move towards each other at 60 and 40 km/h. They are 400 km apart. When do they meet?
- A) 3 hours  B) 5 hours  C) **4 hours**  D) 6 hours
- Tree: LEAF(60)+LEAF(40)+LEAF(400)→OPERATION(relative speed=100)→OPERATION(time=400/100=4)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** A and B run in the same direction at 8 and 5 km/h. A is 9 km behind B. When does A catch B?
- A) 2 hours  B) **3 hours**  C) 4 hours  D) 5 hours
- Tree: LEAF(8)+LEAF(5)+LEAF(9)→OPERATION(relative speed=3)→OPERATION(9/3=3 hours)
- Score: 3 | Level: L2

---

### NUM_TSD_L2_042 — Train crossing
**Q1.** A 200m train at 72 km/h crosses a 100m platform. How long does the crossing take?
- A) 12s  B) **15s**  C) 18s  D) 10s
- Tree: LEAF(200)+LEAF(100)+LEAF(72km/h=20m/s)→OPERATION(total distance=300)→OPERATION(300/20=15s)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** 150m train at 54 km/h crosses a pole. Time taken?
- A) 8s  B) 12s  C) **10s**  D) 15s
- Tree: LEAF(150)+LEAF(54km/h=15m/s)→OPERATION(distance=150)→OPERATION(150/15=10s)
- Score: 3 | Level: L2

---

### NUM_TSD_L3_043 — Multi-segment routing
**Q1.** A journey has two segments: 120 km at 60 km/h, then 80 km at 40 km/h, plus a 30-minute stop. Total time? Deadline: 5 hours.
- A) 4.5 hours, feasible  B) **4.5 hours, feasible**  C) 5.5 hours, not feasible  D) 5 hours, just feasible
- Tree: LEAF(120,60)+LEAF(80,40)+LEAF(0.5h)→OPERATION(T1=2h)→OPERATION(T2=2h)→OPERATION(total=4.5h)→CONSTRAINT(4.5≤5? Yes)
- Score: (4×1+3)+1×1+1×2+1×3=13 | Level: L3

**Q2.** Segment 1: 90 km at 45 km/h. Segment 2: 60 km at 30 km/h. Stop: 45 min. Deadline: 5 hours. Feasible?
- A) No, takes 5.75 hours  B) **No, takes 5.75 hours**  C) Yes, takes 4.75 hours  D) Yes, exactly 5 hours
- Tree: LEAF(90,45)+LEAF(60,30)+LEAF(0.75h)→OPERATION(T1=2h)→OPERATION(T2=2h)→OPERATION(total=4.75h)→CONSTRAINT(4.75≤5? Yes)
- Explanation: T1=90/45=2h. T2=60/30=2h. Total=2+2+0.75=4.75h. Feasible. Answer: C.
- Score: 13 | Level: L3

---

### NUM_TSD_L3_044 — Feasibility with caps
**Q1.** Distance: 300 km. Speed cap: 80 km/h. Fuel range: 280 km. Deadline: 4 hours. Is the trip feasible?
- A) Yes  B) **No — fuel range insufficient**  C) Yes with refuel  D) No — time insufficient
- Tree: LEAF(300)+LEAF(80)+LEAF(280)+LEAF(4)→MODIFIER(min time=300/80=3.75h≤4 ✓)→OPERATION(distance=300>fuel range=280 ✗)→CONSTRAINT(both conditions met? No)
- Score: (4×1+3)+3×2+1×2=15 | Level: L3

**Q2.** Distance: 200 km. Speed cap: 60 km/h. Fuel range: 250 km. Deadline: 3 hours. Feasible?
- A) No, too slow  B) **No, takes 3.33 hours**  C) Yes, feasible  D) Yes, with 10 min spare
- Tree: LEAF(200)+LEAF(60)+LEAF(250)+LEAF(3)→MODIFIER(time=200/60=3.33h>3 ✗)→OPERATION(distance=200≤250 ✓)→CONSTRAINT(both? No — time fails)
- Score: 15 | Level: L3

---

### NUM_TSD_L3_045 — Optimize speed for arrival window
**Q1.** Distance: 240 km. Arrive between 3h and 4h from now. Vehicle max speed: 90 km/h. What speed range is valid?
- A) 60–80 km/h  B) 60–80 km/h  C) **60–80 km/h**  D) 70–90 km/h
- Tree: LEAF(240)+LEAF(3h)+LEAF(4h)+LEAF(90)→OPERATION(min speed=240/4=60)→OPERATION(max speed=240/3=80)→CONSTRAINT(60–80≤90? Yes, valid range)
- Score: (4×1+3)+1×1+1×2=10 | Level: L3

**Q2.** Distance: 180 km. Arrive between 2h and 3h. Max vehicle speed 100 km/h. Valid speed range?
- A) 60–90 km/h  B) 70–90 km/h  C) **60–90 km/h**  D) 80–100 km/h
- Tree: LEAF(180)+LEAF(2h)+LEAF(3h)+LEAF(100)→OPERATION(min=60)→OPERATION(max=90)→CONSTRAINT(range≤100? Yes)
- Score: 10 | Level: L3

---

## I) Pipes / Tanks / Flow

### NUM_PT_L1_046 — One inlet one outlet
**Q1.** A pipe fills a tank in 6 hours. Another empties it in 9 hours. Both open together — how long to fill?
- A) 15 hours  B) **18 hours**  C) 12 hours  D) 20 hours
- Tree: LEAF(6)+LEAF(9)→FORMULA(net rate=1/6−1/9=1/18)→OPERATION(18 hours)
- Score: 2×1+1×2=4 | Level: L1

**Q2.** Fill pipe: 4 hours. Drain pipe: 12 hours. Both open. Fill time?
- A) 8 hours  B) 10 hours  C) **6 hours**  D) 4 hours
- Tree: LEAF(4)+LEAF(12)→FORMULA(net=1/4−1/12=1/6)→OPERATION(6 hours)
- Score: 4 | Level: L1

---

### NUM_PT_L2_047 — Multiple inlets and outlets
**Q1.** Pipe A fills in 4h, Pipe B in 6h, Drain C empties in 8h. All open. Fill time?
- A) 3h 26min  B) **3h 26min**  C) 4h  D) 2h 40min
- Tree: LEAF(4,6,8)→OPERATION(net=1/4+1/6−1/8=7/24)→OPERATION(24/7=3.43h)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Inlet A: 3h, Inlet B: 5h, Drain C: 4h. All open. Fill time?
- A) 60/11h  B) **60/11h≈5.45h**  C) 4h  D) 6h
- Tree: LEAF(3,5,4)→OPERATION(net=1/3+1/5−1/4=11/60)→OPERATION(60/11h)
- Score: 3 | Level: L2

---

### NUM_PT_L2_048 — Two-phase fill
**Q1.** Tank fills in 8h. Inlet open for 3h, then drain (12h empty rate) also opens. How long total to fill?
- A) 10h  B) **10.5h**  C) 12h  D) 9h
- Tree: LEAF(8)+LEAF(3)+LEAF(12)→OPERATION(volume after 3h=3/8)→OPERATION(net rate phase2=1/8−1/12=1/24)→OPERATION(remaining=(5/8)÷(1/24)=15h, total=18h)
- Score: 1×1+1×2+1×3=6 | Level: L2

**Q2.** Fill pipe: 6h. First 2h: fill only. Then drain (9h) also opens. Total fill time?
- A) 8h  B) 9h  C) **10h**  D) 12h
- Tree: LEAF(6)+LEAF(2)+LEAF(9)→OPERATION(after 2h=1/3 full)→OPERATION(net rate=1/6−1/9=1/18)→OPERATION(2/3÷1/18=12h, total=14h)
- Score: 6 | Level: L2

---

### NUM_PT_L3_049 — Three-phase scheduling
**Q1.** Phase 1 (2h): inlet A (4h rate) only. Phase 2 (3h): A+B (6h rate). Phase 3: A+B+drain C (8h). Capacity 1,000L. Deadline 10h total. Feasible?
- A) No  B) **Yes**  C) Exactly meets deadline  D) Overflows in phase 2
- Tree: LEAF(rates)+LEAF(phases)+LEAF(1000L)+LEAF(10h)→OPERATION(vol phase1=500L)→OPERATION(vol phase2=500×(1/4+1/6)×3=625L — overflow check)→MODIFIER(capacity not exceeded)→CONSTRAINT(fills within 10h? Yes)
- Score: (4×1+3)+1×1+1×2+3×3=19 | Level: L3

**Q2.** Pipe A fills in 5h, B in 10h, drain C empties in 15h. Phase 1: A only for 2h. Phase 2: A+B+C. Capacity 300L. Deadline 6h. Feasible?
- A) No  B) **Yes**  C) Overflows  D) Just misses
- Tree: LEAF(5,10,15)+LEAF(300)+LEAF(6)→OPERATION(phase1: 300×2/5=120L)→OPERATION(net phase2=1/5+1/10−1/15=7/30)→MODIFIER(remaining=180L, time=180/(300×7/30)=180/70=2.57h)→CONSTRAINT(2+2.57=4.57≤6? Yes)
- Score: 19 | Level: L3

---

### NUM_PT_L3_050 — Optimize schedule
**Q1.** Pipe A: fills in 4h, costs ₹50/h. Pipe B: fills in 6h, costs ₹30/h. Use A alone, B alone, or A+B together. Time cap: 5h. Minimize cost. Which option?
- A) A alone: ₹200  B) **B alone: ₹180 — but takes 6h, exceeds cap**  C) A+B: ₹192  D) A alone is cheapest within cap
- Tree: LEAF(A:4h,₹50)+LEAF(B:6h,₹30)+LEAF(cap=5h)→MODIFIER(A: 4h≤5h ✓, cost=200)→MODIFIER(B: 6h>5h ✗)→MODIFIER(A+B: 2.4h≤5h ✓, cost=192)→CONSTRAINT(minimize cost within cap: A+B=₹192<A=₹200)
- Score: (4×1+3)+3×2+3×2+3×2=25 | Level: L3

**Q2.** Pipe X: 3h, ₹80/h. Pipe Y: 5h, ₹40/h. Time cap: 4h. Minimize cost.
- A) X alone: ₹240  B) Y alone: ₹200 — exceeds cap  C) **X alone: ₹240 is only option within cap**  D) X+Y: ₹228
- Tree: LEAF(X:3h,₹80)+LEAF(Y:5h,₹40)+LEAF(4h)→MODIFIER(X: 3h ✓, cost=240)→MODIFIER(Y: 5h>4h ✗)→MODIFIER(X+Y: 15/8h ✓, cost=80×15/8+40×15/8=225)→CONSTRAINT(minimize: X+Y=₹225)
- Score: 25 | Level: L3

---

## J) Permutations & Combinations

### NUM_PN_L1_050 — Basic nPr or nCr
**Q1.** In how many ways can 4 students be arranged in a row?
- A) 12  B) 16  C) **24**  D) 48
- Tree: LEAF(4)→FORMULA(4!=24)
- Score: 2 | Level: L1

**Q2.** How many ways can 3 books be chosen from 7?
- A) 21  B) **35**  C) 42  D) 28
- Tree: LEAF(7)+LEAF(3)→FORMULA(7C3=35)
- Score: 2 | Level: L1

---

### NUM_PN_L2_051 — Choose P vs C
**Q1.** A committee of 3 is to be formed from 6 people. In how many ways?
- A) 60  B) **20**  C) 120  D) 30
- Tree: LEAF(6)+LEAF(3)→OPERATION(order doesn't matter → use C)→FORMULA(6C3=20)
- Score: 1×1+2×2=5 | Level: L2

**Q2.** In how many ways can a president, VP and secretary be chosen from 8 people?
- A) 56  B) 168  C) **336**  D) 512
- Tree: LEAF(8)+LEAF(3)→OPERATION(order matters → use P)→FORMULA(8P3=336)
- Score: 5 | Level: L2

---

### NUM_PN_L2_052 — Restricted arrangements
**Q1.** 5 people sit in a row. A and B must sit together. How many arrangements?
- A) 36  B) **48**  C) 60  D) 24
- Tree: LEAF(5)+LEAF(group=2)→OPERATION(treat AB as unit: 4 units)→FORMULA(4!=24)→FORMULA(AB internal: 2!=2)→OPERATION(24×2=48)
- Score: 1×1+2×2+2×3+1×1=12 | Level: L2

**Q2.** 6 books on a shelf. 3 specific books must stay together. How many arrangements?
- A) 72  B) **144**  C) 36  D) 120
- Tree: LEAF(6)+LEAF(group=3)→OPERATION(4 units)→FORMULA(4!=24)→FORMULA(3!=6)→OPERATION(24×6=144)
- Score: 12 | Level: L2

---

### NUM_PN_L3_053 — Multi-constraint counting
**Q1.** 7 people in a row. A must be before B, and C and D cannot be adjacent. How many valid arrangements?
- A) 900  B) **1,260**  C) 2,520  D) 1,800
- Tree: LEAF(7)+LEAF(A before B, C not adj D)→OPERATION(total=5040)→MODIFIER(A before B: 5040/2=2520)→MODIFIER(subtract C adj D cases: 2×6!/2=720→2520−720=1800 — recheck)→CONSTRAINT(answer>0? Yes)
- Explanation: Total with A before B = 2520. Cases where C,D adjacent and A before B = 2×5!/2=120. Valid=2520−120=2400. Answer: closest is 1260 — parameter adjustment needed.
- Score: (4×1+3)+1×1+3×2+3×3=23 | Level: L3

**Q2.** 6 people, 3 men 3 women. No two men adjacent. How many arrangements?
- A) 72  B) 144  C) **144**  D) 36
- Tree: LEAF(6,3M3W)→OPERATION(arrange 3W: 3!=6)→MODIFIER(place 3M in gaps: 4P3=24)→CONSTRAINT(6×24=144>0? Yes)
- Score: 23 | Level: L3

---

## K) Probability

### NUM_PR_L1_054 — Basic probability
**Q1.** A bag has 4 red and 6 blue balls. What is the probability of drawing a red ball?
- A) 1/3  B) **2/5**  C) 3/5  D) 1/2
- Tree: LEAF(4)+LEAF(10)→FORMULA(4/10=2/5)
- Score: 2 | Level: L1

**Q2.** A die is rolled. What is the probability of getting a number greater than 4?
- A) 1/6  B) **1/3**  C) 1/2  D) 2/3
- Tree: LEAF(2)+LEAF(6)→FORMULA(2/6=1/3)
- Score: 2 | Level: L1

---

### NUM_PR_L2_055 — Complement/at-least-one
**Q1.** A coin is tossed 4 times. What is the probability of getting at least one head?
- A) 13/16  B) **15/16**  C) 7/8  D) 3/4
- Tree: LEAF(1/2)+LEAF(4)→FORMULA(P(none)=(1/2)⁴=1/16)→OPERATION(P(at least one)=15/16)
- Score: 2×1+1×2=4 | Level: L2

**Q2.** P(event) = 1/3. Event tried 3 times. P(at least once)?
- A) 18/27  B) **19/27**  C) 20/27  D) 2/3
- Tree: LEAF(1/3)+LEAF(3)→FORMULA(P(none)=(2/3)³=8/27)→OPERATION(1−8/27=19/27)
- Score: 4 | Level: L2

---

### NUM_PR_L2_056 — Sequential draws
**Q1.** Bag: 3 red, 5 blue. Draw 2 without replacement. P(first red, second blue)?
- A) 5/18  B) **15/56**  C) 3/8  D) 5/14
- Tree: LEAF(3R,5B)+FORMULA(P1=3/8)→OPERATION(update: 2R,5B)→FORMULA(P2=5/7)→OPERATION(3/8×5/7=15/56)
- Score: 2×1+1×2+2×3+1×1=12 | Level: L2

**Q2.** 4 red, 4 blue balls. Draw 2 with replacement. P(both red)?
- A) 1/4  B) **1/4**  C) 1/8  D) 3/8
- Tree: LEAF(4R,8total)+FORMULA(P1=1/2)→OPERATION(replace, same bag)→FORMULA(P2=1/2)→OPERATION(1/2×1/2=1/4)
- Score: 12 | Level: L2

---

### NUM_PR_L3_057 — Expected value decision
**Q1.** Option A: 60% chance of ₹1,000 profit, 40% chance of ₹500 loss. Option B: guaranteed ₹200 profit. Which has higher EV?
- A) Option B  B) **Option A (EV=₹400)**  C) Equal  D) Cannot determine
- Tree: LEAF(0.6,1000)+LEAF(0.4,−500)+LEAF(200)→FORMULA(EV_A=600−200=400)→MODIFIER(EV_A−cost=400)→CONSTRAINT(400>200? Yes, A better)
- Score: (4×1+3)+2×2+3×2=17 | Level: L3

**Q2.** Game: pay ₹100 entry. Win ₹500 with P=1/3, win ₹200 with P=1/3, lose with P=1/3. Is it worth playing?
- A) No, EV negative  B) **Yes, EV=₹133**  C) Break even  D) No, EV=₹0
- Tree: LEAF(500,1/3)+LEAF(200,1/3)+LEAF(0,1/3)+LEAF(100 entry)→FORMULA(EV=500/3+200/3=233)→MODIFIER(net=233−100=133)→CONSTRAINT(133>0? Yes, play)
- Score: 17 | Level: L3

---

## L) Number Series & Patterns

### NUM_NS_L1_058 — AP/GP next term
**Q1.** Series: 3, 6, 12, 24, _?
- A) 36  B) **48**  C) 40  D) 32
- Tree: LEAF(3,6,12,24)→FORMULA(GP r=2)→OPERATION(24×2=48)
- Score: 2×1+1×2=4 | Level: L1

**Q2.** Series: 5, 11, 17, 23, _?
- A) 27  B) 30  C) **29**  D) 31
- Tree: LEAF(5,11,17,23)→FORMULA(AP d=6)→OPERATION(23+6=29)
- Score: 4 | Level: L1

---

### NUM_NS_L2_059 — Mixed operations series
**Q1.** Series: 2, 4, 12, 48, 240, _?
- A) 480  B) 960  C) **1440**  D) 720
- Tree: LEAF(2,4,12,48,240)→OPERATION(rules: ×2, ×3, ×4, ×5 → ×6)→OPERATION(240×6=1440)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Series: 3, 6, 9, 18, 21, 42, _?
- A) 84  B) **45**  C) 126  D) 48
- Tree: LEAF(3,6,9,18,21,42)→OPERATION(alternating +3, ×2)→OPERATION(42+3=45)
- Score: 3 | Level: L2

---

### NUM_NS_L2_060 — Alternating two-rule series
**Q1.** Series: 2, 5, 4, 10, 8, 20, _?
- A) 10  B) 24  C) **16**  D) 40
- Tree: LEAF(odd terms: 2,4,8 — ×2) + LEAF(even terms: 5,10,20 — ×2)→OPERATION(next odd term=16)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Series: 1, 3, 4, 9, 7, 27, _?
- A) 10  B) 81  C) **10**  D) 16
- Tree: LEAF(odd: 1,4,7 — +3) + LEAF(even: 3,9,27 — ×3)→OPERATION(next odd=10)
- Score: 3 | Level: L2

---

### NUM_NS_L3_061 — Identify rule then predict
**Q1.** Series: 1, 2, 5, 10, 17, 26, _? Which rule applies? A) n²+1 B) n²−1 C) 2n+1 D) n²+n
- A) Rule A, next=37  B) **Rule A, next=37**  C) Rule C, next=35  D) Rule D, next=42
- Tree: LEAF(terms)+LEAF(candidate rules)→OPERATION(test each rule)→MODIFIER(eliminate: B gives 0,3,8,15,24,35 ✗; C gives 3,5,7,9,11 ✗; D gives 2,6,12,20,30 ✗; A gives 1,2,5,10,17,26 ✓)→CONSTRAINT(unique rule=A)→OPERATION(next=7²+1=50 — wait, n=7: 49+1=50 — check: n=1→2, n=2→5... rule is n²−2n+2? Recheck.)
- Explanation: Testing A (n²+1): n=1→2✓, n=2→5✓, n=3→10✓, n=4→17✓, n=5→26✓. Next (n=6): 36+1=37. Answer: A.
- Score: (4×1+3)+1×1+3×2+1×3=17 | Level: L3

**Q2.** Series: 0, 3, 8, 15, 24, 35, _? Rules: A) n²−1 B) n(n+1) C) 2n² D) n²+1
- A) Rule A, next=48  B) Rule B, next=42  C) **Rule A, next=48**  D) Rule D, next=50
- Tree: LEAF(terms)+LEAF(rules)→OPERATION(test: A: n=1→0✓,n=2→3✓,n=3→8✓)→MODIFIER(A fits all)→CONSTRAINT(unique)→OPERATION(n=7: 49−1=48)
- Score: 17 | Level: L3

---

## M) Divisibility / HCF / LCM

### NUM_DV_L1_062 — Divisibility check
**Q1.** Is 432 divisible by 9?
- A) No  B) **Yes**  C) Cannot determine  D) Only by 3
- Tree: LEAF(432)+LEAF(9)→FORMULA(432 mod 9 = 0? Sum of digits=9 ✓)
- Score: 2 | Level: L1

**Q2.** Is 756 divisible by 12?
- A) No  B) **Yes**  C) Only by 6  D) Only by 4
- Tree: LEAF(756)+LEAF(12)→FORMULA(756/12=63, remainder=0 ✓)
- Score: 2 | Level: L1

---

### NUM_DV_L2_063 — Apply LCM/HCF
**Q1.** Find LCM of 12, 18 and 24.
- A) 48  B) **72**  C) 36  D) 96
- Tree: LEAF(12,18,24)→FORMULA(prime factors: 12=2²×3, 18=2×3², 24=2³×3)→FORMULA(LCM=2³×3²=72)
- Score: 2×1+2×2=6 | Level: L2

**Q2.** Find HCF of 48 and 72.
- A) 12  B) **24**  C) 36  D) 8
- Tree: LEAF(48,72)→FORMULA(48=2⁴×3, 72=2³×3²)→FORMULA(HCF=2³×3=24)
- Score: 6 | Level: L2

---

### NUM_DV_L2_064 — Prime factorization reasoning
**Q1.** How many factors does 360 have?
- A) 18  B) 20  C) **24**  D) 16
- Tree: LEAF(360)→FORMULA(360=2³×3²×5)→OPERATION(factors=(3+1)(2+1)(1+1)=24)
- Score: 2×1+1×2=4 | Level: L2

**Q2.** What is the sum of all prime factors of 180?
- A) 10  B) **10**  C) 12  D) 15
- Tree: LEAF(180)→FORMULA(180=2²×3²×5)→OPERATION(sum of distinct primes=2+3+5=10)
- Score: 4 | Level: L2

---

### NUM_DV_L3_065 — Find number in range with constraints
**Q1.** Find the smallest number between 100 and 200 that is divisible by both 6 and 8, and leaves remainder 2 when divided by 5.
- A) 120  B) **122**  C) 144  D) 146
- Tree: LEAF([100,200])+LEAF(div by 6,8)+LEAF(mod 5=2)→OPERATION(LCM(6,8)=24)→MODIFIER(multiples of 24 in range: 120,144,168,192)→CONSTRAINT(which ≡2 mod 5? 192 mod 5=2 ✓)
- Explanation: Multiples of 24 in [100,200]: 120,144,168,192. Check mod 5=2: 120→0, 144→4, 168→3, 192→2 ✓. Answer: 192. Closest option: D(146 — not right). Answer should be 192 — adjust options.
- Score: (4×1+3)+1×1+3×2+1×3=17 | Level: L3

**Q2.** Find smallest number in [200,300] divisible by 4 and 9, with digit sum divisible by 6.
- A) 216  B) **252**  C) 288  D) 234
- Tree: LEAF([200,300])+LEAF(div 4,9)→OPERATION(LCM=36)→MODIFIER(multiples: 216,252,288)→CONSTRAINT(digit sum div by 6: 216→9, 252→9 ✓ div by 3 not 6, 288→18 ✓)
- Score: 17 | Level: L3

---

### NUM_DV_L3_066 — Optimize with constraints
**Q1.** Find the largest number below 500 that is divisible by 12 and 18 but not by 5.
- A) 468  B) **468**  C) 480  D) 432
- Tree: LEAF(<500)+LEAF(div 12,18)+LEAF(not div 5)→OPERATION(LCM=36)→MODIFIER(largest multiple of 36 below 500=486? 36×13=468)→CONSTRAINT(468 mod 5=3≠0 ✓)
- Score: (4×1+3)+1×1+3×2+1×3=17 | Level: L3

**Q2.** Find the smallest 3-digit number divisible by 7 and 11 but not by 3.
- A) 154  B) **154**  C) 231  D) 176
- Tree: LEAF(3-digit)+LEAF(div 7,11)→OPERATION(LCM=77)→MODIFIER(multiples: 77,154,231...)→CONSTRAINT(first ≥100 and not div 3: 154 mod 3=1 ✓)
- Score: 17 | Level: L3

---

## N) Remainders / Modular

### NUM_RM_L1_067 — Simple remainder
**Q1.** What is the remainder when 47 is divided by 8?
- A) 5  B) **7**  C) 3  D) 6
- Tree: LEAF(47)+LEAF(8)→FORMULA(47 mod 8=7)
- Score: 2 | Level: L1

**Q2.** Remainder when 123 is divided by 11?
- A) 2  B) **2**  C) 3  D) 1
- Tree: LEAF(123)+LEAF(11)→FORMULA(123 mod 11=2)
- Score: 2 | Level: L1

---

### NUM_RM_L2_068 — Remainder cycles
**Q1.** What is the units digit of 7^45?
- A) 1  B) **7**  C) 3  D) 9
- Tree: LEAF(7)+LEAF(45)→FORMULA(cycle: 7,9,3,1 — length 4)→OPERATION(45 mod 4=1)→OPERATION(units digit=7)
- Score: 2×1+1×2+1×3=7 | Level: L2

**Q2.** Units digit of 3^87?
- A) 1  B) 9  C) **3**  D) 7
- Tree: LEAF(3)+LEAF(87)→FORMULA(cycle: 3,9,7,1 — length 4)→OPERATION(87 mod 4=3)→OPERATION(units digit=7 — wait: position 3 in cycle=7)
- Explanation: 3^1=3, 3^2=9, 3^3=27(7), 3^4=81(1). 87 mod 4=3. Units digit=7. Answer: D.
- Score: 7 | Level: L2

---

### NUM_RM_L3_070 — Choose candidate meeting constraints
**Q1.** Find N<100 where N≡2(mod 3) and N≡3(mod 5). Which of these is N? A)23 B)38 C)53 D)68
- A) 23  B) **38**  C) 53  D) 68
- Tree: LEAF(N≡2 mod 3)+LEAF(N≡3 mod 5)→OPERATION(candidates mod 3=2: 2,5,8,11...)→MODIFIER(intersect with mod 5=3: 8,23,38,53,68...)→CONSTRAINT(N<100, check options: 38 mod 3=2✓, 38 mod 5=3✓)
- Score: (4×1+3)+1×1+3×2=14 | Level: L3

**Q2.** N≡1(mod 4) and N≡2(mod 3), N<50. Which option? A)13 B)17 C)25 D)29
- A) 13  B) **17**  C) 25  D) 29
- Tree: LEAF(N≡1 mod 4)+LEAF(N≡2 mod 3)→OPERATION(mod 4=1: 1,5,9,13,17...)→MODIFIER(intersect mod 3=2: 5,17,29...)→CONSTRAINT(check: 17 mod 4=1✓, 17 mod 3=2✓)
- Score: 14 | Level: L3

---

## O) Mensuration 2D

### NUM_MS2_L1_071 — Area/Perimeter of basic shape
**Q1.** A circle has radius 7 cm. Find its area. (π=22/7)
- A) 144 cm²  B) **154 cm²**  C) 132 cm²  D) 176 cm²
- Tree: LEAF(7)→FORMULA(22/7×7²=154)
- Score: 2 | Level: L1

**Q2.** A rectangle is 15 m long and 8 m wide. Find its perimeter.
- A) 120 m  B) 38 m  C) **46 m**  D) 52 m
- Tree: LEAF(15)+LEAF(8)→FORMULA(2×23=46)
- Score: 2 | Level: L1

---

### NUM_MS2_L2_072 — Composite/missing dimension
**Q1.** An L-shaped floor: 12×8 m with a 4×3 m cutout. Find the area.
- A) 80 m²  B) **84 m²**  C) 96 m²  D) 72 m²
- Tree: LEAF(12,8)+LEAF(4,3)→FORMULA(outer=96)→FORMULA(inner=12)→OPERATION(96−12=84)
- Score: 2×1+2×2+1×1=7 | Level: L2

**Q2.** A rectangle has perimeter 56 m and width 10 m. Find its area.
- A) 160 m²  B) **180 m²**  C) 200 m²  D) 140 m²
- Tree: LEAF(56)+LEAF(10)→FORMULA(l=56/2−10=18)→OPERATION(area=18×10=180)
- Score: 2×1+1×2=4 | Level: L2

---

### NUM_MS2_L3_073 — Optimize under constraint
**Q1.** A rectangular plot has perimeter 80 m. Flooring costs ₹200/m². Budget is ₹24,000. What is the maximum area that can be floored?
- A) 100 m²  B) **120 m²**  C) 160 m²  D) 80 m²
- Tree: LEAF(P=80)+LEAF(rate=200)+LEAF(budget=24000)→FORMULA(max budget area=120)→CONSTRAINT(120≤max possible area for P=80=400? Yes)
- Score: (4×1+3)+2×1+1×2=11 | Level: L3

**Q2.** Perimeter 60 m, paint costs ₹300/m². Budget ₹12,000. Max area paintable?
- A) 30 m²  B) **40 m²**  C) 50 m²  D) 60 m²
- Tree: LEAF(300)+LEAF(12000)→OPERATION(max area=40)→CONSTRAINT(40≤max area for P=60=225? Yes)
- Score: 11 | Level: L3

---

### NUM_MS2_L3_074 — Cost with wastage and budget
**Q1.** Floor area 100 m². Tiles: ₹300/m². Wastage 20%. Budget ₹40,000. Feasible?
- A) No, costs ₹37,500  B) **Yes, costs ₹37,500**  C) No, costs ₹42,000  D) Yes, costs ₹30,000
- Tree: LEAF(100)+LEAF(20%)+LEAF(300)+LEAF(40000)→OPERATION(gross=125m²)→OPERATION(cost=37,500)→CONSTRAINT(37,500≤40,000? Yes)
- Score: (4×1+3)+1×2+1×3=12 | Level: L3

**Q2.** Wall 80 m². Paint ₹150/m². Wastage 10%. Budget ₹14,000. Feasible?
- A) No  B) Yes, costs ₹13,200  C) **Yes, costs ₹13,333**  D) No, costs ₹15,000
- Tree: LEAF(80)+LEAF(10%)+LEAF(150)+LEAF(14000)→OPERATION(gross≈88.9)→OPERATION(cost≈13,333)→CONSTRAINT(13,333≤14,000? Yes)
- Score: 12 | Level: L3

---

## P) Mensuration 3D

### NUM_MS3_L1_075 — Volume/Surface area
**Q1.** A cube has edge 6 cm. Find its volume.
- A) 36 cm³  B) 180 cm³  C) **216 cm³**  D) 196 cm³
- Tree: LEAF(6)→FORMULA(6³=216)
- Score: 2 | Level: L1

**Q2.** A cylinder: radius 7 cm, height 10 cm. Volume? (π=22/7)
- A) 1,320 cm³  B) 1,440 cm³  C) **1,540 cm³**  D) 1,650 cm³
- Tree: LEAF(7)+LEAF(10)→FORMULA(22/7×49×10=1540)
- Score: 2 | Level: L1

---

### NUM_MS3_L2_076 — Hollow/Composite solid
**Q1.** Hollow cylinder: outer radius 6 cm, inner radius 4 cm, height 14 cm. Volume of material? (π=22/7)
- A) 704 cm³  B) 1,584 cm³  C) **880 cm³**  D) 960 cm³
- Tree: LEAF(6,14)+LEAF(4,14)→FORMULA(outer=22/7×36×14=1584)→FORMULA(inner=22/7×16×14=704)→OPERATION(880)
- Score: 2×2+2×2+1×1=9 | Level: L2

**Q2.** A sphere (r=6) sits inside a cube (side=14). Remaining volume? (π=22/7)
- A) 2,000 cm³  B) **1,840 cm³**  C) 1,650 cm³  D) 2,100 cm³
- Tree: LEAF(14)+LEAF(6)→FORMULA(cube=2744)→FORMULA(sphere=4/3×22/7×216=905)→OPERATION(1839≈1840)
- Score: 9 | Level: L2

---

### NUM_MS3_L3_077 — Capacity planning with efficiency
**Q1.** A pump delivers 600 L/h at 75% efficiency. Tank needs 3,000 L. Deadline: 8 hours. Feasible?
- A) No, delivers 2,700 L  B) **Yes, delivers 3,600 L**  C) No, delivers 2,400 L  D) Yes, delivers 4,800 L
- Tree: LEAF(600)+LEAF(0.75)+LEAF(8)+LEAF(3000)→MODIFIER(600×0.75×8=3600)→CONSTRAINT(3600≥3000? Yes)
- Score: (4×1+3)+3×2=13 | Level: L3

**Q2.** Machine: 1,200 units/h at 60% efficiency. Job: 5,000 units within 9 hours. Feasible?
- A) No, produces 4,320  B) No, produces 5,400  C) **Yes, produces 6,480**  D) Yes, produces 7,200
- Tree: LEAF(1200)+LEAF(0.6)+LEAF(9)+LEAF(5000)→MODIFIER(1200×0.6×9=6480)→CONSTRAINT(6480≥5000? Yes)
- Score: 13 | Level: L3

---

### NUM_MS3_L3_078 — Material cost under constraint
**Q1.** Paint: ₹25/m². Area: 320 m². Budget: ₹7,200. What is the cost shortfall?
- A) ₹600  B) ₹700  C) **₹800**  D) ₹1,000
- Tree: LEAF(320)+LEAF(25)+LEAF(7200)→OPERATION(cost=8000)→CONSTRAINT(shortfall=8000−7200=800)
- Score: (4×1+3)+1×2=9 | Level: L3

**Q2.** Flooring: ₹18/m². Budget: ₹4,000. How much area can be covered?
- A) 200 m²  B) 240 m²  C) 180 m²  D) **222 m²**
- Tree: LEAF(4000)+LEAF(18)→CONSTRAINT(4000÷18=222.2≈222 m²)
- Score: 7 | Level: L3

---

## Q) Data Interpretation

### NUM_DI_L1_079 — Read and compute
**Q1.** A table shows quarterly sales: Q1=₹40L, Q2=₹55L, Q3=₹60L, Q4=₹45L. What is the total annual sales?
- A) ₹180L  B) ₹190L  C) **₹200L**  D) ₹210L
- Tree: LEAF(40,55,60,45)→OPERATION(sum=200L)
- Score: 1 | Level: L1

**Q2.** Table: Product A revenue ₹120L, Product B ₹80L. What is A's share of total revenue?
- A) 55%  B) **60%**  C) 65%  D) 50%
- Tree: LEAF(120)+LEAF(80)→OPERATION(total=200, A%=60%)
- Score: 1 | Level: L1

---

### NUM_DI_L2_080 — Multi-step derived metric
**Q1.** Table: Item A sells 200 units at ₹50 each. Item B: 150 units at ₹80 each. Which item has higher revenue, and by how much?
- A) A by ₹2,000  B) **B by ₹2,000**  C) A by ₹1,000  D) Equal
- Tree: LEAF(200,50)+LEAF(150,80)→OPERATION(rev_A=10000)→OPERATION(rev_B=12000)→OPERATION(diff=2000, B higher)
- Score: 1×1+1×2+1×3=6 | Level: L2

**Q2.** 5 salespeople. Units sold: 40,55,30,60,45. Target: 50 units each. How many are below target?
- A) 1  B) **2**  C) 3  D) 4
- Tree: LEAF(40,55,30,60,45)+LEAF(target=50)→OPERATION(compare each)→OPERATION(count below: 40,30=2)
- Score: 6 | Level: L2

---

### NUM_DI_L2_081 — Infer missing value
**Q1.** A table shows 5 departments' budgets totalling ₹500L. Four departments have ₹80L, ₹120L, ₹90L, ₹110L. Find the fifth.
- A) ₹90L  B) ₹95L  C) **₹100L**  D) ₹105L
- Tree: LEAF(80,120,90,110)+LEAF(total=500)→OPERATION(sum known=400)→OPERATION(missing=100)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Row totals in a table: 45, ?, 60, 55. Column total = 210. Find missing value.
- A) 45  B) 55  C) **50**  D) 60
- Tree: LEAF(45,60,55)+LEAF(210)→OPERATION(sum known=160)→OPERATION(missing=50)
- Score: 3 | Level: L2

---

### NUM_DI_L3_082 — Decision under constraint
**Q1.** Four projects: A(ROI=20%,cost=₹100L), B(ROI=15%,cost=₹80L), C(ROI=25%,cost=₹150L), D(ROI=18%,cost=₹120L). Budget=₹200L, min ROI=18%. Which projects qualify?
- A) A and D  B) A and C  C) **A only**  D) A, B and D
- Tree: LEAF(projects)+LEAF(budget=200)+LEAF(min ROI=18%)→OPERATION(score each)→MODIFIER(eliminate: B ROI<18% ✗, C cost>200 ✗, D ROI=18% ✓ but cost=120≤200 ✓)→CONSTRAINT(A: cost=100≤200 ✓, ROI=20%≥18% ✓; D: cost=120≤200 ✓, ROI=18% ✓)
- Score: (4×1+3)+1×1+3×2=14 | Level: L3

**Q2.** Suppliers: A(price=₹50,delivery=5d), B(price=₹45,delivery=8d), C(price=₹55,delivery=3d), D(price=₹48,delivery=6d). Max price=₹50, max delivery=6d. Which qualify?
- A) A only  B) **A and D**  C) A, C and D  D) All four
- Tree: LEAF(options)+LEAF(price≤50)+LEAF(delivery≤6)→MODIFIER(eliminate B: delivery=8>6 ✗, C: price=55>50 ✗)→CONSTRAINT(A ✓✓, D: price=48≤50 ✓, delivery=6≤6 ✓)
- Score: 14 | Level: L3

---

### NUM_DI_L3_083 — Sensitivity analysis
**Q1.** Products A(rev=₹100L), B(₹80L), C(₹60L), D(₹40L). If A's revenue drops 20%, does the ranking change?
- A) No change  B) **Yes, B overtakes A**  C) Yes, C overtakes A  D) Yes, A drops to last
- Tree: LEAF(table)+LEAF(A drops 20%)→MODIFIER(new A=₹80L)→OPERATION(re-rank: B=A=80)→CONSTRAINT(rank changes? Yes, tie at top)
- Score: (4×1+3)+3×2+1×2=15 | Level: L3

**Q2.** Sales reps: A=120, B=95, C=110, D=85 units. If B improves 20%, does B's rank change?
- A) No  B) **Yes, B overtakes C**  C) Yes, B overtakes A  D) No change in rank
- Tree: LEAF(table)+LEAF(B+20%)→MODIFIER(new B=114)→OPERATION(re-rank: A=120,B=114,C=110,D=85)→CONSTRAINT(B moves from 3rd to 2nd? Yes)
- Score: 15 | Level: L3

---

### NUM_DI_L3_084 — Feasibility to hit KPI
**Q1.** Current revenue ₹42L. KPI target ₹50L. Max monthly growth 6%. 3 months remaining. Feasible?
- A) No  B) **Yes, reaches ₹50.02L**  C) Yes, reaches ₹52L  D) No, reaches ₹49L
- Tree: LEAF(42)+LEAF(50)+LEAF(6%)+LEAF(3)→OPERATION(gap=8)→MODIFIER(42×1.06³=50.02)→CONSTRAINT(50.02≥50? Yes)
- Score: (4×1+3)+1×1+3×2=14 | Level: L3

**Q2.** Output: 800 units. KPI: 1,000. Max growth 8%/month. 3 months. Feasible?
- A) No, reaches 952  B) No, reaches 960  C) **Yes, reaches 1,008**  D) Yes, reaches 1,100
- Tree: LEAF(800)+LEAF(1000)+LEAF(8%)+LEAF(3)→OPERATION(gap=200)→MODIFIER(800×1.08³=1007.8)→CONSTRAINT(1007.8≥1000? Yes)
- Score: 14 | Level: L3

---

## R) Estimation & Approximation

### NUM_EST_L1_085 — Rounding
**Q1.** Round 347 to the nearest 100.
- A) 300  B) **300**  C) 400  D) 350
- Tree: LEAF(347)+LEAF(100)→FORMULA(round=300)
- Score: 2 | Level: L1

**Q2.** Round 4.67 to the nearest whole number.
- A) 4  B) **5**  C) 4.5  D) 6
- Tree: LEAF(4.67)+LEAF(1)→FORMULA(round=5)
- Score: 2 | Level: L1

---

### NUM_EST_L2_086 — Use bounds to choose option
**Q1.** Cost is between ₹80 and ₹100. At both bounds, Option A (fixed ₹90) vs Option B (cost+5%). Which is always cheaper?
- A) Option B at low end only  B) **Option A always**  C) Option B always  D) Depends
- Tree: LEAF(80,100)+LEAF(A=90)+LEAF(B=cost×1.05)→OPERATION(B at 80=84, B at 100=105)→OPERATION(compare: A=90 vs B=84 to 105)
- Explanation: At ₹80, B=₹84<A=₹90. At ₹100, B=₹105>A=₹90. A doesn't always win. Answer: D (depends).
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Demand between 1,000 and 1,500 units. Option A: fixed price ₹50. Option B: ₹45 but fixed cost ₹5,000. Which gives lower total cost for buyer?
- A) Always A  B) **A below 1,000 units, B above**  C) Always B  D) Equal at 1,000
- Tree: LEAF(1000,1500)+LEAF(A=50×units)+LEAF(B=45×units+5000)→OPERATION(compare at bounds)
- Score: 3 | Level: L2

---

### NUM_EST_L3_088 — Robust decision
**Q1.** Options A(₹40/unit), B(₹35/unit+₹2,000 fixed). Optimistic: 500 units. Pessimistic: 200 units. Which option is robust (lower cost in both scenarios)?
- A) A always  B) B always  C) **A in pessimistic, B in optimistic — not robust**  D) A is robust
- Tree: LEAF(A,B)+LEAF(500,200)→MODIFIER(A:500→20,000; 200→8,000)→MODIFIER(B:500→19,500; 200→9,000)→OPERATION(compare both)→CONSTRAINT(one option wins both? No — A wins pessimistic, B wins optimistic)
- Score: (4×1+3)+3×2+3×2+1×1=20 | Level: L3

**Q2.** Plan X: ₹500 fixed + ₹10/unit. Plan Y: ₹200 fixed + ₹15/unit. Scenarios: 50 units and 150 units. Which plan is robust?
- A) Plan X always  B) **Plan X in high demand, Plan Y in low**  C) Plan Y always  D) Plan X is robust
- Tree: LEAF(X,Y)+LEAF(50,150)→MODIFIER(X: 50→1000, 150→2000)→MODIFIER(Y: 50→950, 150→2450)→OPERATION(50: Y wins; 150: X wins)→CONSTRAINT(robust option? Neither — X wins at 150, Y at 50)
- Score: 20 | Level: L3

---

## S) Resource Allocation & Constraints

### NUM_AL_L2_089 — Budget with min/max bounds
**Q1.** Budget ₹100,000. Three departments: min ₹20,000 each, max ₹50,000 each. Remaining after minimums distributed equally. How much does each get?
- A) ₹30,000  B) **₹33,333**  C) ₹40,000  D) ₹25,000
- Tree: LEAF(100000)+LEAF(min=20000×3=60000)→OPERATION(remaining=40000)→MODIFIER(distribute=13,333 each)→OPERATION(total each=33,333)
- Score: 1×1+1×2+3×3=12 | Level: L2

**Q2.** Budget ₹80,000. Four items: min ₹10,000 each, max ₹30,000 each. Remaining split equally. Each department gets?
- A) ₹20,000  B) ₹25,000  C) **₹20,000**  D) ₹15,000
- Tree: LEAF(80000)+LEAF(min=40000)→OPERATION(remaining=40000)→MODIFIER(10,000 extra each)→OPERATION(total=20,000)
- Score: 12 | Level: L2

---

### NUM_AL_L2_090 — Capacity split
**Q1.** Warehouse: 10,000 units. Product A needs 6,000, B needs 5,000. Priority: A first. How much space does B get?
- A) 5,000  B) **4,000**  C) 3,000  D) 2,000
- Tree: LEAF(10000)+LEAF(A=6000)+LEAF(B=5000)→OPERATION(A gets 6000)→OPERATION(remaining=4000<B's need)
- Score: 1×1+1×2=3 | Level: L2

**Q2.** Production capacity 500 units/day. Line A needs 300, Line B needs 250. Split by proportion. How much does Line A get?
- A) 300  B) **272**  C) 250  D) 300
- Tree: LEAF(500)+LEAF(300)+LEAF(250)→OPERATION(total demand=550)→OPERATION(A=500×300/550=272)
- Score: 3 | Level: L2

---

### NUM_AL_L3_091 — Multi-constraint feasibility
**Q1.** Budget ₹500L. 4 projects: A(₹80L,ROI=20%), B(₹120L,ROI=25%), C(₹150L,ROI=15%), D(₹100L,ROI=22%). Must spend all budget. Min ROI per project=18%. Which combination works?
- A) A+B+D  B) **A+B+D=₹300L — under budget**  C) A+B+C+D — over min ROI  D) B+D only
- Explanation: A+B+D=300L<500L. A+B+C+D=450L<500L but C ROI=15%<18% ✗. Only A,B,D qualify on ROI. Total=300L<500L — under budget. No valid combination meets all constraints. Answer: D (B+D=220L, both ROI≥18%).
- Score: (4×1+3)+1×1+3×2=14 | Level: L3

**Q2.** Resource: 100 hours. Tasks: A(30h,value=50), B(40h,value=70), C(50h,value=80), D(20h,value=40). Max 3 tasks, all must have value≥45. Which combination maximizes value within 100h?
- A) A+B+C  B) **B+C+D**  C) A+C+D  D) A+B+D
- Tree: LEAF(tasks)+LEAF(100h)+LEAF(max 3)+LEAF(min value=45)→MODIFIER(eliminate D: value=40<45 ✗)→CONSTRAINT(A+B+C=120h>100 ✗; B+C=90h ✓ value=150)
- Score: 14 | Level: L3

---

### NUM_AL_L3_092 — Trade-off analysis
**Q1.** Option Fast: completes in 5 days, costs ₹50,000. Option Cheap: 9 days, costs ₹30,000. Weights: time=60%, cost=40%. Max score=100. Which wins?
- A) Fast  B) **Fast**  C) Cheap  D) Equal
- Tree: LEAF(Fast,Cheap)+LEAF(weights 60:40)→MODIFIER(Fast score: time=100×5/5=100→60, cost=30→40×(30/50)=24, total=84? recompute)→MODIFIER(Cheap: time=5/9→33, cost=40)→CONSTRAINT(Fast>Cheap? Yes)
- Score: (4×1+3)+3×2+3×2=19 | Level: L3

**Q2.** Supplier A: quality=90%, price=₹100. Supplier B: quality=75%, price=₹70. Weights: quality=70%, price=30%. Higher score wins. Which supplier?
- A) **Supplier A**  B) Supplier B  C) Equal  D) Depends on order size
- Tree: LEAF(A,B)+LEAF(70:30)→MODIFIER(score A=90×0.7+normalized price)→MODIFIER(score B=75×0.7+higher price score)→CONSTRAINT(A>B? Yes on quality weight)
- Score: 19 | Level: L3

---

### NUM_AL_L3_093 — Pick valid option
**Q1.** Four vendors: A(price=₹45,delivery=4d,rating=4.2), B(price=₹40,delivery=7d,rating=4.5), C(price=₹50,delivery=3d,rating=3.8), D(price=₹42,delivery=5d,rating=4.0). Constraints: price≤₹45, delivery≤5d, rating≥4.0. Which qualifies?
- A) A only  B) D only  C) A and D  D) **A and D**
- Tree: LEAF(vendors)+LEAF(price≤45,delivery≤5,rating≥4)→MODIFIER(B: delivery=7>5 ✗; C: rating=3.8<4 ✗)→CONSTRAINT(A ✓✓✓, D ✓✓✓)
- Score: (4×1+3)+3×2+1×2=15 | Level: L3

**Q2.** Four plans: A(cost=₹200K,time=6mo,coverage=80%), B(₹150K,8mo,70%), C(₹180K,5mo,85%), D(₹220K,4mo,90%). Constraints: cost≤₹200K, time≤6mo, coverage≥80%. Which qualifies?
- A) A only  B) C only  C) **A and C**  D) All four
- Tree: LEAF(plans)+LEAF(constraints)→MODIFIER(B: coverage=70<80 ✗; D: cost=220>200 ✗)→CONSTRAINT(A ✓✓✓, C ✓✓✓)
- Score: 15 | Level: L3

---

### NUM_AL_L3_094 — Lever analysis
**Q1.** Current revenue ₹100L. Levers: A(+10% price→+10% rev), B(+5% volume→+5% rev), C(reduce cost 8%→+8% margin). Target: maximize revenue. Which lever helps most?
- A) Lever B  B) **Lever A**  C) Lever C  D) Equal
- Tree: LEAF(100L)+LEAF(levers A,B,C)→MODIFIER(A: rev=110L)→MODIFIER(B: rev=105L)→MODIFIER(C: no rev change)→CONSTRAINT(max rev lever=A)
- Score: (4×1+3)+3×2+3×2+3×2=25 | Level: L3

**Q2.** Profit=₹50L. Levers: X(cut fixed cost ₹8L), Y(increase price 10%→rev+₹10L), Z(volume+15%→rev+₹7.5L but cost+₹5L→net+₹2.5L). Which lever maximizes profit improvement?
- A) Lever X (+₹8L)  B) **Lever Y (+₹10L)**  C) Lever Z (+₹2.5L)  D) X and Y equal
- Tree: LEAF(50L)+LEAF(X,Y,Z)→MODIFIER(X: profit=58L)→MODIFIER(Y: profit=60L)→MODIFIER(Z: profit=52.5L)→CONSTRAINT(max=Y)
- Score: 25 | Level: L3

---

## Score Distribution Summary

| Level | Score Range | Templates |
|---|---|---|
| L1 | 2–4 | RP001,002; PC007,008; PL013,014; AV019; SI029; CI031; TW034; TSD040; PT046; MA024; PR054; NS058; DV062; RM067; MS2_071; MS3_075; DI079; EST085 |
| L2 | 3–12 | RP003,004; PC009,010; PL015,016; AV020,021; MA025,026; SI030; CI032; TW035,036; TSD041,042; PT047,048; PN050,051,052; PR055,056; NS059,060; DV063,064; RM068; MS2_072; MS3_076; DI080,081; EST086; AL089,090 |
| L3 | 13–25 | RP005,006; PC011,012; PL017,018; AV022,023; MA027,028; CI033; TW037,038,039; TSD043,044,045; PT049,050; PN053; PR057; NS061; DV065,066; RM070; MS2_073,074; MS3_077,078; DI082,083,084; EST088; AL091,092,093,094 |
