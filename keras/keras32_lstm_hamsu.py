# 함수형 모델로 리모델하시오

from numpy import array
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input


#1. 데이터
x = array([[1,2,3],[2,3,4],[3,4,5],[4,5,6],
           [5,6,7],[6,7,8],[7,8,9],[8,9,10],
           [9,10,11],[10,11,12],
           [20,30,40],[30,40,50],[40,50,60]])   
y = array([4,5,6,7,8,9,10,11,12,13,50,60,70])

x_predict = array([50, 60, 70])

x = x.reshape(x.shape[0], x.shape[1], 1)
print('x.reshape :', x.reshape) 



#2. 모델구성
input1 = Input(shape=(3, 1)) 
input1_1 = LSTM(1, name='lstm')(input1)
input1_2 = Dense(9, name='dense1')(input1_1)
input1_3 = Dense(2, name= 'dense2')(input1_2)


output1 = Dense(10, name='dense3')(input1_3)
output1_2 = Dense(2, name='dense4')(output1)
output1_3 = Dense(6, name='dense5')(output1_2)
output1_4 = Dense(1, name='dense6')(output1_3)

model = Model(inputs = input1, outputs = output1_4)

# model.summary()

#3. 실행
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=0, mode='auto')
model.compile(loss='mse',optimizer='adam') 
model.fit(x, y, epochs=3100, batch_size=16, verbose=2)#, callbacks=[early_stopping])  #5104
x_predict = x_predict.reshape(1, 3, 1)

print(x_predict)

y_predict = model.predict(x_predict)
print(y_predict)