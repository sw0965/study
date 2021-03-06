#35copy본
#lstm 레이어를 5개 엮어서 dense 결과를 이겨내시오

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
# return_sequences=True
input1 = Input(shape=(3, 1)) 
input1_1 = LSTM(10, return_sequences=True, name='lstm1')(input1)
input1_1 = LSTM(20, return_sequences=True, name='lstm2')(input1_1)
input1_1 = LSTM(30, return_sequences=True, name='lstm3')(input1_1)
input1_1 = LSTM(40, return_sequences=True, name='lstm4')(input1_1)
input1_1 = LSTM(50, return_sequences=False, name='lstm5')(input1_1)
input1_1 = Dense(60)(input1_1)
input1_1 = Dense(70)(input1_1)
input1_1 = Dense(80)(input1_1)
input1_1 = Dense(90)(input1_1)
input1_1 = Dense(100)(input1_1)





output1 = Dense(110)(input1_1)
output1_1 = Dense(100)(output1)
output1_1 = Dense(80)(output1_1)
output1_1 = Dense(70)(output1_1)
output1_1 = Dense(60)(output1_1)
output1_1 = Dense(50)(output1_1)
output1_1 = Dense(40)(output1_1)
output1_1 = Dense(30)(output1_1)
output1_1 = Dense(20)(output1_1)
output1_1 = Dense(10)(output1_1)
output1_1 = Dense(1)(output1_1)


model = Model(inputs = input1, outputs = output1_1)


model.summary()

#3. 실행
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=20, mode='auto')
model.compile(loss='mse',optimizer='adam') 
model.fit(x, y, epochs=10000, batch_size=10, verbose=2, callbacks=[early_stopping])  #5104
x_predict = x_predict.reshape(1, 3, 1)

print(x_predict)

y_predict = model.predict(x_predict)
print(y_predict)
