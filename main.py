import streamlit as st
st.title("첫 app")
name=st.text_input("이름을 입력하시오")
if name:
  if name=="홍길동":
    st.success("반갑습니다.")
  else:
    st.warning("누구세요")
