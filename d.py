import streamlit as st
import calendar
from datetime import datetime,date,time
if 'page' not in st.session_state:
    st.session_state.page='main'
    

if 'up' not in st.session_state:
    st.session_state.up=[]


if 'y' not in st.session_state:
    st.session_state.y = 2026
if 'm' not in st.session_state:
    st.session_state.m = 1
if 'd' not in st.session_state:
    st.session_state.d = 1
y = st.session_state.y
m = st.session_state.m
d = st.session_state.d
def getp(y1,m1,d1):
    r=[]
    c=0
    for i in st.session_state.up:
        a=str(i['날짜']).split('-')
        if int(a[0])==y1 and int(a[1])==m1 and int(a[2])==d1:
            c+=1
            r.append(i)
    return r,c

@st.dialog("일정")
def popup():
    st.write(f'{m}월{d}일')
    z,x=getp(y,m,d)
    if len(z)==0:
        st.write('')
    else:
        for i in z:

            st.write(f'일정:{i['일정']}, 메모:{i['메모']}, 시간:{i['시간']}')
if st.session_state.page=='main':

    st.header('대충달력이름')
    b1,b2,b3=st.columns(3)
    if b1.button('⬅'):
        m-=1
        if m==0:
            m=12
            y-=1
        st.session_state.y = y
        st.session_state.m = m
        st.rerun()
    if b3.button('➡'):
        m+=1
        if m==13:
            m=1
            y+=1
        st.session_state.y = y
        st.session_state.m = m
        st.rerun()
    b2.write(f'{y}년{m}월')
    v=['월','화','수','목','금','토','일']
    c=calendar.monthcalendar(y,m)
    co=st.columns(7)
    
    for i in range(7):
        with co[i]:
            st.write(v[i])
            for e in c:
                d=e[i]
                if d==0:
                    st.write(' ')
                else:
                    
                    cc,vv=getp(y,m,d)

                    if st.button(f'{str(d)},일정:{str(vv)}'):
                        st.session_state.d=d
                        popup()
                        
    if st.button('일정추가'):
        st.session_state.page='일정'
        st.rerun()
elif st.session_state.page=='일정':
     
    n=st.text_input('일정')
    e=0

    if not n:
        st.caption('일정을 쓰면 저장할수있습니다')

    m=st.text_area('메모')
    d=st.date_input('날짜입력')
    t=st.time_input('시간')

   
    
    if st.button('추가'):
        a={'일정':n,'메모':m,'시간':t,'날짜':d}
        d_str = str(d)
        st.session_state.up.append(a)
        st.session_state.page='main'
        st.rerun()
