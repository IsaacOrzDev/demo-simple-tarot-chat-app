import streamlit as st
from chat import chat
from draw import draw_card

'''
# Tarot Chat 🔮
'''

num_of_cards = 3


def select_card(input):
    result = draw_card(input, num_of_cards)
    print(result)
    st.session_state.card = result["card"]
    st.session_state.position = result["position"]


def reset():
    st.session_state.clear()


if "card" not in st.session_state:
    st.chat_message("assistant").write("""
    Welcome to the enchanting world of Tarot.\n
    Each card holds wisdom and symbolism, offering guidance and insight into your path.\n
    Please chose a card and let its secrets unfold before you.
    """)
    for i in range(0, num_of_cards):
        st.button(f"🂠 Chose Card #{i+1}",
                  key=f"card{i}", on_click=lambda: select_card(i))

else:
    if "messages" not in st.session_state:
        response = chat(
            f"How about the drawing result?", [], st.session_state['card'], st.session_state['position'])
        st.session_state["messages"] = [
            {"role": "AI",
                "content": f"You have drawn {st.session_state['card']} in {st.session_state['position']} position.\n {response}"}
        ]
    if "messages" in st.session_state:
        st.button("Reset Drawing and conversations",
                  key="reset", on_click=reset)
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input(placeholder="Please ask any question if you want to know more about the result"):
            st.session_state.messages.append(
                {"role": "Human", "content": prompt})
            st.chat_message("user").write(prompt)
            response = chat(prompt,  st.session_state.messages,
                            st.session_state['card'], st.session_state['position'])
            st.session_state.messages.append(
                {"role": "AI", "content": response})
            st.chat_message("assistant").write(response)
