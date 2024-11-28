import hashlib
import cantools

# dbc 파일 경로
normal_dbc_path = "D:\python code\test1.dbc"
malware_dbc_path = "D:\python code\malware_test1.dbc"

# 해시 함수 정의
def hash_block(data):
    hash_func = hashlib.sha256()  # SHA-256 해시 함수 사용
    hash_func.update(data.encode('utf-8'))
    return hash_func.hexdigest()

# dbc 파일 읽기 함수
def read_dbc(file_path):
    try:
        db = cantools.database.load_file(file_path)
        messages = db.messages
        return messages
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 무결성 검증 함수
def integrity_verification(normal_dbc_messages, malware_dbc_messages):
    # 초기 상태값 설정
    state = "initial_state"
    
    # 정상 dbc 파일 해시 생성
    for msg in normal_dbc_messages:
        block_data = str(msg)  # 각 메시지를 문자열로 변환하여 블록 데이터로 사용
        state = hash_block(state + block_data)
    
    # 멀웨어 dbc 파일 해시 생성 및 비교
    for msg in malware_dbc_messages:
        block_data = str(msg)
        state = hash_block(state + block_data)
    
    # 최종 해시 검증
    if state == hash_block(str(normal_dbc_messages)):
        print("Integrity Verified: CAN.dbc is valid.")
    else:
        print("Integrity Error: Malware detected in dbc file.")

# dbc 파일 로드
normal_dbc_messages = read_dbc(normal_dbc_path)
malware_dbc_messages = read_dbc(malware_dbc_path)

# 무결성 검증 수행
if normal_dbc_messages and malware_dbc_messages:
    integrity_verification(normal_dbc_messages, malware_dbc_messages)
else:
    print("DBC 파일을 불러오는 데 실패했습니다.")
