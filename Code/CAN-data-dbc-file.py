import cantools
from cantools.database.can.formats import dbc

db = cantools.db.Database()


signal_1 = cantools.db.Signal(
    name='singanl1',
    start=0,    #시작 비트 위치
    length=8,   #1바이트
    byte_order='little_endian',
    is_signed=False #부호 없는 값
)

signal_2 = cantools.db.Signal(
     name='singanl2',
    start=8,
    length=8,
    byte_order='little_endian',
    is_signed=False
)


#메시지 생성
message = cantools.db.Message(
    frame_id=1, #메시지 id는 정수 
    name='Test1 Message',
    length=8,
    signals=[signal_1, signal_2]
)

#메시지를 데이터베이스에 추가
db.messages.append(message)

#.dbc파일 저장
with open('test1.dbc','w') as f:
    f.write(dbc.dump_string(db))

print("test1.dbc파일 생성 완료")
