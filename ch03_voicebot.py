# # # # # # import streamlit as st

# # # # # # ## 메인 함수 ##
# # # # # # def main():
# # # # # #     st.set_page_config(
# # # # # #         page_title = "음성 비서 프로그램",
# # # # # #         layout = "wide"
# # # # # #     )

# # # # # # # 제목
# # # # # # st.header("음성 비서 프로그램")

# # # # # # # 구분선
# # # # # # st.markdown("---")

# # # # # # # 기본 설명
# # # # # # with st.expander("음성비서 프로그램에 관하여", expanded=True):
# # # # # #     st.write(
# # # # # #         """
# # # # # #         - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
# # # # # #         - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
# # # # # #         - 답변은 OpenAI의 GPT 모델을 활용했습니다.
# # # # # #         - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
# # # # # #         """
# # # # # #     )

# # # # # #     st.markdown("")



# # # # # import streamlit as st
# # # # # import time

# # # # # with st.sidebar:
# # # # #     with st.echo():
# # # # #         st.write("This code will be printed to the sidebar.")

# # # # #     with st.spinner("Loading..."):
# # # # #         time.sleep(5)
# # # # #     st.success("Done!")
# # # # # #-----------------------------------------------------------------------------

# # # # # # import streamlit as st

# # # # # # st.set_page_config(
# # # # # #     page_title="Ex-stream-ly Cool App",
# # # # # #     page_icon="🧊",
# # # # # #     layout="wide",
# # # # # #     initial_sidebar_state="expanded",
# # # # # #     menu_items={
# # # # # #         'Get Help': 'https://www.extremelycoolapp.com/help',
# # # # # #         'Report a bug': "https://www.extremelycoolapp.com/bug",
# # # # # #         'About': "# This is a header. This is an *extremely* cool app!"
# # # # # #     }
# # # # # # )

# # # # # # ctrl + c : stopping

# # # # # # #---------------------------------------------------------
# # # # # # import streamlit as st

# # # # # # st.header("_Streamlit_ is :blue[cool] :sunglasses:")
# # # # # # st.header("This is a header with a divider", divider="gray")
# # # # # # st.header("These headers have rotating dividers", divider=True)
# # # # # # st.header("One", divider=True)
# # # # # # st.header("Two", divider=True)
# # # # # # st.header("Three", divider=True)
# # # # # # st.header("Four", divider=True)


# # # # # # #---------------------------------------------------------

# # # # # # import streamlit as st

# # # # # # st.markdown("*Streamlit* is **really** ***cool***.")
# # # # # # st.markdown('''
# # # # # #     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
# # # # # #     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
# # # # # # st.markdown("Here's a bouquet &mdash;\
# # # # # #             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# # # # # # multi = '''If you end a line with two spaces,
# # # # # # a soft return is used for the next line.

# # # # # # Two (or more) newline characters in a row will result in a hard return.
# # # # # # '''
# # # # # # st.markdown(multi)

# # # # # # #---------------------------------------------------------

# # # # # # import streamlit as st

# # # # # # st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# # # # # # with st.expander("See explanation", expanded=True):
# # # # # #     st.write('''
# # # # # #         The chart above shows some numbers I picked for you.
# # # # # #         I rolled actual dice for these, so they're *guaranteed* to
# # # # # #         be random.
# # # # # #     ''')
# # # # # #     st.image("https://static.streamlit.io/examples/dice.jpg")

# # # # import streamlit as st
# # # # import openai

# # # # ## 메인 함수 ##
# # # # def main():
# # # #     st.set_page_config(
# # # #         page_title = "음성 비서 프로그램"
# # # #         )

# # # # # 제목
# # # # st.header("음성 비서 프로그램")

# # # # # 구분선
# # # # st.markdown("---")

# # # # # 기본 설명
# # # # with st.expander("음성비서 프로그램에 관하여", expanded=True):
# # # #     st.write(
# # # #         """
# # # #         - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
# # # #         - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
# # # #         - 답변은 OpenAI의 GPT 모델을 활용했습니다.
# # # #         - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
# # # #         """
# # # #     )

# # # # # 사이드바 생성
# # # # with st.sidebar:
# # # #     # Open AI API 키 입력받기
# # # #     openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key",
# # # #                                    value="", type="password")
# # # #     st.markdown("")

# # # #     # GPT 모델을 선택하기 위한 라디오 버튼 생성
# # # #     model = st.radio(label="GPT 모델", options=['gpt-4', 'gpt-3.5-turbo'])

# # # #     st.markdown("")

# # # #     # 리셋 버튼 생성
# # # #     if st.button(label="초기화"):
# # # #         # 리셋 코드
# # # #         pass

# # # import streamlit as st
# # # import openai

# # # ## 메인 함수 ##
# # # def main():
# # #     st.set_page_config(
# # #         page_title = "음성 비서 프로그램"
# # #         )

# # # # 제목
# # # st.header("음성 비서 프로그램")

# # # # 구분선
# # # st.markdown("---")

# # # # 기본 설명
# # # with st.expander("음성비서 프로그램에 관하여", expanded=True):
# # #     st.write(
# # #         """
# # #         - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
# # #         - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
# # #         - 답변은 OpenAI의 GPT 모델을 활용했습니다.
# # #         - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
# # #         """
# # #     )

# # # # 사이드바 생성
# # # with st.sidebar:
# # #     # Open AI API 키 입력받기
# # #     openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key",
# # #                                    value="", type="password")
# # #     st.markdown("")

# # #     # GPT 모델을 선택하기 위한 라디오 버튼 생성
# # #     model = st.radio(label="GPT 모델", options=['gpt-4', 'gpt-3.5-turbo'])

# # #     st.markdown("")

# # #     # 리셋 버튼 생성
# # #     if st.button(label="초기화"):
# # #         # 리셋 코드
# # #         pass

# # # # 기능 구현 공간
# # # col1,col2 = st.columns(2)
# # # with col1:
# # #     # 왼쪽 영역 작성
# # #     st.subheader("질문하기")

# # # with col2:
# # #     # 오른쪽 영역 작성
# # #     st.subheader("질문/답변")

# # import streamlit as st
# # import openai
# # import numpy as np

# # ## 메인 함수 ##
# # def main():
# #     st.set_page_config(
# #         page_title = "음성 비서 프로그램"
# #         )

# # # 제목
# # st.header("음성 비서 프로그램")

# # # 구분선
# # st.markdown("---")

# # # 기본 설명
# # with st.expander("음성비서 프로그램에 관하여", expanded=True):
# #     st.write(
# #         """
# #         - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
# #         - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
# #         - 답변은 OpenAI의 GPT 모델을 활용했습니다.
# #         - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
# #         """
# #     )

# # # 사이드바 생성
# # with st.sidebar:
# #     # Open AI API 키 입력받기
# #     openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key",
# #                                    value="", type="password")
# #     st.markdown("")

# #     # GPT 모델을 선택하기 위한 라디오 버튼 생성
# #     model = st.radio(label="GPT 모델", options=['gpt-4', 'gpt-3.5-turbo'])

# #     st.markdown("")

# #     # 리셋 버튼 생성
# #     if st.button(label="초기화"):
# #         # 리셋 코드
# #         st.session_state["chat"] = []
# #         st.session_state["messages"] = \
# #         [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
# #         st.session_state["check_audio"] = []

# # # 기능 구현 공간
# # col1,col2 = st.columns(2)
# # with col1:
# #     # 왼쪽 영역 작성
# #     st.subheader("질문하기")

# #     # session state 초기화
# #     if 'chat' not in st.session_state:
# #         st.session_state['chat'] = []
    
# #     if 'messages' not in st.session_state:
# #         st.session_state['messages'] = \
# #         [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
    
# #     if 'check_audio' not in st.session_state:
# #         st.session_state['check_audio'] = []

# # with col2:
# #     # 오른쪽 영역 작성
# #     st.subheader("질문/답변")


# import streamlit as st
# import openai
# import numpy as np

# # audiorecorder 패키지 추가
# from audiorecorder import audiorecorder

# ## 메인 함수 ##
# def main():
#     st.set_page_config(
#         page_title = "음성 비서 프로그램"
#         )

# # 제목
# st.header("음성 비서 프로그램")

# # 구분선
# st.markdown("---")

# # 기본 설명
# with st.expander("음성비서 프로그램에 관하여", expanded=True):
#     st.write(
#         """
#         - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
#         - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
#         - 답변은 OpenAI의 GPT 모델을 활용했습니다.
#         - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
#         """
#     )

# # 사이드바 생성
# with st.sidebar:
#     # Open AI API 키 입력받기
#     openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key",
#                                    value="", type="password")
#     st.markdown("")

#     # GPT 모델을 선택하기 위한 라디오 버튼 생성
#     model = st.radio(label="GPT 모델", options=['gpt-4', 'gpt-3.5-turbo'])

#     st.markdown("")

#     # 리셋 버튼 생성
#     if st.button(label="초기화"):
#         # 리셋 코드
#         st.session_state["chat"] = []
#         st.session_state["messages"] = \
#         [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
#         st.session_state["check_audio"] = []

# # 기능 구현 공간
# col1,col2 = st.columns(2)
# with col1:
#     # 왼쪽 영역 작성
#     st.subheader("질문하기")

#     # session state 초기화
#     if 'chat' not in st.session_state:
#         st.session_state['chat'] = []
    
#     if 'messages' not in st.session_state:
#         st.session_state['messages'] = \
#         [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
    
#     if 'check_audio' not in st.session_state:
#         st.session_state['check_audio'] = []

#     # 음성 녹음 아이콘 추가
#     audio = audiorecorder("클릭하여 녹음하기", "녹음 중...")
#     if len(audio) > 0 and not np.array_equal(audio, st.session_state["check_audio"]):
#         # 음성 재생
#         st.audio(audio.export().read())

# with col2:
#     # 오른쪽 영역 작성
#     st.subheader("질문/답변")

##### 기본 정보 입력 #####
import streamlit as st
# audiorecorder 패키지 추가
from audiorecorder import audiorecorder
# OpenAI 패키지 추가
import openai
# 파일 삭제를 위한 패키지 추가
import os
# 시간 정보를 위한 패키지 추가
from datetime import datetime
# TTS 패키기 추가
from gtts import gTTS
# 음원 파일 재생을 위한 패키지 추가
import base64

##### 기능 구현 함수 #####
def STT(audio):
    # 파일 저장
    filename='input.mp3'
    audio.export(filename, format="mp3")
    # 음원 파일 열기
    audio_file = open(filename, "rb")
    # Whisper 모델을 활용해 텍스트 얻기
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    audio_file.close()
    # 파일 삭제
    os.remove(filename)
    return transcript["text"]

def ask_gpt(prompt, model):
    response = openai.ChatCompletion.create(model=model, messages=prompt)
    system_message = response["choices"][0]["message"]
    return system_message["content"]

def TTS(response):
    # gTTS 를 활용하여 음성 파일 생성
    filename = "output.mp3"
    tts = gTTS(text=response,lang="ko")
    tts.save(filename)

    # 음원 파일 자동 재생생
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="True">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md,unsafe_allow_html=True,)
    # 파일 삭제
    os.remove(filename)

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성 비서 프로그램",
        layout="wide")

    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False

    # 제목 
    st.header("음성 비서 프로그램")
    # 구분선
    st.markdown("---")

    # 기본 설명
    with st.expander("음성비서 프로그램에 관하여", expanded=True):
        st.write(
        """     
        - 음성비서 프로그램의 UI는 스트림릿을 활용했습니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper AI를 활용했습니다. 
        - 답변은 OpenAI의 GPT 모델을 활용했습니다. 
        - TTS(Text-To-Speech)는 구글의 Google Translate TTS를 활용했습니다.
        """
        )

        st.markdown("")

    # 사이드바 생성
    with st.sidebar:

        # Open AI API 키 입력받기
        openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key", value="", type="password")

        st.markdown("---")

        # GPT 모델을 선택하기 위한 라디오 버튼 생성
        model = st.radio(label="GPT 모델",options=["gpt-4", "gpt-3.5-turbo"])

        st.markdown("---")

        # 리셋 버튼 생성
        if st.button(label="초기화"):
            # 리셋 코드 
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
            st.session_state["check_reset"] = True
            
    # 기능 구현 공간
    col1, col2 =  st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")
        # 음성 녹음 아이콘 추가
        audio = audiorecorder("클릭하여 녹음하기", "녹음중...")
        if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
            # 음성 재생 
            st.audio(audio.export().read())
            # 음원 파일에서 텍스트 추출
            question = STT(audio)

            # 채팅을 시각화하기 위해 질문 내용 저장
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"]+ [("user",now, question)]
            # GPT 모델에 넣을 프롬프트를 위해 질문 내용 저장
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "user", "content": question}]

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")
        if  (audio.duration_seconds > 0)  and (st.session_state["check_reset"]==False):
            # ChatGPT에게 답변 얻기
            response = ask_gpt(st.session_state["messages"], model)

            # GPT 모델에 넣을 프롬프트를 위해 답변 내용 저장
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "system", "content": response}]

            # 채팅 시각화를 위한 답변 내용 저장
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"]+ [("bot",now, response)]

            # 채팅 형식으로 시각화 하기
            for sender, time, message in st.session_state["chat"]:
                if sender == "user":
                    st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
                else:
                    st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
            
            # gTTS 를 활용하여 음성 파일 생성 및 재생
            TTS(response)
        else:
            st.session_state["check_reset"] = False

if __name__=="__main__":
    main()