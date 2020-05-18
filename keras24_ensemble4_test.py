#1. 데이터
import numpy as np
x1 = np.array([range(1,101),range(311,411),range(100)])

y1 = np.array([range(101,201),range(411,511),range(100,200)])
y2 = np.array([range(501,601), range(711,811), range(100)])

x1 = np.transpose(x1)
y1 = np.transpose(y1)
y2 = np.transpose(y2)


from sklearn.model_selection import train_test_split
x1_train,x1_test,y1_train,y1_test, y2_train, y2_test = train_test_split( 
    x1, y1, y2, shuffle=False, train_size=0.8)



# print("x_train",x1_train,"\ny_train",y1_train)
# print("x_test",x1_test,"\ny_test",y1_test)


#2. 모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input # DNN구조의 기본

input1 = Input(shape=(3, ))
dense1_1 = Dense(222, activation='relu')(input1)
dense1_2 = Dense(222, activation='relu')(dense1_1)
dense1_3 = Dense(222, activation='relu')(dense1_2)
dense1_4 = Dense(222, activation='relu')(dense1_3)
dense1_5 = Dense(111, activation='relu')(dense1_4)
dense1_6 = Dense(100, activation='relu')(dense1_5)
dense1_7 = Dense(80, activation='relu')(dense1_6)
dense1_8 = Dense(50, activation='relu')(dense1_7)
dense1_9 = Dense(30, activation='relu')(dense1_8)
dense1_10 = Dense(10, activation='relu')(dense1_9)


# input2 = Input(shape=(1, ))
# dense2_1 = Dense(333, activation='relu', name='bit1')(input2)
# dense2_2 = Dense(555, activation='relu', name='bit2')(dense2_1)
# dense2_3 = Dense(333, activation='relu', name='bit3')(dense2_2)
# dense2_4 = Dense(444, activation='relu', name='bit4')(dense2_3)
# dense2_5 = Dense(111, activation='relu', name='bit5')(dense2_4)
# dense2_6 = Dense(150, activation='relu', name='bit6')(dense2_5)
# dense2_7 = Dense(100, activation='relu', name='bit7')(dense2_6)
# dense2_8 = Dense(80, activation='relu', name='bit8')(dense2_7)
# dense2_9 = Dense(30, activation='relu', name='bit9')(dense2_8)
# dense2_10 = Dense(10, activation='relu', name='bit10')(dense2_9)

# from keras.layers.merge import concatenate #단순병합
# merge1 = concatenate(dense1_10)

middle1 = Dense(30)(dense1_10)
middle1 = Dense(5)(middle1)
middle1 = Dense(7)(middle1)

###### output 모델 구성 ######
#첫번째 아웃풋
output1 = Dense(30)(middle1) #middle 위에 합쳤던거 마지막 이름을 가져다 인풋으로 쓴다.
output1_2 = Dense(7)(output1)
output1_3 = Dense(3)(output1_2)
#두번째 아웃풋
output2 = Dense(30)(middle1)
output2_2 = Dense(7)(output2)
output2_3 = Dense(3)(output2_2)


model = Model(inputs = input1, outputs = [output1_3, output2_3]) #히든레이어 명시가 필요없으니 위에 명시를 해주는것 Sequential() 이거처럼

'''
model.summary()
'''

#600
#3. 훈련
model.compile(loss='mse',optimizer='adam', metrics=['mse']) # 회기방식과 분류방식 2가지 ?  # mse는 실제 값과 예측값의 차이를 평균하는것 
model.fit(x1_train,
          [y1_train,y2_train],epochs=150, batch_size=1
, validation_split=0.25, verbose=2) # batch_size = 32(default)
'''
model.summary()
'''
#4. 평가, 예측
loss = model.evaluate(x1_test,
                          [y1_test,y2_test],batch_size=1) # evaluate -> 결과 반환(기본적으로 loss와 metrics를 반환)을 loss와 acc에 받겠다.


print("loss : ",loss)
# print("mse : ",mse)


y1_predict, y2_predict = model.predict(x1_test)
# print("===================")
# print(y1_predict)
# print("===================")
# print(y2_predict)



#RMSE 구하기 #낮을수록 좋다
from sklearn.metrics import mean_squared_error
def RMSE(y_test,y_predict):
    return np.sqrt(mean_squared_error(y_test,y_predict))
RMSE = RMSE(y1_test, y1_predict)
print("RMSE : ", RMSE)


# print("RMSE : ", RMSE(y_test,y_predict))


# from sklearn.metrics import mean_squared_error
# def RMSE(y1_test,y1_predict):
#     return np.sqrt(mean_squared_error(y1_test,y1_predict))
# print("RMSE : ", RMSE(y1_test,y1_predict))

# from sklearn.metrics import mean_squared_error
# def RMSE(y2_test,y2_predict):
#     return np.sqrt(mean_squared_error(y2_test,y2_predict))
# print("RMSE : ", RMSE(y2_test,y2_predict))



#R2 구하기 # 1에 근접할수록 좋다. 다른 보조지표와 같이 쓴다.
from sklearn.metrics import r2_score
r2 = r2_score(y1_test,y1_predict)
print("R2 : ", r2)




 # Question


 # Note
# verbose 넣어보기

 # homework
