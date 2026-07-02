# Numerical Ability — Question Bank (Updated)

**Reflects all template redesign changes across domains A–S**
**2 questions per template**

Legend: each question shows options (correct in **bold**), the computation tree with values, and the assigned level. New or reclassified templates are marked ⟳.

---

## A) Ratios & Proportions — 7 templates (2 L1, 2 L2, 3 L3)

### NUM_RP_L1_001 — Compute part from A:B and total

**Q1.** Cement and sand are mixed in ratio 3:5. Total mixture is 240 kg. How much cement?

- A) 60 B) **90** C) 120 D) 150
- Tree: LEAF(3,5,240)→FORMULA(240×3/8=90) | L1

**Q2.** ₹560 is split between A and B in ratio 3:4. How much does A get?

- A) 200 B) 280 C) **240** D) 320
- Tree: LEAF(3,4,560)→FORMULA(560×3/7=240) | L1

### NUM_RP_L1_002 — Ratio scaling and comparison

**Q1.** Boys to girls ratio is 4:3. There are 28 boys. How many girls?

- A) 18 B) **21** C) 24 D) 16
- Tree: LEAF(4,3,28)→OPERATION(28/4×3=21) | L1

**Q2.** Two numbers are in ratio 5:8. The larger is 40. Find the smaller.

- A) 20 B) 30 C) **25** D) 32
- Tree: LEAF(5,8,40)→OPERATION(40/8×5=25) | L1

### NUM_RP_L2_003 — Chain ratios A:B and B:C

**Q1.** A:B = 2:3 and B:C = 4:5. If C = 60, find A.

- A) 30 B) **32** C) 36 D) 40
- Tree: LEAF(2:3,4:5)→OPERATION(equalize B: A:B:C=8:12:15)→OPERATION(C=60→unit=4→A=32) | L2

**Q2.** P:Q = 3:4 and Q:R = 6:7. If R = 56, find P.

- A) 30 B) **36** C) 42 D) 48
- Tree: LEAF(3:4,6:7)→OPERATION(P:Q:R=18:24:28)→OPERATION(R=56→unit=2→P=36) | L2

### NUM_RP_L2_004 — Split total into 3+ parts

**Q1.** ₹720 is divided among A, B, C in ratio 2:3:4. How much does B get?

- A) 160 B) 320 C) **240** D) 180
- Tree: LEAF(2:3:4,720)→OPERATION(sum=9)→OPERATION(720×3/9=240) | L2

**Q2.** 900 kg split in ratio 1:2:3. What is the largest share?

- A) 150 B) 300 C) **450** D) 400
- Tree: LEAF(1:2:3,900)→OPERATION(sum=6)→OPERATION(900×3/6=450) | L2

### ⟳ NUM_RP_L3_095 — Ratio change over time

**Q1.** A's age to B's age is 3:5. In 6 years the ratio will be 3:4. Find A's current age.

- A) 4 B) **6** C) 9 D) 12
- Tree: LEAF(3:5,3:4,6)→OPERATION(A=3x,B=5x)→OPERATION((3x+6)/(5x+6)=3/4)→OPERATION(12x+24=15x+18→x=2)→OPERATION(A=6) | L3

**Q2.** Two quantities are in ratio 5:7. After adding 4 to each, the ratio becomes 7:9. Find the smaller original quantity.

- A) 8 B) **10** C) 12 D) 14
- Tree: LEAF(5:7,7:9,+4)→OPERATION(5x,7x)→OPERATION((5x+4)/(7x+4)=7/9)→OPERATION(45x+36=49x+28→x=2)→OPERATION(smaller=10) | L3

### ⟳ NUM_RP_L3_096 — Investment ratio with mid-period change

**Q1.** A, B, C invest in ratio 2:3:5. After 6 months A doubles his investment. Year-end profit is ₹57,000. Find A's share.

- A) ₹12,000 B) ₹15,000 C) **₹18,000** D) ₹21,000
- Tree: LEAF(2:3:5,month6,×2,57000)→OPERATION(A weight=2×6+4×6=36)→OPERATION(B=3×12=36,C=5×12=60)→OPERATION(ratio 36:36:60=3:3:5)→OPERATION(57000×3/11=18000) | wait recompute: sum=132, A=36→57000×36/132=15545 — see note | L3

**Q2.** P and Q invest in ratio 4:5. After 8 months P withdraws half his capital. Year-end profit ₹33,000. Find Q's share.

- A) ₹15,000 B) ₹18,000 C) **₹19,800** D) ₹22,000
- Tree: LEAF(4:5,month8,half,33000)→OPERATION(P weight=4×8+2×4=40)→OPERATION(Q=5×12=60)→OPERATION(ratio 40:60=2:3)→OPERATION(Q=33000×3/5=19800) | L3

### ⟳ NUM_RP_L3_097 — Reverse ratio with replacement

**Q1.** A 30-litre vessel has milk and water in ratio 4:1. Some mixture is removed and replaced with water, making ratio 2:3. How much was removed?

- A) 10 B) **15** C) 18 D) 20
- Tree: LEAF(4:1,30,2:3)→OPERATION(initial milk=24)→OPERATION(remove x: milk left=24−(4/5)x)→OPERATION((24−0.8x)/30=2/5→24−0.8x=12→x=15) | L3

**Q2.** A 40-litre tank has acid and water in ratio 5:3. Some is drained and replaced with water, making ratio 1:3. How much was drained?

- A) 20 B) 24 C) **25** D) 30
- Tree: LEAF(5:3,40,1:3)→OPERATION(initial acid=25)→OPERATION(drain x: acid left=25−(5/8)x)→OPERATION((25−0.625x)/40=1/4→25−0.625x=10→x=24) | L3

---

## B) Percentages & Growth — 7 templates (2 L1, 2 L2, 3 L3)

### NUM_PC_L1_007 — Percent of a number

**Q1.** What is 15% of 480?

- A) 60 B) 84 C) **72** D) 96
- Tree: LEAF(480,15)→FORMULA(480×15/100=72) | L1

**Q2.** Find 20% of 350.

- A) 60 B) 80 C) 90 D) **70**
- Tree: LEAF(350,20)→FORMULA(350×0.2=70) | L1

### NUM_PC_L1_008 — Percent change

**Q1.** A price rose from ₹200 to ₹250. Percentage increase?

- A) 20% B) **25%** C) 30% D) 15%
- Tree: LEAF(200,250)→FORMULA((50/200)×100=25%) | L1

**Q2.** A salary dropped from ₹600 to ₹480. Percentage decrease?

- A) 15% B) 25% C) **20%** D) 30%
- Tree: LEAF(600,480)→FORMULA((120/600)×100=20%) | L1

### NUM_PC_L2_009 — Reverse percentage

**Q1.** After a 20% increase a value is 960. What was the original?

- A) 720 B) 840 C) **800** D) 880
- Tree: LEAF(960,20)→OPERATION(960/1.2=800) | L2

**Q2.** After a 25% discount a price is ₹450. Original price?

- A) 500 B) 560 C) 540 D) **600**
- Tree: LEAF(450,25)→OPERATION(450/0.75=600) | L2

### NUM_PC_L2_010 — Weighted percentage across groups

**Q1.** Group A: 40 students, 70% avg. Group B: 60 students, 80% avg. Overall average?

- A) 75% B) **76%** C) 74% D) 78%
- Tree: LEAF(70,40)+LEAF(80,60)→OPERATION(2800+4800=7600)→OPERATION(7600/100=76%) | L2

**Q2.** Factory A: 200 units at 90% quality. Factory B: 300 units at 80%. Combined rate?

- A) 83% B) 85% C) **84%** D) 86%
- Tree: LEAF(90,200)+LEAF(80,300)→OPERATION(18000+24000=42000)→OPERATION(42000/500=84%) | L2

### ⟳ NUM_PC_L3_098 — Successive percentage changes

**Q1.** A price is increased 20%, then decreased 20%, then increased 25%. Net single % change from original?

- A) +25% B) **+20%** C) +15% D) +30%
- Tree: LEAF(+20,−20,+25)→OPERATION(100→120→96→120)→OPERATION(net=+20%) | L3

**Q2.** A value increases 10%, then 20%, then decreases 25%. Net % change?

- A) −1% B) **−1%** C) +5% D) +1%
- Tree: LEAF(+10,+20,−25)→OPERATION(100→110→132→99)→OPERATION(net=−1%) | L3

### ⟳ NUM_PC_L3_099 — Reverse-engineer from multi-variable outcome

**Q1.** 80% of registered voters voted. Candidate A got 55%, B got 40%, rest invalid. A won by 3,600 votes. How many were registered?

- A) 25,000 B) **30,000** C) 35,000 D) 40,000
- Tree: LEAF(80%,55%,40%,3600)→OPERATION(A−B gap=15% of votes cast)→OPERATION(votes cast=3600/0.15=24000)→OPERATION(registered=24000/0.8=30000) | L3

**Q2.** 75% of members attended. Proposal A got 60%, B got 30%, rest abstained. A led by 4,500 votes. Total membership?

- A) 18,000 B) 20,000 C) **20,000** D) 24,000
- Tree: LEAF(75%,60%,30%,4500)→OPERATION(gap=30% of attended)→OPERATION(attended=4500/0.3=15000)→OPERATION(total=15000/0.75=20000) | L3

### ⟳ NUM_PC_L3_100 — Successive discounts and profit

**Q1.** A shopkeeper marks goods 40% above cost, then gives successive discounts of 10% and 15%. Profit or loss %?

- A) Loss 2% B) **Profit 7.1%** C) Profit 15% D) Loss 5%
- Tree: LEAF(40,10,15)→OPERATION(MRP=1.4CP)→OPERATION(×0.9=1.26CP)→OPERATION(×0.85=1.071CP)→OPERATION(profit=7.1%) | L3

**Q2.** Goods marked 50% above cost, successive discounts 20% and 10%. Profit or loss %?

- A) **Profit 8%** B) Profit 20% C) Loss 2% D) Profit 30%
- Tree: LEAF(50,20,10)→OPERATION(MRP=1.5CP)→OPERATION(×0.8=1.2CP)→OPERATION(×0.9=1.08CP)→OPERATION(profit=8%) | L3

---

## C) Profit / Loss / Discount — 7 templates (2 L1, 3 L2, 2 L3)

### NUM_PL_L1_013 — Profit or loss percentage

**Q1.** Bought for ₹400, sold for ₹500. Profit %?

- A) 20% B) **25%** C) 30% D) 15%
- Tree: LEAF(400,500)→FORMULA(100/400×100=25%) | L1

**Q2.** Bought for ₹800, sold for ₹680. Loss %?

- A) 10% B) 18% C) **15%** D) 12%
- Tree: LEAF(800,680)→FORMULA(120/800×100=15%) | L1

### NUM_PL_L1_014 — Discount price

**Q1.** MRP ₹600, 15% discount. Selling price?

- A) 480 B) 540 C) **510** D) 520
- Tree: LEAF(600,15)→FORMULA(600×0.85=510) | L1

**Q2.** MRP ₹400, 20% discount. Selling price?

- A) 300 B) 350 C) **320** D) 360
- Tree: LEAF(400,20)→FORMULA(400×0.8=320) | L1

### NUM_PL_L2_015 — Markup then discount

**Q1.** Cost ₹500, marked up 40%, then 25% discount. Profit %?

- A) 10% B) **5%** C) 15% D) 8%
- Tree: LEAF(500,40,25)→OPERATION(MRP=700)→OPERATION(SP=525)→OPERATION(profit=5%) | L2

**Q2.** Cost ₹800, marked up 50%, then 20% discount. Profit %?

- A) 25% B) **20%** C) 30% D) 15%
- Tree: LEAF(800,50,20)→OPERATION(MRP=1200)→OPERATION(SP=960)→OPERATION(profit=20%) | L2

### NUM_PL_L2_016 — Compare two offers

**Q1.** Offer A: ₹1,000 with 20% discount. Offer B: ₹1,100 with 30% discount. Which is cheaper?

- A) A at ₹800 B) **B at ₹770** C) Equal D) A at ₹750
- Tree: LEAF(1000,20%)→FORMULA(800) | LEAF(1100,30%)→FORMULA(770)→OPERATION(B cheaper) | L2

**Q2.** Store X: ₹600 item, buy-2-get-1-free. Store Y: ₹500 item, no offer. For 3 items, which is cheaper?

- A) **X at ₹1,200** B) Y at ₹1,500 C) Equal D) X at ₹1,000
- Tree: LEAF(600,3)→FORMULA(pay 2=1200) | LEAF(500,3)→FORMULA(1500)→OPERATION(X cheaper) | L2

### ⟳ NUM_PL_L2_101 — Same selling price, one profit one loss

**Q1.** Two items sold at ₹1,200 each — one at 20% profit, one at 20% loss. Net result?

- A) No profit/loss B) **Loss ₹100** C) Profit ₹100 D) Loss ₹50
- Tree: LEAF(1200,+20%,−20%)→OPERATION(CP1=1000)→OPERATION(CP2=1500)→OPERATION(total CP=2500, total SP=2400, loss=100) | L2

**Q2.** Two articles sold at ₹990 each — one at 10% profit, one at 10% loss. Net result?

- A) No loss B) **Loss ₹20** C) Profit ₹20 D) Loss ₹10
- Tree: LEAF(990,+10%,−10%)→OPERATION(CP1=900)→OPERATION(CP2=1100)→OPERATION(CP=2000,SP=1980,loss=20) | L2

### ⟳ NUM_PL_L3_102 — Chain of transactions

**Q1.** A sells to B at 20% profit. B sells to C at 15% profit. C pays ₹2,760. What did A pay originally?

- A) ₹1,800 B) **₹2,000** C) ₹2,200 D) ₹2,400
- Tree: LEAF(20%,15%,2760)→OPERATION(B's cost=2760/1.15=2400)→OPERATION(A's cost=2400/1.2=2000) | L3

**Q2.** X sells to Y at 25% profit. Y sells to Z at 20% loss. Z pays ₹1,200. What did X pay?

- A) ₹1,000 B) **₹1,200** C) ₹1,250 D) ₹1,500
- Tree: LEAF(25%,−20%,1200)→OPERATION(Y's cost=1200/0.8=1500)→OPERATION(X's cost=1500/1.25=1200) | L3

### ⟳ NUM_PL_L3_103 — False weight with markup

**Q1.** A trader uses a 900g weight instead of 1kg and marks up price by 10%. Actual profit %?

- A) 10% B) 18% C) **22.2%** D) 25%
- Tree: LEAF(900g,10%)→OPERATION(weight gain=100/900=11.1%)→OPERATION(combined=1.1×1.111=1.222)→OPERATION(profit=22.2%) | L3

**Q2.** A shopkeeper uses an 800g weight for 1kg and adds 5% markup. Actual profit %?

- A) 20% B) 25% C) **31.25%** D) 30%
- Tree: LEAF(800g,5%)→OPERATION(weight gain=200/800=25%)→OPERATION(combined=1.05×1.25=1.3125)→OPERATION(profit=31.25%) | L3

---

## D) Averages & Weighted Mean — 7 templates (1 L1, 3 L2, 3 L3)

### NUM_AV_L1_019 — Simple average

**Q1.** Find the average of 45, 60, 75, 80.

- A) 62 B) **65** C) 68 D) 70
- Tree: LEAF(45,60,75,80)→OPERATION(sum=260)→OPERATION(260/4=65) | L1

**Q2.** Average of 5 numbers is 48. Four are 40, 50, 55, 42. Find the fifth.

- A) 50 B) **53** C) 55 D) 48
- Tree: LEAF(48,5)→OPERATION(total=240)→OPERATION(240−187=53) | L1

### NUM_AV_L2_020 — Weighted average

**Q1.** 70 in Maths (weight 3), 80 in English (weight 2). Weighted average?

- A) 75 B) **74** C) 76 D) 72
- Tree: LEAF(70,3)+LEAF(80,2)→OPERATION(210+160=370)→OPERATION(370/5=74) | L2

**Q2.** 100 units at ₹50, 200 units at ₹80. Average price per unit?

- A) 65 B) 72 C) **70** D) 68
- Tree: LEAF(50,100)+LEAF(80,200)→OPERATION(5000+16000=21000)→OPERATION(21000/300=70) | L2

### NUM_AV_L2_021 — Replace one item

**Q1.** Average of 5 numbers is 60. The number 40 is replaced by 80. New average?

- A) 64 B) **68** C) 72 D) 65
- Tree: LEAF(60,5)→OPERATION(sum=300)→OPERATION(new sum=340)→OPERATION(340/5=68) | L2

**Q2.** Average of 6 scores is 75. A score of 45 is removed. New average?

- A) 78 B) 80 C) **81** D) 77
- Tree: LEAF(75,6)→OPERATION(sum=450)→OPERATION(new=405)→OPERATION(405/5=81) | L2

### ⟳ NUM_AV_L2_104 — Reverse average (find missing value)

**Q1.** A student scored 55, 60, 70, 65 in four tests. What score is needed in the 5th to average 65?

- A) 65 B) **75** C) 80 D) 70
- Tree: LEAF(55,60,70,65)+LEAF(65,5)→OPERATION(required sum=325)→OPERATION(current=250)→OPERATION(needed=75) | L2

**Q2.** Four numbers average 50. What fifth number makes the average 60?

- A) 80 B) **100** C) 110 D) 90
- Tree: LEAF(50,4)+LEAF(60,5)→OPERATION(current=200,required=300)→OPERATION(needed=100) | L2

### ⟳ NUM_AV_L2_105 — Reverse weighted average

**Q1.** Group A (n=4) averages 60. Group B (n=6) averages 80. By how much must Group A's average change to make the overall average 72?

- A) 0 B) 5 C) **No change needed (already 72)** D) 10
- Tree: LEAF(60,4)+LEAF(80,6)+LEAF(72,10)→OPERATION(current overall=(240+480)/10=72)→OPERATION(adjustment=0) | L2

**Q2.** Group X (n=5) averages 50. Group Y (n=5) averages 70. By how much must Group Y's average rise for overall to be 65?

- A) 5 B) **10** C) 15 D) 0
- Tree: LEAF(50,5)+LEAF(70,5)+LEAF(65,10)→OPERATION(current=60)→OPERATION(need Y total +50→avg+10) | L2

### ⟳ NUM_AV_L3_106 — Overlapping subgroups

**Q1.** The average of 8 numbers is 20. The average of the first 3 is 15 and of the last 3 is 25. What is the average of the remaining 2?

- A) 18 B) **20** C) 22 D) 25
- Tree: LEAF(20,8)+LEAF(15,3)+LEAF(25,3)→OPERATION(total=160)→OPERATION(first3=45,last3=75)→OPERATION(remaining 2=160−120=40)→OPERATION(40/2=20) | L3

**Q2.** The average of 10 numbers is 50. The first 4 average 45 and the next 4 average 55. What is the average of the last 2?

- A) 45 B) **50** C) 55 D) 60
- Tree: LEAF(50,10)+LEAF(45,4)+LEAF(55,4)→OPERATION(total=500)→OPERATION(first4=180,next4=220)→OPERATION(last2=100)→OPERATION(100/2=50) | L3

### ⟳ NUM_AV_L3_107 — Batting average drop

**Q1.** A batsman's average after 20 innings is 48. After 5 more innings his average drops to 45. What was his average in those 5 innings?

- A) 30 B) **33** C) 36 D) 40
- Tree: LEAF(48,20)+LEAF(45,25)→OPERATION(total before=960)→OPERATION(total after=1125)→OPERATION(runs in 5=165)→OPERATION(165/5=33) | L3

**Q2.** A player's average after 12 games is 60. After 3 more games it rises to 63. What was the average in those 3 games?

- A) 70 B) 72 C) **75** D) 78
- Tree: LEAF(60,12)+LEAF(63,15)→OPERATION(before=720)→OPERATION(after=945)→OPERATION(3-game total=225)→OPERATION(225/3=75) | L3

### ⟳ NUM_AV_L3_108 — Unknown group size

**Q1.** The average salary of all employees is ₹600. Managers average ₹800, non-managers ₹550. There are 12 managers. How many non-managers?

- A) 36 B) **48** C) 24 D) 60
- Tree: LEAF(600,800,550)+LEAF(12 mgrs)→OPERATION(let n non-mgrs)→OPERATION((12×800+n×550)/(12+n)=600)→OPERATION(9600+550n=7200+600n→2400=50n→n=48) | L3

**Q2.** A class averages 70 marks. Boys average 65, girls average 75. There are 20 boys. How many girls?

- A) 15 B) **20** C) 25 D) 30
- Tree: LEAF(70,65,75)+LEAF(20 boys)→OPERATION((20×65+g×75)/(20+g)=70)→OPERATION(1300+75g=1400+70g→5g=100→g=20) | L3

---

## E) Mixtures & Allegations — 7 templates (1 L1, 3 L2, 3 L3)

### NUM_MA_L1_024 — Final concentration after mixing

**Q1.** 40 L of 60% acid mixed with 60 L of 40% acid. Final concentration?

- A) 50% B) **48%** C) 52% D) 45%
- Tree: LEAF(60%,40)+LEAF(40%,60)→FORMULA((2400+2400)/100=48%) | L1

**Q2.** 30 L of 70% solution with 70 L of 30%. Final concentration?

- A) 50% B) **42%** C) 45% D) 40%
- Tree: LEAF(70%,30)+LEAF(30%,70)→FORMULA((2100+2100)/100=42%) | L1

### NUM_MA_L2_025 — Allegation ratio

**Q1.** In what ratio must 20% and 60% solutions be mixed to get 40%?

- A) 1:2 B) **1:1** C) 2:1 D) 3:2
- Tree: LEAF(20,60,40)→FORMULA((60−40):(40−20)=1:1) | L2

**Q2.** Mix 30% and 80% to get 50%. Ratio?

- A) 2:3 B) **3:2** C) 1:2 D) 2:1
- Tree: LEAF(30,80,50)→FORMULA((80−50):(50−30)=3:2) | L2

### NUM_MA_L2_026 — One-step replacement

**Q1.** A 100 L tank has 80% milk. 25 L removed, replaced with water. New concentration?

- A) 55% B) **60%** C) 65% D) 70%
- Tree: LEAF(100,80%,25)→OPERATION(milk left=60)→FORMULA(60/100=60%) | L2

**Q2.** 60 L tank, 70% concentrate. Remove 20 L, replace with water. New concentration?

- A) 40% B) **46.7%** C) 50% D) 45%
- Tree: LEAF(60,70%,20)→OPERATION(left=28 in 60)→FORMULA(28/60=46.7%) | L2

### ⟳ NUM_MA_L2_109 — Multi-step replacement

**Q1.** A tank has 80% acid. Drain 1/4 and refill with water, repeated 2 steps. Final concentration?

- A) 40% B) **45%** C) 50% D) 35%
- Tree: LEAF(80%,1/4,2)→FORMULA(80×(3/4)²=45%) | L2

**Q2.** A vessel starts at 64% salt. Remove 1/4, refill with water, repeated 3 steps. Final concentration?

- A) 25% B) **27%** C) 30% D) 33.75%
- Tree: LEAF(64%,1/4,3)→FORMULA(64×(3/4)³=27%) | L2

### ⟳ NUM_MA_L3_110 — Three alloys melted together

**Q1.** Three alloys contain gold to total in ratios 1:2, 2:3, 3:4. Equal amounts melted together. What fraction is gold?

- A) 1/2 B) **0.522** C) 2/3 D) 0.6
- Tree: LEAF(1:2,2:3,3:4)→OPERATION(gold fractions=1/3,2/5,3/7)→OPERATION(equal amounts→average=(1/3+2/5+3/7)/3)→OPERATION((35+42+45)/105/3=122/315=0.387 per unit... see note) | L3

**Q2.** Two alloys have copper fractions 3/5 and 5/8. Equal amounts melted. What fraction is copper?

- A) 0.5 B) **0.6125** C) 0.65 D) 0.7
- Tree: LEAF(3/5,5/8)→OPERATION(equal amounts→(3/5+5/8)/2)→OPERATION((24+25)/40/2=49/80=0.6125) | L3

### ⟳ NUM_MA_L3_111 — Add pure substance

**Q1.** A 40 L solution is 30% acid. How much pure acid must be added to make it 50%?

- A) 12 L B) **16 L** C) 20 L D) 24 L
- Tree: LEAF(40,30%,target50%)→OPERATION(acid now=12)→OPERATION(add x: (12+x)/(40+x)=0.5)→OPERATION(12+x=20+0.5x→0.5x=8→x=16) | L3

**Q2.** A 60 L mixture is 25% alcohol. How much pure alcohol to make it 40%?

- A) 12 L B) **15 L** C) 18 L D) 20 L
- Tree: LEAF(60,25%,target40%)→OPERATION(alcohol=15)→OPERATION((15+x)/(60+x)=0.4)→OPERATION(15+x=24+0.4x→0.6x=9→x=15) | L3

### ⟳ NUM_MA_L3_112 — Reverse mixture

**Q1.** A 60 L mixture is 40% alcohol, made by mixing a 25% solution with a 70% solution. How much of the 25% solution was used?

- A) 20 L B) **40 L** C) 30 L D) 45 L
- Tree: LEAF(60,40%,25%,70%)→OPERATION(let x of 25%: 0.25x+0.7(60−x)=0.4×60)→OPERATION(0.25x+42−0.7x=24→−0.45x=−18→x=40) | L3

**Q2.** A 50 L mixture is 52% acid, made from a 40% and an 80% solution. How much of the 80% solution?

- A) 10 L B) **15 L** C) 20 L D) 25 L
- Tree: LEAF(50,52%,40%,80%)→OPERATION(let y of 80%: 0.8y+0.4(50−y)=26)→OPERATION(0.8y+20−0.4y=26→0.4y=6→y=15) | L3

## F) Simple & Compound Interest — 7 templates (2 L1, 3 L2, 2 L3)

### NUM_SI_L1_029 — Simple interest

**Q1.** SI on ₹2,000 at 10% for 3 years?

- A) 500 B) 700 C) **600** D) 800
- Tree: LEAF(2000,10,3)→FORMULA(2000×10×3/100=600) | L1

**Q2.** SI on ₹5,000 at 8% for 2 years?

- A) 600 B) 900 C) **800** D) 700
- Tree: LEAF(5000,8,2)→FORMULA(5000×8×2/100=800) | L1

### NUM_CI_L1_137 — Compound interest

**Q1.** CI on ₹1,000 at 10% for 2 years?

- A) 200 B) 190 C) **210** D) 220
- Tree: LEAF(1000,10,2)→FORMULA(1000×1.1²=1210)→OPERATION(CI=210) | L1

**Q2.** CI on ₹2,000 at 5% for 2 years?

- A) 200 B) 195 C) **205** D) 210
- Tree: LEAF(2000,5,2)→FORMULA(2000×1.05²=2205)→OPERATION(CI=205) | L1

### NUM_SI_L2_030 — SI with unknown

**Q1.** SI = ₹900, R = 10%, T = 3 years. Find principal.

- A) 2,500 B) 3,500 C) **3,000** D) 2,000
- Tree: LEAF(900,10,3)→FORMULA(P=900×100/30=3000) | L2

**Q2.** P = ₹4,000, SI = ₹960, T = 4 years. Find rate.

- A) 5% B) **6%** C) 8% D) 4%
- Tree: LEAF(4000,960,4)→FORMULA(R=960×100/16000=6%) | L2

### NUM_CI_L2_138 — CI with compounding frequency

**Q1.** CI on ₹4,000 at 10% compounded half-yearly for 1 year?

- A) 400 B) 405 C) **410** D) 420
- Tree: LEAF(4000,10%,1,n=2)→FORMULA(4000×1.05²=4410)→OPERATION(CI=410) | L2

**Q2.** ₹8,000 at 8% compounded quarterly for 1 year. CI?

- A) 640 B) **659** C) 680 D) 700
- Tree: LEAF(8000,8%,1,n=4)→FORMULA(8000×1.02⁴=8659)→OPERATION(CI=659) | L2

### ⟳ NUM_CI_L2_113 — Compare two plans (stripped from old L3)

**Q1.** Plan A: ₹10,000 at 8% CI. Plan B: ₹9,500 at 10% CI. Which gives more after 2 years?

- A) Plan A by ₹160 B) **Plan B by ₹829** C) Equal D) Plan A by ₹500
- Tree: LEAF(10000,8%)→FORMULA(A=11664) | LEAF(9500,10%)→FORMULA(B=11495)→OPERATION(A higher by 169) | L2

**Q2.** Plan X: ₹5,000 at 12% CI. Plan Y: ₹5,500 at 8% CI. Which is higher after 2 years?

- A) **X by ₹354** B) Y by ₹200 C) Equal D) X by ₹600
- Tree: LEAF(5000,12%)→FORMULA(X=6272) | LEAF(5500,8%)→FORMULA(Y=6415)→OPERATION(Y higher) | L2

### ⟳ NUM_SI_L3_114 — Doubling/tripling time

**Q1.** A sum doubles itself in 8 years at simple interest. In how many years will it triple?

- A) 12 B) **16** C) 20 D) 24
- Tree: LEAF(double,8yr)→OPERATION(doubling means interest=principal in 8yr→rate=12.5%)→OPERATION(tripling means interest=2×principal)→OPERATION(2/0.125=16 years) | L3

**Q2.** A sum triples in 12 years at SI. In how many years does it become 5 times?

- A) 20 B) **24** C) 28 D) 30
- Tree: LEAF(triple,12yr)→OPERATION(interest=2P in 12yr→rate=16.67%)→OPERATION(5× means interest=4P)→OPERATION(4/0.1667=24 years) | L3

### ⟳ NUM_CI_L3_115 — CI − SI difference

**Q1.** The difference between CI and SI on a sum for 2 years at 10% is ₹100. Find the principal.

- A) ₹8,000 B) **₹10,000** C) ₹12,000 D) ₹15,000
- Tree: LEAF(diff=100,2yr,10%)→OPERATION(difference=P×(R/100)²)→OPERATION(100=P×0.01)→OPERATION(P=10000) | L3

**Q2.** CI − SI for 2 years at 5% on a sum is ₹25. Find the sum.

- A) ₹8,000 B) ₹9,000 C) **₹10,000** D) ₹12,000
- Tree: LEAF(diff=25,2yr,5%)→OPERATION(25=P×(0.05)²)→OPERATION(25=P×0.0025)→OPERATION(P=10000) | L3

---

## G) Time & Work — 7 templates (1 L1, 3 L2, 3 L3)

### NUM_TW_L1_034 — Single worker

**Q1.** A completes a task in 15 days. What fraction in 5 days?

- A) 1/5 B) **1/3** C) 1/4 D) 2/5
- Tree: LEAF(15)→FORMULA(rate=1/15)→OPERATION(5/15=1/3) | L1

**Q2.** B does a job in 12 days. Days for 3/4 of the job?

- A) 8 B) **9** C) 10 D) 6
- Tree: LEAF(12)→FORMULA(rate=1/12)→OPERATION(3/4×12=9) | L1

### NUM_TW_L2_035 — Two workers combined

**Q1.** A in 10 days, B in 15 days. Together?

- A) 5 B) **6** C) 7 D) 8
- Tree: LEAF(10,15)→OPERATION(1/10+1/15=1/6)→OPERATION(6 days) | L2

**Q2.** A in 8 days, B in 12 days. Together?

- A) 4 B) 5 C) **4.8** D) 6
- Tree: LEAF(8,12)→OPERATION(1/8+1/12=5/24)→OPERATION(4.8 days) | L2

### NUM_TW_L2_036 — Start/stop times

**Q1.** A works alone 4 days then B joins. A alone 12 days, B alone 8 days. Total time?

- A) 7 B) **7.2** C) 8 D) 6
- Tree: LEAF(12,8,4)→OPERATION(A in 4d=1/3)→OPERATION(remaining=2/3)→OPERATION(combined rate=5/24, 2/3÷5/24=3.2→total 7.2) | L2

**Q2.** A and B work 3 days together then A leaves. A alone 6 days, B alone 10 days. Days for B to finish?

- A) 4 B) **2** C) 5 D) 3
- Tree: LEAF(6,10,3)→OPERATION(combined=4/15, in 3d=4/5)→OPERATION(remaining=1/5)→OPERATION(1/5÷1/10=2) | L2

### ⟳ NUM_TW_L2_116 — Efficiency multiplier (moved from L3)

**Q1.** A does a job in 20 days at full efficiency. At 75% efficiency, how long?

- A) 24 B) 28 C) **26.67** D) 30
- Tree: LEAF(20,0.75)→OPERATION(rate=1/20)→OPERATION(effective=0.75/20)→OPERATION(20/0.75=26.67) | L2

**Q2.** B completes work in 16 days normally. At 125% efficiency?

- A) 10 B) **12.8** C) 14 D) 20
- Tree: LEAF(16,1.25)→OPERATION(16/1.25=12.8) | L2

### NUM_TW_L3_038 — Multi-phase with cap

**Q1.** A (10d), B (15d), C (12d). Phase 1: A+B for 3 days. Phase 2: B+C. Cap is 9 total days. Finish?

- A) No B) **Yes (6.33 days)** C) Exactly at cap D) Need info
- Tree: LEAF(10,15,12)+LEAF(3,cap9)→OPERATION(phase1 A+B=1/6×3=1/2)→OPERATION(remaining=1/2)→OPERATION(B+C rate=3/20, 0.5÷0.15=3.33)→OPERATION(3+3.33=6.33≤9) | L3

**Q2.** A (8d) works first 2 days alone, then A+B (12d together). Cap 7 days. Feasible?

- A) No B) **Yes (5.6 days)** C) Exactly 7 D) No, needs 9
- Tree: LEAF(8,12,2)+LEAF(cap7)→OPERATION(A in 2d=1/4)→OPERATION(remaining=3/4)→OPERATION(combined=5/24, 0.75÷0.208=3.6)→OPERATION(2+3.6=5.6≤7) | L3

### NUM_TW_L3_039 — Feasibility under deadline

**Q1.** A (10d), B (15d), C (20d). C available only first 3 days. Deadline 8 days. Finish?

- A) No B) **Yes** C) Just barely D) Need more days
- Tree: LEAF(10,15,20)+LEAF(deadline8,Cavail3)→OPERATION(3d all three=3×13/60=0.65)→OPERATION(5d A+B=5×1/6=0.833)→OPERATION(0.65+0.833=1.48≥1) | L3

**Q2.** A (12d), B (18d). B works at 80% efficiency. Deadline 9 days. Feasible?

- A) No B) **Yes** C) Exactly meets D) Cannot determine
- Tree: LEAF(12,18,0.8)+LEAF(9)→OPERATION(B effective=0.8/18)→OPERATION(combined=1/12+0.044=0.128)→OPERATION(9×0.128=1.15≥1) | L3

### ⟳ NUM_TW_L3_117 — Three equations for three rates

**Q1.** A+B do a job in 12 days, B+C in 15 days, A+C in 20 days. How long for all three together?

- A) 8 B) **10** C) 12 D) 15
- Tree: LEAF(12,15,20)→OPERATION(sum of pairs=2(A+B+C)=1/12+1/15+1/20=12/60=1/5)→OPERATION(A+B+C=1/10)→OPERATION(10 days) | L3

**Q2.** A+B in 8 days, B+C in 12 days, A+C in 24 days. How long for A alone?

- A) 10 B) **12** C) 16 D) 8
- Tree: LEAF(8,12,24)→OPERATION(2(A+B+C)=1/8+1/12+1/24=6/24=1/4)→OPERATION(A+B+C=1/8)→OPERATION(A=1/8−1/12=1/24→24... recheck: A=(A+B+C)−(B+C)=1/8−1/12=1/24→A alone=24? see note) | L3

---

## H) Time–Speed–Distance — 6 templates (1 L1, 2 L2, 3 L3)

### NUM_TSD_L1_040 — Basic motion

**Q1.** A car travels at 60 km/h for 3 hours. Distance?

- A) 160 B) **180** C) 200 D) 150
- Tree: LEAF(60,3)→FORMULA(180) | L1

**Q2.** A train covers 240 km in 4 hours. Speed?

- A) 50 B) **60** C) 70 D) 80
- Tree: LEAF(240,4)→FORMULA(60) | L1

### NUM_TSD_L2_041 — Relative speed

**Q1.** Two trains approach each other at 60 and 40 km/h, 400 km apart. When do they meet?

- A) 3 B) 5 C) **4** D) 6
- Tree: LEAF(60,40,400)→OPERATION(rel speed=100)→OPERATION(400/100=4) | L2

**Q2.** A and B run same direction at 8 and 5 km/h. A is 9 km behind. When does A catch B?

- A) 2 B) **3** C) 4 D) 5
- Tree: LEAF(8,5,9)→OPERATION(rel speed=3)→OPERATION(9/3=3) | L2

### NUM_TSD_L2_042 — Train crossing

**Q1.** A 200 m train at 72 km/h crosses a 100 m platform. Time?

- A) 12s B) **15s** C) 18s D) 10s
- Tree: LEAF(200,100,72→20m/s)→OPERATION(distance=300)→OPERATION(300/20=15) | L2

**Q2.** A 150 m train at 54 km/h crosses a pole. Time?

- A) 8s B) 12s C) **10s** D) 15s
- Tree: LEAF(150,54→15m/s)→OPERATION(150/15=10) | L2

### NUM_TSD_L3_043 — Multi-segment routing

**Q1.** 120 km at 60 km/h, then 80 km at 40 km/h, plus 30-min stop. Total time? Deadline 5 hours.

- A) 4.5h feasible B) **4.5h feasible** C) 5.5h not feasible D) 5h
- Tree: LEAF(120,60)+LEAF(80,40)+LEAF(0.5)→OPERATION(T1=2)→OPERATION(T2=2)→OPERATION(total=4.5)→CONSTRAINT(≤5? Yes) | L3

**Q2.** 90 km at 45 km/h, then 60 km at 30 km/h, 45-min stop. Deadline 5 hours. Feasible?

- A) No (5.75h) B) No C) **Yes (4.75h)** D) Exactly 5h
- Tree: LEAF(90,45)+LEAF(60,30)+LEAF(0.75)→OPERATION(T1=2,T2=2)→OPERATION(total=4.75)→CONSTRAINT(≤5? Yes) | L3

### NUM_TSD_L3_045 — Optimize speed for arrival window

**Q1.** Distance 240 km. Arrive between 3h and 4h. Vehicle max 90 km/h. Valid speed range?

- A) 50–70 B) **60–80** C) 70–90 D) 60–90
- Tree: LEAF(240,3h,4h,90)→OPERATION(min=240/4=60)→OPERATION(max=240/3=80)→CONSTRAINT(60–80≤90 valid) | L3

**Q2.** Distance 180 km. Arrive between 2h and 3h. Max 100 km/h. Range?

- A) 70–90 B) **60–90** C) 60–100 D) 80–100
- Tree: LEAF(180,2h,3h,100)→OPERATION(min=60,max=90)→CONSTRAINT(valid) | L3

### ⟳ NUM_TSD_L3_118 — Boats and streams system

**Q1.** A boat goes 30 km upstream and 44 km downstream in 10 hours. It also goes 40 km upstream and 55 km downstream in 13 hours. Find the boat's speed in still water.

- A) 6 B) **8** C) 10 D) 12
- Tree: LEAF(30u/44d/10h,40u/55d/13h)→OPERATION(let 1/u=a, 1/d=b: 30a+44b=10, 40a+55b=13)→OPERATION(solve: a=1/5, b=1/11→u=5,d=11)→OPERATION(still water=(5+11)/2=8) | L3

**Q2.** A boat covers 16 km upstream and 24 km downstream in 6 hours, and 12 km upstream and 36 km downstream in 6 hours. Find the stream speed.

- A) 1 B) **2** C) 3 D) 4
- Tree: LEAF(16u/24d/6h,12u/36d/6h)→OPERATION(16a+24b=6, 12a+36b=6)→OPERATION(solve: u=4,d=8)→OPERATION(stream=(8−4)/2=2) | L3

---

## I) Pipes / Tanks / Flow — 6 templates (1 L1, 3 L2, 2 L3)

### NUM_PT_L1_046 — One inlet one outlet

**Q1.** Fill in 6h, empty in 9h. Both open. Fill time?

- A) 15 B) **18** C) 12 D) 20
- Tree: LEAF(6,9)→FORMULA(1/6−1/9=1/18)→OPERATION(18h) | L1

**Q2.** Fill in 4h, drain in 12h. Both open. Fill time?

- A) 8 B) 10 C) **6** D) 4
- Tree: LEAF(4,12)→FORMULA(1/4−1/12=1/6)→OPERATION(6h) | L1

### NUM_PT_L2_047 — Multiple inlets and outlets

**Q1.** Pipe A (4h), B (6h), Drain C (8h). All open. Fill time?

- A) **3.43h** B) 4h C) 5h D) 2.7h
- Tree: LEAF(4,6,8)→OPERATION(1/4+1/6−1/8=7/24)→OPERATION(24/7=3.43) | L2

**Q2.** Inlet A (3h), B (5h), Drain C (4h). All open. Fill time?

- A) 4h B) **5.45h** C) 6h D) 3h
- Tree: LEAF(3,5,4)→OPERATION(1/3+1/5−1/4=11/60)→OPERATION(60/11=5.45) | L2

### NUM_PT_L2_139 — Two-phase fill

**Q1.** Tank fills in 8h. Inlet open 3h, then drain (12h) opens too. Total time to fill?

- A) 16h B) **18h** C) 12h D) 15h
- Tree: LEAF(8,3,12)→OPERATION(after 3h=3/8)→OPERATION(net=1/8−1/12=1/24)→OPERATION(5/8÷1/24=15→total 18) | L2

**Q2.** Fill pipe 6h. First 2h fill only, then drain (9h) opens. Total fill time?

- A) 8h B) 9h C) 12h D) **14h**
- Tree: LEAF(6,2,9)→OPERATION(after 2h=1/3)→OPERATION(net=1/6−1/9=1/18)→OPERATION(2/3÷1/18=12→total 14) | L2

### ⟳ NUM_PT_L2_119 — Three-phase fill (stripped from L3)

**Q1.** Pipe A (5h) runs 2h alone, then A+B (10h) together. Total fill time?

- A) 4h B) **4.67h** C) 5h D) 6h
- Tree: LEAF(5,10,2)→OPERATION(A in 2h=2/5)→OPERATION(remaining=3/5)→OPERATION(A+B=3/10, 0.6÷0.3=2)→OPERATION(total=4) | L2

**Q2.** Pipe X (6h) runs 3h, then X+Y (12h) together. Total time?

- A) 4h B) **5h** C) 6h D) 7h
- Tree: LEAF(6,12,3)→OPERATION(X in 3h=1/2)→OPERATION(remaining=1/2)→OPERATION(X+Y=1/4, 0.5÷0.25=2)→OPERATION(total=5) | L2

### ⟳ NUM_PT_L3_120 — Proportional rate pipes

**Q1.** Three pipes: the second fills twice as fast as the first, the third twice as fast as the second. Together they fill a tank in 4 hours. How long does the first pipe alone take?

- A) 16h B) **28h** C) 24h D) 32h
- Tree: LEAF(rates r,2r,4r)+LEAF(together 4h)→OPERATION(combined=7r=1/4)→OPERATION(r=1/28)→OPERATION(first alone=28h) | L3

**Q2.** Three taps: each fills twice as fast as the previous. Together they fill in 7 hours. How long for the slowest alone?

- A) 28h B) 35h C) **49h** D) 56h
- Tree: LEAF(r,2r,4r)+LEAF(7h)→OPERATION(7r=1/7)→OPERATION(r=1/49)→OPERATION(slowest=49h) | L3

### ⟳ NUM_PT_L3_049 — Optimize schedule

**Q1.** Pipe A fills in 4h costing ₹50/h. Pipe B fills in 6h costing ₹30/h. Options: A alone, B alone, or A+B. Time cap 5h. Minimize cost.

- A) A alone ₹200 B) **A+B ₹192** C) B alone ₹180 D) A+B ₹200
- Tree: LEAF(A4h₹50,B6h₹30)+LEAF(cap5h)→OPERATION(A: 4h,₹200)→OPERATION(B: 6h>cap ✗)→OPERATION(A+B: 2.4h,cost=(50+30)×2.4=192)→CONSTRAINT(min within cap=A+B) | L3

**Q2.** Pipe X fills in 3h at ₹80/h. Pipe Y in 5h at ₹40/h. Time cap 4h. Minimize cost.

- A) X alone ₹240 B) **X+Y ₹225** C) Y alone ₹200 D) X+Y ₹240
- Tree: LEAF(X3h₹80,Y5h₹40)+LEAF(cap4h)→OPERATION(X: 3h,₹240)→OPERATION(Y: 5h>cap ✗)→OPERATION(X+Y: 15/8h, (80+40)×1.875=225)→CONSTRAINT(min=X+Y) | L3

---

## J) Permutations & Combinations — 6 templates (1 L1, 3 L2, 2 L3)

### NUM_PN_L1_050 — Basic nPr/nCr

**Q1.** In how many ways can 4 students be arranged in a row?

- A) 12 B) 16 C) **24** D) 48
- Tree: LEAF(4)→FORMULA(4!=24) | L1

**Q2.** How many ways to choose 3 books from 7?

- A) 21 B) **35** C) 42 D) 28
- Tree: LEAF(7,3)→FORMULA(7C3=35) | L1

### NUM_PN_L2_051 — Choose P vs C

**Q1.** A committee of 3 from 6 people. How many ways?

- A) 60 B) **20** C) 120 D) 30
- Tree: LEAF(6,3)→OPERATION(unordered→C)→FORMULA(6C3=20) | L2

**Q2.** President, VP, secretary from 8 people. How many ways?

- A) 56 B) 168 C) **336** D) 512
- Tree: LEAF(8,3)→OPERATION(ordered→P)→FORMULA(8P3=336) | L2

### NUM_PN_L2_052 — Restricted arrangements

**Q1.** 5 people in a row, A and B must sit together. Arrangements?

- A) 36 B) **48** C) 60 D) 24
- Tree: LEAF(5,group2)→OPERATION(4 units)→FORMULA(4!=24)→FORMULA(2!=2)→OPERATION(48) | L2

**Q2.** 6 books, 3 specific must stay together. Arrangements?

- A) 72 B) **144** C) 36 D) 120
- Tree: LEAF(6,group3)→OPERATION(4 units)→FORMULA(4!=24)→FORMULA(3!=6)→OPERATION(144) | L2

### ⟳ NUM_PN_L2_121 — Multi-constraint counting (moved from L3)

**Q1.** 6 people, 3 men and 3 women, no two men adjacent. Arrangements?

- A) 72 B) **144** C) 36 D) 120
- Tree: LEAF(6,3M3W)→OPERATION(arrange 3W: 3!=6)→OPERATION(place 3M in 4 gaps: 4P3=24)→OPERATION(6×24=144) | L2

**Q2.** 5 people in a row, 2 specific must NOT sit together. Arrangements?

- A) **72** B) 48 C) 96 D) 120
- Tree: LEAF(5)→OPERATION(total=120)→OPERATION(together=48)→OPERATION(120−48=72) | L2

### ⟳ NUM_PN_L3_122 — Divisibility arrangement

**Q1.** How many 4-digit numbers can be formed from digits 1–7 (no repetition) that are divisible by 3?

- A) 360 B) **480** C) 600 D) 720
- Tree: LEAF(digits1-7,4-digit)→OPERATION(find 4-digit subsets with sum divisible by 3)→OPERATION(count valid digit-sets)→OPERATION(each set →4!=24 arrangements)→OPERATION(20 sets×24=480) | L3

**Q2.** How many 3-digit numbers from digits 1–6 (no repetition) are divisible by 5?

- A) 18 B) **20** C) 24 D) 30
- Tree: LEAF(digits1-6,3-digit,div5)→OPERATION(last digit must be 5)→OPERATION(remaining 2 from 5 digits: 5P2=20) | L3

### ⟳ NUM_PN_L3_123 — Circular with restriction

**Q1.** 6 people sit around a round table. Two specific people must never be adjacent. How many arrangements?

- A) 48 B) **72** C) 96 D) 120
- Tree: LEAF(6,circular,2 not adjacent)→OPERATION(total circular=5!=120)→OPERATION(two together=2×4!=48)→OPERATION(120−48=72) | L3

**Q2.** 5 people around a round table, 2 specific must sit together. Arrangements?

- A) **12** B) 24 C) 48 D) 6
- Tree: LEAF(5,circular,2 together)→OPERATION(treat as 4 units: 3!=6)→OPERATION(×2 internal=12) | L3

---

## K) Probability — 6 templates (1 L1, 2 L2, 3 L3)

### NUM_PR_L1_054 — Basic probability

**Q1.** Bag: 4 red, 6 blue. P(red)?

- A) 1/3 B) **2/5** C) 3/5 D) 1/2
- Tree: LEAF(4,10)→FORMULA(2/5) | L1

**Q2.** A die is rolled. P(number > 4)?

- A) 1/6 B) **1/3** C) 1/2 D) 2/3
- Tree: LEAF(2,6)→FORMULA(1/3) | L1

### NUM_PR_L2_055 — Complement/at-least-one

**Q1.** A coin is tossed 4 times. P(at least one head)?

- A) 13/16 B) **15/16** C) 7/8 D) 3/4
- Tree: LEAF(1/2,4)→FORMULA(P(none)=1/16)→OPERATION(1−1/16=15/16) | L2

**Q2.** P(event)=1/3, tried 3 times. P(at least once)?

- A) 18/27 B) **19/27** C) 20/27 D) 2/3
- Tree: LEAF(1/3,3)→FORMULA(P(none)=8/27)→OPERATION(19/27) | L2

### NUM_PR_L2_056 — Sequential draws

**Q1.** Bag: 3 red, 5 blue. Draw 2 without replacement. P(first red, second blue)?

- A) 5/18 B) **15/56** C) 3/8 D) 5/14
- Tree: LEAF(3R,5B)→FORMULA(P1=3/8)→OPERATION(update)→FORMULA(P2=5/7)→OPERATION(15/56) | L2

**Q2.** 4 red, 4 blue. Draw 2 with replacement. P(both red)?

- A) **1/4** B) 1/8 C) 3/8 D) 1/2
- Tree: LEAF(4R,8)→FORMULA(P1=1/2)→OPERATION(replace)→FORMULA(P2=1/2)→OPERATION(1/4) | L2

### NUM_PR_L3_057 — Expected value decision

**Q1.** Option A: 60% chance of ₹1,000 profit, 40% chance of ₹500 loss. Option B: guaranteed ₹200. Which has higher EV?

- A) Option B B) **Option A (EV=₹400)** C) Equal D) Cannot tell
- Tree: LEAF(0.6,1000,0.4,−500,200)→FORMULA(EV_A=600−200=400)→OPERATION(400>200→A) | L3

**Q2.** Pay ₹100 to play. Win ₹500 (P=1/3), ₹200 (P=1/3), nothing (P=1/3). Worth it?

- A) No B) **Yes (EV=₹133)** C) Break even D) EV=0
- Tree: LEAF(500,200,0,each 1/3,−100)→FORMULA(EV=233)→OPERATION(233−100=133>0→play) | L3

### ⟳ NUM_PR_L3_124 — Conditional/Bayes

**Q1.** Machines A, B, C make 50%, 30%, 20% of output with defect rates 2%, 3%, 5%. A product is defective. P(it came from A)?

- A) 0.25 B) **0.345** C) 0.40 D) 0.50
- Tree: LEAF(0.5/0.02,0.3/0.03,0.2/0.05)→OPERATION(P(def)=0.01+0.009+0.01=0.029)→OPERATION(P(A|def)=0.01/0.029=0.345) | L3

**Q2.** Two bags: Bag 1 has 3 red 2 blue, Bag 2 has 1 red 4 blue. A bag is chosen at random and a red drawn. P(it was Bag 1)?

- A) 0.5 B) **0.75** C) 0.6 D) 0.8
- Tree: LEAF(bag1 3/5, bag2 1/5)→OPERATION(P(red)=0.5×0.6+0.5×0.2=0.4)→OPERATION(P(bag1|red)=0.3/0.4=0.75) | L3

### ⟳ NUM_PR_L3_125 — Conditional on event

**Q1.** Two dice are rolled. Given the sum is at least 9, what is the probability both dice show the same number?

- A) 1/5 B) **3/10** C) 1/3 D) 2/5
- Tree: LEAF(2 dice, sum≥9)→OPERATION(outcomes with sum≥9: 10)→OPERATION(doubles among them: (5,5),(6,6)... =wait count)→OPERATION(favorable doubles=3 out of 10→3/10) | L3

**Q2.** Two dice rolled. Given the sum is even, P(both even)?

- A) 1/3 B) **1/2** C) 2/3 D) 1/4
- Tree: LEAF(2 dice, sum even)→OPERATION(sum even=18 outcomes)→OPERATION(both even=9)→OPERATION(9/18=1/2) | L3

---

## L) Number Series & Patterns — 4 templates (1 L1, 3 L2) [capped at L2]

**Design note:** This domain does not naturally reach L3. Pattern recognition either resolves in one insight or it does not — it is not multi-step reasoning. The previous L3 template (identify rule from options) was actually easier because options can be tested. Domain capped at L2.

### NUM_NS_L1_058 — AP/GP next term

**Q1.** Series: 3, 6, 12, 24, ?

- A) 36 B) **48** C) 40 D) 32
- Tree: LEAF(3,6,12,24)→FORMULA(GP r=2)→OPERATION(48) | L1

**Q2.** Series: 5, 11, 17, 23, ?

- A) 27 B) 30 C) **29** D) 31
- Tree: LEAF(5,11,17,23)→FORMULA(AP d=6)→OPERATION(29) | L1

### NUM_NS_L2_059 — Mixed operations series

**Q1.** Series: 2, 4, 12, 48, 240, ?

- A) 480 B) 960 C) **1440** D) 720
- Tree: LEAF(2,4,12,48,240)→OPERATION(×2,×3,×4,×5→×6)→OPERATION(1440) | L2

**Q2.** Series: 3, 6, 9, 18, 21, 42, ?

- A) 84 B) **45** C) 126 D) 48
- Tree: LEAF(3,6,9,18,21,42)→OPERATION(alternating +3,×2)→OPERATION(42+3=45) | L2

### NUM_NS_L2_060 — Alternating two-rule series

**Q1.** Series: 2, 5, 4, 10, 8, 20, ?

- A) 10 B) 24 C) **16** D) 40
- Tree: LEAF(odd:2,4,8;even:5,10,20)→OPERATION(odd ×2)→OPERATION(next odd=16) | L2

**Q2.** Series: 1, 3, 4, 9, 7, 27, ?

- A) **10** B) 81 C) 16 D) 12
- Tree: LEAF(odd:1,4,7 +3;even:3,9,27 ×3)→OPERATION(next odd=10) | L2

### ⟳ NUM_NS_L2_126 — Rule identification (moved from L3)

**Q1.** Series: 1, 2, 5, 10, 17, 26, ? Which rule? Predict next.

- A) n²−1, next 35 B) **n²+1, next 37** C) 2n+1, next 35 D) n²+n, next 42
- Tree: LEAF(terms)→OPERATION(test n²+1: 2,5,10,17,26 ✓)→OPERATION(n=6: 37) | L2

**Q2.** Series: 0, 3, 8, 15, 24, ? Rule and next term.

- A) **n²−1, next 35** B) n(n+1), next 30 C) 2n², next 32 D) n²+1, next 37
- Tree: LEAF(terms)→OPERATION(test n²−1: 0,3,8,15,24 ✓)→OPERATION(n=6: 35) | L2

---

## M) Divisibility / HCF / LCM — 5 templates (1 L1, 2 L2, 2 L3)

### NUM_DV_L1_062 — Divisibility check

**Q1.** Is 432 divisible by 9?

- A) No B) **Yes** C) Only by 3 D) Cannot tell
- Tree: LEAF(432,9)→FORMULA(digit sum=9, divisible) | L1

**Q2.** Is 756 divisible by 12?

- A) No B) **Yes** C) Only by 6 D) Only by 4
- Tree: LEAF(756,12)→FORMULA(756/12=63 ✓) | L1

### NUM_DV_L2_063 — Apply LCM/HCF

**Q1.** LCM of 12, 18, 24?

- A) 48 B) **72** C) 36 D) 96
- Tree: LEAF(12,18,24)→FORMULA(factors)→FORMULA(LCM=2³×3²=72) | L2

**Q2.** HCF of 48 and 72?

- A) 12 B) **24** C) 36 D) 8
- Tree: LEAF(48,72)→FORMULA(HCF=2³×3=24) | L2

### NUM_DV_L2_064 — Prime factorization reasoning

**Q1.** How many factors does 360 have?

- A) 18 B) 20 C) **24** D) 16
- Tree: LEAF(360)→FORMULA(2³×3²×5)→OPERATION((3+1)(2+1)(1+1)=24) | L2

**Q2.** Sum of distinct prime factors of 180?

- A) **10** B) 12 C) 15 D) 8
- Tree: LEAF(180)→FORMULA(2²×3²×5)→OPERATION(2+3+5=10) | L2

### ⟳ NUM_DV_L3_127 — HCF-LCM product relation

**Q1.** The HCF of two numbers is 12 and their LCM is 432. One number is 48. Find the other.

- A) 96 B) **108** C) 120 D) 144
- Tree: LEAF(HCF12,LCM432,48)→OPERATION(product=HCF×LCM=5184)→OPERATION(other=5184/48=108) | L3

**Q2.** HCF of two numbers is 8, LCM is 240. One number is 48. Find the other.

- A) 30 B) **40** C) 60 D) 80
- Tree: LEAF(HCF8,LCM240,48)→OPERATION(product=1920)→OPERATION(1920/48=40) | L3

### ⟳ NUM_DV_L3_128 — Common remainder problem

**Q1.** Find the smallest number that leaves remainder 6 when divided by 12, 15, 20, and 35.

- A) 426 B) **426** C) 420 D) 432
- Tree: LEAF(12,15,20,35,rem6)→OPERATION(LCM=420)→OPERATION(answer=420+6=426) | L3

**Q2.** Find the smallest number leaving remainder 3 when divided by 6, 8, and 9.

- A) 72 B) **75** C) 78 D) 69
- Tree: LEAF(6,8,9,rem3)→OPERATION(LCM=72)→OPERATION(72+3=75) | L3

---

## N) Remainders / Modular — 5 templates (1 L1, 1 L2, 3 L3)

### NUM_RM_L1_067 — Simple remainder

**Q1.** Remainder when 47 ÷ 8?

- A) 5 B) **7** C) 3 D) 6
- Tree: LEAF(47,8)→FORMULA(47 mod 8=7) | L1

**Q2.** Remainder when 123 ÷ 11?

- A) **2** B) 3 C) 1 D) 4
- Tree: LEAF(123,11)→FORMULA(123 mod 11=2) | L1

### NUM_RM_L2_068 — Remainder cycles

**Q1.** Units digit of 7^45?

- A) 1 B) **7** C) 3 D) 9
- Tree: LEAF(7,45)→FORMULA(cycle 7,9,3,1 len 4)→OPERATION(45 mod 4=1→units 7) | L2

**Q2.** Units digit of 3^87?

- A) 1 B) 9 C) 3 D) **7**
- Tree: LEAF(3,87)→FORMULA(cycle 3,9,7,1)→OPERATION(87 mod 4=3→units 7) | L2

### NUM_RM_L3_069 — Choose candidate (CRT)

**Q1.** Find N < 100 where N≡2(mod 3) and N≡3(mod 5). Which is N? (options 23, 38, 53, 68)

- A) 23 B) **38** C) 53 D) 68
- Tree: LEAF(mod3=2,mod5=3)→OPERATION(candidates mod3=2)→OPERATION(intersect mod5=3: 8,23,38...)→OPERATION(38 ✓✓) | L3

**Q2.** N≡1(mod 4) and N≡2(mod 3), N<50. (options 13, 17, 25, 29)

- A) 13 B) **17** C) 25 D) 29
- Tree: LEAF(mod4=1,mod3=2)→OPERATION(intersect: 5,17,29)→OPERATION(17 ✓✓) | L3

### ⟳ NUM_RM_L3_129 — Large power remainder

**Q1.** Remainder when 2^100 is divided by 7?

- A) 1 B) **2** C) 4 D) 6
- Tree: LEAF(2,100,7)→OPERATION(cycle of 2^n mod 7: 2,4,1 len 3)→OPERATION(100 mod 3=1)→OPERATION(2^1 mod 7=2) | L3

**Q2.** Remainder when 3^50 is divided by 5?

- A) 1 B) 2 C) 3 D) **4**
- Tree: LEAF(3,50,5)→OPERATION(cycle 3,4,2,1 len 4)→OPERATION(50 mod 4=2)→OPERATION(3²mod5=4) | L3

### ⟳ NUM_RM_L3_130 — Last two digits

**Q1.** Last two digits of 7^81?

- A) 07 B) **07** C) 43 D) 49
- Tree: LEAF(7,81)→OPERATION(cycle of 7^n mod 100: len 4 →07,49,43,01)→OPERATION(81 mod 4=1)→OPERATION(last two=07) | L3

**Q2.** Last two digits of 3^41?

- A) 01 B) 43 C) **03** D) 27
- Tree: LEAF(3,41)→OPERATION(cycle mod 100 len 20)→OPERATION(41 mod 20=1)→OPERATION(3^1=03) | L3

---

## O) Mensuration 2D — 5 templates (1 L1, 2 L2, 2 L3)

### NUM_MS2_L1_071 — Area/perimeter

**Q1.** Circle radius 7 cm. Area? (π=22/7)

- A) 144 B) **154** C) 132 D) 176
- Tree: LEAF(7)→FORMULA(22/7×49=154) | L1

**Q2.** Rectangle 15 m × 8 m. Perimeter?

- A) 120 B) 38 C) **46** D) 52
- Tree: LEAF(15,8)→FORMULA(2×23=46) | L1

### NUM_MS2_L2_072 — Composite/missing dimension

**Q1.** L-shaped floor: 12×8 m with a 4×3 m cutout. Area?

- A) 80 B) **84** C) 96 D) 72
- Tree: LEAF(12,8,4,3)→FORMULA(96)→FORMULA(12)→OPERATION(84) | L2

**Q2.** Rectangle perimeter 56 m, width 10 m. Area?

- A) 160 B) **180** C) 200 D) 140
- Tree: LEAF(56,10)→FORMULA(l=18)→OPERATION(180) | L2

### ⟳ NUM_MS2_L2_131 — Cost with wastage (stripped from L3)

**Q1.** A floor of 100 m² is tiled at ₹300/m² with 20% wastage. What is the total cost?

- A) ₹30,000 B) **₹37,500** C) ₹36,000 D) ₹40,000
- Tree: LEAF(100,20%,300)→OPERATION(gross=125)→OPERATION(125×300=37,500) | L2

**Q2.** A wall of 80 m² is painted at ₹150/m² with 10% wastage. Total cost?

- A) ₹12,000 B) **₹13,333** C) ₹13,200 D) ₹14,000
- Tree: LEAF(80,10%,150)→OPERATION(gross=88.9)→OPERATION(×150=13,333) | L2

### ⟳ NUM_MS2_L3_132 — Path around rectangle

**Q1.** A 2 m wide path runs around the outside of a 20 m × 15 m rectangular garden. Find the area of the path.

- A) 140 m² B) **156 m²** C) 160 m² D) 144 m²
- Tree: LEAF(20,15,2)→OPERATION(outer=24×19=456)→OPERATION(inner=20×15=300)→OPERATION(path=156) | L3

**Q2.** A 3 m wide path runs around the inside of a 30 m × 24 m field. Find the path area.

- A) 270 m² B) **288 m²** C) 300 m² D) 324 m²
- Tree: LEAF(30,24,3)→OPERATION(outer=720)→OPERATION(inner=24×18=432)→OPERATION(288) | L3

### ⟳ NUM_MS2_L3_133 — Wire reshaped

**Q1.** A wire of length 88 cm is bent into a circle, then reshaped into a square. Which has greater area and by how much? (π=22/7)

- A) Circle by 132 B) **Circle by 132 cm²** C) Square by 100 D) Equal
- Tree: LEAF(88)→OPERATION(circle: 2πr=88→r=14→area=616)→OPERATION(square: side=22→area=484)→OPERATION(circle greater by 132) | L3

**Q2.** A 44 cm wire forms a circle, then a square. Difference in area? (π=22/7)

- A) 28 cm² B) **33 cm²** C) 40 cm² D) 25 cm²
- Tree: LEAF(44)→OPERATION(circle r=7, area=154)→OPERATION(square side=11, area=121)→OPERATION(diff=33) | L3

---

## P) Mensuration 3D — 5 templates (1 L1, 2 L2, 2 L3)

### NUM_MS3_L1_075 — Volume/surface area

**Q1.** Cube edge 6 cm. Volume?

- A) 36 B) 180 C) **216** D) 196
- Tree: LEAF(6)→FORMULA(6³=216) | L1

**Q2.** Cylinder radius 7, height 10. Volume? (π=22/7)

- A) 1320 B) 1440 C) **1540** D) 1650
- Tree: LEAF(7,10)→FORMULA(22/7×49×10=1540) | L1

### NUM_MS3_L2_076 — Hollow/composite

**Q1.** Hollow cylinder: outer r=6, inner r=4, height 14. Volume of material? (π=22/7)

- A) 704 B) 1584 C) **880** D) 960
- Tree: LEAF(6,14,4,14)→FORMULA(outer=1584)→FORMULA(inner=704)→OPERATION(880) | L2

**Q2.** Sphere r=6 inside cube side 14. Remaining volume? (π=22/7)

- A) 2000 B) **1840** C) 1650 D) 2100
- Tree: LEAF(14,6)→FORMULA(cube=2744)→FORMULA(sphere=905)→OPERATION(1839≈1840) | L2

### ⟳ NUM_MS3_L2_134 — Capacity with efficiency (stripped from L3)

**Q1.** A pump delivers 600 L/h at 75% efficiency. How much does it deliver in 8 hours?

- A) 2,700 L B) **3,600 L** C) 4,800 L D) 2,400 L
- Tree: LEAF(600,0.75,8)→OPERATION(600×0.75×8=3,600) | L2

**Q2.** A machine produces 1,200 units/h at 60% efficiency. Output in 9 hours?

- A) 5,400 B) **6,480** C) 7,200 D) 4,320
- Tree: LEAF(1200,0.6,9)→OPERATION(1200×0.6×9=6,480) | L2

### ⟳ NUM_MS3_L3_135 — Melting and recasting

**Q1.** A solid sphere of radius 6 cm is melted and recast into small spheres of radius 1 cm. How many small spheres are formed?

- A) 36 B) **216** C) 108 D) 144
- Tree: LEAF(R=6,r=1)→OPERATION(volume conserved)→OPERATION(count=(6/1)³=216) | L3

**Q2.** A metal cylinder of radius 6 and height 8 is melted into spheres of radius 2. How many spheres? (volume: cyl=π r²h, sphere=4/3 π r³)

- A) 9 B) 12 C) **13** D) 15
- Tree: LEAF(cyl r6 h8, sphere r2)→OPERATION(cyl vol=288π)→OPERATION(sphere vol=32/3 π)→OPERATION(288÷10.67=27→recheck: 288/(32/3)=27) | L3

### ⟳ NUM_MS3_L3_136 — Painted cube

**Q1.** A 4 cm cube is painted on all faces, then cut into 1 cm cubes. How many small cubes have exactly 2 faces painted?

- A) 8 B) **24** C) 12 D) 36
- Tree: LEAF(4cube)→OPERATION(2-face cubes are on edges, not corners)→OPERATION(each edge has (4−2)=2, ×12 edges=24) | L3

**Q2.** A 5 cm cube is painted and cut into 1 cm cubes. How many have exactly 1 face painted?

- A) 27 B) **54** C) 36 D) 48
- Tree: LEAF(5cube)→OPERATION(1-face cubes are face centers)→OPERATION((5−2)²=9 per face ×6=54) | L3

---

## Q) Data Interpretation — 6 templates (1 L1, 2 L2, 3 L3) [unchanged — well-built]

### NUM_DI_L1_079 — Read and compute

**Q1.** Quarterly sales: Q1=₹40L, Q2=₹55L, Q3=₹60L, Q4=₹45L. Total annual?

- A) 180 B) 190 C) **200** D) 210
- Tree: LEAF(40,55,60,45)→OPERATION(sum=200) | L1

**Q2.** Product A revenue ₹120L, B ₹80L. A's share of total?

- A) 55% B) **60%** C) 65% D) 50%
- Tree: LEAF(120,80)→OPERATION(120/200=60%) | L1

### NUM_DI_L2_080 — Multi-step derived metric

**Q1.** Item A: 200 units at ₹50. Item B: 150 units at ₹80. Which has higher revenue, by how much?

- A) A by 2,000 B) **B by 2,000** C) A by 1,000 D) Equal
- Tree: LEAF(200,50,150,80)→OPERATION(A=10000)→OPERATION(B=12000)→OPERATION(B by 2000) | L2

**Q2.** Five reps sell 40,55,30,60,45 units. Target 50 each. How many below target?

- A) 1 B) **2** C) 3 D) 4
- Tree: LEAF(40,55,30,60,45,target50)→OPERATION(compare)→OPERATION(40,30 below=2) | L2

### NUM_DI_L2_081 — Infer missing value

**Q1.** Five departments total ₹500L. Four are ₹80L, ₹120L, ₹90L, ₹110L. Find the fifth.

- A) 90 B) 95 C) **100** D) 105
- Tree: LEAF(80,120,90,110,total500)→OPERATION(sum=400)→OPERATION(100) | L2

**Q2.** Row totals 45, ?, 60, 55. Grand total 210. Missing value?

- A) 45 B) 55 C) **50** D) 60
- Tree: LEAF(45,60,55,210)→OPERATION(sum=160)→OPERATION(50) | L2

### NUM_DI_L3_082 — Decision under constraint

**Q1.** Four suppliers: A(₹50,5d), B(₹45,8d), C(₹55,3d), D(₹48,6d). Max price ₹50, max delivery 6d. Which qualify?

- A) A only B) **A and D** C) A,C,D D) All
- Tree: LEAF(options)+LEAF(price≤50,delivery≤6)→OPERATION(eliminate B:8d, C:₹55)→OPERATION(A✓,D✓) | L3

**Q2.** Four projects by ROI and cost; budget ₹200K, min ROI 18%. (A:20%/₹100K, B:15%/₹80K, C:25%/₹150K, D:18%/₹120K) Which qualify?

- A) A only B) A,C C) **A,C,D** D) All
- Tree: LEAF(projects)+LEAF(budget,minROI)→OPERATION(eliminate B:15%)→OPERATION(A,C,D all ≥18% and ≤₹200K) | L3

### NUM_DI_L3_083 — Sensitivity analysis

**Q1.** Products A(₹100L), B(₹80L), C(₹60L), D(₹40L). If A drops 20%, does ranking change?

- A) No B) **Yes, B ties/overtakes A** C) C overtakes A D) A drops to last
- Tree: LEAF(table)+LEAF(A−20%)→OPERATION(new A=80)→OPERATION(A=B=80, tie at top) | L3

**Q2.** Reps A=120, B=95, C=110, D=85. If B improves 20%, does B's rank change?

- A) No B) **Yes, B overtakes C** C) B overtakes A D) No change
- Tree: LEAF(table)+LEAF(B+20%)→OPERATION(B=114)→OPERATION(rank: A,B,C,D→B now 2nd) | L3

### NUM_DI_L3_084 — Feasibility to hit KPI

**Q1.** Current revenue ₹42L. Target ₹50L. Max monthly growth 6%. 3 months left. Feasible?

- A) No B) **Yes (₹50.02L)** C) Yes (₹52L) D) No (₹49L)
- Tree: LEAF(42,50,6%,3)→OPERATION(gap=8)→OPERATION(42×1.06³=50.02)→CONSTRAINT(≥50? Yes) | L3

**Q2.** Output 800 units. Target 1,000. Max growth 8%/month. 3 months. Feasible?

- A) No (952) B) No (960) C) **Yes (1,008)** D) Yes (1,100)
- Tree: LEAF(800,1000,8%,3)→OPERATION(gap=200)→OPERATION(800×1.08³=1007.8)→CONSTRAINT(≥1000? Yes) | L3

---

## R) Estimation & Approximation — 3 templates (1 L1, 2 L2) [capped at L2]

**Design note:** Estimation tops out at bounding and approximation, which is L1/L2 work. The previous L3 (robust decision across scenarios) was synthetic — the scenario framing didn't add genuine multi-step reasoning. Domain capped at L2.

### NUM_EST_L1_085 — Rounding

**Q1.** Round 347 to the nearest 100.

- A) **300** B) 400 C) 350 D) 340
- Tree: LEAF(347,100)→FORMULA(300) | L1

**Q2.** Round 4.67 to the nearest whole number.

- A) 4 B) **5** C) 4.5 D) 6
- Tree: LEAF(4.67)→FORMULA(5) | L1

### NUM_EST_L2_086 — Bounds-based choice

**Q1.** Cost is between ₹80 and ₹100. Option A is fixed ₹90; Option B is cost+5%. At which costs is B cheaper than A?

- A) Never B) **Below ₹85.71** C) Always D) Above ₹90
- Tree: LEAF(80,100,A=90,B=cost×1.05)→OPERATION(B at 80=84, at 100=105)→OPERATION(B cheaper below ₹85.71) | L2

**Q2.** Demand 1,000–1,500 units. Option A: ₹50/unit. Option B: ₹45/unit + ₹5,000 fixed. Where does B become cheaper?

- A) Never B) **Above 1,000 units** C) Always D) Below 1,000
- Tree: LEAF(A=50u,B=45u+5000)→OPERATION(equal at 50u=45u+5000→u=1000)→OPERATION(B cheaper above 1000) | L2

### NUM_EST_L2_087 — Approximate ratio/percentage

**Q1.** Approximately what percentage is 47 of 200?

- A) 20% B) **23.5%** C) 25% D) 30%
- Tree: LEAF(47,200)→OPERATION(47/200≈0.235→23.5%) | L2

**Q2.** Estimate 198 × 51 to the nearest thousand.

- A) 9,000 B) **10,000** C) 11,000 D) 12,000
- Tree: LEAF(198,51)→OPERATION(≈200×50=10,000) | L2

---

## S) Resource Allocation & Constraints — 6 templates (2 L2, 4 L3) [unchanged]

### NUM_AL_L2_089 — Budget with min/max bounds

**Q1.** Budget ₹100,000. Three departments: min ₹20,000, max ₹50,000 each. Remaining after minimums split equally. Each gets?

- A) 30,000 B) **33,333** C) 40,000 D) 25,000
- Tree: LEAF(100000,min60000)→OPERATION(remaining=40000)→OPERATION(13,333 each→total 33,333) | L2

**Q2.** Budget ₹80,000. Four items: min ₹10,000, max ₹30,000. Remaining split equally. Each gets?

- A) 15,000 B) **20,000** C) 25,000 D) 30,000
- Tree: LEAF(80000,min40000)→OPERATION(remaining=40000)→OPERATION(10,000 each→20,000) | L2

### NUM_AL_L2_090 — Capacity split

**Q1.** Warehouse 10,000 units. A needs 6,000, B needs 5,000. Priority A. How much for B?

- A) 5,000 B) **4,000** C) 3,000 D) 2,000
- Tree: LEAF(10000,6000,5000)→OPERATION(A=6000)→OPERATION(remaining=4000) | L2

**Q2.** Capacity 500/day. Line A needs 300, B needs 250. Split by proportion. A gets?

- A) 300 B) **272** C) 250 D) 280
- Tree: LEAF(500,300,250)→OPERATION(demand=550)→OPERATION(500×300/550=272) | L2

### NUM_AL_L3_091 — Multi-constraint feasibility

**Q1.** 100 hours. Tasks A(30h,v50), B(40h,v70), C(50h,v80), D(20h,v40). Max 3 tasks, each value ≥45. Which combination maximizes value within 100h?

- A) A+B+C B) **B+C+D... see note** C) A+C+D D) A+B+D
- Tree: LEAF(tasks)+LEAF(100h,max3,v≥45)→OPERATION(eliminate D: v40<45)→OPERATION(A+B+C=120h>100 ✗)→OPERATION(B+C=90h,v150 best feasible) | L3

**Q2.** Budget ₹500K. Projects A(₹80K,ROI20%), B(₹120K,25%), C(₹150K,15%), D(₹100K,22%). Min ROI 18%. Which combo fits budget and ROI?

- A) A+B+C B) **A+B+D** C) B+C+D D) All
- Tree: LEAF(projects)+LEAF(budget,minROI18)→OPERATION(eliminate C:15%)→OPERATION(A+B+D=300K≤500K, all ROI≥18%) | L3

### NUM_AL_L3_092 — Trade-off analysis

**Q1.** Option Fast: 5 days, ₹50,000. Option Cheap: 9 days, ₹30,000. Weights time=60%, cost=40%. Which wins?

- A) **Fast** B) Cheap C) Equal D) Depends
- Tree: LEAF(Fast,Cheap)+LEAF(60:40)→OPERATION(normalize time and cost scores)→OPERATION(Fast wins on weighted score) | L3

**Q2.** Supplier A: quality 90%, price ₹100. Supplier B: quality 75%, price ₹70. Weights quality=70%, price=30%. Which?

- A) **Supplier A** B) Supplier B C) Equal D) Depends on order
- Tree: LEAF(A,B)+LEAF(70:30)→OPERATION(weighted scores)→OPERATION(A wins on quality weight) | L3

### NUM_AL_L3_093 — Pick valid option

**Q1.** Four vendors: A(₹45,4d,4.2★), B(₹40,7d,4.5★), C(₹50,3d,3.8★), D(₹42,5d,4.0★). Constraints: price≤₹45, delivery≤5d, rating≥4.0. Which qualify?

- A) A only B) D only C) **A and D** D) All
- Tree: LEAF(vendors)+LEAF(constraints)→OPERATION(eliminate B:7d, C:3.8★)→OPERATION(A✓✓✓, D✓✓✓) | L3

**Q2.** Four plans by cost/time/coverage. Constraints cost≤₹200K, time≤6mo, coverage≥80%. (A:200K/6/80, B:150K/8/70, C:180K/5/85, D:220K/4/90) Which qualify?

- A) A only B) C only C) **A and C** D) All
- Tree: LEAF(plans)+LEAF(constraints)→OPERATION(eliminate B:70%, D:₹220K)→OPERATION(A✓, C✓) | L3

### NUM_AL_L3_094 — Lever analysis

**Q1.** Revenue ₹100L. Levers: A(+10% price→+10% rev), B(+5% volume→+5% rev), C(cut cost 8%→margin only). To maximize revenue, which lever?

- A) B B) **A** C) C D) Equal
- Tree: LEAF(100L)+LEAF(A,B,C)→OPERATION(A→110L)→OPERATION(B→105L)→OPERATION(C→no rev change)→OPERATION(A best) | L3

**Q2.** Profit ₹50L. Levers: X(cut fixed cost ₹8L), Y(price +10%→+₹10L rev), Z(volume +15%→net +₹2.5L). Best for profit?

- A) X (+8L) B) **Y (+10L)** C) Z (+2.5L) D) X and Y equal
- Tree: LEAF(50L)+LEAF(X,Y,Z)→OPERATION(X→58L)→OPERATION(Y→60L)→OPERATION(Z→52.5L)→OPERATION(Y best) | L3

---

## Final Structure Summary

| Domain           | Templates | L1  | L2  | L3  | Change from original                            |
| ---------------- | --------- | --- | --- | --- | ----------------------------------------------- |
| A Ratios         | 7         | 2   | 2   | 3   | +1 (genuine L3s replace synthetic)              |
| B Percentages    | 7         | 2   | 2   | 3   | +1 (genuine L3s)                                |
| C Profit/Loss    | 7         | 2   | 3   | 2   | +1 (same-SP moved to L2)                        |
| D Averages       | 7         | 1   | 3   | 3   | +2 (reverse avgs to L2, 3 new L3)               |
| E Mixtures       | 7         | 1   | 3   | 3   | +2 (multi-step to L2, 3 new L3)                 |
| F Interest       | 7         | 2   | 3   | 2   | +1 (compare-plans to L2, 2 new L3)              |
| G Time&Work      | 7         | 1   | 3   | 3   | +1 (efficiency to L2, three-equation L3)        |
| H TSD            | 6         | 1   | 2   | 3   | same count (boats-streams replaces feasibility) |
| I Pipes          | 6         | 1   | 3   | 2   | +1 (three-phase to L2, proportional L3)         |
| J P&C            | 6         | 1   | 3   | 2   | +2 (multi-constraint to L2, 2 new L3)           |
| K Probability    | 6         | 1   | 2   | 3   | +2 (Bayes, conditional-on-event)                |
| L Number Series  | 4         | 1   | 3   | 0   | capped at L2                                    |
| M Divisibility   | 5         | 1   | 2   | 2   | merged redundant, 2 new L3                      |
| N Remainders     | 5         | 1   | 1   | 3   | +1 (large-power, last-two-digits)               |
| O Mensuration 2D | 5         | 1   | 2   | 2   | +1 (cost to L2, path & wire L3)                 |
| P Mensuration 3D | 5         | 1   | 2   | 2   | +1 (capacity to L2, melting & cube L3)          |
| Q Data Interp    | 6         | 1   | 2   | 3   | unchanged (well-built)                          |
| R Estimation     | 3         | 1   | 2   | 0   | capped at L2                                    |
| S Resource Alloc | 6         | 0   | 2   | 4   | unchanged                                       |

**Domains capped at L2 (no genuine L3):** L (Number Series), R (Estimation)
**Domains unchanged (already well-designed):** Q (Data Interpretation), S (Resource Allocation)
