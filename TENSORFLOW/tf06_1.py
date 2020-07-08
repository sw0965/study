'''
틀린방식임..

import tensorflow as tf

tf.set_random_seed(777)


x_train_hold = tf.placeholder(dtype=tf.int32)
y_train_hold = tf.placeholder(dtype=tf.int32)

x_train = [1,2,3]
y_train = [3,5,7]

feed_dict = {x_train_hold:x_train, y_train_hold:y_train}


W = tf.Variable(tf.random_normal([1]), name='Weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# sess = tf.Session()
# sess.run(tf.global_variables_initializer()) 
# print(sess.run(W))

hypothesis = x_train * W + b       

cost = tf.reduce_mean(tf.square(hypothesis - y_train))  

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost) 

with tf.Session() as sess:  
# with tf.compat.v1.Session as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(hypothesis, feed_dict=feed_dict)


    for step in range(2001):    
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b])  

        if step % 20 == 0:  
            print(step, cost_val, W_val, b_val)'''


# 선생님 방식
import tensorflow as tf

tf.set_random_seed(777)


x_train = tf.placeholder(dtype=tf.float32, shape=[None])
y_train = tf.placeholder(dtype=tf.float32, shape=[None])

# x_train = [1,2,3]
# y_train = [3,5,7]

# feed_dict = {x_train_hold:x_train, y_train_hold:y_train}


W = tf.Variable(tf.random_normal([1]), name='Weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# sess = tf.Session()
# sess.run(tf.global_variables_initializer()) 
# print(sess.run(W))

hypothesis = x_train * W + b       

cost = tf.reduce_mean(tf.square(hypothesis - y_train))  

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost) 

with tf.Session() as sess:  
    sess.run(tf.global_variables_initializer())


    for step in range(2001):    
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b], feed_dict={x_train:[1, 2, 3], y_train:[3, 5, 7]})  

        if step % 20 == 0:  
            print(step, cost_val, W_val, b_val)
    
    print('예측: ', sess.run(hypothesis, feed_dict={x_train:[4]}))         # 예측:  [9.000078]
    print('예측: ', sess.run(hypothesis, feed_dict={x_train:[5, 6]}))      # 예측:  [11.000123 13.000169]
    print('예측: ', sess.run(hypothesis, feed_dict={x_train:[6, 7, 8]}))   # 예측:  [13.000169 15.000214 17.000257]
# predict 해보자






# 0 9.57655 [0.9361049] [0.5172017]
# 20 0.086847536 [1.9033724] [0.9433994]
# 40 0.00080549903 [1.9952551] [0.98448116]
# 60 2.3717801e-05 [2.0037947] [0.98886895]
# 80 1.5123468e-05 [2.0044084] [0.98974043]
# 100 1.36779345e-05 [2.0042765] [0.9902556]
# 120 1.2421726e-05 [2.0040824] [0.99071676]
# 140 1.1282136e-05 [2.0038917] [0.99115336]
# 160 1.0246219e-05 [2.0037088] [0.99156904]
# 180 9.306408e-06 [2.0035348] [0.99196506]
# 200 8.452352e-06 [2.0033689] [0.9923425]
# 220 7.677576e-06 [2.0032103] [0.99270225]
# 240 6.972796e-06 [2.0030596] [0.99304515]
# 260 6.3322354e-06 [2.0029156] [0.9933719]
# 280 5.751796e-06 [2.002779] [0.9936833]
# 300 5.223627e-06 [2.0026484] [0.99398005]
# 320 4.7440417e-06 [2.002524] [0.9942628]
# 340 4.309954e-06 [2.0024056] [0.9945322]
# 360 3.914273e-06 [2.0022926] [0.99478906]
# 380 3.555152e-06 [2.002185] [0.9950338]
# 400 3.2290327e-06 [2.0020823] [0.99526715]
# 420 2.93284e-06 [2.0019846] [0.9954895]
# 440 2.6639725e-06 [2.0018914] [0.9957013]
# 460 2.4195554e-06 [2.0018027] [0.9959032]
# 480 2.1975839e-06 [2.0017178] [0.99609554]
# 500 1.9961442e-06 [2.001637] [0.9962788]
# 520 1.8132781e-06 [2.0015604] [0.99645334]
# 540 1.6472442e-06 [2.0014875] [0.9966198]
# 560 1.4960714e-06 [2.0014174] [0.9967785]
# 580 1.3586615e-06 [2.0013506] [0.9969296]
# 600 1.2342756e-06 [2.001288] [0.99707365]
# 620 1.1211503e-06 [2.0012271] [0.99721104]
# 640 1.0188086e-06 [2.00117] [0.99734163]
# 660 9.25396e-07 [2.001115] [0.9974664]
# 680 8.408396e-07 [2.0010626] [0.997585]
# 700 7.6355735e-07 [2.001013] [0.9976983]
# 720 6.939652e-07 [2.0009654] [0.997806]
# 740 6.3046764e-07 [2.00092] [0.9979091]
# 760 5.7255255e-07 [2.0008771] [0.998007]
# 780 5.1999035e-07 [2.0008357] [0.9981007]
# 800 4.726568e-07 [2.0007973] [0.9981895]
# 820 4.2933607e-07 [2.0007591] [0.9982742]
# 840 3.8996254e-07 [2.000724] [0.99835527]
# 860 3.5439925e-07 [2.0006905] [0.9984321]
# 880 3.217523e-07 [2.000657] [0.99850553]
# 900 2.9234928e-07 [2.0006268] [0.9985757]
# 920 2.657921e-07 [2.000598] [0.9986422]
# 940 2.4150154e-07 [2.0005693] [0.9987056]
# 960 2.1936567e-07 [2.0005426] [0.9987666]
# 980 1.9929765e-07 [2.0005178] [0.9988243]
# 1000 1.8124761e-07 [2.0004938] [0.998879]
# 1020 1.646372e-07 [2.00047] [0.9989314]
# 1040 1.4942286e-07 [2.0004478] [0.99898183]
# 1060 1.3577362e-07 [2.0004272] [0.9990295]
# 1080 1.235225e-07 [2.000408] [0.99907464]
# 1100 1.12263116e-07 [2.0003889] [0.9991175]
# 1120 1.0201294e-07 [2.0003698] [0.99915874]
# 1140 9.2600885e-08 [2.0003524] [0.99919844]
# 1160 8.415024e-08 [2.0003364] [0.99923605]
# 1180 7.659628e-08 [2.000321] [0.9992716]
# 1200 6.965519e-08 [2.0003064] [0.9993053]
# 1220 6.333622e-08 [2.000292] [0.9993373]
# 1240 5.751887e-08 [2.0002778] [0.9993683]
# 1260 5.2137334e-08 [2.0002644] [0.99939823]
# 1280 4.7360043e-08 [2.000252] [0.99942666]
# 1300 4.298742e-08 [2.0002406] [0.9994536]
# 1320 3.9158692e-08 [2.0002296] [0.9994791]
# 1340 3.5642888e-08 [2.000219] [0.9995032]
# 1360 3.2405904e-08 [2.0002093] [0.9995261]
# 1380 2.9540615e-08 [2.0001998] [0.99954766]
# 1400 2.6866795e-08 [2.0001903] [0.9995682]
# 1420 2.43953e-08 [2.0001807] [0.9995885]
# 1440 2.2073815e-08 [2.0001717] [0.9996084]
# 1460 1.9999808e-08 [2.0001636] [0.99962723]
# 1480 1.8149573e-08 [2.000156] [0.999645]
# 1500 1.6493155e-08 [2.0001488] [0.9996617]
# 1520 1.5006814e-08 [2.000142] [0.99967736]
# 1540 1.362137e-08 [2.0001357] [0.99969244]
# 1560 1.2419473e-08 [2.0001295] [0.99970675]
# 1580 1.1323228e-08 [2.0001237] [0.99972004]
# 1600 1.0301619e-08 [2.0001183] [0.99973285]
# 1620 9.414862e-09 [2.000113] [0.9997448]
# 1640 8.597397e-09 [2.0001082] [0.999756]
# 1660 7.866977e-09 [2.0001035] [0.9997667]
# 1680 7.173336e-09 [2.0000987] [0.99977726]
# 1700 6.521456e-09 [2.000094] [0.999787]
# 1720 5.939379e-09 [2.0000892] [0.9997965]
# 1740 5.3876192e-09 [2.0000846] [0.99980605]
# 1760 4.8977804e-09 [2.0000803] [0.9998156]
# 1780 4.399984e-09 [2.0000763] [0.99982506]
# 1800 3.988589e-09 [2.0000727] [0.9998335]
# 1820 3.603797e-09 [2.0000691] [0.99984187]
# 1840 3.250534e-09 [2.0000658] [0.9998497]
# 1860 2.9524472e-09 [2.0000627] [0.9998568]
# 1880 2.659154e-09 [2.0000596] [0.999864]
# 1900 2.4172853e-09 [2.0000567] [0.9998704]
# 1920 2.2027962e-09 [2.0000544] [0.9998764]
# 1940 2.0055875e-09 [2.0000515] [0.99988234]
# 1960 1.7963467e-09 [2.0000494] [0.9998882]
# 1980 1.651415e-09 [2.0000472] [0.99989307]
# 2000 1.5034706e-09 [2.000045] [0.99989784]


# 쌤 방식
# 0 9.57655 [0.9361049] [0.5172017]
# 20 0.086847536 [1.9033724] [0.9433994]
# 40 0.00080549903 [1.9952551] [0.98448116]
# 60 2.3717801e-05 [2.0037947] [0.98886895]
# 80 1.5123468e-05 [2.0044084] [0.98974043]
# 100 1.36779345e-05 [2.0042765] [0.9902556]
# 120 1.2421726e-05 [2.0040824] [0.99071676]
# 140 1.1282136e-05 [2.0038917] [0.99115336]
# 160 1.0246219e-05 [2.0037088] [0.99156904]
# 180 9.306408e-06 [2.0035348] [0.99196506]
# 200 8.452352e-06 [2.0033689] [0.9923425]
# 220 7.677576e-06 [2.0032103] [0.99270225]
# 240 6.972796e-06 [2.0030596] [0.99304515]
# 260 6.3322354e-06 [2.0029156] [0.9933719]
# 280 5.751796e-06 [2.002779] [0.9936833]
# 300 5.223627e-06 [2.0026484] [0.99398005]
# 320 4.7440417e-06 [2.002524] [0.9942628]
# 340 4.309954e-06 [2.0024056] [0.9945322]
# 360 3.914273e-06 [2.0022926] [0.99478906]
# 380 3.555152e-06 [2.002185] [0.9950338]
# 400 3.2290327e-06 [2.0020823] [0.99526715]
# 420 2.93284e-06 [2.0019846] [0.9954895]
# 440 2.6639725e-06 [2.0018914] [0.9957013]
# 460 2.4195554e-06 [2.0018027] [0.9959032]
# 480 2.1975839e-06 [2.0017178] [0.99609554]
# 500 1.9961442e-06 [2.001637] [0.9962788]
# 520 1.8132781e-06 [2.0015604] [0.99645334]
# 540 1.6472442e-06 [2.0014875] [0.9966198]
# 560 1.4960714e-06 [2.0014174] [0.9967785]
# 580 1.3586615e-06 [2.0013506] [0.9969296]
# 600 1.2342756e-06 [2.001288] [0.99707365]
# 620 1.1211503e-06 [2.0012271] [0.99721104]
# 640 1.0188086e-06 [2.00117] [0.99734163]
# 660 9.25396e-07 [2.001115] [0.9974664]
# 680 8.408396e-07 [2.0010626] [0.997585]
# 700 7.6355735e-07 [2.001013] [0.9976983]
# 720 6.939652e-07 [2.0009654] [0.997806]
# 740 6.3046764e-07 [2.00092] [0.9979091]
# 760 5.7255255e-07 [2.0008771] [0.998007]
# 780 5.1999035e-07 [2.0008357] [0.9981007]
# 800 4.726568e-07 [2.0007973] [0.9981895]
# 820 4.2933607e-07 [2.0007591] [0.9982742]
# 840 3.8996254e-07 [2.000724] [0.99835527]
# 860 3.5439925e-07 [2.0006905] [0.9984321]
# 880 3.217523e-07 [2.000657] [0.99850553]
# 900 2.9234928e-07 [2.0006268] [0.9985757]
# 920 2.657921e-07 [2.000598] [0.9986422]
# 940 2.4150154e-07 [2.0005693] [0.9987056]
# 960 2.1936567e-07 [2.0005426] [0.9987666]
# 980 1.9929765e-07 [2.0005178] [0.9988243]
# 1000 1.8124761e-07 [2.0004938] [0.998879]
# 1020 1.646372e-07 [2.00047] [0.9989314]
# 1040 1.4942286e-07 [2.0004478] [0.99898183]
# 1060 1.3577362e-07 [2.0004272] [0.9990295]
# 1080 1.235225e-07 [2.000408] [0.99907464]
# 1100 1.12263116e-07 [2.0003889] [0.9991175]
# 1120 1.0201294e-07 [2.0003698] [0.99915874]
# 1140 9.2600885e-08 [2.0003524] [0.99919844]
# 1160 8.415024e-08 [2.0003364] [0.99923605]
# 1180 7.659628e-08 [2.000321] [0.9992716]
# 1200 6.965519e-08 [2.0003064] [0.9993053]
# 1220 6.333622e-08 [2.000292] [0.9993373]
# 1240 5.751887e-08 [2.0002778] [0.9993683]
# 1260 5.2137334e-08 [2.0002644] [0.99939823]
# 1280 4.7360043e-08 [2.000252] [0.99942666]
# 1300 4.298742e-08 [2.0002406] [0.9994536]
# 1320 3.9158692e-08 [2.0002296] [0.9994791]
# 1340 3.5642888e-08 [2.000219] [0.9995032]
# 1360 3.2405904e-08 [2.0002093] [0.9995261]
# 1380 2.9540615e-08 [2.0001998] [0.99954766]
# 1400 2.6866795e-08 [2.0001903] [0.9995682]
# 1420 2.43953e-08 [2.0001807] [0.9995885]
# 1440 2.2073815e-08 [2.0001717] [0.9996084]
# 1460 1.9999808e-08 [2.0001636] [0.99962723]
# 1480 1.8149573e-08 [2.000156] [0.999645]
# 1500 1.6493155e-08 [2.0001488] [0.9996617]
# 1520 1.5006814e-08 [2.000142] [0.99967736]
# 1540 1.362137e-08 [2.0001357] [0.99969244]
# 1560 1.2419473e-08 [2.0001295] [0.99970675]
# 1580 1.1323228e-08 [2.0001237] [0.99972004]
# 1600 1.0301619e-08 [2.0001183] [0.99973285]
# 1620 9.414862e-09 [2.000113] [0.9997448]
# 1640 8.597397e-09 [2.0001082] [0.999756]
# 1660 7.866977e-09 [2.0001035] [0.9997667]
# 1680 7.173336e-09 [2.0000987] [0.99977726]
# 1700 6.521456e-09 [2.000094] [0.999787]
# 1720 5.939379e-09 [2.0000892] [0.9997965]
# 1740 5.3876192e-09 [2.0000846] [0.99980605]
# 1760 4.8977804e-09 [2.0000803] [0.9998156]
# 1780 4.399984e-09 [2.0000763] [0.99982506]
# 1800 3.988589e-09 [2.0000727] [0.9998335]
# 1820 3.603797e-09 [2.0000691] [0.99984187]
# 1840 3.250534e-09 [2.0000658] [0.9998497]
# 1860 2.9524472e-09 [2.0000627] [0.9998568]
# 1880 2.659154e-09 [2.0000596] [0.999864]
# 1900 2.4172853e-09 [2.0000567] [0.9998704]
# 1920 2.2027962e-09 [2.0000544] [0.9998764]
# 1940 2.0055875e-09 [2.0000515] [0.99988234]
# 1960 1.7963467e-09 [2.0000494] [0.9998882]
# 1980 1.651415e-09 [2.0000472] [0.99989307]
# 2000 1.5034706e-09 [2.000045] [0.99989784]