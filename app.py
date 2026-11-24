import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #0B1220;
}

h1 {
    color: #48D8D0;
}


div.stButton > button {
    background-color: #14B8A6;
    color: #062C30;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


st.title("ScamShield")   #title for laarge headding

st.write("your assitance for detecting suspicious message here")   #display text on  the page

message=st.text_area("paste  a suspicious message here")    #creates large texxtbox



def detect_warnings(message):
    message_lower=message.lower()   #stores lowercase in new  variable

    warning=[]    #creating list to store all warning 

    if "urgent" in message_lower:
        warning.append("Urgent language")

    if "prize" in message_lower:
        warning.append("Prize claim")

    if "otp" in message_lower:
        warning.append("OTP mentioned")

    if "password" in message_lower:
        warning.append("Password mentioned")

    if "pay now" in message_lower:
        warning.append("Payment request")

    return warning




if st.button("analyze message"):    #st.button creates clickable button
    if not message.strip(): 
        st.warning("Please enter your message first.")      
                              #st.strip checks wheather the  text contain something other than spaces
        
    else:
        result=detect_warnings(message)
        if result:
            st.subheader("Warning sign detected:")
            for w in result:
                st.write("⚠️",w)
        else:
            st.success("\nNo  configured warning signs detected ")
        score=min(len(result)*20,100)      #here 100 is max 
        st.metric("\nRisk score:",score,"/100")

        if score>40:
            st.error("Result :HIGHER RISK")
        elif score>=20:
            st.warning("Result :CAUTION")
        elif score>0:
            st.info("Result : FEW WARNING SIGNS FOUNFD")
               
        else:
            st.success("No  configured warning signs detected")
          

