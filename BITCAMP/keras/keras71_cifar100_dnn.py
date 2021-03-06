import numpy as np
import matplotlib.pyplot as plt
from   keras.datasets  import cifar100
from   keras.layers    import Dense, Dropout, Input
from   keras.models    import Sequential, Model
from   keras.utils     import np_utils
from   keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard

(x_train, y_train), (x_test, y_test) = cifar100.load_data()

print('x_train :',x_train.shape)
print('x_test :',x_test.shape)
print('y_train :',y_train.shape)
print('y_test :',y_test.shape)

#1. 데이터 전처리
y_train = np_utils.to_categorical(y_train)
y_test  = np_utils.to_categorical(y_test)

# print('x_train :',x_train.shape)
# print('x_test :',x_test.shape)
print('y_train :',y_train.shape)
print('y_test :',y_test.shape)

#2. 데이터 정규화
x_train = x_train.reshape(50000, 32*32*3)/255
x_test  = x_test.reshape (10000, 32*32*3)/255

print('x_train :',x_train.shape)
print('x_test :',x_test.shape)

#.3 모델구성

input1  = Input(shape=(32*32*3,))
dens1   = Dense(20, activation='relu')(input1)
dens2   = Dense(20, activation='relu')(dens1)

output1 = Dense(20, activation='relu')(dens2)
dens3    = Dense(200, activation='relu')(output1)
dens4    = Dense(100)(dens3)

model   = Model(inputs=input1, outputs=dens4)

# model.save('./model/sample/cifar100/model_cifal100.h5')

model.summary()

#.4 모델 훈련
tb            = TensorBoard(log_dir='graph', histogram_freq=0, write_graph=True, write_images=True)
es            = EarlyStopping(monitor='acc', patience=2, mode='auto')
modelpath     = './model/sample/cifar100/cifar100-{epoch:02d}-{val_acc:.4f}.hdf5'
cp            = ModelCheckpoint(filepath=modelpath, monitor='val_acc', save_best_only=True, mode='auto')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
hist          = model.fit(x_train, y_train, validation_split=0.2, epochs=1000, batch_size=128, verbose=1, callbacks=[es,cp,tb])
# D:\Study\study\graph>cd tensorboard --logdir=.(텐서보드 확인 cmd에서)
# model.save_weights('./model/sample/cifar100/weight_cifar100.h5')

#.5 평가 예측
loss,acc = model.evaluate(x_test, y_test, batch_size=32)
print('loss : ', loss)
print('acc : ',acc)
loss_acc = loss,acc
# loss_acc = model.evaluate(x_test, y_test, batch_size=32)

loss     = hist.history['loss']
acc      = hist.history['acc']
val_loss = hist.history['val_loss']
val_acc  = hist.history['val_acc']

print('acc : ', acc)
print('val_acc : ', val_acc)
print('loss_acc : ', loss_acc)

# 그래프 사이즈
plt.figure(figsize=(10, 6))

# loss 그래프
plt.subplot(2, 1, 1) 
plt.plot(hist.history['loss'],     marker='.', c='red',  label='loss')  
plt.plot(hist.history['val_loss'], marker='.', c='blue', label='val_loss') 
plt.grid() 
plt.title('loss')       
plt.ylabel('loss')       
plt.xlabel('epoch')         
plt.legend(loc = 'upper right')

# acc 그래프
plt.subplot(2, 1, 2) 
plt.plot(hist.history['acc'],     marker='.', c='red',  label='acc')  
plt.plot(hist.history['val_acc'], marker='.', c='blue', label='val_acc') 
plt.grid() 
plt.title('acc')     
plt.ylabel('acc')        
plt.xlabel('epoch')           
plt.legend(loc = 'upper right')  
plt.show()


y_pre  = model.predict(x_test)

y_pre  = np.argmax(y_pre,axis=-1)
y_test = np.argmax(y_test,axis=-1)

print(f"y_test[0:20]:{y_test[0:20]}")
print(f"y_pre[0:20]:{y_pre[0:20]}")
